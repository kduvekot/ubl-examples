"""Draw the position of the UBL example world on a depth map of the South Atlantic.

usage: python3 plot_world_position.py            (writes world-position.png next to this script)

Needs numpy and matplotlib. The depth grid is NOAA ETOPO1 at 10 arc-minutes, fetched once from
NOAA's ERDDAP server into <repo>/.review/geo/etopo.csv (not committed):
https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?altitude[(-55):10:(-10)][(-65):10:(25)]
The positions of the real islands are entered by hand (see `real`), not taken from the grid, which is
too coarse to show small islands. The 200-nautical-mile rings are circles around those positions,
not official limits. See README.md in this folder.
"""
import numpy as np, matplotlib, pathlib, urllib.request
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle, Ellipse
HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parents[1] / '.review' / 'geo' / 'etopo.csv'
URL = 'https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?altitude[(-55):10:(-10)][(-65):10:(25)]'
if not DATA.is_file():
    DATA.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(URL, DATA)
_d = np.genfromtxt(DATA, delimiter=',', skip_header=2)
lat = np.unique(_d[:, 0]); lon = np.unique(_d[:, 1]); Z = _d[:, 2].reshape(len(lat), len(lon))
INK='#1f2933'; MUTED='#5f6b7a'; ACC='#c2410c'; LAND='#d9d6cf'
sea=LinearSegmentedColormap.from_list('sea',['#eef5fb','#c9dff1','#9cc3e3','#6ba3d0','#3f7fb8','#225a94','#123c6b'][::-1])
levels=[-7000,-5000,-4000,-3500,-3000,-2500,-2000,-1000,0]
def base(ax,ext):
    ax.contourf(lon,lat,np.where(Z>0,np.nan,Z),levels=levels,cmap=sea,extend='min')
    ax.contourf(lon,lat,Z,levels=[0,9000],colors=[LAND])
    ax.contour(lon,lat,Z,levels=[0],colors=[MUTED],linewidths=0.5)
    ax.set_xlim(ext[0],ext[1]); ax.set_ylim(ext[2],ext[3])
    ax.set_aspect(1/np.cos(np.radians((ext[2]+ext[3])/2)))
    ax.tick_params(colors=MUTED,labelsize=8,length=2)
    for s in ax.spines.values(): s.set_color('#b8c0cc'); s.set_linewidth(0.6)
    ax.xaxis.set_major_formatter(lambda v,p: f"{abs(v):.0f}°{'W' if v<0 else 'E' if v>0 else ''}")
    ax.yaxis.set_major_formatter(lambda v,p: f"{abs(v):.0f}°S")
# placement
dlat=14/111.2; dlon=14/(111.32*np.cos(np.radians(30)))
lon0=-18.27; lat0=-27.86          # map square (0,0)
def pos(i,j): return lon0+dlon*i, lat0-dlat*j
M=dict(w=pos(4,0)[0], e=pos(41,0)[0], n=pos(0,2)[1], s=pos(0,32)[1])
border=pos(22,0)[0]
ISL=(-2.65,-33.0); iw=112/(111.32*np.cos(np.radians(33))); ih=84/111.2
real=[('Tristan da Cunha',-12.3,-37.1),('Gough Island',-9.9,-40.3),('Saint Helena',-5.7,-15.95),('Trindade',-29.3,-20.5),('Falkland Islands',-59.0,-51.7)]
def world(ax,labels=True,towns=False):
    ax.add_patch(Rectangle((M['w'],M['s']),M['e']-M['w'],M['n']-M['s'],fc=ACC,alpha=0.18,ec=ACC,lw=1.4))
    ax.plot([border,border],[M['s'],M['n']],color=ACC,lw=1,ls=(0,(4,3)))
    ax.add_patch(Ellipse(ISL,iw,ih,fc=ACC,alpha=0.35,ec=ACC,lw=1.4))
    lp=pos(39,28)
    ax.plot([lp[0],ISL[0]-iw/2],[lp[1],ISL[1]],color=ACC,lw=1,ls=(0,(1,2)))
fig=plt.figure(figsize=(13,12.6),dpi=200,facecolor='white')
ax=fig.add_axes([0.06,0.50,0.90,0.44]); base(ax,(-62,22,-50,-12)); world(ax)
ax.set_title('Where the world would lie: the South Atlantic',loc='left',fontsize=14,color=INK,pad=10,fontweight='bold')
for n,x,y in real:
    ax.plot(x,y,'o',ms=4,mfc='white',mec=INK,mew=1)
    ax.annotate(n,(x,y),xytext=(6,-3),textcoords='offset points',fontsize=8.5,color=INK)

def ring(ax,x,y,km=370.4):
    t=np.linspace(0,2*np.pi,90); ax.plot(x+km/(111.32*np.cos(np.radians(y)))*np.cos(t), y+km/111.2*np.sin(t), color=INK, lw=0.7, ls=(0,(3,2)))
for n,x,y in real: ring(ax,x,y)
ax.add_patch(Rectangle((-39.5,-35.2),11.0,8.6,fc='none',ec=INK,lw=0.9,hatch='////',alpha=0.55))
ax.annotate('Rio Grande Rise: claimed by Brazil\nas continental shelf since 2018',(-34,-35.2),xytext=(-52,-41.5),fontsize=8.5,color=INK,arrowprops=dict(arrowstyle='-',color=INK,lw=0.8))
ax.text(-12.3,-38.6,'200 nautical miles',fontsize=7.5,color=INK,ha='center')
ax.text(-52,-22,'SOUTH AMERICA',fontsize=10,color=MUTED,ha='center'); ax.text(17.5,-24,'AFRICA',fontsize=10,color=MUTED,ha='center')
ax.text(-13.6,-21.5,'Mid-Atlantic\nRidge',fontsize=8,color='white',ha='center',style='italic')
ax.text(2.5,-27.5,'Walvis Ridge',fontsize=8,color='white',ha='center',style='italic',rotation=38)
ax.annotate('Mainland: Urvania and Bayvarra\non the Mid-Atlantic Ridge',(M['w']+1.5,M['n']),xytext=(-33,-13.2),fontsize=10,color=INK,fontweight='bold',arrowprops=dict(arrowstyle='-',color=INK,lw=0.8),va='top')
ax.annotate('Lisavu, on a seamount\nof the Walvis Ridge',(ISL[0],ISL[1]-ih/2),xytext=(3.5,-39.5),fontsize=10,color=INK,fontweight='bold',arrowprops=dict(arrowstyle='-',color=INK,lw=0.8),ha='center')
ax.text((pos(39,28)[0]+ISL[0])/2,-30.9,'900 km',fontsize=8.5,color=INK,ha='center')
ax.plot(-15.6,-39.8,'x',ms=7,color=INK,mew=1.4); ax.annotate('position in the world data today',(-15.6,-39.8),xytext=(-37,-46.2),fontsize=8.5,color=INK,arrowprops=dict(arrowstyle='-',color=INK,lw=0.8))
# zoom
ax2=fig.add_axes([0.06,0.06,0.90,0.38]); base(ax2,(-21,3,-37.6,-26.0)); world(ax2)
ax2.set_title('Close-up: the sea floor under the mainland and the island',loc='left',fontsize=14,color=INK,pad=10,fontweight='bold')
towns={'Ferrano':(13,22),'Lumeport':(31,28),'Marrowdale':(26,26),'Serravona (mine)':(9,12),'Gullhaven':(31,10),'gas field':(33,3)}
off={'Ferrano':(-44,-3),'Lumeport':(6,-10),'Marrowdale':(-30,7),'Serravona (mine)':(6,3),'Gullhaven':(6,-3),'gas field':(6,2)}
for n,(i,j) in towns.items():
    x,y=pos(i,j); ax2.plot(x,y,'o',ms=4.5,mfc='white',mec=INK,mew=1.1)
    ax2.annotate(n,(x,y),xytext=off[n],textcoords='offset points',fontsize=8.5,color=INK)
ax2.text((M['w']+border)/2,M['s']-0.45,'URVANIA',fontsize=10,color=INK,ha='center',fontweight='bold')
ax2.text((M['e']+border)/2,M['s']-0.45,'BAYVARRA',fontsize=10,color=INK,ha='center',fontweight='bold')
ax2.text(ISL[0],ISL[1]-ih/2-0.5,'LISAVU',fontsize=10,color=INK,ha='center',fontweight='bold')
ax2.annotate('cliffs, facing the\nwest wind and swell',(ISL[0]-iw/2,ISL[1]),xytext=(-5.2,-35.6),fontsize=8.5,color=INK,arrowprops=dict(arrowstyle='-',color=INK,lw=0.8),ha='center')
sx=ISL[0]+iw/2-0.15; ax2.plot(sx,ISL[1],'o',ms=4.5,mfc='white',mec=INK,mew=1.1)
ax2.annotate('Selanu: port and airport\non the lee side',(sx,ISL[1]),xytext=(10,8),textcoords='offset points',fontsize=8.5,color=INK)
ax2.annotate('',xy=(-7.2,-34.0),xytext=(-10.2,-34.0),arrowprops=dict(arrowstyle='-|>',color=INK,lw=1.2)); ax2.text(-8.7,-33.7,'prevailing wind',fontsize=8.5,color=INK,ha='center')
ax2.text(-7.6,-30.9,'900 km to the cliffs, about 1,050 km by sea to Selanu:\n42 hours by ship, 2 hours by air',fontsize=8.5,color=INK,ha='center')
ax2.plot(-12.3,-37.1,'o',ms=4.5,mfc='white',mec=INK,mew=1.1); ax2.annotate('Tristan da Cunha',(-12.3,-37.1),xytext=(7,-3),textcoords='offset points',fontsize=8.5,color=INK)
t=np.linspace(0,np.pi,60); ax2.plot(-12.3+370.4/(111.32*np.cos(np.radians(37.1)))*np.cos(t), -37.1+370.4/111.2*np.sin(t), color=INK, lw=0.7, ls=(0,(3,2))); ax2.text(-12.3,-33.5,'200 nautical miles from Tristan da Cunha',fontsize=7.5,color=INK,ha='center')
# scale bar 500 km at 36.8S
km=500/(111.32*np.cos(np.radians(36.8))); ax2.plot([-20.2,-20.2+km],[-27.0,-27.0],color=INK,lw=2); ax2.text(-20.2+km/2,-26.7,'500 km',fontsize=8.5,color=INK,ha='center')
# depth legend
cax=fig.add_axes([0.62,0.535,0.30,0.011]); 
import matplotlib.cm as cm, matplotlib.colors as mc
cb=fig.colorbar(cm.ScalarMappable(norm=mc.BoundaryNorm(levels,sea.N),cmap=sea),cax=cax,orientation='horizontal',ticks=[-5000,-4000,-3000,-2000,-1000,0])
cb.ax.set_xticklabels(['5,000','4,000','3,000','2,000','1,000','0'],fontsize=7.5,color=INK); cb.outline.set_linewidth(0.4)
fig.text(0.62,0.553,'Depth of the sea floor, metres',fontsize=8,color=INK,ha='left',va='center')
fig.text(0.06,0.015,'Sea floor and coasts: NOAA ETOPO1, sampled every 10 arc-minutes. Shaded orange: the proposed position of the fictional world (map squares of 14 km). Real islands are marked with circles, with a dashed ring at 200 nautical miles.',fontsize=7.5,color=MUTED)
fig.savefig(HERE / 'world-position.png')
print('mainland box lon %.2f..%.2f W, lat %.2f..%.2f S'%(-M['w'],-M['e'],-M['n'],-M['s']))
for n,(i,j) in towns.items(): print(n,'%.2fS %.2fW'%(-pos(i,j)[1],-pos(i,j)[0]))
# checks: any real land inside the boxes?
ii=(lat<=M['n'])&(lat>=M['s']); jj=(lon>=M['w'])&(lon<=M['e'])
sub=Z[np.ix_(ii,jj)]; print('mainland box: max elevation %.0f m, shallowest; mean depth %.0f m; share above -3000 m %.0f%%'%(sub.max(),sub.mean(),100*(sub>-3000).mean()))
ii=(lat<=ISL[1]+ih/2)&(lat>=ISL[1]-ih/2); jj=(lon>=ISL[0]-iw/2)&(lon<=ISL[0]+iw/2); sub=Z[np.ix_(ii,jj)]; print('island box: max %.0f m, mean %.0f m'%(sub.max(),sub.mean()))
def dist(a,b):
    import math
    la1,lo1,la2,lo2=map(math.radians,(a[1],a[0],b[1],b[0])); return 6371*math.acos(math.sin(la1)*math.sin(la2)+math.cos(la1)*math.cos(la2)*math.cos(lo2-lo1))
lp=pos(39,28); print('Lumeport port to island west coast %.0f km; to Selanu (east side) straight %.0f km'%(dist(lp,(ISL[0]-iw/2,ISL[1])),dist(lp,(sx,ISL[1]))))
for n,x,y in real: print('island to',n,'%.0f km'%dist(ISL,(x,y)),'| mainland centre to',n,'%.0f km'%dist(((M['w']+M['e'])/2,(M['n']+M['s'])/2),(x,y)))
