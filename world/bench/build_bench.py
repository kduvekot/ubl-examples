#!/usr/bin/env python3
"""Serra 180 park bench: parametric model, analysis, drawings, renders, report.

Reads parameters.json (the single source of truth) and writes, next to it:
  step/      STEP of the assembly and of each part
  glb/       GLB for the web (assembly, parcels, pallet)
  drawings/  SVG manufacturing drawings
  renders/   PNG product renders (via render.js, Chromium + three.js)
  results.json  every derived figure
  report.md  the report (from report_template.md)

Usage: python build_bench.py [--no-render] [--no-drawings]
See README.md for the environment (build123d in a virtual environment).
"""
import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
from build123d import (Axis, Box, Color, Compound, Cylinder, Kind, Location,
                       Plane, Polygon, Pos, Rot, Sphere, RegularPolygon,
                       extrude, offset, export_step, export_gltf, CenterOf)

HERE = Path(__file__).resolve().parent
P = json.load(open(HERE / "parameters.json", encoding="utf-8"))
ARGS = set(sys.argv[1:])

# --------------------------------------------------------------------------
# small 2D vector helpers in the frame plane: (y, z) = (depth, height)
# --------------------------------------------------------------------------
def v(a, b):
    return np.array([float(a), float(b)])


def rad(a):
    return math.radians(a)


def intersect(p1, d1, p2, d2):
    """Intersection of the lines p1 + t d1 and p2 + s d2."""
    A = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
    t, _ = np.linalg.solve(A, p2 - p1)
    return p1 + t * d1


def poly(pts):
    pts = [(float(p[0]), float(p[1])) for p in pts]
    area = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))
    if area < 0:
        pts = pts[::-1]              # counter-clockwise, so that all faces share one normal
    return Polygon(*pts, align=None)


def band(p0, p1, n, w):
    """Quadrilateral from the segment p0-p1, extended by w along normal n."""
    return poly([p0, p1, p1 + w * n, p0 + w * n])


# --------------------------------------------------------------------------
# 1. Geometry of the side profile (derived from the parameters)
# --------------------------------------------------------------------------
class Profile:
    def __init__(self, p):
        o, e, s, f = p["overall"], p["ergonomics"], p["slats"], p["frame"]
        self.T, self.W, self.L = s["thickness"], s["width"], s["length"]
        self.tilt = rad(e["seat_tilt_deg"])
        self.beta = rad(e["seat_tilt_deg"] + e["seat_back_angle_deg"] - 90)
        self.gap = o["levelling_gap_nominal"]
        self.Hs = o["seat_height_nominal"]
        t, b = self.tilt, self.beta
        self.s = v(math.cos(t), -math.sin(t))      # along the seat, backward
        self.nup = v(math.sin(t), math.cos(t))     # seat normal, up
        self.d = v(math.sin(b), math.cos(b))       # along the back, upward
        self.nr = v(math.cos(b), -math.sin(b))     # back normal, to the rear
        fp = f["front_post"]
        self.post_d = fp["depth"]
        self.F = v(fp["depth"] + s["post_to_slat_gap"], self.Hs)
        self.SD = e["seat_depth"]
        self.Pt = self.F + self.SD * self.s
        self.seat_s = [i * (s["width"] + s["seat_gap"]) for i in range(s["seat_count"])]
        self.back_u = list(s["back_slat_u"])
        self.arm_top = self.Hs + e["armrest_above_seat"]
        self.f = f
        self.foot_top = self.gap + f["feet"]["thickness"]

    # lines
    def seat_line(self, sig, off=0.0):
        """Point on the seat surface line, offset 'off' below it (along -nup)."""
        return self.F + sig * self.s - off * self.nup

    def back_line(self, u, off=0.0):
        """Point on the back surface line, offset 'off' behind it (along nr)."""
        return self.Pt + u * self.d + off * self.nr


def build_profile_faces(pr):
    """Return (web_face, [(flange_face, width, name)], key points) in the (y,z) plane."""
    f = pr.f
    T = pr.T
    sr, br, ar, rl, fp = f["seat_rail"], f["back_rail"], f["armrest"], f["rear_leg"], f["front_post"]
    tf = f["t_flange"]
    ez = v(0, 1)
    ey = v(1, 0)
    # seat rail: from the front face y=0 to the rear face of the back rail
    top0 = pr.seat_line(0, T)
    bot0 = pr.seat_line(0, T + sr["depth"])
    back_rear_p = pr.back_line(0, T + br["depth"])
    back_front_p = pr.back_line(0, T)
    sr_top_front = intersect(top0, pr.s, v(0, 0), ez)
    sr_bot_front = intersect(bot0, pr.s, v(0, 0), ez)
    sr_top_rear = intersect(top0, pr.s, back_rear_p, pr.d)
    sr_bot_rear = intersect(bot0, pr.s, back_rear_p, pr.d)
    seat_rail = poly([sr_top_front, sr_top_rear, sr_bot_rear, sr_bot_front])
    # back rail: from the bottom line of the seat rail up to u_top
    bf_bot = intersect(back_front_p, pr.d, bot0, pr.s)
    brr_bot = intersect(back_rear_p, pr.d, bot0, pr.s)
    bf_top = pr.back_line(br["u_top"], T)
    brr_top = pr.back_line(br["u_top"], T + br["depth"])
    back_rail = poly([bf_bot, bf_top, brr_top, brr_bot])
    # front post: y 0..depth, from inside the foot up to the armrest top
    post = poly([v(0, pr.gap), v(fp["depth"], pr.gap), v(fp["depth"], pr.arm_top), v(0, pr.arm_top)])
    # armrest: z arm_top-depth..arm_top, from y=0 back to the rear face of the back rail
    za = pr.arm_top - ar["depth"] / 2
    y_end_top = intersect(v(0, pr.arm_top), ey, back_rear_p, pr.d)[0]
    y_end_bot = intersect(v(0, pr.arm_top - ar["depth"]), ey, back_rear_p, pr.d)[0]
    arm = poly([v(0, pr.arm_top - ar["depth"]), v(y_end_bot, pr.arm_top - ar["depth"]),
                v(y_end_top, pr.arm_top), v(0, pr.arm_top)])
    # rear leg: centre line from J (seat rail centre x back rail centre) to the rear foot
    J = intersect(pr.seat_line(0, T + sr["depth"] / 2), pr.s, pr.back_line(0, T + br["depth"] / 2), pr.d)
    R = v(rl["foot_y"], pr.gap)
    dl = (R - J) / np.linalg.norm(R - J)
    nl = v(-dl[1], dl[0])          # normal of the leg
    if nl[0] < 0:
        nl = -nl                   # pointing to the rear (+y)
    hw = rl["depth"] / 2
    Jx = J - 25 * dl
    a0, a1 = Jx - hw * nl, Jx + hw * nl
    b0 = intersect(a0, dl, v(0, pr.gap), ey)
    b1 = intersect(a1, dl, v(0, pr.gap), ey)
    leg = poly([a0, b0, b1, a1])
    web = seat_rail + back_rail + post + arm + leg
    rc, rf = f["round_convex"], f["fillet_concave"]
    web = offset(offset(web, rf, kind=Kind.ARC), -rf, kind=Kind.ARC)   # fillets at inner corners
    web = offset(offset(web, -rc, kind=Kind.ARC), rc, kind=Kind.ARC)   # radii at outer corners
    # front end of the armrest: a larger radius in elevation
    rr = ar["front_end_radius"]
    # flanges (strips along one edge of each member), trimmed to the web outline
    flanges = []
    big = 2000
    st_seat = poly([sr_top_front - 50 * pr.s, sr_top_rear + 50 * pr.s,
                    sr_top_rear + 50 * pr.s - tf * pr.nup, sr_top_front - 50 * pr.s - tf * pr.nup])
    flanges.append((st_seat, sr["flange_width"], "seat_rail"))
    st_back = poly([bf_bot - 50 * pr.d, bf_top, bf_top + tf * pr.nr, bf_bot - 50 * pr.d + tf * pr.nr])
    flanges.append((st_back, br["flange_width"], "back_rail"))
    st_post = poly([v(0, pr.gap), v(tf, pr.gap), v(tf, pr.arm_top), v(0, pr.arm_top)])
    flanges.append((st_post, fp["flange_width"], "front_post"))
    st_arm = poly([v(0, pr.arm_top - tf), v(y_end_top + 50, pr.arm_top - tf), v(y_end_top + 50, pr.arm_top), v(0, pr.arm_top)])
    flanges.append((st_arm, ar["flange_width"], "armrest"))
    c1 = a1 - 60 * dl
    st_leg = poly([c1, intersect(a1, dl, v(0, pr.gap), ey), intersect(a1 - tf * nl, dl, v(0, pr.gap), ey), c1 - tf * nl])
    flanges.append((st_leg, rl["flange_width"], "rear_leg"))
    flanges = [((fa & web), w, n) for fa, w, n in flanges]
    keys = dict(J=J, R=R, sr_top_front=sr_top_front, sr_top_rear=sr_top_rear, bf_bot=bf_bot,
                bf_top=bf_top, brr_top=brr_top, y_arm_end=y_end_top, za=za, dl=dl, nl=nl,
                sr_bot_front=sr_bot_front, sr_bot_rear=sr_bot_rear, brr_bot=brr_bot,
                leg_top=Jx, leg_a1=a1, leg_b1=b1, leg_b0=b0)
    return web, flanges, keys


def frame_solid(pr, x_c):
    """One side frame as a solid, its plane of symmetry at x = x_c."""
    f = pr.f
    web, flanges, keys = build_profile_faces(pr)
    tw = f["t_web"]
    solid = Pos(x_c - tw / 2, 0, 0) * extrude(Plane.YZ * web, tw)
    for fa, w, _n in flanges:
        solid = solid + Pos(x_c - w / 2, 0, 0) * extrude(Plane.YZ * fa, w)
    ft = f["feet"]
    for key in ("front", "rear"):
        q = ft[key]
        foot = Pos(x_c, (q["y0"] + q["y1"]) / 2, pr.gap + ft["thickness"] / 2) * Box(ft["width"], q["y1"] - q["y0"], ft["thickness"])
        # radius the plan corners of the foot (casting radius)
        solid = solid + foot
    for key in ("front", "rear"):
        q = ft[key]
        solid = solid - Pos(x_c, q["hole_y"], pr.gap + ft["thickness"] / 2) * Cylinder(ft["hole_diameter"] / 2, ft["thickness"] + 2)
    # bolt holes in the seat-rail and back-rail flanges
    for xb in bolt_x_offsets(x_c):
        for pnt, axis in bolt_points(pr):
            solid = solid - hole_cyl(xb, pnt, axis, f["steel_hole_diameter"] / 2, pr.T - 1, pr.T + f["t_flange"] + 1)
    return solid, keys


def bolt_x_offsets(x_c):
    xs = P["slats"]["bolt_x_from_end"]
    if x_c < P["slats"]["length"] / 2:
        return list(xs)
    return [P["slats"]["length"] - x for x in xs]


def bolt_points(pr):
    """(point on the slat's exposed face in (y,z), axis into the slat) for every slat."""
    out = []
    for s0 in pr.seat_s:
        out.append((pr.seat_line(s0 + pr.W / 2), -pr.nup))
    for u0 in pr.back_u:
        out.append((pr.back_line(u0 + pr.W / 2), pr.nr))
    return out


def hole_cyl(x, pnt, axis, r, d0, d1):
    """Cylinder of radius r along 'axis' (in y,z) from depth d0 to d1 below the point."""
    ax3 = (0.0, float(axis[0]), float(axis[1]))
    length = d1 - d0
    c = pnt + (d0 + length / 2) * axis
    cyl = Cylinder(r, length)
    # orient: Cylinder axis is Z; rotate about X so Z maps to ax3
    ang = math.degrees(math.atan2(-ax3[1], ax3[2]))
    return Pos(x, float(c[0]), float(c[1])) * Rot(ang, 0, 0) * cyl


# --------------------------------------------------------------------------
# slats, bolts
# --------------------------------------------------------------------------
def slat_local():
    s = P["slats"]
    L, W, T, ch = s["length"], s["width"], s["thickness"], s["edge_chamfer"]
    prof = poly([v(ch, 0), v(W - ch, 0), v(W, ch), v(W, T - ch), v(W - ch, T), v(ch, T), v(0, T - ch), v(0, ch)])
    # profile in local (y, z) with z 0..T, then shift so that the top face is at z=0
    body = Pos(0, 0, -T) * extrude(Plane.YZ * prof, L)
    for xb in s["bolt_x_from_end"] + [L - x for x in s["bolt_x_from_end"]]:
        body = body - Pos(xb, W / 2, -T / 2) * Cylinder(s["hole_diameter"] / 2, T + 2)
    return body


def place_seat(pr, sh, i):
    p0 = pr.seat_line(pr.seat_s[i])
    return Pos(0, float(p0[0]), float(p0[1])) * Rot(-math.degrees(pr.tilt), 0, 0) * sh


def place_back(pr, sh, j):
    p0 = pr.back_line(pr.back_u[j])
    return Pos(0, float(p0[0]), float(p0[1])) * Rot(90 - math.degrees(pr.beta), 0, 0) * sh


def bolt_parts_local():
    """Carriage bolt, washer and nut in local coordinates: slat face at z=0, axis -Z."""
    b = P["bolts"]
    T, tf = P["slats"]["thickness"], P["frame"]["t_flange"]
    a, h = b["head_diameter"] / 2, b["head_height"]
    R = (a * a + h * h) / (2 * h)
    head = (Pos(0, 0, h - R) * Sphere(R)) & (Pos(0, 0, h / 2) * Box(2 * a + 2, 2 * a + 2, h))
    neck = Pos(0, 0, -b["neck_length"] / 2) * Box(b["neck_square"], b["neck_square"], b["neck_length"])
    shank = Pos(0, 0, -b["length"] / 2) * Cylinder(b["d"] / 2, b["length"])
    bolt = head + neck + shank
    z_w = -(T + tf)
    washer = Pos(0, 0, z_w - b["washer_t"] / 2) * (Cylinder(b["washer_od"] / 2, b["washer_t"]) - Cylinder(b["washer_id"] / 2, b["washer_t"] + 1))
    zn = z_w - b["washer_t"] - b["nut_height"] / 2
    nut = Pos(0, 0, zn) * (extrude(RegularPolygon(b["nut_af"] / math.sqrt(3), 6), b["nut_height"], both=False).moved(Location((0, 0, -b["nut_height"] / 2))) - Cylinder(b["d"] / 2, b["nut_height"] + 2))
    return bolt, washer, nut


def place_on_axis(sh, x, pnt, axis):
    """Place a local part (axis -Z from the face point) at x, pnt with the given inward axis."""
    # local -Z must map to axis -> local +Z maps to -axis
    up = -axis
    ang = math.degrees(math.atan2(-up[0], up[1]))
    return Pos(x, float(pnt[0]), float(pnt[1])) * Rot(ang, 0, 0) * sh


# --------------------------------------------------------------------------
# 2. Build the bench
# --------------------------------------------------------------------------
def build_bench():
    pr = Profile(P)
    x_c = P["frame"]["x_centre"]
    L = P["slats"]["length"]
    frame_L, keys = frame_solid(pr, x_c)
    frame_R = Pos(L - 2 * x_c, 0, 0) * frame_L
    sl = slat_local()
    seats = [place_seat(pr, sl, i) for i in range(len(pr.seat_s))]
    backs = [place_back(pr, sl, j) for j in range(len(pr.back_u))]
    bolt, washer, nut = bolt_parts_local()
    bolts, washers, nuts = [], [], []
    for xc in (x_c, L - x_c):
        for xb in bolt_x_offsets(xc):
            for pnt, axis in bolt_points(pr):
                bolts.append(place_on_axis(bolt, xb, pnt, axis))
                washers.append(place_on_axis(washer, xb, pnt, axis))
                nuts.append(place_on_axis(nut, xb, pnt, axis))
    return dict(pr=pr, keys=keys, frame_L=frame_L, frame_R=frame_R, seats=seats, backs=backs,
                slat=sl, bolt=bolt, washer=washer, nut=nut, bolts=bolts, washers=washers, nuts=nuts)


# --------------------------------------------------------------------------
# 3. Analysis helpers
# --------------------------------------------------------------------------
def t_section(h, b, tw, tf):
    """T-section with the flange (b x tf) at one edge, in-plane depth h. Returns A, I, W_min, perimeter."""
    hw = h - tf
    A_f, A_w = b * tf, tw * hw
    A = A_f + A_w
    z_f, z_w = h - tf / 2, hw / 2
    zc = (A_f * z_f + A_w * z_w) / A
    I = b * tf ** 3 / 12 + A_f * (z_f - zc) ** 2 + tw * hw ** 3 / 12 + A_w * (z_w - zc) ** 2
    W = I / max(zc, h - zc)
    per = 2 * b + 2 * hw            # cooling perimeter (both flange faces, web faces)
    # out-of-plane bending (about the axis in the frame plane)
    I_oop = tf * b ** 3 / 12 + hw * tw ** 3 / 12
    W_oop = I_oop / (b / 2)
    return dict(A=A, I=I, W=W, zc=zc, perimeter=per, I_oop=I_oop, W_oop=W_oop)


def slat_beam(L, supports, udl=(), points=(), E=11000.0, I=None, W=None, n=3601):
    """Slat as a beam on two supports with overhangs. udl: (x0, x1, q N/mm); points: (x, F)."""
    x = np.linspace(0, L, n)
    dx = x[1] - x[0]
    q = np.zeros(n)
    for x0, x1, qq in udl:
        q[(x >= x0) & (x <= x1)] += qq
    Fp = np.zeros(n)
    for xp, F in points:
        Fp[int(round(xp / dx))] += F
    load = q * dx + Fp
    a, b = supports
    tot = load.sum()
    mom_a = (load * (x - a)).sum()
    Rb = mom_a / (b - a)
    Ra = tot - Rb
    ia, ib = int(round(a / dx)), int(round(b / dx))
    react = np.zeros(n)
    react[ia] -= Ra
    react[ib] -= Rb
    net = load + react               # downward positive
    V = np.cumsum(net)               # shear just right of each point
    M = -np.cumsum(V) * dx           # sagging positive
    M -= M[-1] * 0                   # free end has M=0 by statics
    k = M / (E * I)                  # curvature
    th = np.cumsum(k) * dx
    w = np.cumsum(th) * dx
    # impose w(a)=w(b)=0 by a linear correction
    wa, wb = w[ia], w[ib]
    w = w - (wa + (wb - wa) * (x - a) / (b - a))
    w = -w                           # downward deflection positive
    mid = (x >= a) & (x <= b)
    return dict(Ra=Ra, Rb=Rb, Mmax=float(np.max(np.abs(M))), sigma=float(np.max(np.abs(M)) / W),
                w_span=float(np.max(w[mid])), w_end=float(max(w[0], w[-1])), x=x, M=M, w=w)


class Frame2D:
    """Plane frame with Euler-Bernoulli beam elements, 3 DOF per node."""

    def __init__(self):
        self.nodes, self.elems, self.loads, self.fix = [], [], {}, []

    def node(self, p):
        self.nodes.append(np.array(p, float))
        return len(self.nodes) - 1

    def elem(self, i, j, sec, name, E=210000.0):
        self.elems.append((i, j, sec, name, E))

    def solve(self):
        n = len(self.nodes)
        K = np.zeros((3 * n, 3 * n))
        Fv = np.zeros(3 * n)
        T_all = []
        for i, j, sec, name, E in self.elems:
            pi, pj = self.nodes[i], self.nodes[j]
            Lv = pj - pi
            L = np.linalg.norm(Lv)
            c, s = Lv / L
            A, I = sec["A"], sec["I"]
            k = np.array([
                [E * A / L, 0, 0, -E * A / L, 0, 0],
                [0, 12 * E * I / L ** 3, 6 * E * I / L ** 2, 0, -12 * E * I / L ** 3, 6 * E * I / L ** 2],
                [0, 6 * E * I / L ** 2, 4 * E * I / L, 0, -6 * E * I / L ** 2, 2 * E * I / L],
                [-E * A / L, 0, 0, E * A / L, 0, 0],
                [0, -12 * E * I / L ** 3, -6 * E * I / L ** 2, 0, 12 * E * I / L ** 3, -6 * E * I / L ** 2],
                [0, 6 * E * I / L ** 2, 2 * E * I / L, 0, -6 * E * I / L ** 2, 4 * E * I / L]])
            Tm = np.zeros((6, 6))
            for o in (0, 3):
                Tm[o:o + 2, o:o + 2] = [[c, s], [-s, c]]
                Tm[o + 2, o + 2] = 1
            kg = Tm.T @ k @ Tm
            dof = [3 * i, 3 * i + 1, 3 * i + 2, 3 * j, 3 * j + 1, 3 * j + 2]
            K[np.ix_(dof, dof)] += kg
            T_all.append((k, Tm, dof, L))
        for nd, f in self.loads.items():
            Fv[3 * nd:3 * nd + 3] += f
        fixed = []
        for nd, dofs in self.fix:
            fixed += [3 * nd + d for d in dofs]
        free = [d for d in range(3 * n) if d not in fixed]
        u = np.zeros(3 * n)
        u[free] = np.linalg.solve(K[np.ix_(free, free)], Fv[free])
        Rxn = K @ u - Fv
        res = []
        for (i, j, sec, name, E), (k, Tm, dof, L) in zip(self.elems, T_all):
            fl = k @ (Tm @ u[dof])
            N = max(abs(fl[0]), abs(fl[3]))
            M = max(abs(fl[2]), abs(fl[5]))
            sig = abs(fl[0]) / sec["A"] + abs(fl[2]) / sec["W"]
            sig2 = abs(fl[3]) / sec["A"] + abs(fl[5]) / sec["W"]
            res.append(dict(name=name, N=N, M=M, sigma=max(sig, sig2)))
        return u, Rxn, res


# --------------------------------------------------------------------------
# 4. Packaging and pallet
# --------------------------------------------------------------------------
def bbox_dims(sh):
    bb = sh.bounding_box()
    return [bb.max.X - bb.min.X, bb.max.Y - bb.min.Y, bb.max.Z - bb.min.Z], bb


def build_packaging(B, M):
    pk = P["packaging"]
    fc = pk["frame_carton"]
    fd, _ = bbox_dims(B["frame_L"])          # x (thickness), y (depth), z (height)
    thick, depth, height = fd
    cl = fc["clearance"]
    inner = [height + 2 * cl[0], depth + 2 * cl[1], thick + 2 * cl[2]]   # L x W x H, frame lying flat
    t = fc["board_thickness"]
    outer = [inner[0] + 4 * t, inner[1] + 4 * t, inner[2] + 2 * t]       # tray + lid: two walls each side
    # board area: tray (L+2H)(W+2H) and lid of the same blank
    blank = (outer[0] + 2 * outer[2]) * (outer[1] + 2 * outer[2]) / 1e6
    carton_kg = 2 * blank * fc["board_gm2"] / 1000 + fc["pads_kg"]
    # slat bundle: 3 + 2 pattern
    sb = pk["slat_bundle"]
    W, T, L = P["slats"]["width"], P["slats"]["thickness"], P["slats"]["length"]
    e = sb["edge_protector_thickness"]
    bundle = [L + 2 * sb["end_cap_thickness"], 3 * W + 2 * e, 2 * T + 2 * e]
    bundle_pack_kg = sb["straps"] * sb["strap_kg"] + 4 * sb["protector_kg_per_m"] * bundle[0] / 1000 + sb["film_kg"]
    # pallet
    pp = pk["pallet"]
    pl, pw = pp["length"], pp["width"]
    db, bb_, blk, sbd = pp["deck_board"], pp["bottom_board"], pp["block"], pp["stringer_board"]
    pallet_parts = []
    z = 0
    # bottom boards (along the length)
    for k in range(pp["bottom_boards"]):
        y = (pw - bb_[0]) * k / (pp["bottom_boards"] - 1) + bb_[0] / 2
        pallet_parts.append(Pos(pl / 2, y, bb_[1] / 2) * Box(pl, bb_[0], bb_[1]))
    z = bb_[1]
    for i in range(3):
        for k in range(3):
            x = (pl - blk[0]) * i / 2 + blk[0] / 2
            y = (pw - blk[1]) * k / 2 + blk[1] / 2
            pallet_parts.append(Pos(x, y, z + blk[2] / 2) * Box(blk[0], blk[1], blk[2]))
    z += blk[2]
    for i in range(3):            # stringer boards across the width on top of the blocks
        x = (pl - sbd[0]) * i / 2 + sbd[0] / 2
        pallet_parts.append(Pos(x, pw / 2, z + sbd[1] / 2) * Box(sbd[0], pw, sbd[1]))
    z += sbd[1]
    for k in range(pp["deck_boards_top"]):
        y = (pw - db[0]) * k / (pp["deck_boards_top"] - 1) + db[0] / 2
        pallet_parts.append(Pos(pl / 2, y, z + db[1] / 2) * Box(pl, db[0], db[1]))
    z += db[1]
    pallet_h = z
    pallet_vol = sum(p.volume for p in pallet_parts)
    pallet_kg = pallet_vol / 1e9 * P["materials"]["pine_density_pallet"]
    pallet = Compound(children=[x.moved(Location()) for x in pallet_parts])
    # load: 2 x 2 slat bundles at the bottom, a slip sheet, 2 columns of 4 frame cartons
    n = pp["benches"]
    load = []
    y0 = (pw - 2 * bundle[1]) / 2
    for layer in range(2):
        for k in range(2):
            load.append(("bundle", Pos(pl / 2, y0 + bundle[1] * (k + 0.5), pallet_h + bundle[2] * (layer + 0.5)) * Box(*bundle)))
    zc = pallet_h + 2 * bundle[2] + 3
    yc = (pw - outer[1]) / 2
    xc0 = (pl - 2 * outer[0]) / 2
    for col in range(2):
        for lev in range(2 * n // 2):
            load.append(("carton", Pos(xc0 + outer[0] * (col + 0.5), yc + outer[1] / 2, zc + outer[2] * (lev + 0.5)) * Box(*outer)))
    top = zc + outer[2] * (2 * n // 2) + 5
    load_dims = [pl, max(pw, outer[1]), top]
    return dict(frame_bbox=fd, carton_inner=inner, carton_outer=outer, carton_kg=carton_kg, carton_blank_m2=blank,
                bundle=bundle, bundle_pack_kg=bundle_pack_kg, pallet=pallet, pallet_parts=pallet_parts,
                pallet_h=pallet_h, pallet_kg=pallet_kg, load=load, load_dims=load_dims,
                cartons_fit=(2 * outer[0] <= pl and outer[1] <= pw + 0.1), bundles_fit=(bundle[0] <= pl))


# --------------------------------------------------------------------------
# 5. Casting: risers and gating for one mould (the two frames of one bench)
# --------------------------------------------------------------------------
def build_casting(B, M):
    pr, keys = B["pr"], B["keys"]
    f, c = P["frame"], P["casting"]
    x_c, tw = f["x_centre"], f["t_web"]
    rho = P["materials"]["steel_density"]
    sec_wall = t_section(f["seat_rail"]["depth"], f["seat_rail"]["flange_width"], tw, f["t_flange"])
    M_wall = sec_wall["A"] / sec_wall["perimeter"]                 # mm, 2D modulus of the bar
    M_j = c["wall_modulus_factor_junction"] * M_wall
    M_r = c["riser_modulus_factor"] * M_j
    k_cyl = c["riser_h_over_d"] / (4 * c["riser_h_over_d"] + 1)   # M = k D for a top riser, base excluded
    D_calc = M_r / k_cyl
    D = max(D_calc, c["riser_min_diameter"])
    H = c["riser_h_over_d"] * D
    T_in = tw / 25.4
    FD = 6 * math.sqrt(T_in) * 25.4                               # mm, each side of a riser
    ar = f["armrest"]
    za = pr.arm_top - ar["depth"] / 2
    post_y = f["front_post"]["depth"] / 2
    J = keys["J"]
    seat_cl = (pr.seat_line(0, pr.T + f["seat_rail"]["depth"] / 2), pr.s)
    back_cl = (pr.back_line(0, pr.T + f["back_rail"]["depth"] / 2), pr.d)
    j_post_seat = intersect(seat_cl[0], seat_cl[1], v(post_y, 0), v(0, 1))
    j_post_arm = v(post_y, za)
    j_arm_back = intersect(v(0, za), v(1, 0), back_cl[0], back_cl[1])
    back_top = pr.back_line(f["back_rail"]["u_top"] - 10, pr.T + f["back_rail"]["depth"] / 2)
    ftf, ftr = f["feet"]["front"], f["feet"]["rear"]
    foot_f = v((ftf["y0"] + ftf["y1"]) / 2, pr.gap + f["feet"]["thickness"] / 2)
    foot_r = v((ftr["y0"] + ftr["y1"]) / 2, pr.gap + f["feet"]["thickness"] / 2)
    leg_bot = v(f["rear_leg"]["foot_y"], pr.foot_top + 10)
    junctions = dict(post_seat=j_post_seat, post_arm=j_post_arm, J=J, arm_back=j_arm_back, foot_front=foot_f, foot_rear=foot_r)
    runs = [("front post, foot to seat rail", v(post_y, pr.foot_top), j_post_seat, True),
            ("front post, seat rail to armrest", j_post_seat, j_post_arm, False),
            ("seat rail", j_post_seat, J, False),
            ("back rail, seat to armrest", J, j_arm_back, False),
            ("back rail, armrest to top", j_arm_back, back_top, True),
            ("armrest", j_post_arm, j_arm_back, False),
            ("rear leg", J, leg_bot, True)]
    risers_pts = [("junction " + k, p) for k, p in junctions.items()]
    run_info = []
    for name, a, b, _ in runs:
        Lr = float(np.linalg.norm(b - a))
        n_int = max(0, math.ceil(Lr / (2 * FD)) - 1)
        for k in range(n_int):
            risers_pts.append(("on " + name, a + (b - a) * (k + 1) / (n_int + 1)))
        run_info.append(dict(run=name, length=round(Lr), intermediate_risers=n_int))
    frame = B["frame_L"]
    top_x = x_c + f["seat_rail"]["flange_width"] / 2     # top of the casting in the mould (x up)
    risers = []
    for name, p in risers_pts:
        x0 = x_c + tw / 2
        h_tot = (top_x - x0) + H
        risers.append(Pos(x0 + h_tot / 2, float(p[0]), float(p[1])) * Rot(0, 90, 0) * Cylinder(D / 2, h_tot))
    riser_union = risers[0]
    for r in risers[1:]:
        riser_union = riser_union + r
    riser_net = riser_union - frame
    V_frame = frame.volume
    V_risers = riser_net.volume
    # junction-only scheme (no intermediate risers)
    rj = risers[:len(junctions)]
    ru = rj[0]
    for r in rj[1:]:
        ru = ru + r
    V_risers_j = (ru - frame).volume
    # gating for two frames in one mould
    n_fr = c["frames_per_mould"]
    W_guess = n_fr * (V_frame + V_risers) / 1e9 * rho * 1.12
    t_pour = c["pour_time_k"] * math.sqrt(W_guess)
    h = c["pour_head"] / 1000
    vel = c["discharge_coefficient"] * math.sqrt(2 * 9.81 * h)
    A_choke = W_guess / (c["liquid_density"] * t_pour * vel) * 1e6      # mm2
    gr = c["gating_ratio"]
    A_run = A_choke * gr[1] / gr[0]
    A_gate_tot = A_choke * gr[2] / gr[0]
    d_sprue = math.sqrt(4 * A_choke / math.pi)
    run_h = math.sqrt(A_run / 1.2)
    run_w = 1.2 * run_h
    # the second frame is the first mirrored about y = y_m, so that the two main junctions J
    # face each other across a short runner; one ingate into each J (the heaviest node)
    y_m = P["overall"]["depth"] + 30
    J_b = v(2 * y_m - J[0], J[1])
    zr = float(J[1])
    yr0, yr1 = float(J[0]) + 45, float(J_b[0]) - 45
    n_gates = n_fr
    gate_w = 20.0
    gate_t = A_gate_tot / n_gates / gate_w
    ys = (yr0 + yr1) / 2
    gating = [Pos(x_c, ys, zr) * Box(run_w, yr1 - yr0 - 2 * 30, run_h)]
    gating.append(Pos(x_c + c["pour_head"] / 2, ys, zr) * Rot(0, 90, 0) * Cylinder(d_sprue / 2, c["pour_head"]))
    gating.append(Pos(x_c, ys, zr) * Rot(0, 90, 0) * Cylinder(d_sprue, 2 * run_h))   # sprue well
    for y0g, y1g in ((float(J[0]), yr0 + 30), (yr1 - 30, float(J_b[0]))):
        gating.append(Pos(x_c, (y0g + y1g) / 2, zr) * Box(gate_t, abs(y1g - y0g), gate_w))
    g_union = gating[0]
    for g in gating[1:]:
        g_union = g_union + g
    flip = Pos(x_c, y_m, 0) * Rot(0, 0, 180) * Pos(-x_c, -y_m, 0)
    frame2 = flip * frame
    g_net = g_union - frame - frame2
    V_gating = g_net.volume + c["basin_volume_cm3"] * 1000
    casting_kg = V_frame / 1e9 * rho
    poured = n_fr * (V_frame + V_risers) / 1e9 * rho + V_gating / 1e9 * rho
    poured_j = n_fr * (V_frame + V_risers_j) / 1e9 * rho + V_gating / 1e9 * rho
    riser2 = riser_net.mirror(Plane(origin=(0, y_m, 0), z_dir=(0, 1, 0)))   # risers stay on the cope side
    parts = []
    for sh, nm in ((frame, "casting_1"), (frame2, "casting_2"), (riser_net, "risers_1"), (riser2, "risers_2"), (g_net, "gating")):
        c_ = sh.moved(Location())
        c_.label = nm
        parts.append(c_)
    cluster = Compound(children=parts, label="mould_cluster")
    return dict(M_wall=M_wall, M_j=M_j, M_r=M_r, D_calc=D_calc, D=D, H=H, FD=FD, n_risers=len(risers),
                n_risers_junction=len(junctions), runs=run_info, V_risers=V_risers, V_risers_j=V_risers_j,
                riser_kg=V_risers / 1e9 * rho, riser_kg_j=V_risers_j / 1e9 * rho,
                W_guess=W_guess, t_pour=t_pour, vel=vel, A_choke=A_choke, d_sprue=d_sprue, A_run=A_run,
                run_w=run_w, run_h=run_h, gate_t=gate_t, gate_w=gate_w, n_gates=n_gates,
                gating_kg=V_gating / 1e9 * rho, casting_kg=casting_kg,
                poured=poured, yield_=n_fr * casting_kg / poured, poured_j=poured_j, yield_j=n_fr * casting_kg / poured_j,
                cluster=cluster, risers=riser_net, gating=g_net, junctions=junctions, runner_len=yr1 - yr0 - 60, y_m=y_m)


# --------------------------------------------------------------------------
# 6. Masses, loads, checks
# --------------------------------------------------------------------------
def set_wood(key):
    """Put the properties of one slat wood (parameters.json 'woods') into P['materials'] for analyse()."""
    w = P["woods"][key]
    m = P["materials"]
    m["wood_key"] = key
    m["wood_density"] = w["density"]
    f_mk = w["f_mk_base"] * w["strength_ratio"]
    E_alt = (P["materials"]["wood"]["clear_wood_oak_12pct"]["MOE"] * 1.1 if key == "oak"
             else w["E0_mean"] * w.get("E_ratio_clear", 1.0))
    m["wood"].update(dict(cls=w["base_class"], f_mk=f_mk, E0_mean=w["E0_mean"], k_mod_short_sc3=w["k_mod_short"],
                          k_mod_short_sc2=w.get("k_mod_short_sc2", w["k_mod_short"]), gamma_M=w["gamma_M"], E_alt=E_alt))
    return w


def analyse(B):
    pr = B["pr"]
    mat = P["materials"]
    rho_s, rho_w = mat["steel_density"], mat["wood_density"]
    R = {}
    fr = B["frame_L"]
    V_fr = fr.volume
    A_fr = fr.area
    m_fr_bare = V_fr / 1e9 * rho_s
    m_draft = m_fr_bare * P["frame"]["draft_mass_allowance_pct"] / 100
    g = mat["galvanising"]
    zinc_min = A_fr / 1e6 * g["mean_min_gm2"] / 1000
    zinc_typ = zinc_min * g["typical_factor"]
    pc = mat["powder_coat"]
    powder = A_fr / 1e6 * pc["thickness_um"] * 1e-6 * pc["density"]
    m_frame = m_fr_bare + m_draft + zinc_typ + powder
    cg = fr.center(CenterOf.MASS)
    sl = B["slat"]
    V_sl = sl.volume
    m_slat = V_sl / 1e9 * rho_w
    bt, ws, nt = B["bolt"], B["washer"], B["nut"]
    rho_ss = P["bolts"]["density"]                  # stainless steel A2, no coating
    m_bolt = bt.volume / 1e9 * rho_ss * P["bolts"]["thread_mass_factor"]
    m_washer = ws.volume / 1e9 * rho_ss
    m_nut = nt.volume / 1e9 * rho_ss
    m_fix = m_bolt + m_washer + m_nut
    m_boltset = P["bolts"]["count"] * m_fix + P["bolts"]["bag_mass"]
    net = 2 * m_frame + P["slats"]["count"] * m_slat + m_boltset
    # centre of gravity of the bench
    parts = [(B["frame_L"], m_frame), (B["frame_R"], m_frame)] + [(s, m_slat) for s in B["seats"] + B["backs"]]
    cgs = np.array([list(tuple(p.center(CenterOf.MASS))) for p, _ in parts])
    ms = np.array([m for _, m in parts])
    cg_b = (cgs * ms[:, None]).sum(0) / ms.sum()
    # interference checks (should be 0)
    inter = {}
    for nm, a, b in [("frame/seat slat 1", B["frame_L"], B["seats"][0]), ("frame/seat slat 3", B["frame_L"], B["seats"][2]),
                     ("frame/back slat 1", B["frame_L"], B["backs"][0]), ("frame/back slat 2", B["frame_L"], B["backs"][1])]:
        try:
            inter[nm] = round((a & b).volume / 1000, 3)
        except Exception:
            inter[nm] = 0.0
    # overall dimensions
    allp = Compound(children=[x.moved(Location()) for x in [B["frame_L"], B["frame_R"]] + B["seats"] + B["backs"]])
    bb = allp.bounding_box()
    f = P["frame"]
    over_arm = P["slats"]["length"] - 2 * (f["x_centre"] - f["armrest"]["flange_width"] / 2)
    between_arms = P["slats"]["length"] - 2 * (f["x_centre"] + f["armrest"]["flange_width"] / 2)
    top_back = pr.back_line(pr.back_u[1] + pr.W)
    R["dims"] = dict(length=bb.max.X - bb.min.X, depth=bb.max.Y - bb.min.Y, height=bb.max.Z,
                     z_min=bb.min.Z, over_armrests=over_arm, between_armrests=between_arms,
                     seat_width_per_person=between_arms / P["ergonomics"]["seats"],
                     seat_front=pr.Hs, P=pr.Pt.tolist(), F=pr.F.tolist(), back_top=top_back.tolist(),
                     back_rel_P=[float(pr.back_line(u)[1] - pr.Pt[1]) for u in (pr.back_u[0], pr.back_u[0] + pr.W, pr.back_u[1], pr.back_u[1] + pr.W)],
                     seat_surface_depth=float(pr.seat_s[-1] + pr.W), throat=float(pr.SD - pr.seat_s[-1] - pr.W),
                     arm_clear_lower=float(pr.arm_top - f["armrest"]["depth"] - pr.back_line(pr.back_u[0] + pr.W)[1]),
                     arm_clear_upper=float(pr.back_line(pr.back_u[1])[1] - pr.arm_top),
                     back_height_above_seat=float(top_back[1] - pr.Hs), beta=math.degrees(pr.beta),
                     slat_span=P["slats"]["length"] - 2 * f["x_centre"], overhang=f["x_centre"],
                     slat_overhang_beyond_frame=f["x_centre"] - f["seat_rail"]["flange_width"] / 2,
                     back_rail_top_y=float(B["keys"]["brr_top"][0]))
    R["mass"] = dict(frame_volume_l=V_fr / 1e6, frame_area_m2=A_fr / 1e6, frame_bare=m_fr_bare, frame_draft=m_draft,
                     zinc_min=zinc_min, zinc_typ=zinc_typ, powder=powder, frame=m_frame,
                     frame_cg=[cg.X, cg.Y, cg.Z], slat_volume_l=V_sl / 1e6, slat=m_slat,
                     slat_box_volume_l=P["slats"]["length"] * P["slats"]["width"] * P["slats"]["thickness"] / 1e6,
                     bolt=m_bolt, washer=m_washer, nut=m_nut, fixing=m_fix, boltset=m_boltset, net=net,
                     steel_in_product=2 * (m_fr_bare + m_draft),
                     stainless_fixings=P["bolts"]["count"] * m_fix, zinc_bench=2 * zinc_typ, zinc_bench_min=2 * zinc_min,
                     powder_bench=2 * powder, wood_bench=P["slats"]["count"] * m_slat, wood_key=mat["wood_key"],
                     bench_cg=cg_b.tolist())
    R["interference_cm3"] = inter
    web, flanges, _k = build_profile_faces(pr)
    brk = {"web (all members)": web.area * f["t_web"] / 1e6}
    for fa, w, nm in flanges:
        brk["flange " + nm] = fa.area * (w - f["t_web"]) / 1e6
    ftp = f["feet"]
    brk["feet (2)"] = sum((ftp[k]["y1"] - ftp[k]["y0"]) * ftp["width"] * ftp["thickness"] for k in ("front", "rear")) / 1e6
    R["mass"]["breakdown_l"] = brk
    R["mass"]["breakdown_kg"] = {k: vv * rho_s / 1000 for k, vv in brk.items()}
    # ---- slats ----
    s = P["slats"]
    wd = mat["wood"]
    I_s = s["width"] * s["thickness"] ** 3 / 12
    W_s = s["width"] * s["thickness"] ** 2 / 6
    a, b = f["x_centre"], s["length"] - f["x_centre"]
    Ls = s["length"]
    g0 = P["loads"]["g"]
    lo = P["loads"]
    seat_x0, seat_x1 = f["x_centre"] + f["armrest"]["flange_width"] / 2, Ls - f["x_centre"] - f["armrest"]["flange_width"] / 2
    seat_len = seat_x1 - seat_x0
    q1 = lo["ur_sf_0450_mass"] * g0 / s["seat_count"] / seat_len
    E_d = wd["E0_mean"]
    E_wh = wd["E_alt"]
    lc_s = {}
    lc_s["UR-SF-0450 (450 kg over the seat)"] = slat_beam(Ls, (a, b), udl=[(seat_x0, seat_x1, q1)], E=E_d, I=I_s, W=W_s)
    lc_s["UR-SF-0450, E from clear-wood data"] = slat_beam(Ls, (a, b), udl=[(seat_x0, seat_x1, q1)], E=E_wh, I=I_s, W=W_s)
    centres = [seat_x0 + seat_len * (k + 0.5) / 3 for k in range(3)]
    pad = lo["seat_pad_length"]

    def pad_udl(xc, F):
        return (xc - pad / 2, xc + pad / 2, F / pad)
    per = s["seat_count"]
    lc_s["EN 581-2 contract, 2000 N on the centre seat"] = slat_beam(
        Ls, (a, b), udl=[pad_udl(centres[1], lo["en581_contract_seat"] / per), pad_udl(centres[0], lo["en581_other_seats"] / per),
                         pad_udl(centres[2], lo["en581_other_seats"] / per)], E=E_d, I=I_s, W=W_s)
    lc_s["EN 581-2 contract, 2000 N on an end seat"] = slat_beam(
        Ls, (a, b), udl=[pad_udl(centres[0], lo["en581_contract_seat"] / per), pad_udl(centres[1], lo["en581_other_seats"] / per),
                         pad_udl(centres[2], lo["en581_other_seats"] / per)], E=E_d, I=I_s, W=W_s)
    lc_s["EN 581-2 back 560 N, all on the upper back slat, centre seat"] = slat_beam(
        Ls, (a, b), udl=[pad_udl(centres[1], lo["en581_back"])], E=E_d, I=I_s, W=W_s)
    lc_s["Three adults of 80 kg, one per seat (service)"] = slat_beam(
        Ls, (a, b), udl=[pad_udl(cx, 80 * g0 / per) for cx in centres], E=E_d, I=I_s, W=W_s)
    k_h = min((150 / s["thickness"]) ** 0.2, wd["k_h_max"])
    f_md = wd["f_mk"] * wd["k_mod_short_sc3"] * k_h / wd["gamma_M"]
    f_md_sc2 = wd["f_mk"] * wd.get("k_mod_short_sc2", wd["k_mod_short_sc3"]) * k_h / wd["gamma_M"]
    R["slats"] = dict(I=I_s, W=W_s, span=b - a, q_ur=q1, seat_len=seat_len, k_h=k_h, f_md=f_md, f_md_sc2=f_md_sc2,
                      f_mk=wd["f_mk"], E_d=E_d, E_wh=E_wh, cases={})
    for k, r in lc_s.items():
        R["slats"]["cases"][k] = dict(Ra=r["Ra"], Rb=r["Rb"], Mmax=r["Mmax"], sigma=r["sigma"], w_span=r["w_span"],
                                      w_end=r["w_end"], sigma_d=lo["gamma_Q"] * r["sigma"], util_d=lo["gamma_Q"] * r["sigma"] / f_md,
                                      ratio_fmk=r["sigma"] / wd["f_mk"], L_over_w=(b - a) / r["w_span"] if r["w_span"] > 0 else None)
    # ---- frame (2D frame model of the more heavily loaded side frame) ----
    keys = B["keys"]
    tw, tf = f["t_web"], f["t_flange"]
    secs = {k: t_section(f[k]["depth"], f[k]["flange_width"], tw, tf) for k in ("seat_rail", "back_rail", "armrest", "rear_leg", "front_post")}
    R["sections"] = {k: {kk: round(vv, 1) for kk, vv in sv.items()} for k, sv in secs.items()}
    za = pr.arm_top - f["armrest"]["depth"] / 2
    post_y = f["front_post"]["depth"] / 2
    seat_cl0 = pr.seat_line(0, pr.T + f["seat_rail"]["depth"] / 2)
    back_cl0 = pr.back_line(0, pr.T + f["back_rail"]["depth"] / 2)
    J = keys["J"]
    p_ps = intersect(seat_cl0, pr.s, v(post_y, 0), v(0, 1))
    p_pa = v(post_y, za)
    p_ab = intersect(v(0, za), v(1, 0), back_cl0, pr.d)
    foot_f = v(post_y, pr.gap)
    foot_r = v(f["rear_leg"]["foot_y"], pr.gap)

    def proj(pt, p0, d):
        return p0 + np.dot(pt - p0, d) * d

    def frame_case(seat_F, back_F=0.0, arm_F=0.0, front_F=0.0):
        """seat_F: list of 3 vertical loads (N) at the seat slats, back_F on the upper back slat (perp.)."""
        fm = Frame2D()
        nf = fm.node(foot_f)
        nps = fm.node(p_ps)
        npa = fm.node(p_pa)
        seat_nodes = [fm.node(proj(pr.seat_line(s0 + pr.W / 2), seat_cl0, pr.s)) for s0 in pr.seat_s]
        nJ = fm.node(J)
        back_nodes = [fm.node(proj(pr.back_line(u0 + pr.W / 2), back_cl0, pr.d)) for u0 in pr.back_u]
        nab = fm.node(p_ab)
        nr_ = fm.node(foot_r)
        narm_mid = fm.node((p_pa + p_ab) / 2)
        fm.elem(nf, nps, secs["front_post"], "front post (lower)")
        fm.elem(nps, npa, secs["front_post"], "front post (upper)")
        chain = [nps] + seat_nodes + [nJ]
        for i0, i1 in zip(chain[:-1], chain[1:]):
            fm.elem(i0, i1, secs["seat_rail"], "seat rail")
        # back rail: J - lower slat - armrest junction - upper slat (sorted along the rail)
        bn = sorted([(np.dot(fm.nodes[k] - J, pr.d), k) for k in back_nodes + [nab]])
        chain = [nJ] + [k for _, k in bn]
        for i0, i1 in zip(chain[:-1], chain[1:]):
            fm.elem(i0, i1, secs["back_rail"], "back rail")
        fm.elem(npa, narm_mid, secs["armrest"], "armrest")
        fm.elem(narm_mid, nab, secs["armrest"], "armrest")
        fm.elem(nJ, nr_, secs["rear_leg"], "rear leg")
        fm.fix = [(nf, [0, 1]), (nr_, [0, 1])]
        for k, F in zip(seat_nodes, seat_F):
            fm.loads[k] = np.array([0.0, -F, 0.0])
        if front_F:
            fm.loads[seat_nodes[0]] = fm.loads.get(seat_nodes[0], np.zeros(3)) + np.array([0.0, -front_F, 0.0])
        if back_F:
            fb = back_F * pr.nr
            fm.loads[back_nodes[1]] = np.array([fb[0], fb[1], 0.0])
        if arm_F:
            fm.loads[narm_mid] = np.array([0.0, -arm_F, 0.0])
        u, Rx, res = fm.solve()
        smax = max(res, key=lambda r: r["sigma"])
        disp = max(np.hypot(u[3 * k], u[3 * k + 1]) for k in range(len(fm.nodes)))
        return dict(sigma_max=smax["sigma"], member=smax["name"], disp_max=float(disp),
                    R_front=float(Rx[3 * nf + 1]), R_rear=float(Rx[3 * nr_ + 1]),
                    H_front=float(Rx[3 * nf]), H_rear=float(Rx[3 * nr_]), members=res, nodes=[n.tolist() for n in fm.nodes])

    frac_end = (b - centres[0]) / (b - a)
    frac_mid = (b - centres[1]) / (b - a)
    frac_far = (b - centres[2]) / (b - a)
    tot = lo["ur_sf_0450_mass"] * g0
    lc_f = {}
    lc_f["UR-SF-0450, 450 kg over the seat"] = frame_case([tot / 2 / per] * per)
    near = (lo["en581_contract_seat"] * frac_end + lo["en581_other_seats"] * (frac_mid + frac_far))
    lc_f["EN 581-2 contract, seat 2000 N (end seat) + 750 N + 750 N, back 560 N"] = frame_case([near / per] * per, back_F=lo["en581_back"] * frac_end)
    lc_f["EN 581-2 contract, arm downward 900 N"] = frame_case([0, 0, 0], arm_F=lo["en581_arm_down"])
    lc_f["EN 581-2 contract, seat front edge 1300 N (end seat)"] = frame_case([0, 0, 0], front_F=lo["en581_front_edge"] * frac_end)
    Rp = mat["cast_steel"]["Rp02"]
    R["frame"] = dict(fractions=dict(end=frac_end, mid=frac_mid, far=frac_far), cases={})
    for k, r in lc_f.items():
        R["frame"]["cases"][k] = dict(sigma_max=r["sigma_max"], member=r["member"], disp_max=r["disp_max"],
                                      util_test=r["sigma_max"] / Rp, util_uls=lo["gamma_Q"] * r["sigma_max"] / (Rp / lo["gamma_M0_steel"]),
                                      R_front=r["R_front"], R_rear=r["R_rear"], H_front=r["H_front"], H_rear=r["H_rear"])
    # out-of-plane hand check: 400 N sideways at the armrest front end, post as a cantilever from the seat rail
    h_post = float(p_pa[1] - p_ps[1])
    s_side = 400 * h_post / secs["front_post"]["W_oop"]
    R["frame"]["side_load"] = dict(F=400, lever=h_post, sigma=s_side, util_uls=lo["gamma_Q"] * s_side / Rp)
    # D20's own check of the seat bar: 40 x 14 mm bar, 150 kg on a frame
    R["frame"]["world_check"] = dict(section="40 x 14", W_flat=40 * 14 ** 2 / 6, W_edge=14 * 40 ** 2 / 6)
    return R


# --------------------------------------------------------------------------
# 7. Variants for the sensitivity of the frame mass
# --------------------------------------------------------------------------
def frame_variant_mass(t):
    """Bare frame mass with web and flanges of thickness t (same layout)."""
    saved = (P["frame"]["t_web"], P["frame"]["t_flange"])
    P["frame"]["t_web"], P["frame"]["t_flange"] = t, t
    try:
        pr = Profile(P)
        fr, _ = frame_solid(pr, P["frame"]["x_centre"])
        return fr.volume / 1e9 * P["materials"]["steel_density"]
    finally:
        P["frame"]["t_web"], P["frame"]["t_flange"] = saved


# --------------------------------------------------------------------------
# 8. Export STEP and GLB
# --------------------------------------------------------------------------
def labelled(sh, name, rgb):
    sh = sh.moved(Location())
    sh.label = name
    sh.color = Color(*rgb)
    return sh


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def assembly(B, colour="GRY", explode=None):
    fr_rgb = hex_rgb(P["materials"]["colours"][colour]["srgb_approx"])
    wood = (0.69, 0.53, 0.33)
    zinc = (0.72, 0.73, 0.74)
    ch = []
    ex = explode or {}
    ch.append(labelled(Pos(-ex.get("frame", 0), 0, 0) * B["frame_L"], "frame_left", fr_rgb))
    ch.append(labelled(Pos(ex.get("frame", 0), 0, 0) * B["frame_R"], "frame_right", fr_rgb))
    for i, s in enumerate(B["seats"]):
        ch.append(labelled(Pos(0, 0, ex.get("slat", 0)) * s, f"slat_seat_{i + 1}", wood))
    for j, s in enumerate(B["backs"]):
        ch.append(labelled(Pos(0, ex.get("slat", 0) * 0.6, ex.get("slat", 0)) * s, f"slat_back_{j + 1}", wood))
    hw = []
    for k, (b, w, n) in enumerate(zip(B["bolts"], B["washers"], B["nuts"])):
        xsgn = -1 if b.center().X < P["slats"]["length"] / 2 else 1
        hw.append(labelled(Pos(0, 0, ex.get("bolt", 0)) * b, f"bolt_{k + 1}", zinc))
        hw.append(labelled(Pos(xsgn * ex.get("frame", 0) * 0.5, 0, -ex.get("nut", 0)) * w, f"washer_{k + 1}", zinc))
        hw.append(labelled(Pos(xsgn * ex.get("frame", 0) * 0.5, 0, -ex.get("nut", 0)) * n, f"nut_{k + 1}", zinc))
    ch.append(Compound(children=hw, label="fixings"))
    return Compound(children=ch, label="Serra_180_" + colour)


def export_all(B, C, K):
    sd, gd = HERE / "step", HERE / "glb"
    sd.mkdir(exist_ok=True)
    gd.mkdir(exist_ok=True)
    asm = assembly(B)
    export_step(asm, sd / "VI-B180_assembly.step", timestamp="2026-11-17T00:00:00")
    fr_rgb = hex_rgb(P["materials"]["colours"]["GRY"]["srgb_approx"])
    export_step(Compound(children=[labelled(B["frame_L"], "VI-C180_side_frame", fr_rgb)], label="VI-C180"), sd / "VI-C180_side_frame.step", timestamp="2026-11-17T00:00:00")
    export_step(Compound(children=[labelled(B["slat"], "VI-B180-03_slat", (0.69, 0.53, 0.33))], label="VI-B180-03"), sd / "VI-B180-03_slat.step", timestamp="2026-11-17T00:00:00")
    fx = Compound(children=[labelled(B["bolt"], "carriage_bolt_M8x60", (0.72, 0.73, 0.74)),
                            labelled(B["washer"], "washer_8", (0.72, 0.73, 0.74)),
                            labelled(B["nut"], "nut_M8", (0.72, 0.73, 0.74))], label="VI-B180-04_fixing")
    export_step(fx, sd / "VI-B180-04_fixing_M8.step", timestamp="2026-11-17T00:00:00")
    export_step(C["cluster"], sd / "VI-C180_mould_cluster.step", timestamp="2026-11-17T00:00:00")
    pal = Compound(children=[labelled(p, f"pallet_{i}", (0.80, 0.68, 0.48)) for i, p in enumerate(K["pallet_parts"])], label="pallet")
    export_step(pal, sd / "VI-B180_pallet.step", timestamp="2026-11-17T00:00:00")
    # GLB (metres for three.js, tolerances in mm)
    for col in ("GRY", "GRN"):
        export_gltf(assembly(B, col), gd / f"serra180_{col}.glb", binary=True, linear_deflection=0.4, angular_deflection=0.35)
    # parcels: two frame cartons side by side, the slat bundle in front of them
    co = K["carton_outer"]
    bu = K["bundle"]
    parc = []
    parc.append(labelled(Pos(co[0] / 2, co[1] / 2, co[2] / 2) * Box(*co), "carton_1", (0.72, 0.58, 0.40)))
    parc.append(labelled(Pos(co[0] * 1.5 + 120, co[1] / 2, co[2] / 2) * Box(*co), "carton_2", (0.72, 0.58, 0.40)))
    W, T = P["slats"]["width"], P["slats"]["thickness"]
    e = P["packaging"]["slat_bundle"]["edge_protector_thickness"]
    yb = -bu[1] - 180
    x0 = (2 * co[0] + 120 - bu[0]) / 2
    sl = B["slat"]
    k = 0
    for row, n in ((0, 3), (1, 2)):
        for i in range(n):
            y = yb + e + (i + (0.5 if row else 0)) * W
            z = T * (row + 1)
            parc.append(labelled(Pos(x0, y, z) * sl, f"bundle_slat_{k}", (0.69, 0.53, 0.33)))
            k += 1
    for xs in (0.12, 0.38, 0.62, 0.88):
        x = x0 + xs * P["slats"]["length"]
        parc.append(labelled(Pos(x, yb + bu[1] / 2, bu[2] / 2) * (Box(16, bu[1] + 1.6, bu[2] + 1.6) - Box(17, bu[1], bu[2])), f"strap_{xs}", (0.15, 0.30, 0.55)))
    export_gltf(Compound(children=parc, label="parcels"), gd / "serra180_parcels.glb", binary=True, linear_deflection=0.5, angular_deflection=0.4)
    # pallet of four benches
    pl = [labelled(p, f"pallet_{i}", (0.80, 0.68, 0.48)) for i, p in enumerate(K["pallet_parts"])]
    for i, (kind, sh) in enumerate(K["load"]):
        pl.append(labelled(sh, f"{kind}_{i}", (0.72, 0.58, 0.40) if kind == "carton" else (0.69, 0.53, 0.33)))
    export_gltf(Compound(children=pl, label="pallet_load"), gd / "serra180_pallet.glb", binary=True, linear_deflection=1.0, angular_deflection=0.5)
    return asm


# --------------------------------------------------------------------------
# 9. Drawings (SVG, A3 landscape, mm)
# --------------------------------------------------------------------------
def unit(a):
    a = np.array(a, float)
    return a / np.linalg.norm(a)


def project(shape, n, up, hidden=True):
    """Orthographic hidden-line projection. Returns (visible, hidden) polylines in world-consistent 2D
    coordinates u = P.X, v = P.Y, with Y = up (made perpendicular) and X = n x Y."""
    n = unit(n)
    up = np.array(up, float)
    Y = unit(up - np.dot(up, n) * n)
    X = np.cross(n, Y)
    bb = shape.bounding_box()
    c = np.array([(bb.min.X + bb.max.X) / 2, (bb.min.Y + bb.max.Y) / 2, (bb.min.Z + bb.max.Z) / 2])
    O = c - 20000 * n
    vis, hid = shape.project_to_viewport(tuple(O), tuple(Y), tuple(c))
    du, dv = float(np.dot(O, X)), float(np.dot(O, Y))

    def pl(edges):
        out = []
        for e in edges:
            Lh = e.length
            if Lh < 1e-6:
                continue
            k = 2 if e.geom_type.name == "LINE" else max(3, min(60, int(Lh / 1.5) + 2))
            pts = [e @ t for t in np.linspace(0, 1, k)]
            out.append([(p.X + du, p.Y + dv) for p in pts])
        return out
    return pl(vis), (pl(hid) if hidden else [])


def to2d(p3, n, up):
    n = unit(n)
    up = np.array(up, float)
    Y = unit(up - np.dot(up, n) * n)
    X = np.cross(n, Y)
    p3 = np.array(p3, float)
    return float(np.dot(p3, X)), float(np.dot(p3, Y))


VIEWS = {
    "front": ((0, 1, 0), (0, 0, 1)),
    "left": ((1, 0, 0), (0, 0, 1)),
    "inside": ((-1, 0, 0), (0, 0, 1)),
    "top": ((0, 0, -1), (0, 1, 0)),
    "iso": ((0.62, 0.95, -0.62), (0, 0, 1)),
}


def fmt(x, nd=0):
    if nd == 0:
        return f"{x:.0f}"
    return f"{x:.{nd}f}"


class Sheet:
    def __init__(self, number, title, scale, size=(420, 297)):
        self.number, self.title, self.scale, self.size = number, title, scale, size
        self.el = []

    def add(self, s):
        self.el.append(s)

    def line(self, pts, cls="vis"):
        d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
        self.add(f'<polyline class="{cls}" points="{d}"/>')

    def text(self, x, y, s, size=2.5, anchor="start", rot=0, weight="normal", cls="txt"):
        tr = f' transform="rotate({rot:.2f} {x:.2f} {y:.2f})"' if rot else ""
        s = str(s).replace("&", "&amp;").replace("<", "&lt;")
        self.add(f'<text class="{cls}" x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}"{tr}>{s}</text>')

    def rect(self, x, y, w, h, cls="frame"):
        self.add(f'<rect class="{cls}" x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}"/>')

    def arrow(self, tip, dirv):
        d = unit(dirv)
        nrm = np.array([-d[1], d[0]])
        t = np.array(tip)
        b = t - 2.6 * d
        p1, p2 = b + 0.55 * nrm, b - 0.55 * nrm
        self.add(f'<polygon class="arr" points="{t[0]:.2f},{t[1]:.2f} {p1[0]:.2f},{p1[1]:.2f} {p2[0]:.2f},{p2[1]:.2f}"/>')

    def dim(self, p1, p2, off, text=None, orient="h", size=2.5):
        """Dimension between paper points p1, p2. orient h/v/a; off: offset of the dimension line (mm, signed)."""
        p1, p2 = np.array(p1, float), np.array(p2, float)
        if orient == "h":
            d = np.array([1.0, 0.0])
        elif orient == "v":
            d = np.array([0.0, -1.0])
        else:
            d = unit(p2 - p1)
        nrm = np.array([-d[1], d[0]])
        a = p1 + nrm * (off + np.dot(p1 - p1, nrm))
        # dimension line points on the line through a with direction d
        base = p1 + nrm * off if orient == "a" else None
        if orient == "h":
            y = p1[1] + off if abs(off) > 0 else p1[1]
            y = min(p1[1], p2[1]) + off if off < 0 else max(p1[1], p2[1]) + off
            q1, q2 = np.array([p1[0], y]), np.array([p2[0], y])
        elif orient == "v":
            x = max(p1[0], p2[0]) + off if off > 0 else min(p1[0], p2[0]) + off
            q1, q2 = np.array([x, p1[1]]), np.array([x, p2[1]])
        else:
            q1, q2 = p1 + nrm * off, p2 + nrm * off
        for p, q in ((p1, q1), (p2, q2)):
            e = q - p
            L = np.linalg.norm(e)
            if L > 0.3:
                u_ = e / L
                self.line([tuple(p + 0.8 * u_), tuple(q + 1.2 * u_)], "ext")
        self.line([tuple(q1), tuple(q2)], "dimln")
        L = np.linalg.norm(q2 - q1)
        if L < 1e-6:
            return
        u_ = (q2 - q1) / L
        if L > 7:
            self.arrow(q1, -u_)
            self.arrow(q2, u_)
        else:
            self.arrow(q1, u_)
            self.arrow(q2, -u_)
        m = (q1 + q2) / 2
        ang = math.degrees(math.atan2(u_[1], u_[0]))
        if ang > 90.1 or ang < -89.9:
            ang += 180
        tn = np.array([u_[1], -u_[0]])
        if tn[1] > 0:
            tn = -tn
        pos = m + tn * 0.9
        if L < 7:
            pos = q2 + u_ * (4 + len(str(text)) * 0.9) + tn * 0.9
        self.text(pos[0], pos[1], text, size=size, anchor="middle", rot=ang)

    def leader(self, p, q, s, size=2.5):
        self.line([p, q, (q[0] + (8 if q[0] >= p[0] else -8), q[1])], "dimln")
        self.arrow(p, np.array(p) - np.array(q))
        self.text(q[0] + (9 if q[0] >= p[0] else -9), q[1] - 0.6, s, size=size, anchor="start" if q[0] >= p[0] else "end")

    def balloon(self, p, q, n):
        self.line([p, q], "dimln")
        self.add(f'<circle class="dot" cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="0.6"/>')
        self.add(f'<circle class="vis" cx="{q[0]:.2f}" cy="{q[1]:.2f}" r="3.6" fill="white"/>')
        self.text(q[0], q[1] + 1.2, n, size=3.5, anchor="middle")

    def title_block(self, mass=None, material=None, notes=()):
        W, H = self.size
        x0, y0 = W - 10 - 180, H - 10 - 38
        self.rect(x0, y0, 180, 38, "tb")
        pr = P["product"]
        rows = [(x0, y0, 180, 9)]
        self.line([(x0, y0 + 9), (x0 + 180, y0 + 9)], "tbl")
        self.text(x0 + 3, y0 + 6.2, "Valdara Industries", 5, weight="bold")
        self.text(x0 + 177, y0 + 6.2, "Ferrano, Urvania", 2.5, anchor="end")
        self.line([(x0, y0 + 21), (x0 + 180, y0 + 21)], "tbl")
        self.text(x0 + 3, y0 + 12.5, "Title", 1.8, cls="lbl")
        self.text(x0 + 3, y0 + 18.4, f"Serra 180 – {self.title}", 4.2, weight="bold")
        cols = [("Drawing no.", f"{pr['drawing_prefix']}-{self.number}"), ("Rev.", pr["revision"]),
                ("Scale", self.scale), ("Size", "A3" if self.size[0] == 420 else "A4"),
                ("Date", pr["drawing_date"]), ("Units", "mm")]
        widths = [52, 12, 22, 14, 26, 14]
        xx = x0
        for (lab, val), w in zip(cols, widths):
            self.text(xx + 1.5, y0 + 24, lab, 1.8, cls="lbl")
            self.text(xx + 1.5, y0 + 29, val, 3.0)
            xx += w
            if xx < x0 + 180:
                self.line([(xx, y0 + 21), (xx, y0 + 30.5)], "tbl")
        self.line([(x0 + 140, y0 + 21), (x0 + 140, y0 + 38)], "tbl")
        self.text(x0 + 141.5, y0 + 24, "Item", 1.8, cls="lbl")
        self.text(x0 + 141.5, y0 + 29, pr["item_number"], 3.0)
        self.line([(x0, y0 + 30.5), (x0 + 180, y0 + 30.5)], "tbl")
        self.text(x0 + 1.5, y0 + 33, "Material / mass", 1.8, cls="lbl")
        self.text(x0 + 1.5, y0 + 36.8, (material or "see bill of materials") + (f"   mass {mass}" if mass else ""), 2.4)
        self.text(x0 + 141.5, y0 + 33, "Projection", 1.8, cls="lbl")
        self.text(x0 + 141.5, y0 + 36.8, "first angle (ISO 5456-2)", 2.0)
        return x0, y0

    def notes(self, x, y, lines, size=2.3, head="Notes"):
        self.text(x, y, head, 3.0, weight="bold")
        for i, s in enumerate(lines):
            self.text(x, y + 4.5 + i * (size + 1.4), s, size)

    def save(self, path):
        W, H = self.size
        css = """
        .vis{fill:none;stroke:#000;stroke-width:0.45;stroke-linejoin:round;stroke-linecap:round}
        .thin{fill:none;stroke:#000;stroke-width:0.25}
        .hid{fill:none;stroke:#000;stroke-width:0.22;stroke-dasharray:1.6,0.9}
        .ctr{fill:none;stroke:#000;stroke-width:0.18;stroke-dasharray:6,1,1,1}
        .ext{fill:none;stroke:#000;stroke-width:0.16}
        .dimln{fill:none;stroke:#000;stroke-width:0.18}
        .arr{fill:#000;stroke:none}
        .dot{fill:#000}
        .frame{fill:none;stroke:#000;stroke-width:0.7}
        .tb{fill:none;stroke:#000;stroke-width:0.6}
        .tbl{fill:none;stroke:#000;stroke-width:0.3}
        .sec{fill:url(#hatch);stroke:#000;stroke-width:0.45;fill-rule:evenodd}
        .txt{font-family:'DejaVu Sans','Liberation Sans',Arial,Helvetica,sans-serif;fill:#000}
        .lbl{font-family:'DejaVu Sans','Liberation Sans',Arial,Helvetica,sans-serif;fill:#555}
        .cut{fill:none;stroke:#000;stroke-width:0.7}
        .box{fill:none;stroke:#000;stroke-width:0.3}
        .fillg{fill:#e8e8e8;stroke:#000;stroke-width:0.3}
        """
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">'
                f'<title>Valdara Industries, Serra 180 – {self.title} ({P["product"]["drawing_prefix"]}-{self.number})</title>'
                f'<defs><style>{css}</style><pattern id="hatch" width="2" height="2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
                f'<line x1="0" y1="0" x2="0" y2="2" stroke="#000" stroke-width="0.18"/></pattern></defs>'
                f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>'
                f'<rect class="frame" x="10" y="10" width="{W - 20}" height="{H - 20}"/>')
        Path(path).write_text(head + "\n".join(self.el) + "</svg>\n", encoding="utf-8")


class ViewMap:
    def __init__(self, ox, oy, k):
        self.ox, self.oy, self.k = ox, oy, k

    def __call__(self, u, v_):
        return (self.ox + self.k * u, self.oy - self.k * v_)


def draw_proj(sh, vm, vis, hid):
    for pl in hid:
        sh.line([vm(*p) for p in pl], "hid")
    for pl in vis:
        sh.line([vm(*p) for p in pl], "vis")


def section_polys(solid, origin, xdir, normal):
    """Cut 'solid' with a plane; return polygons (lists of local 2D points) of the cut faces."""
    pl = Plane(origin=tuple(origin), x_dir=tuple(xdir), z_dir=tuple(normal))
    from build123d import Rectangle
    cut = solid & (pl * Rectangle(150, 150))
    loc = pl.to_local_coords(cut)
    polys = []
    for fc in loc.faces():
        for w in [fc.outer_wire()] + list(fc.inner_wires()):
            pts = []
            for e in w.order_edges():
                k = 2 if e.geom_type.name == "LINE" else 12
                pts += [(p.X, p.Y) for p in [e @ t for t in np.linspace(0, 1, k)]]
            polys.append(pts)
    return polys


def draw_section(sh, polys, cx, cy, k, label, dims=True):
    allp = np.array([p for pl in polys for p in pl])
    mn, mx = allp.min(0), allp.max(0)
    c = (mn + mx) / 2

    def m(p):
        return (cx + k * (p[0] - c[0]), cy - k * (p[1] - c[1]))
    d = " ".join("M " + " L ".join(f"{m(p)[0]:.2f},{m(p)[1]:.2f}" for p in pl) + " Z" for pl in polys)
    sh.add(f'<path class="sec" d="{d}"/>')
    w, h = (mx - mn) * k
    if dims:
        sh.dim((cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2), 5, fmt(mx[0] - mn[0]), "h")
        sh.dim((cx + w / 2, cy - h / 2), (cx + w / 2, cy + h / 2), 5, fmt(mx[1] - mn[1]), "v")
    sh.text(cx, cy - h / 2 - 4, label, 3.5, anchor="middle", weight="bold")
    return w, h


def make_drawings(B, R, C, K):
    dd = HERE / "drawings"
    dd.mkdir(exist_ok=True)
    pr = B["pr"]
    f = P["frame"]
    mass = R["mass"]
    bench = Compound(children=[x.moved(Location()) for x in [B["frame_L"], B["frame_R"]] + B["seats"] + B["backs"] + B["bolts"] + B["washers"] + B["nuts"]])
    # sanity: projection mapping
    probe = Pos(300, 200, 100) * Box(10, 10, 10)
    for name, (n, up) in VIEWS.items():
        vis, _ = project(probe, n, up, hidden=False)
        pts = np.array([p for pl in vis for p in pl])
        exp = to2d((300, 200, 100), n, up)
        assert np.allclose(pts.mean(0), exp, atol=1.0), (name, pts.mean(0), exp)
    sheets = []
    # ---------------- 001 general arrangement ----------------
    s = Sheet("001", "General arrangement", "1:10")
    k = 0.1
    fv = project(bench, *VIEWS["front"], hidden=False)
    lv = project(bench, *VIEWS["left"], hidden=False)
    tv = project(bench, *VIEWS["top"], hidden=False)
    vf = ViewMap(30, 112, k)               # front view: u = x, v = z
    vl = ViewMap(320, 112, k)              # left view: u = -y
    vt = ViewMap(30, 140 + 0, k)           # top view: u = x, v = y (below the front view; back at top)
    vt = ViewMap(30, 205, k)
    draw_proj(s, vf, *fv)
    draw_proj(s, vl, *lv)
    draw_proj(s, vt, *tv)
    s.text(120, 132, "FRONT VIEW", 3.5, anchor="middle", weight="bold")
    s.text(289, 132, "VIEW FROM THE LEFT", 3.5, anchor="middle", weight="bold")
    s.text(120, 222, "TOP VIEW", 3.5, anchor="middle", weight="bold")
    D = R["dims"]
    L = P["slats"]["length"]
    s.dim(vf(0, D["height"]), vf(L, D["height"]), -6, f"{fmt(L)} over the slats")
    s.dim(vf(f["x_centre"] - f["armrest"]["flange_width"] / 2, D["height"]), vf(L - f["x_centre"] + f["armrest"]["flange_width"] / 2, D["height"]), -13, f"{fmt(D['over_armrests'])} over the armrests")
    s.dim(vf(f["x_centre"], 0), vf(L - f["x_centre"], 0), 8, f"{fmt(D['slat_span'])} frame centres")
    s.dim(vf(0, 0), vf(0, D["height"]), -6, fmt(D["height"]), "v")
    s.dim(vf(L, 0), vf(L, pr.Hs), 6, f"{fmt(pr.Hs)} ({P['overall']['seat_height_range'][0]}–{P['overall']['seat_height_range'][1]})", "v")
    s.dim(vf(L, 0), vf(L, pr.arm_top), 16, fmt(pr.arm_top), "v")
    s.line([vf(-10, 0), vf(L + 30, 0)], "thin")
    s.text(*vf(L + 35, 2), "ground", 2.2)
    # left view dims (u = -y)
    s.dim(vl(-P["overall"]["depth"], 0), vl(0, 0), 8, fmt(D["depth"]))
    Fp, Pp = pr.F, pr.Pt
    s.dim(vl(-Fp[0], Fp[1]), vl(-Pp[0], Pp[1]), 8, f"seat depth {fmt(pr.SD)}", "a")
    bt = pr.back_line(pr.back_u[1] + pr.W)
    s.dim(vl(-bt[0], bt[1]), vl(0, bt[1]), -4, f"{fmt(bt[0])} front to top of back")
    s.leader(vl(-(Fp[0] + 150), Fp[1] - 10), (vl(0, 0)[0] + 14, vl(0, 520)[1]), f"seat tilt {P['ergonomics']['seat_tilt_deg']}°")
    s.leader(vl(-(Pp[0] + 0.3 * 200 * math.sin(pr.beta)), Pp[1] + 200), (vl(0, 0)[0] + 14, vl(0, 600)[1]), f"seat to back {P['ergonomics']['seat_back_angle_deg']}°")
    s.leader(vl(-50, pr.arm_top), (vl(0, 0)[0] + 14, vl(0, 690)[1]), f"armrest {fmt(P['ergonomics']['armrest_above_seat'])} above seat")
    s.dim(vl(-P["overall"]["depth"], 0), vl(-P["overall"]["depth"], D["height"]), -6, fmt(D["height"]), "v")
    # top view dims
    s.dim(vt(0, 0), vt(0, P["overall"]["depth"]), -6, fmt(P["overall"]["depth"]), "v")
    s.dim(vt(L, 0), vt(L, pr.F[0]), 6, fmt(pr.F[0]), "v")
    for xh in (f["x_centre"],):
        s.line([vt(xh, -15), vt(xh, P["overall"]["depth"] + 15)], "ctr")
        s.line([vt(L - xh, -15), vt(L - xh, P["overall"]["depth"] + 15)], "ctr")
    s.notes(232, 150, [
        f"1  Seat height {fmt(pr.Hs)} mm at the front edge of the seat when anchored, with the",
        f"   frames {fmt(P['overall']['levelling_gap_nominal'])} mm above the plinth on levelling nuts; adjustable",
        f"   {P['overall']['seat_height_range'][0]} to {P['overall']['seat_height_range'][1]} mm (gap 0 to 20 mm, grouted after levelling).",
        "2  Fixed to the ground by four M12 ground anchors (separate item),",
        "   two per side frame, through the Ø14 holes in the feet.",
        f"3  Slats: 5, {fmt(P['slats']['length'])} x {fmt(P['slats']['width'])} x {fmt(P['slats']['thickness'])}, thermally modified ash (oak",
        f"   until April); 3 on the seat (gaps {fmt(P['slats']['seat_gap'])}), 2 on the back; 20 carriage",
        "   bolts M8 x 60, nuts and washers in stainless steel A2 (A4 at the coast).",
        f"4  Overall: {fmt(L)} long over the slats, {fmt(D['over_armrests'])} over the armrests,",
        f"   {fmt(D['depth'])} deep, {fmt(D['height'])} high. Seat width between the",
        f"   armrests {fmt(D['between_armrests'])} = 3 x {fmt(D['seat_width_per_person'])}.",
        f"5  Bench net mass {mass['net']:.1f} kg (frames galvanised and coated).",
        "6  Load: UR-SF-0450, 450 kg on the seat, 1 h, no lasting",
        "   deformation; checked also against EN 581-2 (contract use).",
    ])
    s.title_block(mass=f"{mass['net']:.1f} kg net", material="see BOM, drawing 005")
    s.save(dd / "VI-DWG-B180-001_general_arrangement.svg")
    sheets.append("001")
    # ---------------- 002 side frame ----------------
    s = Sheet("002", "Side frame VI-C180, cast steel", "1:4, 1:2")
    k = 0.25
    fr = B["frame_L"]
    iv = project(fr, *VIEWS["inside"])
    gap = pr.gap
    vi = ViewMap(40, 245, k)          # u = y, v = z ; datum: underside of the feet (z = gap)
    draw_proj(s, ViewMap(40, 245 - gap * k * 0, k), *iv)
    def vz(y, z):
        return vi(y, z)
    s.text(40 + 310 * k, 25, "VIEW FROM THE BENCH CENTRE", 3.5, anchor="middle", weight="bold")
    keys = B["keys"]
    # datums
    s.line([vz(-20, gap), vz(650, gap)], "ctr")
    s.text(*vz(655, gap - 2), "datum A (underside of feet)", 2.0)
    s.dim(vz(0, gap), vz(P["overall"]["depth"], gap), 10 if False else 9, fmt(P["overall"]["depth"]))
    ftp = f["feet"]
    s.dim(vz(0, gap), vz(ftp["front"]["hole_y"], gap), 16, fmt(ftp["front"]["hole_y"]))
    s.dim(vz(0, gap), vz(ftp["rear"]["hole_y"], gap), 22, fmt(ftp["rear"]["hole_y"]))
    s.dim(vz(ftp["rear"]["y0"], gap), vz(ftp["rear"]["y1"], gap), 4, fmt(ftp["rear"]["y1"] - ftp["rear"]["y0"]))
    s.dim(vz(0, gap), vz(ftp["front"]["y1"], gap), 4, fmt(ftp["front"]["y1"]))
    zt = keys["brr_top"]
    top_z = max(keys["bf_top"][1], zt[1])
    s.dim(vz(0, gap), vz(0, pr.arm_top), -8, fmt(pr.arm_top - gap), "v")
    s.dim(vz(0, gap), vz(0, keys["sr_top_front"][1]), -16, fmt(keys["sr_top_front"][1] - gap, 0), "v")
    s.dim(vz(P["overall"]["depth"], gap), vz(P["overall"]["depth"], top_z), 8, fmt(top_z - gap), "v")
    s.dim(vz(0, pr.arm_top), vz(f["front_post"]["depth"], pr.arm_top), -6, fmt(f["front_post"]["depth"]))
    s.dim(vz(keys["y_arm_end"] - 60, pr.arm_top), vz(keys["y_arm_end"] - 60, pr.arm_top - f["armrest"]["depth"]), 4, fmt(f["armrest"]["depth"]), "v")
    s.leader(vz(*(pr.seat_line(200, pr.T))), (vz(250, 560)[0], vz(250, 560)[1]), f"seat rail, top {P['ergonomics']['seat_tilt_deg']}° to horizontal")
    s.leader(vz(*(pr.back_line(330, pr.T))), (vz(420, 830)[0], vz(420, 830)[1]), f"back rail, front face {math.degrees(pr.beta):.0f}° to vertical")
    s.leader(vz(ftp["rear"]["hole_y"], gap + ftp["thickness"]), (vz(420, 90)[0], vz(420, 90)[1]), f"2 x Ø{ftp['hole_diameter']} anchor holes")
    # section cuts
    secs_def = []
    def cutline(p, d_, lab):
        nrm = v(-d_[1], d_[0])
        a, b_ = p - 32 * nrm, p + 32 * nrm
        s.line([vz(*a), vz(*(a + 9 * nrm))], "cut")
        s.line([vz(*b_), vz(*(b_ - 9 * nrm))], "cut")
        s.text(*vz(*(a - 6 * nrm)), lab, 3.5, anchor="middle", weight="bold")
        s.text(*vz(*(b_ + 6 * nrm)), lab, 3.5, anchor="middle", weight="bold")
    J = keys["J"]
    mid_seat = pr.seat_line(150, pr.T + f["seat_rail"]["depth"] / 2)
    mid_back = pr.back_line(130, pr.T + f["back_rail"]["depth"] / 2)
    mid_arm = v(260, pr.arm_top - f["armrest"]["depth"] / 2)
    mid_post = v(f["front_post"]["depth"] / 2, 220)
    leg_d = keys["dl"]
    mid_leg = J + 0.5 * (v(f["rear_leg"]["foot_y"], gap) - J)
    for p, d_, lab in ((mid_seat, pr.s, "A"), (mid_back, pr.d, "B"), (mid_arm, v(1, 0), "C"), (mid_post, v(0, 1), "D"), (mid_leg, leg_d, "E")):
        cutline(p, d_, lab)
        secs_def.append((p, d_, lab))
    # sections (1:2), viewed along the member
    xs, ys = 268, 52
    pos = [(255, 55), (335, 55), (255, 105), (335, 105), (255, 150)]
    names = {"A": "seat rail", "B": "back rail", "C": "armrest", "D": "front post", "E": "rear leg"}
    for (p, d_, lab), (cx, cy) in zip(secs_def, pos):
        nrm = v(-d_[1], d_[0])
        xd = (-1, 0, 0) if lab in ("A", "C") else (1, 0, 0)       # flange of seat rail and armrest drawn on top
        polys = section_polys(fr, (f["x_centre"], p[0], p[1]), xd, (0, d_[0], d_[1]))
        draw_section(s, polys, cx, cy, 0.5, f"{lab}–{lab}  {names[lab]}")
    s.text(372, 172, "", 2)
    # hole table
    rows = []
    hx = bolt_x_offsets(f["x_centre"])
    for i, (pnt, axis) in enumerate(bolt_points(pr)):
        q = pnt + pr.T * axis
        rows.append((f"H{i + 1}", "seat" if i < 3 else "back", q[0], q[1] - gap, math.degrees(math.atan2(-axis[0], -axis[1])) if i < 3 else math.degrees(math.atan2(axis[1], axis[0]))))
    tx, ty = 300, 140
    s.text(tx, ty, "Bolt holes Ø" + fmt(f["steel_hole_diameter"]) + " through flange, 2 per point at x = web ±20", 2.4, weight="bold")
    s.text(tx, ty + 5, "hole   rail    y        z (from A)   axis", 2.2)
    for i, r in enumerate(rows):
        s.text(tx, ty + 9.5 + i * 3.6, f"{r[0]:<5}  {r[1]:<5}  {r[2]:6.1f}   {r[3]:6.1f}       normal to rail", 2.2)
    s.notes(232, 205, [
        f"1  Material {P['materials']['cast_steel']['grade']}, Rp0.2 ≥ {P['materials']['cast_steel']['Rp02']} MPa.",
        f"2  Walls {f['t_web']} mm (web and flanges); concave radii R{f['fillet_concave']}, edges R{f['round_convex']}.",
        f"3  Draft {f['draft_deg']}° on faces normal to the parting plane (web mid-plane).",
        "4  Symmetric about the web mid-plane: one casting for both sides.",
        "5  Open T-sections only, no closed cavities (EN ISO 14713-2);",
        "   hang for galvanising from the anchor holes, armrest down.",
        f"6  Hot-dip galvanised EN ISO 1461 (≥ {P['materials']['galvanising']['mean_min_um']} µm mean), then",
        f"   powder coated {P['materials']['powder_coat']['thickness_um']} µm, RAL 7011 / 6005 approx.",
        "7  General tolerances ISO 8062-3 DCTG 10; holes drilled ±0.3.",
        "8  Melt number cast in (loose letters, per casting day); serial number",
        "   hard-stamped on the inside of the rear leg after fettling.",
    ], size=2.2)
    s.title_block(mass=f"{mass['frame_bare']:.1f} kg cast, {mass['frame']:.1f} kg coated", material=P["materials"]["cast_steel"]["grade"])
    s.save(dd / "VI-DWG-B180-002_side_frame.svg")
    # ---------------- 003 slat ----------------
    s = Sheet("003", "Slat, thermally modified ash or oak", "1:5, 1:2, 1:1")
    sl = B["slat"]
    k = 0.2
    tvw = project(sl, (0, 0, -1), (0, 1, 0))
    v3 = ViewMap(30, 75, k)
    draw_proj(s, v3, *tvw)
    s.text(30 + 900 * k, 40, "PLAN 1:5 (top face, bolt heads side)", 3.5, anchor="middle", weight="bold")
    Wd = P["slats"]["width"]
    Th = P["slats"]["thickness"]
    s.dim(v3(0, Wd), v3(L, Wd), -7, fmt(L))
    xs_ = P["slats"]["bolt_x_from_end"]
    s.dim(v3(0, 0), v3(xs_[0], 0), 6, fmt(xs_[0]))
    s.dim(v3(0, 0), v3(xs_[1], 0), 12, fmt(xs_[1]))
    s.dim(v3(L - xs_[0], 0), v3(L, 0), 6, fmt(xs_[0]))
    s.dim(v3(L - xs_[1], 0), v3(L, 0), 12, fmt(xs_[1]))
    s.dim(v3(L, 0), v3(L, Wd), 6, fmt(Wd), "v")
    s.line([v3(-8, Wd / 2), v3(L + 8, Wd / 2)], "ctr")
    # end view 1:1, drawn from the profile
    ch = P["slats"]["edge_chamfer"]
    e0 = ViewMap(45, 175, 1.0)
    prof = [(ch, 0), (Wd - ch, 0), (Wd, ch), (Wd, Th - ch), (Wd - ch, Th), (ch, Th), (0, Th - ch), (0, ch), (ch, 0)]
    s.line([e0(*q) for q in prof], "vis")
    hd = P["slats"]["hole_diameter"]
    for yy in (Wd / 2 - hd / 2, Wd / 2 + hd / 2):
        s.line([e0(yy, 0), e0(yy, Th)], "hid")
    s.line([e0(Wd / 2, -5), e0(Wd / 2, Th + 5)], "ctr")
    s.text(45 + Wd / 2, 112, "END VIEW 1:1", 3.5, anchor="middle", weight="bold")
    s.dim(e0(0, 0), e0(Wd, 0), 8, fmt(Wd))
    s.dim(e0(Wd, 0), e0(Wd, Th), 7, fmt(Th), "v")
    s.leader(e0(ch / 2, Th - ch / 2), (e0(40, Th + 16)[0], e0(40, Th + 16)[1]), f"{ch} x 45°, 4 long edges")
    # detail of an end 1:2 in plan
    k5 = 0.5
    dv = project(sl & (Pos(80, Wd / 2, -Th / 2) * Box(160, Wd + 2, Th + 2)), (0, 0, -1), (0, 1, 0), hidden=False)
    v5 = ViewMap(175, 185, k5)
    draw_proj(s, v5, dv[0], [])
    s.text(175 + 80 * k5, 117, "DETAIL OF AN END 1:2 (plan)", 3.5, anchor="middle", weight="bold")
    s.dim(v5(0, Wd), v5(xs_[0], Wd), -6, fmt(xs_[0]))
    s.dim(v5(0, Wd), v5(xs_[1], Wd), -12, fmt(xs_[1]))
    s.dim(v5(0, 0), v5(0, Wd / 2), -6, fmt(Wd / 2, 1), "v")
    s.line([v5(-4, Wd / 2), v5(165, Wd / 2)], "ctr")
    s.leader(v5(xs_[1] + 3.2, Wd / 2 - 3.2), (v5(150, -25)[0], v5(150, -25)[1]), f"4 x Ø{fmt(hd)} through")
    s.text(*v5(162, Wd + 4), "break", 2.0)
    s.notes(232, 205, [
        "1  From May 2026: European ash, graded LS13 (EN 338 D40) before",
        "   thermal modification at about 212 °C; delivered at about 5 %",
        f"   moisture, {P['woods']['tm_ash']['density']} kg/m³, mass {R['woods_mass']['tm_ash']:.2f} kg. Until April: oak heartwood,",
        f"   kiln-dried 12 %, EN 338 D30, {P['woods']['oak']['density']} kg/m³, mass {R['woods_mass']['oak']:.2f} kg. Planed four sides.",
        "2  Holes pre-drilled Ø9; in thermally modified ash the square seat",
        "   of the bolt neck is pre-formed (8.2 mm square, 5 mm deep).",
        "3  Grain parallel to the length; no knots over 20 mm within",
        "   150 mm of the ends; seal the end grain (wax emulsion).",
        "4  Holes on the centre line of the width, at 80 and 120 mm from",
        "   each end (end distance a3,t = max(7d; 80 mm), EN 1995-1-1).",
        "5  Same slat for seat and back; 5 per bench.",
    ], size=2.2)
    s.title_block(mass=f"{R['woods_mass']['tm_ash']:.2f} kg (oak {R['woods_mass']['oak']:.2f} kg)", material="thermally modified ash / oak")
    s.save(dd / "VI-DWG-B180-003_slat.svg")
    # ---------------- 004 exploded assembly ----------------
    s = Sheet("004", "Exploded assembly", "not to scale")
    ex = assembly(B, explode={"frame": 420, "slat": 260, "bolt": 140, "nut": 90})
    n, up = VIEWS["iso"]
    iso = project(ex, n, up)
    allp = np.array([p for pl in iso[0] for p in pl])
    mn, mx = allp.min(0), allp.max(0)
    kk = min(330 / (mx[0] - mn[0]), 190 / (mx[1] - mn[1]))
    vi4 = ViewMap(45 - kk * mn[0], 40 + kk * mx[1], kk)
    draw_proj(s, vi4, iso[0], [])
    labels = [("frame_left", 1), ("frame_right", 1), ("slat_seat_1", 2), ("slat_back_2", 2), ("bolt_1", 3), ("washer_1", 4), ("nut_1", 5)]
    named = {c.label: c for c in ex.children}
    fx = [c for c in ex.children if c.label == "fixings"][0]
    for c in fx.children:
        named[c.label] = c
    for i, (lab, num) in enumerate(labels):
        c = named[lab].center()
        p = vi4(*to2d((c.X, c.Y, c.Z), n, up))
        q = (p[0] + (18 if i % 2 == 0 else -18), p[1] - 16)
        s.balloon(p, q, str(num))
    s.notes(232, 205, [
        "Assembly sequence (crew of two):",
        "1  Set the side frames (1) over the four ground anchors; check spacing",
        f"   {fmt(R['dims']['slat_span'])} mm between frame centres with a slat (2).",
        "2  Level on the anchor nuts to the seat height; tighten the anchors.",
        "3  Lay the three seat slats and two back slats; push the carriage",
        "   bolts (3, stainless A2) through slat and flange; washer (4) and",
        f"   nut (5) under the flange; tighten to {P['bolts']['torque_Nm']['tm_ash']} N m in thermally modified",
        f"   ash, {P['bolts']['torque_Nm']['oak']} N m in oak. Grout under the feet.",
        "4  Yearly: retighten the slat bolts; touch up the coating.",
    ], size=2.2)
    s.title_block(material="see BOM, drawing 005")
    s.save(dd / "VI-DWG-B180-004_exploded_assembly.svg")
    # ---------------- 005 bill of materials ----------------
    s = Sheet("005", "Bill of materials", "–")
    bom = bom_rows(R)
    x0, y0 = 20, 30
    cols = [("Item", 12), ("Part number", 34), ("Description", 120), ("Qty", 12), ("Material", 80), ("Unit kg", 20), ("Total kg", 22)]
    xx = x0
    for nm, w in cols:
        s.text(xx + 1.5, y0, nm, 2.8, weight="bold")
        xx += w
    tw_ = sum(w for _, w in cols)
    s.line([(x0, y0 + 2), (x0 + tw_, y0 + 2)], "thin")
    for i, r in enumerate(bom):
        yy = y0 + 8 + i * 7
        xx = x0
        for (nm, w), val in zip(cols, r):
            s.text(xx + 1.5, yy, val, 2.6)
            xx += w
        s.line([(x0, yy + 2.5), (x0 + tw_, yy + 2.5)], "ext")
    yy = y0 + 8 + len(bom) * 7 + 4
    s.text(x0 + tw_ - 2, yy, f"Bench net mass {mass['net']:.2f} kg with thermally modified ash ({R['woods_net']['oak']:.2f} kg with oak)", 3.2, anchor="end", weight="bold")
    s.notes(20, yy + 14, [
        "Not part of the bench: ground anchor set (4 x M12 with levelling nuts and washers), a separate item, supplied with it.",
        f"Masses computed from the solid model: cast steel 7850 kg/m³, stainless A2 {P['bolts']['density']} kg/m³; thermally modified ash {P['woods']['tm_ash']['density']} kg/m³ (about 5 %), oak {P['woods']['oak']['density']} kg/m³ (12 %); zinc per EN ISO 1461 for castings",
        f"(≥ 575 g/m² mean, taken x {P['materials']['galvanising']['typical_factor']} as typical); powder {P['materials']['powder_coat']['thickness_um']} µm at {P['materials']['powder_coat']['density']} kg/m³; draft allowance {f['draft_mass_allowance_pct']} % of the casting.",
    ], size=2.4)
    s.title_block(mass=f"{mass['net']:.1f} kg net")
    s.save(dd / "VI-DWG-B180-005_bill_of_materials.svg")
    # ---------------- 006 parcels ----------------
    s = Sheet("006", "Parcels (knocked down, 3 per bench)", "1:10")
    k = 0.1
    co, ci = K["carton_outer"], K["carton_inner"]
    W_ = R["parcels"]
    # carton 1 and 2: plan with the frame inside (outline), and edge view
    for idx, (ox, lab) in enumerate(((30, "PARCEL 1 OF 3: frame carton"), (130, "PARCEL 2 OF 3: frame carton with bolt set"))):
        vm = ViewMap(ox, 140, k)
        s.add(f'<rect class="box" x="{vm(0, co[1])[0]:.2f}" y="{vm(0, co[1])[1]:.2f}" width="{co[0] * k:.2f}" height="{co[1] * k:.2f}"/>')
        s.add(f'<rect class="ext" x="{vm(2 * 4, co[1] - 8)[0]:.2f}" y="{vm(8, co[1] - 8)[1]:.2f}" width="{ci[0] * k:.2f}" height="{ci[1] * k:.2f}"/>')
        # frame outline in the carton (inside view, rotated: frame height along the carton length)
        fvis, _ = project(B["frame_L"], *VIEWS["inside"], hidden=False)
        cl = P["packaging"]["frame_carton"]["clearance"]
        for pl in fvis:
            pts = [vm(8 + cl[0] + (pz - gap), 8 + cl[1] + py) for py, pz in pl]
            s.line(pts, "thin")
        if idx == 1:
            s.add(f'<rect class="fillg" x="{vm(560, 150)[0]:.2f}" y="{vm(560, 150)[1]:.2f}" width="{150 * k:.2f}" height="{100 * k:.2f}"/>')
            s.leader(vm(635, 100), (vm(420, -330)[0], vm(420, -330)[1]), "bolt set in a bag, taped to the tray")
        s.text(ox + co[0] * k / 2, 140 - co[1] * k - 6, lab, 3.0, anchor="middle", weight="bold")
        s.dim(vm(0, 0), vm(co[0], 0), 6, fmt(co[0]))
        s.dim(vm(co[0], 0), vm(co[0], co[1]), 5, fmt(co[1]), "v")
        ev = ViewMap(ox, 160, k)
        s.add(f'<rect class="box" x="{ev(0, co[2])[0]:.2f}" y="{ev(0, co[2])[1]:.2f}" width="{co[0] * k:.2f}" height="{co[2] * k:.2f}"/>')
        s.dim(ev(co[0], 0), ev(co[0], co[2]), 5, fmt(co[2]), "v")
        kg = W_["carton1"] if idx == 0 else W_["carton2"]
        s.text(ox, 172, f"{kg:.1f} kg gross; one person", 2.6)
    # slat bundle cross-section 1:2 and side 1:10
    bu = K["bundle"]
    vb = ViewMap(250, 120, 0.5)
    e = P["packaging"]["slat_bundle"]["edge_protector_thickness"]
    T_ = P["slats"]["thickness"]
    s.add(f'<rect class="box" x="{vb(0, bu[2])[0]:.2f}" y="{vb(0, bu[2])[1]:.2f}" width="{bu[1] * 0.5:.2f}" height="{bu[2] * 0.5:.2f}"/>')
    for row, nn in ((0, 3), (1, 2)):
        for i in range(nn):
            y = e + (i + (0.5 if row else 0)) * Wd
            z = e + T_ * row
            s.add(f'<rect class="fillg" x="{vb(y, z + T_)[0]:.2f}" y="{vb(y, z + T_)[1]:.2f}" width="{Wd * 0.5:.2f}" height="{T_ * 0.5:.2f}"/>')
    s.text(250 + bu[1] * 0.25, 120 - bu[2] * 0.5 - 14, "PARCEL 3 OF 3: slat bundle", 3.0, anchor="middle", weight="bold")
    s.text(250 + bu[1] * 0.25, 120 - bu[2] * 0.5 - 9, "section 1:2, 3 + 2 slats, edge protectors, 4 straps", 2.2, anchor="middle")
    s.dim(vb(0, 0), vb(bu[1], 0), 6, fmt(bu[1]))
    s.dim(vb(bu[1], 0), vb(bu[1], bu[2]), 5, fmt(bu[2]), "v")
    vs = ViewMap(222, 150, k)
    s.add(f'<rect class="box" x="{vs(0, bu[2])[0]:.2f}" y="{vs(0, bu[2])[1]:.2f}" width="{bu[0] * k:.2f}" height="{bu[2] * k:.2f}"/>')
    for xs2 in (0.12, 0.38, 0.62, 0.88):
        xq = xs2 * bu[0]
        s.line([vs(xq, -3), vs(xq, bu[2] + 3)], "vis")
    s.dim(vs(0, 0), vs(bu[0], 0), 6, fmt(bu[0]))
    s.text(222, 172, f"{W_['bundle']:.1f} kg gross; two people (length {fmt(bu[0])} mm)", 2.6)
    s.notes(30, 190, [
        f"Carton: FEFCO 0320 tray and lid, single-wall C flute {P['packaging']['frame_carton']['board_gm2']} g/m²; corrugated corner pads; inside",
        f"{fmt(ci[0])} x {fmt(ci[1])} x {fmt(ci[2])} for a frame of {fmt(K['frame_bbox'][2])} x {fmt(K['frame_bbox'][1])} x {fmt(K['frame_bbox'][0])} (clearance {P['packaging']['frame_carton']['clearance'][0]}/{P['packaging']['frame_carton']['clearance'][1]}/{P['packaging']['frame_carton']['clearance'][2]} mm). Carton mass {K['carton_kg']:.2f} kg.",
        f"Bundle: five slats 3 + 2, corrugated edge protectors {e} mm, end caps, 4 PET straps, film; packing {K['bundle_pack_kg']:.2f} kg.",
        "Marks on every parcel: \"Serra 180  VI-B180  parcel n of 3\", the lot number and the GTIN; on the bundle \"two-person lift\".",
        f"Handling (ISO 11228-1): one person up to 25 kg, two people up to about 33 kg; parcels {W_['carton1']:.1f} / {W_['carton2']:.1f} / {W_['bundle']:.1f} kg; bench gross {W_['gross']:.1f} kg.",
        f"Slats of thermally modified ash (from May 2026). With oak slats (until April): bundle {R['woods_bundle']['oak']:.1f} kg, bench gross {R['woods_gross']['oak']:.1f} kg.",
    ], size=2.4)
    s.title_block(mass=f"{W_['gross']:.1f} kg gross per bench", material="corrugated board, PET straps, PE film")
    s.save(dd / "VI-DWG-B180-006_parcels.svg")
    # ---------------- 007 pallet and loading ----------------
    s = Sheet("007", "Pallet of four benches, loading", "1:20, 1:100")
    k = 0.05
    pal = Compound(children=[x.moved(Location()) for x in K["pallet_parts"] + [sh for _, sh in K["load"]]])
    pfv = project(pal, *VIEWS["front"], hidden=False)
    plv = project(pal, *VIEWS["left"], hidden=False)
    vp = ViewMap(30, 80, k)
    draw_proj(s, vp, pfv[0], [])
    vq = ViewMap(170 + 700 * k, 80, k)
    draw_proj(s, vq, plv[0], [])
    ld = K["load_dims"]
    s.text(30 + ld[0] * k / 2, 36, "PALLET, SIDE", 3.0, anchor="middle", weight="bold")
    s.text(170 + 350 * k, 36, "PALLET, END", 3.0, anchor="middle", weight="bold")
    s.dim(vp(0, 0), vp(ld[0], 0), 6, fmt(ld[0]))
    s.dim(vp(ld[0], 0), vp(ld[0], ld[2]), 6, fmt(ld[2]), "v")
    s.dim(vp(ld[0], 0), vp(ld[0], K["pallet_h"]), 16, fmt(K["pallet_h"]), "v")
    s.dim(vq(-ld[1], 0), vq(0, 0), 6, fmt(ld[1]))
    T_ = R["transport"]
    # loading plans (1:100)
    yb = 120
    for j, key in enumerate(("trailer", "container_40", "container_45")):
        t = P["transport"][key]
        tt = T_[key]
        k2 = 0.01
        oy = yb + j * 32
        s.add(f'<rect class="vis" x="30" y="{oy:.2f}" width="{t["length"] * k2:.2f}" height="{t["width"] * k2:.2f}"/>')
        for r_ in range(tt["rows"]):
            for c_ in range(tt["across"]):
                used = r_ * tt["across"] + c_ < tt["floor_needed"]
                s.add(f'<rect class="{'fillg' if used else 'box'}" x="{30 + r_ * P["packaging"]["pallet"]["length"] * k2 + 0.5:.2f}" y="{oy + c_ * P["packaging"]["pallet"]["width"] * k2 + 0.6:.2f}" width="{P["packaging"]["pallet"]["length"] * k2 - 0.4:.2f}" height="{P["packaging"]["pallet"]["width"] * k2 - 0.4:.2f}"/>')
        s.text(30 + t["length"] * k2 + 4, oy + 5, f"{t['name']}: inside {fmt(t['length'])} x {fmt(t['width'])} x {fmt(t['height'])}", 2.4)
        s.text(30 + t["length"] * k2 + 4, oy + 9.5, f"{tt['floor']} floor positions ({tt['rows']} x {tt['across']}); {tt['layers_fit']} layers fit; 25 pallets need {tt['floor_needed']} positions in 2 layers", 2.4)
        s.text(30 + t["length"] * k2 + 4, oy + 14, f"load {T_['load_kg'] / 1000:.2f} t of a payload of {t['payload_kg'] / 1000:.1f} t; grey: the 13 positions used", 2.4)
    s.notes(232, 40, [
        f"Pallet: {P['packaging']['pallet']['type']},",
        f"{fmt(P['packaging']['pallet']['length'])} x {fmt(P['packaging']['pallet']['width'])} x {fmt(K['pallet_h'])}, {K['pallet_kg']:.1f} kg.",
        "Load: four slat bundles (2 x 2) at the bottom, a slip sheet,",
        "eight frame cartons in two columns of four, a top cap; stretch",
        "film; four corner boards. Moved by fork-lift, four-way entry.",
        f"Goods {T_['pallet_goods_kg']:.1f} kg, pallet gross {T_['pallet_gross_kg']:.1f} kg.",
        f"Stacking: up to {T_['stack_max']} high (top load on the cartons only through",
        "the top cap and corner boards).",
    ], size=2.3)
    s.title_block(mass=f"{T_['pallet_gross_kg']:.0f} kg per pallet", material="heat-treated softwood (ISPM 15)")
    s.save(dd / "VI-DWG-B180-007_pallet_and_loading.svg")
    # ---------------- 008 casting: gating and risers ----------------
    s = Sheet("008", "Casting method: mould with two frames", "1:5")
    k = 0.2
    cv = project(C["cluster"], (-1, 0, 0), (0, 0, 1), hidden=False)
    allp = np.array([p for pl in cv[0] for p in pl])
    mn, mx = allp.min(0), allp.max(0)
    kk = 0.2
    vc = ViewMap(25 - kk * mn[0], 40 + kk * mx[1], kk)
    draw_proj(s, vc, cv[0], [])
    s.text(30 + (mx[0] - mn[0]) * kk / 2, 32, "PLAN OF THE MOULD, COPE REMOVED: two castings, top risers (circles), sprue, runner, ingates", 2.8, anchor="middle", weight="bold")
    s.notes(25, 212, [
        f"Two frames per mould (one bench), mirrored; sprue between them,",
        f"runner {fmt(C['run_w'])} x {fmt(C['run_h'])} mm, {fmt(C['runner_len'])} mm long; one ingate into each main",
        f"junction J ({fmt(C['gate_w'])} x {fmt(C['gate_t'])} mm). Choke (sprue) Ø{C['d_sprue']:.0f} mm.",
        f"Pouring {C['W_guess']:.0f} kg in about {C['t_pour']:.0f} s (t = {P['casting']['pour_time_k']}√W), head {P['casting']['pour_head']} mm.",
        f"Risers (modulus method): wall modulus {C['M_wall']:.1f} mm, junction",
        f"{C['M_j']:.1f} mm, riser ≥ {C['M_r']:.1f} mm: Ø{C['D']:.0f} x {C['H']:.0f} mm top risers.",
        f"Feeding distance {C['FD']:.0f} mm each side (SFSA bar rule): {C['n_risers']} risers",
        f"per frame ({C['n_risers_junction']} at junctions, {C['n_risers'] - C['n_risers_junction']} along members).",
        f"Poured {C['poured']:.1f} kg for {2 * C['casting_kg']:.1f} kg of castings: yield {100 * C['yield_']:.0f} %.",
        f"Junction risers only: {C['poured_j']:.1f} kg, yield {100 * C['yield_j']:.0f} % (centre-line porosity).",
    ], size=2.3)
    s.title_block(mass=f"{C['poured']:.1f} kg poured per mould", material=P["materials"]["cast_steel"]["grade"])
    s.save(dd / "VI-DWG-B180-008_casting_method.svg")
    return sorted(p.name for p in dd.glob("*.svg"))


def bom_rows(R):
    m = R["mass"]
    b = P["bolts"]
    rows = [
        ("1", "VI-C180", "Side frame, cast steel, hot-dip galvanised, powder coated", "2", P["materials"]["cast_steel"]["grade"], f"{m['frame']:.2f}", f"{2 * m['frame']:.2f}"),
        ("2", "VI-B180-03", f"Slat {P['slats']['length']} x {P['slats']['width']} x {P['slats']['thickness']}, planed, 4 holes (from May 2026)", "5", "thermally modified ash, about 5 %", f"{R['woods_mass']['tm_ash']:.2f}", f"{5 * R['woods_mass']['tm_ash']:.2f}"),
        ("2a", "VI-B180-03", "Slat, as item 2 (deliveries until April 2026)", "(5)", "oak heartwood, kiln-dried 12 %", f"{R['woods_mass']['oak']:.2f}", f"({5 * R['woods_mass']['oak']:.2f})"),
        ("3", "VI-B180-04", "Cup square neck bolt M8 x 60, ISO 8677", str(b["count"]), "stainless A2-70 (A4-70 coastal)", f"{m['bolt']:.3f}", f"{b['count'] * m['bolt']:.2f}"),
        ("4", "VI-B180-05", "Washer 8, ISO 7089", str(b["count"]), "stainless A2 (A4 coastal)", f"{m['washer']:.4f}", f"{b['count'] * m['washer']:.3f}"),
        ("5", "VI-B180-06", "Hex nut M8, ISO 4032", str(b["count"]), "stainless A2-70 (A4-70 coastal)", f"{m['nut']:.4f}", f"{b['count'] * m['nut']:.3f}"),
        ("6", "VI-B180-07", "Bag for the bolt set", "1", "PE", f"{b['bag_mass']:.2f}", f"{b['bag_mass']:.2f}"),
    ]
    return rows


# --------------------------------------------------------------------------
# 10. Parcels, pallet, vehicles
# --------------------------------------------------------------------------
def logistics(R, K):
    m = R["mass"]
    c1 = m["frame"] + K["carton_kg"]
    c2 = m["frame"] + m["boltset"] + K["carton_kg"]
    bu = P["slats"]["count"] * m["slat"] + K["bundle_pack_kg"]
    R["parcels"] = dict(carton1=c1, carton2=c2, bundle=bu, gross=c1 + c2 + bu, packaging=2 * K["carton_kg"] + K["bundle_pack_kg"])
    pp = P["packaging"]["pallet"]
    n = pp["benches"]
    goods = n * R["parcels"]["gross"]
    extra = pp["slip_sheet_kg"] + pp["top_cap_kg"] + pp["stretch_film_kg"]
    gross = goods + K["pallet_kg"] + extra
    cast_n = P["transport"]["castings_per_pallet"]
    cast_h = K["pallet_h"] + (cast_n // 2) * K["carton_outer"][2] + 5
    cast_gross = cast_n * c1 + K["pallet_kg"] + extra
    T = dict(pallet_goods_kg=goods, pallet_gross_kg=gross, pallet_extra_kg=extra, castings_pallet_kg=cast_gross,
             castings_pallet_h=cast_h, pallet_dims=K["load_dims"])
    nb, ncast = P["transport"]["bench_pallets"], P["transport"]["castings_pallets"]
    T["load_kg"] = nb * gross + ncast * cast_gross
    T["n_pallets"] = nb + ncast
    T["floor_needed"] = math.ceil(T["n_pallets"] / P["transport"]["layers"])
    hmax = max(K["load_dims"][2], cast_h)
    stack = []
    for key in ("trailer", "container_40", "container_45"):
        t = P["transport"][key]
        best = None
        for (a, b) in ((pp["length"], pp["width"]), (pp["width"], pp["length"])):
            rows, across = int(t["length"] // a), int(t["width"] // b)
            if best is None or rows * across > best[0]:
                best = (rows * across, rows, across)
        layers_fit = int(t["height"] // hmax)
        stack.append(layers_fit)
        T[key] = dict(floor=best[0], rows=best[1], across=best[2], layers_fit=layers_fit,
                      capacity=best[0] * min(layers_fit, 3), floor_needed=T["floor_needed"],
                      fits=best[0] * min(layers_fit, P["transport"]["layers"]) >= T["n_pallets"],
                      payload_ok=T["load_kg"] <= t["payload_kg"])
    T["stack_max"] = min(3, min(stack))
    # world pallet 1850 x 650: does the carton fit?
    T["world_pallet_width_ok"] = K["carton_outer"][1] <= P["world_figures"]["pallet_size"][1]
    R["transport"] = T
    return R


def write_results(R, C, K, extra):
    out = dict(R)
    out["casting"] = {k: vv for k, vv in C.items() if k not in ("cluster", "risers", "gating", "junctions")}
    out["casting"]["junctions"] = {k: [float(a) for a in vv] for k, vv in C["junctions"].items()}
    out["packaging"] = {k: vv for k, vv in K.items() if k not in ("pallet", "pallet_parts", "load")}
    out.update(extra)

    def clean(o):
        if isinstance(o, dict):
            return {k: clean(vv) for k, vv in o.items() if k not in ("x", "M", "w")}
        if isinstance(o, (list, tuple)):
            return [clean(vv) for vv in o]
        if isinstance(o, (np.floating, np.integer)):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, float):
            return round(o, 4)
        return o
    (HERE / "results.json").write_text(json.dumps(clean(out), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return clean(out)


def main():
    B = build_bench()
    W = P["woods"]
    per_wood = {}
    for key in (W["comparison_wood"], W["main_wood"]):        # main wood last: it stays in P for the drawings
        set_wood(key)
        Rk = analyse(B)
        Kk = build_packaging(B, Rk)
        logistics(Rk, Kk)
        per_wood[key] = {k: Rk[k] for k in ("mass", "slats", "parcels", "transport")}
    R, K = Rk, Kk
    R["woods_mass"] = {k: v["mass"]["slat"] for k, v in per_wood.items()}
    R["woods_net"] = {k: v["mass"]["net"] for k, v in per_wood.items()}
    R["woods_bundle"] = {k: v["parcels"]["bundle"] for k, v in per_wood.items()}
    R["woods_gross"] = {k: v["parcels"]["gross"] for k, v in per_wood.items()}
    C = build_casting(B, R)
    extra = dict(frame_mass_by_wall={str(t): frame_variant_mass(t) for t in (6, 7, 8, 10)}, woods=per_wood,
                 main_wood=W["main_wood"], comparison_wood=W["comparison_wood"])
    res = write_results(R, C, K, extra)
    print("frame %.2f kg (bare %.2f), net %.2f kg, gross %.2f kg, poured %.1f kg per bench, yield %.0f %%" % (
        R["mass"]["frame"], R["mass"]["frame_bare"], R["mass"]["net"], R["parcels"]["gross"], C["poured"], 100 * C["yield_"]))
    export_all(B, C, K)
    if "--no-drawings" not in ARGS:
        print("drawings:", make_drawings(B, R, C, K))
    if "--no-render" not in ARGS:
        render()
    import report
    report.write(res, HERE)


def render():
    """PNG renders with Chromium (Playwright) and three.js; see render.js and README.md."""
    cmd = ["node", str(HERE / "render.js"), str(HERE)]
    print("render:", " ".join(cmd))
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
