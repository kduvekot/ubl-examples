#!/usr/bin/env python3
"""The Lumeport Exchange's daily noon fixing of the lume against currencies outside the Accord (O231).

Inside the Accord the parities stay fixed (1 lume = 100 ferra = 0.4 coral, world/countries.json
"exchange_rates", O2). Against every other currency the lume floats: its value is a basket of fixed amounts of
five real currencies, like the IMF's SDR, made only of currencies the world does not quote, so the lume is
visibly none of the currencies it is quoted in:

  Swiss franc 30 %, Canadian dollar 25 %, Australian dollar 15 %, Norwegian krone 15 %, Mexican peso 15 %.

The weights hold on the base date, the world date 2026-01-02 (a Friday): the basket amounts are fixed on that
date so that each currency's share of the lume's value is its weight and 1 EUR = 1.20 lume exactly. After that
the amounts stay fixed and the weights drift with the market.

The market is the real one, shifted: a world date D takes the ECB euro foreign exchange reference rates of
D - 1,820 days (260 weeks, so the same weekday five years earlier); on a day without an ECB rate, the most
recent earlier one. The rates are the ECB's file, cut to the currencies used and to 2020-2023, in
world/codelists/sources/ecb-eurofxref/ (provenance and SHA-256 in PROVENANCE-second-round.md).

With r(X, d) the ECB rate (units of X per 1 EUR on day d) and a(C) the basket amounts, one lume is worth
V(d) = sum over C of a(C) / r(C, d) euro, so the fixing is lume per 1 EUR = 1 / V(d) and lume per 1 unit of X
= 1 / (r(X, d) * V(d)). The basket amounts are a(C) = w(C) * r(C, base) / 1.20. The tool computes with exact
fractions and rounds only what it publishes, to 6 significant digits.

Published for every world working day (Monday to Friday) from 2026-01-01 to 2027-12-31: lume per 1 unit of EUR,
USD, JPY, INR, GBP, CNY, ZAR and BRL, the inverse (units per 1 lume), and the ECB date used. The output,
world/fx-fixings.json, is generated; do not edit it by hand.

For the generators:  import fx_fixing; fx_fixing.rate("EUR", "2026-04-10") -> Fraction, lume per 1 EUR
                     fx_fixing.rate("USD", "2026-04-10", quote="XUF") -> ferra per 1 USD (by the parities)
                     fx_fixing.fixing("2026-04-10") -> the published row (the most recent on or before)

Usage: python3 tools/fx_fixing.py           write world/fx-fixings.json
       python3 tools/fx_fixing.py --check   say whether world/fx-fixings.json is current (exit 1 if not)
"""
import csv
import datetime
import json
import os
import sys
from decimal import Decimal
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
SOURCE = os.path.join(ROOT, "world", "codelists", "sources", "ecb-eurofxref", "eurofxref-hist-2020-2023.csv")
COUNTRIES = os.path.join(ROOT, "world", "countries.json")
OUT = os.path.join(ROOT, "world", "fx-fixings.json")

BASKET = (("CHF", Fraction(30, 100)), ("CAD", Fraction(25, 100)), ("AUD", Fraction(15, 100)),
          ("NOK", Fraction(15, 100)), ("MXN", Fraction(15, 100)))
QUOTED = ("EUR", "USD", "JPY", "INR", "GBP", "CNY", "ZAR", "BRL")
NAMES = {"EUR": "euro", "USD": "US dollar", "JPY": "yen", "INR": "Indian rupee", "GBP": "pound sterling",
         "CNY": "yuan renminbi", "ZAR": "rand", "BRL": "Brazilian real", "CHF": "Swiss franc",
         "CAD": "Canadian dollar", "AUD": "Australian dollar", "NOK": "Norwegian krone", "MXN": "Mexican peso"}
SHIFT_DAYS = 1820                       # 260 weeks
BASE_DATE = datetime.date(2026, 1, 2)   # a Friday; 1 EUR = 1.20 lume on this date
EUR_ON_BASE = Fraction(6, 5)
FIRST, LAST = datetime.date(2026, 1, 1), datetime.date(2027, 12, 31)
LUME = "XBL"
DIGITS = 6

_cache = {}


def _ecb():
    """{date: {currency: Fraction units per 1 EUR}} from the ECB extract, and the sorted dates."""
    if "ecb" not in _cache:
        rates = {}
        with open(SOURCE, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                d = datetime.date.fromisoformat(row.pop("Date"))
                rates[d] = {c: Fraction(Decimal(v)) for c, v in row.items()}
        _cache["ecb"] = (rates, sorted(rates))
    return _cache["ecb"]


def source_date(world_date):
    """The ECB date a world date takes: D - 1,820 days, or the most recent earlier day with a rate."""
    rates, dates = _ecb()
    d = world_date - datetime.timedelta(days=SHIFT_DAYS)
    if d < dates[0]:
        raise ValueError(f"no ECB rate on or before {d} (world date {world_date})")
    while d not in rates:
        d -= datetime.timedelta(days=1)
    return d


def basket_amounts():
    """{currency: Fraction} the amounts of each currency in one lume, fixed on the base date."""
    if "basket" not in _cache:
        r = _ecb()[0][source_date(BASE_DATE)]
        _cache["basket"] = {c: w * r[c] / EUR_ON_BASE for c, w in BASKET}
    return _cache["basket"]


def _lume_per_unit(currency, d):
    """Exact lume per 1 unit of currency on ECB date d."""
    r = _ecb()[0][d]
    value_eur = sum(a / r[c] for c, a in basket_amounts().items())     # euro per 1 lume
    per_eur = 1 / value_eur
    return per_eur if currency == "EUR" else per_eur / r[currency]


def _date(world_date):
    return world_date if isinstance(world_date, datetime.date) else datetime.date.fromisoformat(world_date)


def _fixing_day(world_date):
    """The fixing that applies on a date: that day's, or on a weekend the Friday's."""
    d = _date(world_date)
    if not FIRST <= d <= LAST:
        raise ValueError(f"no fixing published for {d}: the table runs from {FIRST} to {LAST}")
    while d.weekday() >= 5:
        d -= datetime.timedelta(days=1)
    if d < FIRST:
        raise ValueError(f"no fixing on or before {_date(world_date)}")
    return d


def _parities():
    """{currency: Fraction lume per 1 unit} for the three Accord currencies (world/countries.json)."""
    if "par" not in _cache:
        with open(COUNTRIES, encoding="utf-8") as f:
            ex = json.load(f)["exchange_rates"]
        _cache["par"] = {LUME: Fraction(1), "XUF": Fraction(str(ex["XUF/XBL"])),
                         "XLC": 1 / Fraction(str(ex["XBL/XLC"]))}
    return _cache["par"]


def rate(currency, world_date, quote=LUME):
    """Units of `quote` (lume by default; ferra XUF or coral XLC by the parities) per 1 unit of `currency` at
    the noon fixing that applies on world_date, exact (round as the document needs). `currency` is one of the
    eight quoted currencies or an Accord currency."""
    par = _parities()
    if quote not in par:
        raise ValueError(f"quote currency {quote} is not an Accord currency")
    if currency in par:
        return par[currency] / par[quote]
    if currency not in QUOTED:
        raise ValueError(f"the Lumeport Exchange does not fix {currency}")
    d = _fixing_day(world_date)
    return _lume_per_unit(currency, source_date(d)) / par[quote]


def fixing(world_date):
    """The published row of world/fx-fixings.json that applies on world_date (that day's or the Friday's)."""
    d = _fixing_day(world_date).isoformat()
    if "rows" not in _cache:
        with open(OUT, encoding="utf-8") as f:
            _cache["rows"] = {row["date"]: row for row in json.load(f)["fixings"]}
    return _cache["rows"][d]


def sig(x, digits=DIGITS):
    """A Fraction as a decimal string with `digits` significant digits (half-even), without exponent."""
    d = Decimal(x.numerator) / Decimal(x.denominator)
    q = Decimal(1).scaleb(d.adjusted() - digits + 1)
    return format(d.quantize(q), "f")


def _exact(x):
    """A Fraction with a terminating decimal expansion, written out exactly."""
    d = Decimal(x.numerator) / Decimal(x.denominator)
    if Fraction(d) != x:
        raise ValueError(f"{x} has no exact decimal form")
    return format(d.normalize(), "f")


def build():
    amounts = basket_amounts()
    base_src = source_date(BASE_DATE)
    base_r = _ecb()[0][base_src]
    rows = []
    d = FIRST
    while d <= LAST:
        if d.weekday() < 5:
            s = source_date(d)
            per = {c: _lume_per_unit(c, s) for c in QUOTED}
            rows.append({"date": d.isoformat(), "source_date": s.isoformat(),
                         "lume_per_unit": {c: sig(v) for c, v in per.items()},
                         "units_per_lume": {c: sig(1 / v) for c, v in per.items()}})
        d += datetime.timedelta(days=1)
    head = {
        "about": "The Lumeport Exchange's daily noon fixing of the lume (XBL) against eight currencies outside the "
                 "Accord (O231). Generated by tools/fx_fixing.py; do not edit by hand. Inside the Accord the "
                 "parities stay fixed (1 lume = 100 ferra = 0.4 coral, world/countries.json); the ferra's and the "
                 "coral's outside rates follow from them.",
        "method": "One lume is a basket of fixed amounts of five currencies, like the IMF's SDR. The amounts were "
                  "fixed on the base date so that each currency's share is its weight and 1 EUR = 1.20 lume. A "
                  "world date takes the ECB euro reference rates of the date 1,820 days (260 weeks, the same "
                  "weekday) earlier, or of the most recent earlier day with a rate. With r(X) the ECB rate (units "
                  "of X per 1 EUR), one lume is worth V = sum a(C) / r(C) euro; lume per 1 EUR = 1 / V and lume "
                  "per 1 unit of X = 1 / (r(X) V). Computed exactly, published to 6 significant digits. Published "
                  "for every working day (Monday to Friday); on a weekend the Friday's fixing applies.",
        "source": {"file": "world/codelists/sources/ecb-eurofxref/eurofxref-hist-2020-2023.csv",
                   "publisher": "European Central Bank, euro foreign exchange reference rates",
                   "provenance": "world/codelists/sources/PROVENANCE-second-round.md"},
        "shift_days": SHIFT_DAYS,
        "base_date": BASE_DATE.isoformat(),
        "base_source_date": base_src.isoformat(),
        "eur_on_base_date": "1.20",
        "basket": [{"currency": c, "name": NAMES[c], "weight_on_base_date": f"{int(w * 100)} %",
                    "ecb_rate_on_base_date": format(Decimal(base_r[c].numerator) / Decimal(base_r[c].denominator), "f"),
                    "amount_per_lume": _exact(amounts[c])} for c, w in BASKET],
        "quoted": [{"currency": c, "name": NAMES[c]} for c in QUOTED],
        "period": {"first": FIRST.isoformat(), "last": LAST.isoformat()},
    }
    text = json.dumps(head, indent=1, ensure_ascii=False)[:-2]
    text += ',\n "fixings": [\n' + ",\n".join("  " + json.dumps(r, ensure_ascii=False) for r in rows) + "\n ]\n}\n"
    return text


def main():
    text = build()
    if "--check" in sys.argv:
        try:
            with open(OUT, encoding="utf-8") as f:
                current = f.read() == text
        except FileNotFoundError:
            current = False
        if not current:
            print("fx_fixing: world/fx-fixings.json is not current; run python3 tools/fx_fixing.py")
            sys.exit(1)
        print("fx_fixing: world/fx-fixings.json is current")
        return
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"fx_fixing: wrote world/fx-fixings.json ({text.count(chr(10) + '  {')} fixings)")


if __name__ == "__main__":
    main()
