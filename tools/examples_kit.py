"""The building blocks of the example documents, shared by every flow.

A flow's scenario (tools/examples_scenarios.py) gives its timeline, its deal
(items and quantities) and, per document, what is particular to it. This kit
turns that into document content with a reason for every value:

  * document numbers, derived from the sender (its initials), a code for the
    document type, the year and a sequence of the flow;
  * dates, from the flow's start date and the day of each document;
  * lines and amounts, from the deal and the items layer, rounded to the
    minor unit of the currency;
  * taxes, from the rules of the seller's country (world/countries.json):
    who pays which tax at which rate, and why not where no tax applies.
"""
import datetime
import zlib
from decimal import Decimal

import codelists
import world_ids
from build_examples import ITEM, PARTY, WORLD, V, Detail, account, amount, item, money, price, qty

CODES = {"Order": "PO", "OrderResponse": "OR", "OrderChange": "OC", "Invoice": "INV", "CreditNote": "CN",
         "DespatchAdvice": "DA", "ReceiptAdvice": "RA", "RemittanceAdvice": "RM",
         "TransportExecutionPlanRequest": "TR", "TransportExecutionPlan": "TEP", "Waybill": "WB",
         "TransportationStatus": "TS", "ExportCustomsDeclaration": "EX", "ImportCustomsDeclaration": "IM",
         "CertificateOfOrigin": "CO", "Shipment": "SH", "Consignment": "CS", "CustomsDeclaration": "CD",
         "Application": "AP", "TransitCustomsDeclaration": "TD", "Catalogue": "CAT", "Forecast": "FC",
         "RetailEvent": "RE", "InventoryReport": "IR", "PurchaseReceipt": "PR", "DigitalAgreement": "DAG",
         "DigitalCapability": "DCP", "ForwardingInstructions": "FI", "PackingList": "PL", "BillOfLading": "BL",
         "Manifest": "MF", "CommonTransportationReport": "CTR", "Statement": "ST", "DeliveryNote": "DN",
         "SelfBilledInvoice": "SBI", "SelfBilledCreditNote": "SBC", "ForecastRevision": "FR", "GoodsCertificate": "GC",
         "WeightStatement": "WS"}


def initials(pid):
    """The prefix of a party's document numbers: its initials, or an airline's ICAO-style designator."""
    if PARTY[pid]["identity"].get("airline_icao"):
        return PARTY[pid]["identity"]["airline_icao"]
    words = [w for w in PARTY[pid]["identity"]["name"].replace("'", "").split() if w.lower() not in ("of", "and", "the")]
    return "".join(w[0] for w in words)[:4].upper()


class Flow:
    """The context of one flow: its start date, its numbering and its deal."""
    def __init__(self, flow_id, start, deal=None, buyer=None):
        self.id, self.start, self.deal = flow_id, datetime.date.fromisoformat(start), deal or []
        self.buyer = buyer         # the buyer of the deal, where the seller has a price of its own for it (D14)
        self.base = 100 + zlib.crc32(flow_id.encode()) % 800      # a stable sequence per flow
        self.numbers = {}          # document numbers, and amounts and dates other documents refer to
        self.count = 0             # the sequence counts document numbers only

    def number(self, key, sender, doc_type):
        """The document number of a document, the same wherever the document is referred to."""
        if key not in self.numbers:
            self.numbers[key] = f"{initials(sender)}-{CODES.get(doc_type, 'DOC')}-26-{self.base + self.count:04d}"
            self.count += 1
        return self.numbers[key]

    def date(self, day):
        return (self.start + datetime.timedelta(days=day)).isoformat()


# ---------------------------------------------------------------- taxes, by the rules of the seller's country
def is_person(pid):
    return PARTY[pid]["identity"].get("person", False)


def is_public(pid):
    return PARTY[pid]["cat"] in ("government", "procurement")


def free_with_name(it):
    """The name of the item another comes free with: the model's name where it comes with each of its variants
    (the care kit with the Marrow bench in oak and in ash), the part of the variants' names before the comma."""
    return ITEM[it["free_with"][0]]["name"].split(",")[0]


def tax_rule(seller, buyer, iid):
    """The tax category of a supply: (code, percent, scheme, reason, exemption reason or None).

    Category codes are UN/EDIFACT 5305: S standard rate, E exempt, G free export item (tax not
    charged), O not subject to tax (outside the scope)."""
    s, b, it = PARTY[seller], PARTY[buyer], ITEM[iid]
    c = WORLD["countries"][s["c"]]
    scheme = c["tax"]["schemes"][0]
    if it.get("levy"):      # the reason a supply is outside the tax, in the exemption reason (D31 point 3, O107)
        return ("O", 0, scheme, f"A public levy the seller collects for {PARTY[it['levy']]['identity']['name']}: not a "
                                "supply, so outside the scope of the sales tax (category O, without a rate).",
                "Collected for a public body, outside the scope of the state sales tax")
    if s["c"] == "XU":
        if it.get("export_carriage"):       # the carriage of exported goods (D41)
            return ("E", 0, scheme, "The carriage of goods directly linked to their export from Urvania is exempt "
                                    "from its value added tax, as in most VAT systems (category E, D41).",
                    "Transport of goods exported from Urvania")
        if b["c"] == "XU":
            return ("S",c["tax"]["schemes"][0]["rates"]["standard"], scheme,
                    "A domestic supply in Urvania: its value added tax applies at the standard rate (category S).", None)
        if it["kind"] == "goods":
            return ("G", 0, scheme, "Goods exported from Urvania: no value added tax is charged on an export "
                                    "(category G, free export item).", "Export of goods outside Urvania")
        return ("O", 0, scheme, "A service supplied outside Urvania, to a customer established abroad, is outside the "
                                "scope of Urvania's value added tax (category O).", "Service supplied outside Urvania")
    if s["c"] == "XB":
        if b["c"] != "XB":
            return ("G", 0, scheme, "An export from Bayvarra: the state sales tax is not charged (category G).",
                    "Export outside Bayvarra")
        if is_person(buyer) and it["id"] != "water":
            state = s["identity"]["address"]["CountrySubentity"]
            return ("S", scheme["rates_by_state"][state], scheme,
                    f"A sale to a consumer: the sales tax of {state}, where the sale takes place, applies (category S).", None)
        if it["id"] == "water":
            return ("E", 0, scheme, "Drinking water is exempt from the state sales tax (category E).", "Drinking water")
        if is_public(buyer):
            return ("E", 0, scheme, "A sale to a public body is exempt from the state sales tax (category E).",
                    "Sale to a public body")
        if it["kind"] == "service":
            return ("E", 0, scheme, "Bayvarra's sales tax is charged only on sales to final consumers; a service to a "
                                    "business is exempt (category E).", "Service to a business")
        if it.get("free_with"):         # given with goods for resale, and handed on with them (furniture/09#F3)
            return ("E", 0, scheme, f"Supplied free with goods for resale: the {it['name']} goes with each "
                                    f"{free_with_name(it).split()[-1].lower()}, and the buyer hands it on "
                                    "with the goods it resells, so it is exempt from the state sales tax as they are; "
                                    "the tax is charged only on the sale to the final consumer (category E).",
                    "Sale for resale or manufacture: supplied free with goods for resale")
        return ("E", 0, scheme, "A sale to a business that resells or processes the goods is exempt from the state sales "
                                "tax, which is charged only on the sale to the final consumer (category E).",
                "Sale for resale or manufacture")
    return ("O", 0, None, "Lisavu has no sales tax or value added tax: no tax applies (category O).", None)


def supply_kind(iid):
    """Whether a line is a supply of goods or of services for SupplyTypeCode (worklist C31): electricity, gas and
    water are goods, whatever their tax treatment; a levy collected for someone else is no supply (None)."""
    it = ITEM[iid]
    kind = it.get("supply", it["kind"])
    return None if kind == "none" else kind


def tax_category(rule, kind=None):
    code, percent, scheme, why, exemption = rule
    out = {"ID": V(code, why)}
    if code != "O":                     # outside the scope of the tax: no rate at all (D15)
        out["Percent"] = V(str(percent), "The rate for this category." if percent else
                           "No tax is charged in this category.")
    if exemption:
        key = exemption.split(": ")[0]      # the code's reason, before any detail of this supply (furniture/09#F3)
        cc = next((k for k, c in WORLD["countries"].items() if key in c["tax"].get("exemption_codes", {})), None)
        if cc:
            out["TaxExemptionReasonCode"] = V(WORLD["countries"][cc]["tax"]["exemption_codes"][key],
                                              f"The exemption reason as a code of {WORLD['countries'][cc]['name']}'s "
                                              "national list, the list of the seller's country.",
                                              listID=codelists.NATIONAL.format(cc, "TaxExemptionReason"))
        detail = exemption.partition(": ")[2]
        out["TaxExemptionReason"] = (Detail(detail, "Why no tax is charged: the code's meaning and the detail of this "
                                                    "supply (UBL rule IND6).") if detail else
                                     V(exemption, "Why no tax is charged, stated rather than left out (UBL rule IND6)."))
    if kind:
        out["SupplyTypeCode"] = V("GOODS" if kind == "goods" else "SERVICES", "Whether the category applies to goods "
                                                                               "or services.")
    if scheme:
        out["TaxScheme"] = {"ID": V(scheme["id"], f"UN/EDIFACT 5153 code of the seller's tax: {scheme['name'].lower()}.")}
    else:
        out["TaxScheme"] = {"Name": V("No general sales tax", "Lisavu has no general tax on sales; the scheme is named "
                                      "only, as UN/EDIFACT 5153 has no code for the absence of a tax.")}
    return out


# ---------------------------------------------------------------- payment: terms, means, references
def rf_reference(text):
    """An ISO 11649 creditor reference: RF, two check digits (ISO 7064 mod 97-10) and the reference."""
    ref = "".join(c for c in text.upper() if c.isalnum())[:21]
    digits = "".join(str(int(c, 36)) for c in ref + "RF00")
    return f"RF{98 - int(digits) % 97:02d}{ref}"


def cross_border(a, b):
    return PARTY[a]["c"] != PARTY[b]["c"]


PLAN_PAYMENT = ("30 days net from the consignment note.", 30)    # the freight term of the framework transport plans


def terms_of(flow, seller, day, kind=None):
    """The payment terms an invoice issued on `day` applies, in the three layers of D22: the contract's (kind
    "plan": the transport plan's freight term, counted from the consignment note), the Trade Accord's utility
    term (kind "utility", D23), or else the seller's standard terms; late payment, where the terms say nothing,
    under the statutory interest of the seller's country. Returns the terms with the day counting starts and the
    due day, so that every due date follows from the terms the document cites (O70)."""
    pay = WORLD["countries"][PARTY[seller]["c"]]["payment"]
    if isinstance(kind, tuple) and kind[0] == "until-O72":   # sea/22: its balance term is settled with the sea flow
        t = terms_of(flow, seller, day)
        return {**t, "due": day + kind[1]}
    if kind == "plan":
        text, days = PLAN_PAYMENT
        start = flow.numbers[f"waybill-day-{seller}"]
        return {"id": None, "text": text, "why": "The payment term of the transport plan this freight is carried "
                "under: the contract wins over the carrier's standard terms (D22).", "start": start,
                "start_why": "From the consignment note's date.", "due": start + days, "discount": None,
                "surcharge": None, "interest": pay.get("statutory_interest")}
    if kind == "utility":
        t = WORLD["payment_terms_accord"]["TA-UTIL"]
        return {"id": "TA-UTIL", "id_why": "The Trade Accord's term for utility bills.", "text": t["terms"],
                "why": t["note"], "start": day, "start_why": "From the bill's date.", "due": day + t["due_days"],
                "discount": None, "surcharge": None, "interest": pay.get("statutory_interest")}
    c = WORLD["countries"][PARTY[seller]["c"]]
    return {"id": f"{PARTY[seller]['c']}-STD", "id_why": f"The standard terms of {c['name']}.", "text": pay["terms"],
            "why": pay["note"], "start": day, "start_why": "From the invoice date.", "due": day + pay["due_days"],
            "discount": pay.get("discount"), "surcharge": pay.get("penalty_surcharge"),
            # terms that set a surcharge for late payment say something on it: no statutory interest beside it (D22)
            "interest": pay.get("penalty_interest") or (None if pay.get("penalty_surcharge")
                                                        else pay.get("statutory_interest"))}


def payment_terms(flow, seller, buyer, t, total, cur, number):
    """The payment terms t (terms_of) as cac:PaymentTerms of an invoice."""
    out = {**({"ID": V(t["id"], t["id_why"])} if t["id"] else {}),
           "Note": V(t["text"], t["why"]),
           "PaymentDueDate": V(flow.date(t["due"]), "The day the amount is due, as the terms count it."),
           "PaymentMeansID": V("1", "The payment means these terms apply to: the credit transfer below.")}
    if t["discount"]:
        dsc = t["discount"]
        out["SettlementDiscountPercent"] = V(dsc["percent"], "The cash discount for early payment.")
        out["SettlementDiscountAmount"] = amount(total * Decimal(dsc["percent"]) / 100, cur, "The discount on the "
                                                 "amount payable, if paid in time.")
        out["SettlementPeriod"] = {"StartDate": V(flow.date(t["start"]), t["start_why"]),
                                   "EndDate": V(flow.date(t["start"] + dsc["days"]), f"For {dsc['days']} days.")}
    if t["surcharge"]:
        pen = t["surcharge"]
        out["PenaltySurchargePercent"] = V(pen["percent"], f"The surcharge per {pen['per']} of late payment.")
        out["PenaltyAmount"] = amount(total * Decimal(pen["percent"]) / 100, cur, "The surcharge for each month "
                                                                                  "late.")
        out["PenaltyPeriod"] = {"StartDate": V(flow.date(t["due"] + 1), "From the day after the due date, with "
                                               "no end: the surcharge runs per month for as long as the amount is "
                                               "late (worklist C38).")}
    if t["interest"]:
        pi = t["interest"]
        out["PenaltyInterestRate"] = {"InterestRatePercent": V(pi["percent"], "The interest on late payment" + (
                                          ": the statutory rate, as the terms say nothing on late payment (D22)."
                                          if t["id"] != f"{PARTY[seller]['c']}-STD" or not WORLD["countries"][
                                              PARTY[seller]["c"]]["payment"].get("penalty_interest") else ".")),
                                      "TimeBasisCode": V(pi["basis"], "A yearly rate."),
                                      "CalculationMethodCode": V("SIMPLE", "Simple interest, per day late.")}
    if t["id"] and t["id"].endswith("-STD") and PARTY[seller]["identity"].get("website"):
        out["PaymentTermsDetailsURI"] = V(PARTY[seller]["identity"]["website"] + "/terms", "The seller's general "
                                                                                           "terms of payment.")
    return out


def clearing_channel(border, seller):
    """The clearing channel of the payment system a transfer runs over: the first the system has (countries.json)."""
    system = WORLD["payment_cross_border"] if border else WORLD["countries"][PARTY[seller]["c"]]["payment"]["system"]
    return system["clearing_channels"][0]


def payment_means(flow, seller, buyer, payee, day, due_days, number, why_account, code="30"):
    """A credit transfer to the payee, with a structured payment reference the bank passes on."""
    border = cross_border(seller, buyer)
    system = WORLD["payment_cross_border"]["system"] if border else \
        WORLD["countries"][PARTY[seller]["c"]]["payment"]["system"]["id"]
    out = {"ID": V("1", "The first, and only, way to pay."),
           "PaymentMeansCode": V(code, "UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of "
                                       "UBL's payment means code list, which code list validation checks.",
                                 listID="UN/EDIFACT EDED 4461"),
           "PaymentMeansDescription": V("Credit transfer", "In words."),
           "PaymentDueDate": V(flow.date(day + due_days), "When the transfer must be credited."),
           "PaymentChannelCode": V(clearing_channel(border, seller), "How the payment system clears and settles the "
                                   "transfer, as an ISO 20022 clearing channel (world/countries.json)."),
           "PaymentRailID": V(system, "The payment system the transfer runs over: "
                              + ("the trade accord's link between the countries." if border else
                                 "the domestic clearing.")),
           "PaymentID": V(rf_reference(number), "The structured creditor reference of ISO 11649 to quote with the "
                                                "payment, made from the invoice number with its check digits."),
           "InstructionNote": V(f"Quote {rf_reference(number)}", "What the payer writes in the transfer.")}
    if border:
        out["ChargeBearerCode"] = V(WORLD["payment_cross_border"]["charge_bearer"], "ISO 20022 SHAR: each side pays "
                                                                                     "its own bank's charges.")
    import build_examples                       # the document the note is on names its kind (worklist C39)
    kind = {"Invoice": "Invoice", "CreditNote": "Credit note", "DebitNote": "Debit note",
            "SelfBilledInvoice": "Self-billed invoice", "SelfBilledCreditNote": "Self-billed credit note",
            "OrderResponse": "Deposit on sales order", "Order": "Order", "Reminder": "Invoice",
            "Statement": "Statement"}.get(build_examples.DOC_TYPE, "Invoice")
    out["PayeeFinancialAccount"] = account(payee, why_account, note=f"{kind} {number}")
    return out


def cost_centre(pid, why, iid=None):
    """The buyer's accounting cost, as code and text, from its identity: the cost centre of its chart for what is
    bought (worklist C14): for the item itself, or for its kind of purchase (freight, energy, telecom, packaging,
    services; world/items.json "purchase"), else the buyer's main cost centre."""
    idn = PARTY[pid]["identity"]
    cc = idn.get("cost_centre")
    chart = idn.get("cost_centres", {})
    if iid:
        cc = chart.get("items", {}).get(iid) or chart.get(ITEM[iid].get("purchase", "goods")) or cc
    if not cc:
        return {}
    return {"AccountingCostCode": V(cc["code"], why), "AccountingCost": V(cc["name"], "The cost centre in words.")}


# ---------------------------------------------------------------- lines and totals
def price_of(iid, buyer=None):
    """The price the seller asks this buyer for the item (world/items.json): a price agreed for the buyer
    (buyer_prices, such as Valdara's distributor price for Lumeway, D14), or else the item's own price, the
    seller's list price."""
    it = ITEM[iid]
    return it.get("buyer_prices", {}).get(buyer) or it["price"]


def unit_price(iid, currency, buyer=None):
    """The item's price for the buyer in `currency`: its own price, or converted at the world's reference rate."""
    pr = price_of(iid, buyer)
    p = Decimal(str(pr["amount"]))
    if pr["currency"] == currency:
        return p
    return money(p * rate(pr["currency"], currency), currency)


def deal_price(d, currency, buyer=None):
    """The unit price of a line of a deal: its own (unit_price, such as the trade price of the urgent air frames,
    where the buyer's own price holds only for goods by sea, O30), else the item's price for the buyer."""
    if "unit_price" in d:
        return Decimal(str(d["unit_price"]))
    return unit_price(d["item"], currency, buyer)


def deal_price_block(d, currency, buyer=None):
    """cac:Price of a line of a deal: its own unit price (deal_price), else the item's price block for the buyer."""
    if "unit_price" in d:
        return line_price(d, currency, buyer)
    return price_block(d["item"], currency, buyer)


def lines(flow, seller, buyer, currency, which="ordered", deal=None):
    """The lines of a commercial document from the deal: (item, quantity, line amount, rule)."""
    out = []
    for d in (deal or flow.deal):
        q = Decimal(str(d[which]))
        p = deal_price(d, currency, buyer)
        out.append((d, q, money(q * p, currency), tax_rule(seller, buyer, d["item"])))
    return out


def tax_total(rows, currency):
    """TaxTotal with one subtotal per tax category; every tax rounded to the currency's minor unit."""
    cats = {}
    for d, q, amt, rule in rows:
        cats.setdefault((rule[0], rule[1]), [rule, Decimal(0)])[1] += amt
    subs, total = [], Decimal(0)
    for (code, percent), (rule, base) in cats.items():
        tax = money(base * Decimal(str(percent)) / 100, currency)
        total += tax
        subs.append({"TaxableAmount": amount(base, currency, "The sum of the line amounts in this tax category."),
                     "TaxAmount": amount(tax, currency, f"{percent} % of the taxable amount, rounded to the minor unit "
                                                        f"of the currency."),
                     "TaxCategory": tax_category(rule)})
    return total, {"TaxAmount": amount(total, currency, "The sum of the tax of all categories."), "TaxSubtotal": subs}


def monetary_total(base, tax, currency, charges=Decimal(0)):
    out = {"LineExtensionAmount": amount(base, currency, "The sum of the line amounts.")}
    if charges:
        out["TaxExclusiveAmount"] = amount(base + charges, currency, "The line amounts plus the charges, without tax.")
    else:
        out["TaxExclusiveAmount"] = amount(base, currency, "The total without tax: the line amounts, no allowances or "
                                                           "charges.")
    out["TaxInclusiveAmount"] = amount(base + charges + tax, currency, "The total without tax plus the tax.")
    if charges:
        out["ChargeTotalAmount"] = amount(charges, currency, "The sum of the charges at document level.")
    out["PayableAmount"] = amount(base + charges + tax, currency, "What the buyer is to pay; stated, not left to be "
                                                                  "calculated (UBL 2.5, 2.2.2 Manifest Values).")
    return out


def currency_of(pid):
    return WORLD["countries"][PARTY[pid]["c"]]["currency"]["code"]


def currency_line(currency, who):
    cur = next(c for c in WORLD["countries"].values() if c["currency"]["code"] == currency)
    decimals = {0: "no minor unit", 2: "two decimals", 3: "three decimals"}[cur["currency"]["minor_units"]]
    return V(currency, f"The {cur['currency']['name'].lower()}, {who}; it has {decimals}.")


# ---------------------------------------------------------------- documents of trade
def order(flow, n, doc, day, why_date, terms_why, location, extra=None, deal=None, key="order", currency=None):
    buyer, seller = doc["from"], doc["to"]
    cur = currency or currency_of(seller)
    rows = lines(flow, seller, buyer, cur, deal=deal)
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    out = {
        "ID": V(flow.number(key, buyer, "Order"), "The buyer's order number."),
        "IssueDate": V(flow.date(day), why_date),
        "OrderTypeCode": V("220", "UN/EDIFACT 1001 code 220: order."),
        "DocumentCurrencyCode": currency_line(cur, "the seller's currency, in which the seller's prices are"
                                              if cur == currency_of(seller) else "the buyer's currency, agreed in the "
                                                                                 "contract"),
        **cost_centre(buyer, iid=rows[0][0]["item"], why="The buyer's cost centre, to be quoted on the invoice."),
        "LineCountNumeric": V(str(len(rows)), "The number of order lines."),
        "DeliveryTerms": {"ID": V(doc["values"]["DeliveryTerms/ID"], terms_why, schemeID="INCOTERMS"),
                          "DeliveryLocation": {"Description": V(location, "Where the delivery terms place the "
                                                                          "handover of the goods.")}},
        "TaxTotal": total,
        "AnticipatedMonetaryTotal": {
            "LineExtensionAmount": amount(base, cur, "The sum of the line amounts."),
            "PayableAmount": amount(base + tax, cur, "What the buyer expects to pay, tax included.")},
        "OrderLine": [{"LineItem": {
            "ID": V(d.get("line", str(i)), "The line number: a line added by a change keeps a number of its own "
                                           "(worklist C34)."),
            "Quantity": qty(q, ITEM[d["item"]]["unit"], d.get("why", "The quantity ordered.")),
            "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
            "Price": deal_price_block(d, cur, buyer),
            "Item": item(d["item"], buyer=buyer, catalogue_ref=flow.numbers.get("catalogue")
                         if flow.numbers.get("catalogue-from") == seller else None)}}
            for i, (d, q, amt, rule) in enumerate(rows, 1)],
    }
    for (d, *_), line in zip(rows, out["OrderLine"]):       # what the scenario adds to a line
        deep_merge(line["LineItem"], d.get("line_extra"))
        deep_merge(line, d.get("orderline_extra"))
    return merge_extra(out, extra)


def order_response(flow, n, doc, day, why, key="order"):
    return {"ID": V(flow.number("order-response", doc["from"], "OrderResponse"), "The seller's number for its response."),
            "IssueDate": V(flow.date(day), why),
            "OrderResponseCode": V("AP", "UN/EDIFACT 4343 code AP: accepted, the order is accepted as it stands."),
            "OrderReference": {"ID": V(flow.numbers[key], "The order this response answers.")}}


def price_block(iid, currency=None, buyer=None):
    it = ITEM[iid]
    pr = price_of(iid, buyer)
    if currency and currency != pr["currency"]:
        r = rate(pr["currency"], currency)
        return {"PriceAmount": price(unit_price(iid, currency, buyer), currency,
                                     f"The seller's price of {pr['amount']} {pr['currency']}, converted "
                                     f"to the buyer's currency at the world's reference rate, as the contract provides."),
                "BaseQuantity": qty(1, it["unit"], "The price is per one unit."),
                "PricingExchangeRate": {
                    "SourceCurrencyCode": V(pr["currency"], "The currency of the seller's price list."),
                    "TargetCurrencyCode": V(currency, "The currency of the order."),
                    "SourceCurrencyBaseRate": V("1", "The rate is for one unit of the seller's currency."),
                    "TargetCurrencyBaseRate": V("1", "Given in single units of the order's currency."),
                    "CalculationRate": V(f"{r.normalize():f}", "The world's reference rate (world/countries.json)."),
                    "MathematicOperatorCode": V("Multiply", "The seller's price times the rate gives the order price."),
                    "Date": V("2026-01-02", "The reference rate of the first working day of the year, fixed in the "
                                            "contract.")}}
    out = {"PriceAmount": price(pr["amount"], pr["currency"],
                                f"No price: the item comes free with each {free_with_name(it)} "
                                "(world/items.json)." if it.get("free_with") else
                                pr["why"] if pr.get("why") else
                                "The seller's price per unit (world/items.json)."),
           "BaseQuantity": qty(1, it["unit"], "The price is per one unit.")}
    return out


CHAIN = WORLD.get("goods_chain", {})


def chain_despatch(flow, sender, iid):
    """What a despatch of the goods chain moves (world/items.json goods_chain, D21): the date and the lines (lots
    or serial ranges) of the sender's ledger entry for the flow, or of Valdara's production shipped in the flow.
    None for an item outside the chain."""
    it = maker(iid)
    led = CHAIN.get("ledgers", {}).get(sender)
    if led:
        for e in led["entries"]:
            if e["flow"] == flow.id:
                lines = [ln for k in ("out", "crossdock") for ln in e.get(k, []) if ln["item"] == it["id"]]
                if lines:
                    return e["date"], lines
    lines, dates = [], set()
    for p in CHAIN.get("production", []):
        for fl, date in p["shipped"]:
            if fl == flow.id and p["item"] == it["id"]:
                lines.append({"item": p["item"], **({"lot": p["lot"], "qty": p["qty"]} if p.get("lot") else
                                                    {"serials": p["serials"]})})
                dates.add(date)
    if lines:
        if len(dates) != 1:
            raise SystemExit(f"{flow.id}: the goods chain ships {iid} on several days")
        return dates.pop(), lines
    if any(p["item"] == it["id"] for p in CHAIN.get("production", [])):
        raise SystemExit(f"{flow.id}: {sender} despatches {iid}, but the goods chain (world/items.json) has no "
                         "entry for it (D21, O65)")
    return None


def chain_slice(lines, skip, q):
    """The part of a goods chain's lines (lots or serial ranges, in order) after the first `skip` units, `q` units
    long: what one of several despatch lines of the same item takes (O172)."""
    out = []
    for ln in lines:
        n = ln.get("qty") or ln["serials"][1] - ln["serials"][0] + 1
        if skip >= n:
            skip -= n
            continue
        take = min(n - skip, q)
        if ln.get("serials"):
            first = ln["serials"][0] + skip
            out.append({**ln, "serials": [first, first + take - 1]})
        else:
            out.append({**ln, "qty": take})
        skip, q = 0, q - take
        if not q:
            break
    return out


def produced(line):
    """The production record entry of a lot or serial range (D21)."""
    for p in CHAIN["production"]:
        if p["item"] == line["item"] and (p.get("lot") == line.get("lot") if line.get("lot") else
                                          p.get("serials") and p["serials"][0] <= line["serials"][0]
                                          and line["serials"][1] <= p["serials"][1]):
            return p
    raise SystemExit(f"goods chain: {line} is in no production record entry (D21, O65)")


def instances(flow, d, which, day, sender=None):
    """ItemInstance for a despatched line: the production lot of the maker, or one instance per serial number;
    for the bench and its spare frame the lots and serials the goods chain moves (D21)."""
    it = ITEM[d["item"]]
    while it.get("resale_of"):         # a resold item keeps the maker's lot and serial numbers
        it = ITEM[it["resale_of"]]
    made = flow.date(day - 3)
    chain = chain_despatch(flow, sender, d["item"]) if sender else None
    if chain:
        date, lines = chain
        if flow.date(day) < date:        # a replacement despatch advice may follow the despatch it replaces
            raise SystemExit(f"{flow.id}: the despatch of {d['item']} is on {flow.date(day)}, before the goods chain "
                             f"(world/items.json) lets it leave, on {date} (O65)")
        q = int(Decimal(str(d[which])))
        same = [x for x in flow.deal if x["item"] == d["item"]]
        moved = sum(ln.get("qty") or ln["serials"][1] - ln["serials"][0] + 1 for ln in lines)
        total = sum(int(Decimal(str(x[which]))) for x in same) if any(x is d for x in same) else q
        if moved != total:
            raise SystemExit(f"{flow.id}: the despatch lines have {total} of {d['item']}, the goods chain moves "
                             f"{moved}")
        if len(same) > 1 and any(x is d for x in same):     # several lines of one item take the chain's lots in turn
            skip = sum(int(Decimal(str(x[which]))) for x in same[:next(i for i, x in enumerate(same) if x is d)])
            lines = chain_slice(lines, skip, q)
        out = []
        for ln in lines:
            p = produced(ln)
            if ln.get("serials"):
                for s_ in range(ln["serials"][0], ln["serials"][1] + 1):
                    out.append(casting_instance(it, s_, p))
            else:
                out.append(lot_instance(it, ln["lot"], p["made"], p))
        return out
    if it.get("serials"):
        q = int(Decimal(str(d[which])))
        first = flow.base * 10          # a stable range per flow: the same castings keep their numbers
        return [casting_instance(it, s_, {"made": made}) for s_ in range(first, first + q)]
    if it.get("lot_prefix"):
        lot = f"{it['lot_prefix']}{flow.date(day - 3).replace('-', '')[4:]}"
        x = lot_instance(it, lot, made)
        if it.get("best_before_months"):
            m = it["best_before_months"]
            d0 = datetime.date.fromisoformat(made)
            until = d0.replace(year=d0.year + (d0.month - 1 + m) // 12, month=(d0.month - 1 + m) % 12 + 1).isoformat()
            x["BestBeforeDate"] = V(until, f"Best used within {m} months: the granulate takes up moisture in storage.")
            x["LotIdentification"]["ExpiryDate"] = V(until, "The lot's quality data apply until then.")
        return [x]
    return None


def lot_instance(it, lot, made, p=None):
    """The ItemInstance of a production lot: its number and day, and the facts the maker records for it (for a lot
    of the goods chain, its coating batch from the production record, D21)."""
    x = {"ManufactureDate": V(made, "The day the lot was produced."),
         "LotIdentification": {"LotNumberID": V(lot, "The production lot, from the maker's prefix and the "
                                                     "production day; a recall names the lot.")}}
    if p and p.get("coating"):
        x["LotIdentification"]["AdditionalItemProperty"] = {
            "Name": V("Coating batch", "A fact about this lot: the galvanising and powder-coating batch its frames "
                                       "went through."),
            "Value": V(p["coating"], "Its batch: each lot has its own, in the coating line's running count of the year "
                                     "(the production record, world/items.json goods_chain, D21).")}
    if it.get("lot_props"):
        x["LotIdentification"]["AdditionalItemProperty"] = [{"Name": V(n_, "A fact about this lot."),
                                                             "Value": V(v, "Its value for this lot.")}
                                                            for n_, v in it["lot_props"]]
    return x


def casting_instance(it, s_, p):
    """The ItemInstance of one serial-numbered casting: its serial, trace and register numbers and the day it was
    cast (the production record entry p, D21)."""
    x = {"ManufactureDate": V(p["made"], "The day the casting was poured and inspected."),
         "SerialID": V(f"{it['serials']}{s_:05d}", "The serial number cast into the frame; every casting is "
                                                   "traceable to its melt, and the numbers rise with the day of "
                                                   "casting.")}
    if p.get("poured"):
        x["ManufactureTime"] = V(p["poured"], "The time the day's melt was poured" + (
            f": {p['poured_why'][0].lower() + p['poured_why'][1:]}" if p.get("poured_why") else
            ", the foundry's first melt of the day."))
    if it.get("trace"):
        x["ProductTraceID"] = V(f"{it['trace']}{s_:05d}", "The trace code on the casting's label, for the "
                                                        "maker's tracing system.")
    if it.get("registration"):
        x["RegistrationID"] = V(f"{it['registration']}{s_:05d}", "The casting's entry in the maker's quality "
                                                               "register, with its inspection result.")
    if p.get("melt"):
        x["AdditionalItemProperty"] = {"Name": V("Melt number", "A fact about this one casting: the melt of iron it "
                                                               "was poured from."),
                                       "Value": V(p["melt"], "Its melt: one per casting day, in the foundry's running "
                                                             "count of the year (the production record, "
                                                             "world/items.json goods_chain, D21).")}
    return x


TRANSIT_DAYS = {"air": 0, "road": 1, "rail": 2, "river": 2, "sea": 3}   # door to door, until the place list (O91)


def despatch_delivery(flow, day):
    """When the goods leave and when they are expected (worklist C27): despatched on the day of the advice, expected
    after the usual transit of the flow's main mode."""
    legs = next(x for x in WORLD["flows"] if x["id"] == flow.id).get("legs", [])
    leg = next((x for x in legs if x["mode"] != "road"), legs[0] if legs else {"mode": "road"})
    mode = leg["mode"]
    flow.numbers["despatch-day"] = day
    flow.numbers["delivery-day"] = day + leg.get("transit_days", TRANSIT_DAYS[mode])
    arrive = flow.date(flow.numbers["delivery-day"])        # a leg may state its own transit
    return {"Despatch": {"ActualDespatchDate": V(flow.date(day), "The goods left on the day of this advice.")},
            "EstimatedDeliveryPeriod": {"StartDate": V(arrive, f"Expected after the usual transit by {mode}."),
                                        "EndDate": V(arrive, "The same day.")}}


def despatch_advice(flow, n, doc, day, why, shipment_why, extra=None, deal=None, key="order"):
    deal = deal or flow.deal
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = {
        "ID": V(flow.number(f"despatch-{key}", doc["from"], "DespatchAdvice"), "The despatching party's number."),
        "IssueDate": V(flow.date(day), why),
        "DespatchAdviceTypeCode": V("DELIVERY", "Advice of goods despatched for delivery."),
        "Note": V("Please check the goods on arrival and report any damage " + (
                      "in your receipt advice." if any(d["flow"] == flow.id and d["doc"] == "ReceiptAdvice"
                                                       for d in WORLD["documents"])
                      else f"on the {transport_document_name(flow)}."),
                  "What the receiver should do; the note names the transport document the flow uses (worklist C30)."),
        "LineCountNumeric": V(str(len(deal)), "The number of lines."),
        "OrderReference": {"ID": V(flow.numbers[key], "The order this despatch fulfils.")},
        "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The despatching party's shipment number."),
                     "GrossWeightMeasure": qty(gross_weight(flow, which, deal), "KGM", shipment_why),
                     "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                             "The consignment the goods travel in, as numbered when the transport "
                                             "was booked.")},
                     "Delivery": despatch_delivery(flow, day)},
        "DespatchLine": [{"ID": V(str(i), "The line number."),
                          "Note": V(d.get("why", "As ordered."), "The line as the order put it."),
                          "DeliveredQuantity": qty(d[which], ITEM[d["item"]]["unit"], "What was despatched."),
                          "OrderLineReference": {"LineID": V(d.get("line", str(i)), "The order line this line "
                                                                                    "fulfils.")},
                          "Item": item(d["item"], buyer=doc["to"], instance=instances(flow, d, which, day, doc["from"]))}
                         for i, d in enumerate(deal, 1)],
    }
    flow.numbers["despatch"] = flow.numbers[f"despatch-{key}"]
    flow.numbers["despatch-to"] = doc["to"]
    return merge_extra(out, extra)


def receipt_advice(flow, n, doc, day, why):
    which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
    short = any("received" in d for d in flow.deal)
    out = {"ID": V(flow.number("receipt", doc["from"], "ReceiptAdvice"), "The receiving party's number."),
            "IssueDate": V(flow.date(day), why),
            "ReceiptAdviceTypeCode": V("Actual", "UBL's receipt advice type code: the goods actually received."),
            "DeliveryAcceptanceCode": V("PARTIAL" if short else "ACCEPTED", "Part of the goods refused." if short
                                        else "All goods accepted."),
            "Note": V("Counted and checked at goods-in.", "How the goods were received."),
            "LineCountNumeric": V(str(len(flow.deal)), "The number of lines."),
            "OrderReference": {"ID": V(flow.numbers["order"], "The order the goods were delivered for.")},
            "DespatchDocumentReference": {"ID": V(flow.numbers["despatch"], "The despatch advice this receipt answers.")},
            "ReceiptLine": [{"ID": V(str(i), "The line number."),
                             "ReceivedQuantity": qty(d.get("received", d[which]), ITEM[d["item"]]["unit"],
                                                     d.get("received_why", "Counted at the goods-in and found as "
                                                                           "announced.")),
                             "Note": V(d.get("received_why", "Received as despatched."), "The line in words."),
                             "ReceivedDate": V(flow.date(day), "Unloaded."),
                             "OrderLineReference": {"LineID": V(d.get("line", str(i)), "The order line.")},
                             "DespatchLineReference": {"LineID": V(str(i), "The despatch line."),
                                                       "DocumentReference": {"ID": V(flow.numbers["despatch"],
                                                                                     "The despatch advice.")}},
                             "Item": item(d["item"], buyer=doc["from"])} for i, d in enumerate(flow.deal, 1)]}
    for d, line in zip(flow.deal, out["ReceiptLine"]):
        if "received" in d:
            refused = Decimal(str(d[which])) - Decimal(str(d["received"]))
            line.update({"RejectedQuantity": qty(refused, ITEM[d["item"]]["unit"], "Refused at goods-in."),
                         "RejectReasonCode": V("DAMAGED", "Why refused."),
                         "RejectReason": V(d["received_why"], "In words."),
                         "RejectActionCode": V("CREDIT", "The receiver asks for a credit, not a replacement."),
                         "QuantityDiscrepancyCode": V("DAMAGED", "Why the quantity differs from the despatch.")})
            out.update({"RejectReasonCode": V("DAMAGED", "The reason for the part refused."),
                        "RejectReason": V("Damaged in transit.", "In words."),
                        "RejectActionCode": V("CREDIT", "A credit is asked for the refused goods.")})
    return out


def gross_weight(flow, which, deal=None):
    """The gross weight of a deal's goods: in their parcels and, where the flow ships on pallets, with the pallets'
    own weight (D20)."""
    return sum((line_gross(flow, d, which) for d in (deal or flow.deal)), Decimal(0))


def invoice(flow, n, doc, day, why_date, refs, rows_spec=None, key="invoice", extra=None, charges=None,
            currency=None, terms=None):
    """A commercial invoice from the seller (doc['from']) to the buyer; rows_spec overrides the deal. terms: the
    kind of payment terms (terms_of): "plan", "utility", or the seller's standard terms."""
    seller, buyer = doc["from"], doc["to"]
    t = terms_of(flow, seller, day, terms)
    due_days = t["due"] - day
    flow.numbers[f"{key}-terms"] = t
    cur = currency or currency_of(seller)
    if rows_spec is None:
        which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
        rows = lines(flow, seller, buyer, cur, which)
    else:
        rows = [(d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * deal_price(d, cur, buyer), cur),
                 tax_rule(seller, buyer, d["item"])) for d in rows_spec]
    rows, gross = line_allowances(rows, cur)
    base = sum(r[2] for r in rows)
    charge_rows = [({"item": c["like"]}, None, money(Decimal(str(c["amount"])), cur), tax_rule(seller, buyer, c["like"]))
                   for c in (charges or [])]
    tax, total = tax_total(rows + charge_rows, cur)
    out = {
        "ID": V(flow.number(key, seller, "Invoice"), "The seller's invoice number."),
        "IssueDate": V(flow.date(day), why_date),
        "DueDate": V(flow.date(t["due"]), f"As the payment terms below count it: {t['text'][0].lower()}{t['text'][1:]}"),
        "InvoiceTypeCode": V("393", "The invoice is assigned to the factor, who collects it: a factored invoice, a "
                                    "subtype UN/EDIFACT 1001 has its own code for.")
        if PARTY.get(doc["parties"].get("PayeeParty"), {}).get("name") == "Factor" else
        V("380", "A commercial invoice, as UN/EDIFACT 1001 codes it."),
        "DocumentCurrencyCode": currency_line(cur, "the seller's currency" if cur == currency_of(seller)
                                              else "the buyer's currency, agreed in the contract"),
        **cost_centre(buyer, iid=rows[0][0]["item"], why="The buyer's cost centre, quoted in its order, so the invoice is booked without "
                            "asking."),
        "LineCountNumeric": V(str(len(rows)), "The number of invoice lines, as a check on the transfer."),
        "DefaultLanguageCode": V(WORLD["countries"][PARTY[seller]["c"]]["languages"][-1], "The language of the "
                                 "texts that carry no language identifier: English, the working language between "
                                 "the countries; a seller from Urvania or the island also gives its notes in its "
                                 "own language."),
        **refs,
        **({"PaymentCurrencyCode": V(cur, "Payment is asked in the invoice currency, also from abroad.")}
           if cross_border(seller, buyer) else {}),
        **({"BuyerAssignedReference": {
            "BuyerReferenceCode": V(f"{PARTY[buyer]['identity']['cost_centre']['code']}-AP", "The buyer's routing "
                                    "code for its invoices: the accounts-payable desk of the cost centre."),
            "BuyerReference": V("Accounts payable, public works", "The desk in words.")}}
           if is_public(buyer) and PARTY[buyer]["identity"].get("cost_centre") else {}),
        "PaymentMeans": payment_means(flow, seller, buyer, doc["parties"].get("PayeeParty", seller), day, due_days,
                                      flow.number(key, seller, "Invoice"), "The account to pay to."),
        "PaymentTerms": payment_terms(flow, seller, buyer, t, base + tax + sum(r[2] for r in charge_rows), cur,
                                      flow.number(key, seller, "Invoice")),
        "TaxTotal": total,
        "LegalMonetaryTotal": monetary_total(base, tax, cur, sum(r[2] for r in charge_rows)),
        "InvoiceLine": [{
            "ID": V(str(i), "The line number."),
            "InvoicedQuantity": qty(q, ITEM[d["item"]]["unit"], d.get("invoice_why", "The quantity delivered.")),
            "LineExtensionAmount": amount(amt, cur, f"{q} × {deal_price(d, cur, buyer)}, rounded to the minor "
                                                    "unit of the currency."),
            "Item": item(d["item"], tax_category(rule, supply_kind(d["item"]))),
            "Price": deal_price_block(d, cur, buyer)} for i, (d, q, amt, rule) in enumerate(rows, 1)],
    }
    line_features(rows, out["InvoiceLine"], cur, gross)
    if rows_spec is None and "OrderReference" in refs:      # the lines of the deal are the lines of the order
        for i, (line, (d, *_)) in enumerate(zip(out["InvoiceLine"], rows), 1):
            line["OrderLineReference"] = {"LineID": V(d.get("line", str(i)), "The order line this invoice line "
                                                                             "bills.")}
    if "TaxPointDate" not in out and PARTY[seller]["c"] == "XU":
        out["TaxPointDate"] = V(flow.date(day), "Urvania's value added tax becomes due on the invoice date.")
    if charges:
        out["AllowanceCharge"] = [{"ChargeIndicator": V("true", "A charge, not an allowance: it adds to the amount."),
                                   "AllowanceChargeReasonCode": V(c["code"], c["code_why"]),
                                   "AllowanceChargeReason": V(c["reason"], c["why"]),
                                   "Amount": amount(c["amount"], cur, c["amount_why"]),
                                   "TaxCategory": tax_category(r[3])} for c, r in zip(charges, charge_rows)]
    stmt = origin_statement(flow, seller, buyer, [d["item"] for d, *_ in rows])
    if stmt:
        out["_origin"] = stmt                    # written into the Note at the end (build_examples.origin_notes)
    flow.numbers[f"{key}-amount"] = base + sum(r[2] for r in charge_rows) + tax
    flow.numbers[f"{key}-date"] = flow.date(day)
    flow.numbers[f"{key}-currency"] = cur
    out = merge_extra(out, extra)
    if any(ITEM[r[0]["item"]]["kind"] == "goods" for r in rows):
        invoice_delivery(flow, out, buyer, day)
    return out


def invoice_delivery(flow, out, buyer, day):
    """An invoice for goods is linked to the delivery it bills (worklist C32): the despatch advice of this sale,
    where the flow has one, and the delivery: where the goods go and when they arrived, or, for an invoice issued
    on despatch, when they left."""
    same = flow.numbers.get("despatch-to") == buyer        # the despatch advice of this sale, not of another
    if same and "despatch" in flow.numbers and "DespatchDocumentReference" not in out:
        out["DespatchDocumentReference"] = {"ID": V(flow.numbers["despatch"], "The despatch advice of the goods "
                                                                              "billed.")}
    if "Delivery" in out:
        return
    legs = next(x for x in WORLD["flows"] if x["id"] == flow.id).get("legs", [])
    leg = next((x for x in legs if x["to"] == buyer), None)
    delivery = {}
    if leg:
        delivery["DeliveryLocation"] = leg_location(leg, "to", "Where the goods billed are delivered.")
    arrived = flow.numbers.get("delivery-day") if same else None
    if arrived is not None and arrived <= day:
        delivery = {"ActualDeliveryDate": V(flow.date(arrived), "The day the goods billed were delivered."),
                    **delivery}
    elif same and flow.numbers.get("despatch-day") is not None:
        delivery["Despatch"] = {"ActualDespatchDate": V(flow.date(flow.numbers["despatch-day"]), "The invoice is "
                                                        "issued on despatch: the day the goods left.")}
    if delivery:
        out["Delivery"] = delivery


def remittance(flow, n, doc, day, why, key="invoice", discount=None, credit=None,
               purpose=("SUPP", "payment to a supplier")):
    """credit: (number, date, amount) of a credit note the payer deducts. purpose: the ISO 20022 purpose of the
    payment, which names what the invoice paid is for (worklist C17)."""
    payer, payee = doc["from"], doc["to"]
    cur, total = flow.numbers[f"{key}-currency"], flow.numbers[f"{key}-amount"]
    paid = money(total * (1 - Decimal(discount) / 100), cur) if discount else total
    if credit:
        paid -= credit[2]
    out = {
        "ID": V(flow.number("remittance", payer, "RemittanceAdvice"), "The payer's remittance number."),
        "IssueDate": V(flow.date(day), why),
        "DocumentCurrencyCode": currency_line(cur, "the currency of the invoice paid"),
        "Note": V("Payment of the invoice below.", "What the advice is for."),
        "TotalDebitAmount": amount(total, cur, "The invoices paid."),
        "TotalCreditAmount": amount(total - paid, cur, "Credits taken: the settlement discount." if discount else
                                    "The credit note deducted." if credit else "No credits taken."),
        "PaymentOrderReference": V(f"{initials(payer)}-PAY-26-{flow.base:04d}", "The payment order the payer gave "
                                                                                "its bank."),
        "InvoicingPartyReference": V(rf_reference(flow.numbers[key]), "The reference the invoicing party asked to "
                                                                      "quote."),
        "LineCountNumeric": V("2" if credit else "1", "The invoice paid" + (" and the credit note deducted."
                                                                             if credit else ".")),
        "TotalPaymentAmount": amount(paid, cur, f"The amount transferred: the payable amount less the {discount} % "
                                                f"discount for payment within the discount period." if discount else
                                     "The amount transferred: the invoice less the credit note." if credit else
                                     "The amount transferred: the payable amount of the invoice."),
        "PaymentMeans": {
            "PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer.", listID="UN/EDIFACT EDED 4461"),
            "InstructionID": V(f"{initials(payer)}-PAY-26-{flow.base:04d}", "The payer's own number for the payment "
                                                                            "order it gave its bank."),
            "PaymentID": V(rf_reference(flow.numbers[key]), "The creditor reference from the invoice, quoted so the "
                                                           "payee can match the payment automatically."),
            "PayerFinancialAccount": account(payer, "The account the payer pays from."),
            "PayeeFinancialAccount": account(doc["parties"].get("PayeeParty", payee), "The account stated on the invoice.")},
        "RemittanceAdviceLine": {
            "ID": V("1", "One invoice paid."),
            "PaymentPurposeCode": V(purpose[0], f"ISO 20022 purpose code {purpose[0]}: {purpose[1]}."),
            "InvoicingPartyReference": V(rf_reference(flow.numbers[key]), "The reference the invoicing party asked "
                                                                          "to quote."),
            "BalanceAmount": amount(0, cur, "Nothing remains open on the invoice after this payment."),
            "DebitLineAmount": amount(total, cur, "The amount of the invoice this payment settles: the whole payable "
                                                  "amount. Paid invoices are debits on a remittance advice, as in the "
                                                  "OASIS example UBL-RemittanceAdvice-2.0-Example."),
            **({"CreditLineAmount": amount(total - paid, cur, "The settlement discount taken, a credit against the "
                                                              "invoice."),
                "Note": V(f"{discount} % discount taken: paid within the discount period of the invoice's terms.",
                          "Why less is paid than invoiced.")} if discount else {}),
            "BillingReference": {"InvoiceDocumentReference": {
                "ID": V(flow.numbers[key], "The invoice this payment settles."),
                "IssueDate": V(flow.numbers[f"{key}-date"], "Its issue date, so the reference is unambiguous.")}}},
    }
    if credit:
        out["RemittanceAdviceLine"] = [out["RemittanceAdviceLine"], {
            "ID": V("2", "The credit note deducted."),
            "CreditLineAmount": amount(credit[2], cur, "The amount of the credit note, set off against the payment."),
            "BillingReference": {"CreditNoteDocumentReference": {
                "ID": V(credit[0], "The credit note deducted."),
                "IssueDate": V(credit[1], "Its issue date.")}}}]
    return out


# ---------------------------------------------------------------- transport
def flow_leg(flow, carrier):
    """The flow's transport leg carried by `carrier` (world/documents.json, "legs")."""
    f = next(x for x in WORLD["flows"] if x["id"] == flow.id)
    return next(leg for leg in f["legs"] if leg["carrier"] == carrier)


def main_leg(flow, carrier):
    """The carrier's main carriage: of several legs, the one that is not the road pre- or on-carriage."""
    f = next(x for x in WORLD["flows"] if x["id"] == flow.id)
    legs = [leg for leg in f["legs"] if leg["carrier"] == carrier]
    return next((leg for leg in legs if leg["mode"] != "road"), legs[0])


def main_service(flow, carrier):
    """The main transport service of a carrier's carriage, chosen by its main leg and its cargo, not by the mode
    alone (worklist C35): a leg names its service in world/documents.json where the mode does not tell it."""
    leg = main_leg(flow, carrier)
    code = leg.get("service") or MODE_SERVICE_CODE[leg["mode"]]
    name = codelists.load()["lists"]["TransportService"]["codes"][code]["name"]
    return {"TransportServiceCode": V(code, f"The main service, by the carrier's main leg ({leg['mode']}) and what "
                                            "it carries."), "Name": V(name, "In words.")}


MODE_SERVICE_CODE = {"road": "FTL", "rail": "RAILCONT", "river": "RIVERBARGE", "sea": "OCEANCONT", "air": "AIRCARGO"}
MODE_SERVICE = {"road": "Full truck load", "rail": "Container train", "river": "River barge", "sea": "Liner service",
                "air": "Air cargo"}


def leg_location(leg, end, why):
    """The place at one end of a transport leg (world/documents.json, from_place and to_place): where the goods are
    taken over or handed over, by its name and, where the world has one, its GLN or UN/LOCODE-form code; not the
    company's name and office address (worklist C10)."""
    pl = leg[f"{end}_place"]
    if pl.get("gln"):
        pid, key = pl["gln"].split(":")
        return {**gln_location(pid, key), "Name": V(pl["name"], why)}
    if pl.get("locode"):
        return place(pl["locode"], why, name=pl["name"])
    return {"Name": V(pl["name"], why)}


def leg_places(flow, carrier):
    leg = flow_leg(flow, carrier)
    return leg, {"FromLocation": leg_location(leg, "from", "Where the goods are taken over."),
                 "ToLocation": leg_location(leg, "to", "Where the goods are handed over.")}


def address_of(pid):
    from build_examples import address
    return address(pid)


# Bonus and commission terms of a transport plan, only where the flow has them (a plan without them says nothing).
TEP_BONUS = {"ore": ("2 % of the freight when the train is delivered on the first day of the service window, "
                     "so that the factory can start the blend a day early.", "The bonus the factory pays for an "
                     "early train: its stockyard can use the ore at once.")}
TEP_COMMISSION = {}      # the barge is booked directly under the framework terms: no broker (plastics/04#F15)
WAITING_LUME = 40        # the waiting-time rate of the framework terms, in lume an hour


def waiting_rate(carrier):
    """The waiting-time rate in the carrier's own currency, at the parities (1 lume = 100 ferra = 0.4 coral)."""
    c = WORLD["countries"][PARTY[carrier]["c"]]["currency"]
    per = {"XBL": Decimal(1), "XUF": Decimal(100), "XLC": Decimal("0.4")}[c["code"]]
    return f"{WAITING_LUME * per:,.0f} {c['name'].lower()}"


def tep_terms(flow, user, provider, days):
    """The terms of a transport plan: payment, a penalty for late delivery, notification before arrival."""
    leg = flow_leg(flow, provider)
    return {"TransportUserSpecialTerms": V("Delivery within the agreed slot; the consignee unloads.", "The user's "
                                                                                                     "terms."),
            "TransportServiceProviderSpecialTerms": V("Waiting time beyond two hours is charged.", "The carrier's."),
            "ChangeConditions": V("Changes up to 24 hours before collection without charge.", "When the plan may "
                                                                                              "change."),
            "PaymentTerms": {"Note": V(PLAN_PAYMENT[0], "When the freight is paid: the term the carrier's "
                                                        "invoices under this plan apply (D22).")},
            "PenaltyPaymentTerms": {"Note": V("For late delivery the carrier is liable for 5 % of the freight per "
                                              "day late, at most 25 %.", "The carrier's liability for delay, in "
                                              "words: PenaltySurchargePercent is a surcharge for late payment, not "
                                              "for late delivery (worklist C19).")},
            **({"BonusPaymentTerms": {"Note": V(*TEP_BONUS[flow.id])}} if flow.id in TEP_BONUS else {}),
            **({"CommissionPaymentTerms": {"Note": V(*TEP_COMMISSION[flow.id])}} if flow.id in TEP_COMMISSION
               else {}),
            "ServiceChargePaymentTerms": {"Note": V(f"Waiting time {waiting_rate(provider)} per hour beyond two "
                                                    "hours.", "The service charge, in the carrier's currency, at "
                                                              "the rate of its framework terms.")},
            "NotificationRequirement": {"NotificationTypeCode": V("PREARRIVAL", "Notice before arrival."),
                                        "PreEventNotificationDurationMeasure": V("2", "Two hours before.",
                                                                                 unitCode="HUR"),
                                        "NotifyParty": party_short(main_leg(flow, provider)["to"]),
                                        "NotificationLocation": leg_location(main_leg(flow, provider), "to",
                                                                             "The place the notice is for: where "
                                                                             "the goods arrive.")}}


def tep_request(flow, n, doc, day, why, start_day, weight, why_weight):
    leg, places = leg_places(flow, doc["to"])
    mode = leg["mode"]
    return {"ID": V(flow.number("tep-request", doc["from"], "TransportExecutionPlanRequest"),
                    "The transport user's request number."),
            "VersionID": V("1", "The first version of the request."),
            "IssueDate": V(flow.date(day), why),
            "Note": V(leg["why"], "The transport asked for."),
            "TransportUserRemarks": V("Please confirm by return.", "The user's remark."),
            "BillToParty": party_short(doc["from"]),
            "TransportContract": {"ID": V(f"{initials(doc['from'])}-{initials(doc['to'])}-FW-2026", "The framework "
                                                                                                  "agreement with "
                                                                                                  "the carrier.")},
            "TransportServiceProviderResponseDeadlinePeriod": {"EndDate": V(flow.date(day + 1), "An answer is "
                                                                                                 "needed by the "
                                                                                                 "next day.")},
            "MainTransportationService": main_service(flow, doc["to"]),
            "ServiceStartTimePeriod": {"StartDate": V(flow.date(start_day), "The day the goods should be collected.")},
            "ServiceEndTimePeriod": {"EndDate": V(flow.date(start_day + 3), "Delivered within three days.")},
            **places,
            "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                    "The transport user's number for this consignment, quoted along the chain."),
                            "GrossWeightMeasure": qty(weight, "KGM", why_weight)}}


def tep(flow, n, doc, day, why, start_day, weight):
    leg, places = leg_places(flow, doc["from"])
    mode = leg["mode"]
    return {"ID": V(flow.number("tep", doc["from"], "TransportExecutionPlan"), "The carrier's number for the agreed plan."),
            "VersionID": V("1", "The first version of the plan."),
            "IssueDate": V(flow.date(day), why),
            "DocumentStatusCode": V("Confirmed", "The carrier confirms the plan as requested. A value of UBL's document "
                                                 "status code list (2.1: Document has been confirmed)."),
            "DocumentStatusReasonCode": V("ASREQUESTED", "Confirmed without changes."),
            "DocumentStatusReasonDescription": V("Capacity available on the requested day.", "Why it is confirmed."),
            "Note": V(leg["why"], "The transport agreed."),
            "TransportUserRemarks": V("Please confirm by return.", "The user's remark from the request."),
            "TransportServiceProviderRemarks": V("Collection as requested; notice two hours before arrival.",
                                                 "The carrier's remark."),
            "BillToParty": party_short(doc["to"]),
            "Signature": {"ID": V(f"{initials(doc['from'])}-SIG-{flow.base}", "The carrier's seal on the plan."),
                          "SignatoryParty": party_short(doc["from"])},
            "TransportContract": {"ID": V(f"{initials(doc['to'])}-{initials(doc['from'])}-FW-2026", "The framework "
                                                                                                  "agreement."),
                                  "ContractType": V("Framework transport agreement", "Its kind.")},
            "TransportUserResponseRequiredPeriod": {"EndDate": V(flow.date(day + 1), "The user may object until "
                                                                                     "the next day.")},
            "TransportServiceProviderResponseRequiredPeriod": {"EndDate": V(flow.date(day), "The carrier answered "
                                                                                            "the same day.")},
            "ValidityPeriod": {"StartDate": V(flow.date(day), "From the confirmation."),
                               "EndDate": V(flow.date(start_day + 3), "Until the carriage is done.")},
            "MainTransportationService": main_service(flow, doc["from"]),
            "AdditionalTransportationService": {"TransportServiceCode": V("NOTIFY", "Pre-arrival notice."),
                                                "Name": V("Notice two hours before arrival", "In words.")},
            "ServiceEndTimePeriod": {"EndDate": V(flow.date(start_day + 3), "Delivered within three days.")},
            **places,
            "TransportExecutionTerms": tep_terms(flow, doc["to"], doc["from"], 3),
            "TransportExecutionPlanRequestDocumentReference": {"ID": V(flow.numbers["tep-request"],
                                                                       "The request this plan answers.")},
            "ServiceStartTimePeriod": {"StartDate": V(flow.date(start_day), "Collection, as requested.")},
            "Consignment": {"ID": V(flow.numbers["consignment"], "The consignment of the request."),
                            "GrossWeightMeasure": qty(weight, "KGM", "The weight the plan is made for.")}}


WAYBILL_KIND = {"road": ("CMR", "Consignment note under the road convention, the CMR"),
                "rail": ("CIM", "Rail consignment note under the Accord's uniform rules for international carriage "
                                "by rail, modelled on the CIM"),       # D37 point 5
                "river": ("CMNI", "Inland waterway consignment note under the CMNI"),
                "air": ("AWB", "Air waybill under the Montreal Convention")}


DOMESTIC_KIND = {"road": ("NATROAD", "Consignment note under the national road carriage law"),
                 "rail": ("NATRAIL", "Consignment note under the national rail carriage law")}


def waybill_kind(flow, carrier):
    """The convention a consignment note follows, by the mode of the carrier's main leg and its scope: the
    international conventions only for carriage between two countries, national law within one (worklist C30,
    D46)."""
    leg = main_leg(flow, carrier)
    start = next(x for x in WORLD["flows"] if x["id"] == flow.id)["legs"]
    first = next(x for x in start if x["carrier"] == carrier)
    domestic = PARTY[first["from"]]["c"] == PARTY[leg["to"]]["c"]
    if domestic and leg["mode"] in DOMESTIC_KIND:
        return DOMESTIC_KIND[leg["mode"]]
    return WAYBILL_KIND[leg["mode"]]


def transport_document_name(flow):
    """What the flow's main transport document is called, for texts that name it."""
    legs = next(x for x in WORLD["flows"] if x["id"] == flow.id).get("legs", [])
    modes = {leg["mode"] for leg in legs}
    return ("bill of lading" if "sea" in modes else "air waybill" if "air" in modes else "consignment note")


def shipping_order(flow):
    """The ShippingOrderID of a shipment: the number of the forwarding instructions it is booked under, to the
    carrier where there are two (worklist C20); None where the flow has no forwarding instructions."""
    return flow.numbers.get("instructions-carrier") or flow.numbers.get("instructions")


def waybill(flow, n, doc, day, why, weight, why_weight, extra=None):
    carrier = doc["from"]
    leg = flow_leg(flow, carrier)
    kind, kind_name = waybill_kind(flow, carrier)
    number = flow.number("waybill", doc["from"], "Waybill")
    flow.numbers[f"waybill-day-{carrier}"] = day          # a freight term may count from it (PLAN_PAYMENT)
    out = {"ID": V(number, "The consignment note number."),
           "CarrierAssignedID": V(f"{initials(carrier)}-{kind}-26-{flow.base:04d}", "The carrier's own number for "
                                                                                    "the carriage."),
           "VersionID": V("1", "The original, not a corrected version."),
           "StatusCode": V("ISSUED", "The note is issued and in force."),
           "IssueDate": V(flow.date(day), why),
           "Name": V(kind_name, "The kind of transport document."),
           **({"ShippingOrderID": V(shipping_order(flow), "The forwarding instructions the carriage is booked "
                                                          "under.")} if shipping_order(flow) else {}),
           "Description": V(leg["why"], "The carriage in words."),
           "Note": V("Three originals: the consignor's, handed over when the carrier took over the goods; the "
                     "consignee's, with the goods; the carrier's, kept by the carrier.", "The originals the convention "
                     "prescribes, as the distribution below lists them; the carrier's own is not distributed "
                     "(worklist C33)."),
           "WaybillTypeCode": V(kind, "The convention the document follows."),
           "ConsolidatedIndicator": V("false", "One consignment, not a consolidation."),
           "OtherInstruction": V("Deliver against signature of the consignee.", "What the carrier must do at "
                                                                               "delivery."),
           "IssueLocation": leg_location(leg, "from", "Where the carrier took over the goods and issued the note."),
           "DocumentDistribution": [
               {"ID": V("1", "The original for the consignor."),
                "DocumentTypeCode": V("Waybill", "The document distributed: this waybill."),
                "DistributionTypeCode": V("ORIGINALHANDED", "The consignor's original, handed over when the carrier "
                                                            "took over the goods, as the convention prescribes."),
                "Party": party_short(leg["from"])},
               {"ID": V("2", "The original for the consignee."),
                "DocumentTypeCode": V("Waybill", "The document distributed: this waybill."),
                "DistributionTypeCode": V("ORIGINALWITHGOODS", "One of the three originals travels with the goods to "
                                                               "the consignee, as the convention prescribes."),
                "DistributionType": Detail("the consignee's original", "the original the consignee signs on "
                                                                         "delivery."),
                "Party": party_short(leg["to"])},
               {"ID": V("3", "The electronic copy."),
                "DocumentTypeCode": V("Waybill", "The document distributed: this waybill."),
                "DistributionTypeCode": V("ELECTRONICCOPY", "The receiver of this message gets a copy, for its "
                                                            "records; the originals are on paper."),
                "DistributionType": V("Electronic copy", "In words."),
                "Party": party_short(doc["to"])}],
           "Signature": {"ID": V(f"{initials(carrier)}-SIG-{number}", "The carrier's signature on taking over the "
                                                                      "goods."),
                         "SignatoryParty": party_short(carrier)},
           "Shipment": {"ID": V(flow.numbers.get("shipment") or flow.number("shipment", doc["from"], "Shipment"),
                                "The shipment as the despatching party numbered it."),
                        "GrossWeightMeasure": qty(weight, "KGM", why_weight),
                        "Consignment": {"ID": V(flow.numbers.get("consignment") or
                                                flow.number("consignment", doc["from"], "Consignment"),
                                                "The consignment of the transport booking.")}}}
    if leg["mode"] == "air":        # an air waybill has one number, the airline's (mast/03#F9, air/04#F17)
        out.pop("CarrierAssignedID")
    if "tep" in flow.numbers:
        out["DocumentReference"] = {"ID": V(flow.numbers["tep"], "The transport plan under which the carriage is "
                                                                 "performed.")}
    return merge_extra(out, extra)


def merge_extra(out, extra):
    if extra:
        for k, v in extra.items():
            out[k] = {**out[k], **v} if isinstance(out.get(k), dict) and isinstance(v, dict) else v
    return out


def deep_merge(out, extra):
    """Merge `extra` into `out` at every level: nested blocks are completed, not replaced."""
    for k, v in (extra or {}).items():
        if isinstance(out.get(k), dict) and isinstance(v, dict) and not isinstance(v, V):
            deep_merge(out[k], v)
        else:
            out[k] = v
    return out


# ---------------------------------------------------------------- customs
def rate(a, b):
    """The world's reference exchange rate: units of b for one unit of a (world/countries.json)."""
    if a == b:
        return Decimal(1)
    r = WORLD["exchange_rates"]
    return Decimal(str(r[f"{a}/{b}"])) if f"{a}/{b}" in r else 1 / Decimal(str(r[f"{b}/{a}"]))


HS_SECTION = {"26": "V", "27": "V", "39": "VII", "44": "IX", "52": "XI", "62": "XI", "73": "XV", "94": "XX"}


ADJECTIVE = {"XU": "Urvanian", "XB": "Bayvarran", "XL": "Lisavan"}


def maker_of(iid):
    it = ITEM[iid]
    while it.get("resale_of"):
        it = ITEM[it["resale_of"]]
    return it


def origin_statement(flow, seller, buyer, iids):
    """The exporter's statement on origin for an invoice of goods from one Accord country to another, the proof of
    origin an import declaration refers to where no certificate of origin is issued (D18, O49), worded as the
    origin declarations of the EU's preferential arrangements."""
    if PARTY[seller]["c"] == PARTY[buyer]["c"]:
        return None
    if any(d["doc"] == "CertificateOfOrigin" for d in WORLD["documents"] if d["flow"] == flow.id):
        return None
    goods = [maker_of(i) for i in iids if ITEM[i].get("kind") == "goods"]
    if not goods or len({g["origin"] for g in goods}) != 1:
        return None
    crit = "/".join(sorted({g["origin_criterion"] for g in goods}))
    return (f"The exporter of the goods covered by this document declares that these goods are of "
            f"{ADJECTIVE[goods[0]['origin']]} preferential origin under the Trade Accord (criterion {crit}).")


def customs_item(iid):
    """The item as goods declared or carried: its classification also says the nature and the kind of cargo."""
    out = item(iid)
    cc = (out.get("CommodityClassification") or [None])[0]
    maker = ITEM[iid]
    while maker.get("resale_of"):
        maker = ITEM[maker["resale_of"]]
    hs = maker.get("hs")
    if cc and hs:
        cc["NatureCode"] = V(HS_SECTION[hs[:2]], "The section of the Harmonized System the goods fall in, the "
                                                 "highest level of the World Customs Organization's classification.")
        if hs[:4] != "2711":        # gas in a pipeline is no cargo: the HS code and the mode say what it is (C82)
            cc["CargoTypeCode"] = V("BULK" if ITEM[iid]["unit"] in ("TNE",) and hs[:2] == "26" else "GEN",
                                    "The kind of cargo: bulk, or general cargo in packages.")
    return out


def flow_packages(flow, iid=None):
    """The packages a flow's goods travel in, piece by piece, where the world lists them (world/documents.json,
    the flow's "packages"): the cotton's 27 bales (D12, O26). None where the flow lists none, or lists them for
    another item."""
    pk = next((f.get("packages") for f in WORLD["flows"] if f["id"] == flow.id), None)
    return pk if pk and (iid is None or pk["item"] == iid) else None


PACKAGING_NAMES = {"BL": "bale, compressed"}     # UN/ECE Recommendation 21, as the world's list holds them


def package_weights(pk):
    """Each listed package as (id, net, gross) in kg: the net weight of the goods in it and, with the package's
    standard tare, its gross weight."""
    tare = Decimal(str(pk["tare_kg"]))
    return [(p["id"], Decimal(str(p["net_kg"])), Decimal(str(p["net_kg"])) + tare) for p in pk["pieces"]]


def kg(x):
    """A weight in kg as a document writes it: no trailing zeros."""
    return f"{Decimal(str(x)).normalize():f}"


def containing_package(flow, iid):
    """The kind of package a goods item travels in, where the flow lists its packages: the packaging type only; the
    number of packages is the consignment's package count, and one entry for all of them identifies none (D12)."""
    pk = flow_packages(flow, iid)
    if not pk:
        return {}
    return {"ContainingPackage": {"PackagingTypeCode": V(pk["type"], f"UN/ECE Recommendation 21 code {pk['type']}: "
                                                         f"{PACKAGING_NAMES[pk['type']]}. The goods travel in "
                                                         f"{len(pk['pieces'])} of them, the consignment's package "
                                                         "count.")}}


def package_count(flow, why):
    """The number of packages of a flow's goods, for a consignment's TotalPackagesQuantity (D12)."""
    pk = flow_packages(flow)
    return qty(len(pk["pieces"]), "EA", why) if pk else None


def by_item(deal):
    """The lines of a deal summed by item: a goods item of a customs or transport document holds all of one kind of
    goods, though an order may give them on several lines (such as the sea order's benches for the port and for
    the buyer's stock, O172). Each merged entry keeps the lines it sums under "lines"."""
    out, seen = [], {}
    for d in deal:
        if d["item"] not in seen:
            seen[d["item"]] = {**d, "lines": [d]}
            out.append(seen[d["item"]])
            continue
        m = seen[d["item"]]
        m["lines"].append(d)
        for k in ("ordered", "delivered", "received"):
            if k in d or k in m:
                m[k] = sum(Decimal(str(x.get(k, x.get("ordered", 0)))) for x in m["lines"])
                m[k] = int(m[k]) if m[k] == int(m[k]) else m[k]
        for k in ("why", "line", "line_extra", "orderline_extra", "received_why"):
            m.pop(k, None)
    return out


def goods_items(flow, currency, value_why, deal=None):
    """GoodsItem per item of the deal (by_item): customs value (converted to `currency` at the reference rate if
    needed), gross weight, quantity and the item with its customs tariff code and origin."""
    deal = by_item(deal or flow.deal)
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = []
    for i, d in enumerate(deal, 1):
        it = ITEM[d["item"]]
        q = Decimal(str(d[which]))
        pr = price_of(d["item"], flow.buyer)        # the transaction value: the price the flow's buyer pays
        value = q * Decimal(str(pr["amount"])) * rate(pr["currency"], currency)
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What the goods are, in words."),
                    "DeclaredCustomsValueAmount": amount(value, currency, value_why),
                    "GrossWeightMeasure": qty(line_gross(flow, d, which), "KGM", line_gross_why(flow, d)),
                    "Quantity": qty(q, it["unit"], "The quantity declared."),
                    **goods_packages(flow, d),
                    "Item": customs_item(d["item"])})
    return out


def transport_goods(flow, deal=None):
    """GoodsItem per line of the deal for a transport document (worklist C21): what is carried, how much, its gross
    weight and its commodity code, without the customs value, which a carrier does not need; one per item
    (by_item)."""
    deal = by_item(deal or flow.deal)
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = []
    for i, d in enumerate(deal, 1):
        it = ITEM[d["item"]]
        if it.get("kind") == "service":
            continue
        q = Decimal(str(d[which]))
        hs = maker(d["item"]).get("hs")
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What is carried, in words."),
                    "GrossWeightMeasure": qty(line_gross(flow, d, which), "KGM", line_gross_why(flow, d)),
                    "Quantity": qty(q, it["unit"], "How much is carried."),
                    **containing_package(flow, d["item"]),
                    **({"Item": {"Name": V(it["name"], "The goods."),
                                 "CommodityClassification": {"CommodityCode": V(hs, "Its Harmonized System "
                                                                                    "subheading, which carriers use "
                                                                                    "to describe the cargo.")}}}
                       if hs else {})})
    return out


def with_transport_goods(flow, shipment=None, consignment=None, deal=None):
    """A transport document says what it carries (worklist C21): a shipment gets the goods items of the deal; a
    consignment without a shipment (a transport plan or request) a summary of them. A scenario's own goods stay."""
    goods = transport_goods(flow, deal)
    if not goods:
        return
    if isinstance(shipment, dict) and "GoodsItem" not in shipment:
        shipment["GoodsItem"] = goods
    elif shipment is None and isinstance(consignment, dict) and "SummaryDescription" not in consignment:
        unit = {"TNE": " t of", "KGM": " kg of", "MTQ": " m³ of", "MWH": " MWh of"}
        consignment["SummaryDescription"] = V("; ".join(
            f"{g['Quantity'].value}{unit.get(g['Quantity'].attrs.get('unitCode'), ' ×')} {g['Description'].value}"
            for g in goods), "What is to be carried, in a few words (worklist C21).")
        consignment.setdefault("TotalGoodsItemQuantity", qty(len(goods), "EA", "The number of goods items."))


def unit_count(flow, deal=None):
    """A shipment's count of pallets, where its goods travel on pallets (D20, worklist C12)."""
    units = pallets(flow, deal or flow.deal)
    return {"TotalTransportHandlingUnitQuantity": qty(len(units), "EA", "The pallets the goods travel on.")} \
        if units else {}


def export_declaration(flow, n, doc, day, why, value_why, deal=None):
    cur = currency_of(doc["from"])
    deal = deal or flow.deal
    return {"ID": V(flow.number("export", doc["from"], "ExportCustomsDeclaration"), "The exporter's reference."),
            "IssueDate": V(flow.date(day), why),
            "CustomsDeclaration": {
                "ID": V(flow.number("export-declaration", doc["from"], "CustomsDeclaration"),
                        "The declaration as lodged with the customs of the exporting country."),
                "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The shipment declared."),
                             "GrossWeightMeasure": qty(gross_weight(flow, "delivered" if any("delivered" in d for d in
                                                                                         deal) else "ordered", deal),
                                                       "KGM", "The gross weight leaving the country."),
                             "GoodsItem": goods_items(flow, cur, value_why, deal),
                             **unit_count(flow, deal),
                             "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment carried."),
                                             **({"TotalPackagesQuantity": qty(parcel_count(flow, deal), "EA",
                                                                              "The parcels declared, on the pallets "
                                                                              "counted above (D20).")}
                                                if pallets(flow, deal) else {})}}}}


def import_declaration(flow, n, doc, day, why, value_why, refs=None, deal=None):
    cur = currency_of(doc["from"])
    deal = deal or flow.deal
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = {"ID": V(flow.number("import", doc["from"], "ImportCustomsDeclaration"), "The importer's declaration number."),
           "IssueDate": V(flow.date(day), why),
           "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The shipment declared."),
                        "GrossWeightMeasure": qty(gross_weight(flow, which, deal), "KGM", "The gross weight arriving."),
                        "GoodsItem": goods_items(flow, cur, value_why, deal),
                        **unit_count(flow, deal)}}
    if refs:
        out["AdditionalDocumentReference"] = refs
    return out


def transportation_status(flow, n, doc, day, event_why, description, location, extra=None, event_type=None):
    if not event_type:
        raise SystemExit(f"{flow.id} {n}: a status report says what happened as a code (worklist C18)")
    out = {"ID": V(flow.number(f"status-{n}", doc["from"], "TransportationStatus"), "The sender's status report number."),
           "IssueDate": V(flow.date(day), event_why),
           "TransportEvent": {"OccurrenceDate": V(flow.date(day), "The day the event took place."),
                              "TransportEventTypeCode": V(event_type, "The kind of event, as the carriers of the "
                                                                      "world code them."),
                              "Description": V(description, "What happened, in words."),
                              "Location": {"Name": V(location, "Where it happened.")}},
           "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                   "The consignment the report is about.")}}
    return merge_extra(out, extra)


# ---------------------------------------------------------------- credit, retail and collaboration
def credit_note(flow, n, doc, day, why, rows_spec, refs, currency=None):
    seller, buyer = doc["from"], doc["to"]
    cur = currency or currency_of(seller)
    rows, gross = line_allowances(spec_rows(rows_spec, seller, buyer, cur), cur)
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    out = {"ID": V(flow.number(f"credit-{n}", seller, "CreditNote"), "The seller's credit note number."),
            "IssueDate": V(flow.date(day), why),
            "CreditNoteTypeCode": V("381", "UN/EDIFACT 1001 code 381: credit note."),
            "DocumentCurrencyCode": currency_line(cur, "the currency of the invoice credited"),
            **cost_centre(buyer, iid=rows[0][0]["item"], why="The buyer's cost centre, as on the invoice credited."),
            "LineCountNumeric": V(str(len(rows)), "The number of lines."),
            "DefaultLanguageCode": V(WORLD["countries"][PARTY[seller]["c"]]["languages"][-1], "The language of the "
                                                                                              "texts."),
            "PaymentTerms": {"Note": V("Settled against the next payment to the seller, unless refunded.",
                                       "How a credit note is settled in the world.")},
            **refs,
            "TaxTotal": total,
            "LegalMonetaryTotal": monetary_total(base, tax, cur),
            "CreditNoteLine": [{"ID": V(str(i), "The line number."),
                                "CreditedQuantity": qty(q, ITEM[d["item"]]["unit"], d["why"]),
                                "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
                                "Item": item(d["item"], tax_category(rule, supply_kind(d["item"]))),
                                "Price": line_price(d, cur, buyer)} for i, (d, q, amt, rule) in enumerate(rows, 1)]}
    line_features(rows, out["CreditNoteLine"], cur, gross)
    return out


def line_allowances(rows, cur):
    """A line allowance lowers the line amount before the totals; returns the rows and the gross line amounts."""
    gross, out = {}, list(rows)
    for k, (d, q, amt, rule) in enumerate(out):
        la = d.get("line_allowance")
        if la:
            gross[k] = amt
            out[k] = (d, q, amt - money(amt * Decimal(la["percent"]) / 100, cur), rule)
    return out, gross


def line_features(rows, lines, cur, gross):
    """What a scenario asks of a line: its allowance, its own tax total, extra elements."""
    for k, ((d, q, amt, rule), line) in enumerate(zip(rows, lines)):
        la = d.get("line_allowance")
        if la:
            line["LineExtensionAmount"] = amount(amt, cur, f"{q} × the price = {gross[k]}, less the {la['percent']} % "
                                                           f"{la['reason'].lower()}.")
            line["AllowanceCharge"] = {"ChargeIndicator": V("false", "An allowance on the line."),
                                       "AllowanceChargeReasonCode": V(la["code"], la["code_why"],
                                                                      listID="UN/EDIFACT EDED 5189"),
                                       "AllowanceChargeReason": V(la["reason"], la["why"]),
                                       "MultiplierFactorNumeric": V(str(Decimal(la["percent"]) / 100), "The rate."),
                                       "Amount": amount(gross[k] - amt, cur, "The deduction on the line."),
                                       "BaseAmount": amount(gross[k], cur, "The line at the full price.")}
            line["ItemPriceExtension"] = {"Amount": amount(gross[k], cur, "Price times quantity, before the "
                                                                          "allowance.")}
        if d.get("line_tax"):
            pct = Decimal(str(rule[1]))
            tax_l = money(amt * pct / 100, cur)
            line["TaxInclusiveLineExtensionAmount"] = amount(amt + tax_l, cur, "The line with its tax.")
            line["TaxTotal"] = {"TaxAmount": amount(tax_l, cur, f"{pct} % of the line amount, for the buyer's "
                                                                "booking per line.")}
        deep_merge(line, d.get("line_extra"))


def spec_rows(rows_spec, seller, buyer, cur):
    """Rows from an explicit list: item, quantity and, for a price difference, an own unit price."""
    out = []
    for d in rows_spec:
        p = Decimal(str(d.get("unit_price", price_of(d["item"], buyer)["amount"])))
        out.append((d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * p, cur), tax_rule(seller, buyer, d["item"])))
    return out


def line_price(d, cur, buyer=None):
    if "unit_price" in d:
        return {"PriceAmount": price(d["unit_price"], cur, d["unit_price_why"]),
                "BaseQuantity": qty(1, ITEM[d["item"]]["unit"], "The price is per one unit.")}
    return price_block(d["item"], buyer=buyer)


def catalogue(flow, n, doc, day, why, items, validity_days, alternative=None):
    flow.numbers["catalogue-from"] = doc["from"]
    return {"ID": V(flow.number("catalogue", doc["from"], "Catalogue"), "The provider's catalogue number."),
            "Name": V(f"{PARTY[doc['from']]['identity']['name']} catalogue", "The catalogue's title."),
            "IssueDate": V(flow.date(day), why),
            "ValidityPeriod": {"StartDate": V(flow.date(day), "The prices apply from the issue date."),
                               "EndDate": V(flow.date(day + validity_days), "Until the next catalogue.")},
            "CatalogueLine": [{"ID": V(str(i), "The line number."),
                               "Item": item(iid, catalogue=(flow.numbers["catalogue"], i)),
                               "RequiredItemLocationQuantity": catalogue_terms(flow, doc, day, validity_days, iid,
                                                                               alternative)}
                              for i, iid in enumerate(items, 1)]}


def price_type(code, tax_included):
    """A code of the world's price type list (lists.json PriceType), checked against what the price it names is:
    with tax or before tax (O28)."""
    lst = codelists.load()["lists"]["PriceType"]
    if lst["tax_included"][code] != tax_included:
        raise SystemExit(f"price type {code}: the list says its price {'includes' if lst['tax_included'][code] else 'excludes'}"
                         f" tax, but the document's price {'includes' if tax_included else 'excludes'} it (O28)")
    return code


def catalogue_terms(flow, doc, day, validity_days, iid, alternative=None):
    """The terms a catalogue line is offered on: lead time, minimum quantity, where it is sold, the price and
    the price list it belongs to. The price is the one for the flow's buyer where the catalogue is sent to it (a
    price agreed for the buyer, such as Lumeway's CIF price for the island, O30), else the seller's own."""
    it = ITEM[iid]
    seller = PARTY[doc["from"]]
    buyer = flow.buyer if flow.buyer == doc["to"] else None
    p = price_block(iid, buyer=buyer)
    p["ValidityPeriod"] = {"StartDate": V(flow.date(day), "The price applies from the catalogue's issue date."),
                           "EndDate": V(flow.date(day + validity_days), "And until the catalogue ends.")}
    p["PriceList"] = {"ID": V(f"{initials(doc['from'])}-PL-{flow.date(day)[:4]}",
                              "The seller's price list this price is taken from."),
                      "StatusCode": V("ORIGINAL", "The first issue of the price list: UBL names original, copy, "
                                                  "revision or cancellation here, not whether the list is in force "
                                                  "(worklist C25).")}
    out = {"LeadTimeMeasure": V(it.get("lead_days", 5), "The days between order and despatch.", unitCode="DAY"),
           "MinimumQuantity": qty(it.get("min_order", 1), it["unit"], "The smallest quantity the seller accepts on an "
                                                                       "order."),
           "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V(PARTY[doc["to"]]["c"], "The market the "
                                                                              "price is offered for: the buyer's "
                                                                              "country, whose sales the tax "
                                                                              "category below treats (worklist C25).")}},
           "Price": p}
    contract = flow.id == "tender"
    kind = price_type("CON" if contract else "TRD", tax_included=False)     # a catalogue price is before tax
    p["PriceTypeCode"] = V(kind, "The kind of price, which buyer and seller both understand: "
                           + ("the price agreed in the framework contract." if contract else "a trade price."))
    p["PriceType"] = V("Contract price" if contract else "Trade price", "The kind of price in words.")
    if alternative:
        p["AlternativeCurrencyPrice"] = {
            "PriceAmount": price(unit_price(iid, alternative, buyer), alternative, "The same price in the buyer's currency, "
                                 "at the world's reference rate on the catalogue's issue day; for information only."),
            "BaseQuantity": qty(1, it["unit"], "Per one unit.")}
    if it.get("max_order"):
        out["MaximumQuantity"] = qty(it["max_order"], it["unit"], "The most one order can take from stock: two "
                                                                   "full 40-foot containers.")
    if it.get("conditions"):
        out["TradingRestrictions"] = V("Not sold to consumers.", "The bench is sold through retailers.")
        out["DeliveryUnit"] = {"BatchQuantity": qty(4, it["unit"], "The benches are delivered per pallet of four."),
                               "ConsumerUnitQuantity": qty(1, it["unit"], "One bench is one consumer unit.")}
        out["Package"] = {"ID": V("PAL-4", "The pallet the price is for."),
                          "Quantity": qty(4, it["unit"], "Four benches to a pallet."),
                          "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet.")}
        full_allowance = {"ChargeIndicator": V("false", "A discount."),
                                  "AllowanceChargeReasonCode": V("95", "The reason for the allowance as a code of UN/EDIFACT "
                                                                       "5189, as EN 16931 uses it: a discount for the "
                                                                       "full container.",
                                                                 listID="UN/EDIFACT EDED 5189"),
                                  "AllowanceChargeReason": V("Full container", "The discount for a full container."),
                                  "MultiplierFactorNumeric": V("0.03", "Three percent off."),
                                  "Amount": amount(Decimal(str(it["price"]["amount"])) * Decimal("0.03"),
                                                   it["price"]["currency"], "The discount per bench."),
                                  "BaseAmount": amount(it["price"]["amount"], it["price"]["currency"],
                                                       "The catalogue price the discount is taken from.")}
        out["ApplicableDeliveryPeriod"] = {"StartDate": V(flow.date(day + 7), "The first deliveries from the "
                                                                              "season's stock."),
                                           "EndDate": V(flow.date(day + validity_days), "The last.")}
    out["ApplicableTaxCategory"] = tax_category(tax_rule(doc["from"], doc["to"], iid))
    if it.get("conditions"):                  # the full-container discount applies only from a full container
        full = {k: v for k, v in out.items() if k not in ("MinimumQuantity", "MaximumQuantity")}
        full["MinimumQuantity"] = qty(FULL_CONTAINER, it["unit"], "A full 40-foot container: 36 pallets of four "
                                                                  "benches in two layers (D20); a smaller order "
                                                                  "does not qualify (worklist C25).")
        full["AllowanceCharge"] = full_allowance
        return [out, full]
    return out


FULL_CONTAINER = 144          # benches in a full 40-foot container: 18 floor positions, two layers, four a pallet


def purchase_receipt(flow, n, doc, day, why, rows_spec, cash, promotion=None):
    seller, buyer = doc["from"], doc["to"]
    cur = currency_of(seller)
    def net(iid):
        shelf = Decimal(str(ITEM[iid]["price"]["amount"]))
        return money(shelf * (1 - Decimal(str(promotion["percent"])) / 100), cur) if promotion else shelf

    rows = [(d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * net(d["item"]), cur),
             tax_rule(seller, buyer, d["item"])) for d in rows_spec]

    def line_price(iid, rule):
        p = price_block(iid)
        p["TaxInclusivePriceAmount"] = price(money(net(iid) * (1 + Decimal(str(rule[1])) / 100), cur), cur,
                                             f"The price the customer pays, with the {rule[1]} % sales tax.")
        if not promotion:
            return p
        shelf = Decimal(str(ITEM[iid]["price"]["amount"]))
        p["PriceAmount"] = price(net(iid), cur, f"The shelf price of {shelf} less the promotion discount.")
        p["PriceChangeReason"] = V(promotion["name"], "Why the price differs from the shelf price.")
        p["AllowanceCharge"] = {
            "ChargeIndicator": V("false", "A discount, not a charge."),
            "AllowanceChargeReasonCode": V("95", "The reason for the allowance as a code of UN/EDIFACT 5189, "
                                                 "as EN 16931 uses it: the promotion is a discount on the price.",
                                           listID="UN/EDIFACT EDED 5189"),
            "AllowanceChargeReason": V(promotion["name"], "The promotion, as the till prints it."),
            "MultiplierFactorNumeric": V(str(Decimal(str(promotion["percent"])) / 100), "The discount rate."),
            "Amount": amount(shelf - net(iid), cur, "The discount per unit, deducted from the shelf price."),
            "BaseAmount": amount(shelf, cur, "The shelf price the discount is taken from.")}
        p["ValidityPeriod"] = {"StartDate": V(flow.date(promotion["from"]), "The first day of the promotion."),
                               "EndDate": V(flow.date(promotion["to"]), "The last day of the promotion.")}
        return p

    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    return {"ID": V(flow.number(f"receipt-{n}", seller, "PurchaseReceipt"), "The till's receipt number."),
            "IssueDate": V(flow.date(day), why),
            "DocumentCurrencyCode": currency_line(cur, "the currency of the shop"),
            "PaymentMeans": {"PaymentMeansCode": V("10", "UN/EDIFACT 4461 code 10: in cash." if cash else
                                                   "UN/EDIFACT 4461 code 10.", listID="UN/EDIFACT EDED 4461")},
            "TaxTotal": total,
            "LegalMonetaryTotal": monetary_total(base, tax, cur),
            "PurchaseReceiptLine": [{"ID": V(str(i), "The line number."),
                                     "Quantity": qty(q, ITEM[d["item"]]["unit"], d["why"]),
                                     "LineExtensionAmount": amount(amt, cur, "Quantity times the price paid, before "
                                                                             "the sales tax."),
                                     "Item": item(d["item"], tax_category(rule, supply_kind(d["item"]))),
                                     "Price": line_price(d["item"], rule)} for i, (d, q, amt, rule) in enumerate(rows, 1)]}



# ---------------------------------------------------------------- self-billing (the customer writes the document)
def self_billed(flow, n, doc, day, why, rows_spec, refs, credit=False):
    """A self-billed invoice or credit note: written by the customer (doc['from']) on behalf of the supplier."""
    customer, supplier = doc["from"], doc["to"]
    cur = currency_of(supplier)
    rows = spec_rows(rows_spec, supplier, customer, cur)
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    line, qname = ("CreditNoteLine", "CreditedQuantity") if credit else ("InvoiceLine", "InvoicedQuantity")
    out = {"ID": V(flow.number(f"self-billed-{n}", customer, "SelfBilledCreditNote" if credit else "SelfBilledInvoice"),
                   "The number the customer gives the self-billed document, under the self-billing agreement."),
           "IssueDate": V(flow.date(day), why),
           "DocumentCurrencyCode": currency_line(cur, "the supplier's currency"),
           **cost_centre(customer, "The customer's own cost centre: it books what it billed itself."),
           "LineCountNumeric": V(str(len(rows)), "The number of lines."),
           "DefaultLanguageCode": V(WORLD["countries"][PARTY[supplier]["c"]]["languages"][-1], "The language of the "
                                                                                               "texts."),
           **refs,
           "TaxTotal": total,
           "LegalMonetaryTotal": monetary_total(base, tax, cur),
           line: [{"ID": V(str(i), "The line number."),
                   qname: qty(q, ITEM[d["item"]]["unit"], d["why"]),
                   "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
                   "Item": item(d["item"], tax_category(rule, supply_kind(d["item"]))),
                   "Price": line_price(d, cur, customer)} for i, (d, q, amt, rule) in enumerate(rows, 1)]}
    if not credit:
        out["InvoiceTypeCode"] = V("389", "UN/EDIFACT 1001 code 389, \"An invoice the invoicee is producing instead "
                                          "of the seller\": exactly what this document is. It repeats what the root "
                                          "SelfBilledInvoice already says, as no narrower subtype applies; 380 "
                                          "would be wrong, since a commercial invoice is the seller's document "
                                          "\"claiming payment\", and the customer claims nothing here, it settles "
                                          "what it owes.")
        number = flow.numbers[f"self-billed-{n}"]
        t = terms_of(flow, supplier, day)
        flow.numbers[f"self-billed-{n}-terms"] = t
        out["DueDate"] = V(flow.date(t["due"]), "The supplier's usual term, which the customer applies to itself.")
        out["PaymentMeans"] = payment_means(flow, supplier, customer, supplier, day, t["due"] - day, number,
                                            "The supplier's account, where the customer pays what it billed itself.")
        out["PaymentTerms"] = payment_terms(flow, supplier, customer, t, base + tax, cur, number)
    else:
        out["CreditNoteTypeCode"] = V("261", "UN/EDIFACT 1001 code 261, \"A document which indicates that the "
                                             "customer is claiming credit in a self billing environment\": the "
                                             "customer corrects its own self-billed invoice. It repeats what the "
                                             "root SelfBilledCreditNote already says, but its definition is exact; "
                                             "381, the supplier's credit note, would not be.")
    flow.numbers[f"self-billed-{n}-amount"] = base + tax
    flow.numbers[f"self-billed-{n}-date"] = flow.date(day)
    return out


# ---------------------------------------------------------------- containers
def container_number(owner, serial):
    """An ISO 6346 container number: owner code, U (freight container), six digits and the check digit. The owner
    codes are ones the BIC register does not hold (world/codelists/sources/bic)."""
    code = f"{owner}U{serial:06d}"
    return f"{code}{world_ids.iso6346_digit(code)}"


# ---------------------------------------------------------------- transport: places, means, events, units
PLACES = {"XUFER": ("Ferrano", "XU"), "XUSRV": ("Serravona", "XU"), "XUFNT": ("Fucinalta mine siding", "XU"),
          "XBMRW": ("Marrowdale", "XB"),
          "XBLMP": ("Port of Lumeport", "XB"), "XBLMA": ("Lumeport airport", "XB"), "XLSEL": ("Port of Selanu", "XL"),
          "XLSLA": ("Selanu airport", "XL")}


def place(code, why, name=None):
    """A cac:Location for a town, port or airport of the map, with a UN/LOCODE-form code of the world."""
    n, c = PLACES[code]
    return {"ID": V(code, "The place's code in the form of a UN/LOCODE, with the world's country code.",
                    schemeID="UN/LOCODE"),
            "Name": V(name or n, why),
            "Address": {"Country": {"IdentificationCode": V(c, "The country the place is in.")}}}


def maker(iid):
    """The item as its maker sells it: a resold item's physical facts are the maker's."""
    it = ITEM[iid]
    while it.get("resale_of"):
        it = ITEM[it["resale_of"]]
    return it


def fleet(pid, fid):
    return next(x for x in PARTY[pid]["fleet"] if x["id"] == fid)


def means(pid, fid, journey=None, why_journey=None, direction=None, ore=False):
    """A cac:TransportMeans from the carrier's fleet (world/parties.json): its registration and the vehicle,
    train, vessel or aircraft."""
    f, c = fleet(pid, fid), PARTY[pid]["c"]
    name = PARTY[pid]["identity"]["name"]
    src = f"the fleet of {name} (world/parties.json)"
    out = {}
    if journey:
        out["JourneyID"] = V(journey, why_journey or "The journey: the carrier's number for this trip.")
    out["RegistrationNationalityID"] = V(c, "The country the means of transport is registered in.")
    out["RegistrationNationality"] = V(WORLD["countries"][c]["name"], "The same, in words.")
    if direction:
        out["DirectionCode"] = V(direction, "The direction of the journey, as carriers name their services.")
    kind = f["name"] if f["name"][:2].isupper() else f["name"][0].lower() + f["name"][1:]
    out["TransportMeansTypeCode"] = V(f["type"], f"The kind of means of transport: {kind}; {src}."
                                      + (f" {f['description']}" if f.get("description") else ""))
    if f["kind"] == "road":
        out["RoadTransport"] = {"LicensePlateID": V(f["plate"], f"The registration plate of the truck; {src}.")}
        if f.get("trailer"):
            out["RoadTransport"]["TrailerLicensePlateID"] = V(f["trailer"], "The trailer's own plate.")
        if f.get("loading_m"):
            out["MeasurementDimension"] = {"AttributeID": V("LOADINGLENGTH", "The length of the loading floor."),
                                           "Measure": V(f["loading_m"], f"Room for {f['pallets']} pallets.",
                                                        unitCode="MTR")}
    if f["kind"] == "rail":
        out["RailTransport"] = {"TrainID": V(f["ore_train"] if ore else f["train"], f"The train number; {src}.")}
    if f["kind"] in ("inland", "sea"):
        m = {"VesselID": V(f["vessel_id"], "The vessel's number in its country's register of ships; a number of the "
                                           "world, not an IMO number.", schemeID="urn:ubl-examples:world:vessel"),
             "VesselName": V(f["name"], f"The vessel's name; {src}."),
             "RadioCallSignID": V(f["call_sign"], f"The radio call sign, in {WORLD['countries'][c]['name']}'s call "
                                                  f"sign series {f['call_sign'][:2]}: no ITU series starts with Q, so "
                                                  "the sign belongs to no real station (world/countries.json)."),
             "MMSIRegistrationID": V(f["mmsi"], "The Maritime Mobile Service Identity, nine digits: the maritime "
                                                f"identification digits {f['mmsi'][:3]} of "
                                                f"{WORLD['countries'][c]['name']}, which the ITU has not allocated to "
                                                "any real country, and the ship's six digits."),
             "GrossTonnageMeasure": V(f["gross_t"], "The gross tonnage of the vessel, a number without a unit.", unitCode="C62"),
             "NetTonnageMeasure": V(f["net_t"], "Its net tonnage, also without a unit.", unitCode="C62"),
             "ShipConfigurationCode": V(f["config"], "The kind of vessel"
                                        + (f", for about {f['capacity_teu']:,} TEU." if f.get("capacity_teu") else ".")),
             "RegistryPortLocation": {"Name": V(f["registry"], "The port the vessel is registered in.")}}
        if f.get("ballast"):
            m["SegregatedBallastMeasure"] = V(f["ballast"], "The capacity of the tanks for ballast water only.",
                                              unitCode="TNE")
            m["ShipsRequirements"] = V("Shore power at the container quay.", "What the ship needs in port.")
            m["RegistryCertificateDocumentReference"] = {"ID": V(f"REG-{f['vessel_id']}", "The ship's certificate "
                                                                 "of registry.")}
        out["MaritimeTransport"] = m
    if f["kind"] == "air":
        out["AirTransport"] = {"AircraftID": V(f["aircraft"], "The aircraft's registration: the nationality mark "
                                                              f"{f['aircraft'][:2]} of {WORLD['countries'][c]['name']}, "
                                                              "a mark no real state uses, and three letters; "
                                                              f"{src}.")}
    if f.get("owner"):
        out["OwnerParty"] = party_short(f["owner"])
    return out


def party_short(pid):
    from build_examples import party
    return party(pid, short=True)


def person(first, family, why, pid=None, role=None, job=None):
    out = {"FirstName": V(first, why), "FamilyName": V(family, "The family name.")}
    if pid:
        out["ID"] = V(pid, "The number of the driving licence.")
    if job:
        out["JobTitle"] = V(job, "The person's position.")
    if role:
        out["RoleCode"] = V(role, "The person's role on board.")
    return out


def event(flow, day, time, why, location=None, type_code=None, ident=None, description=None, done=None, **more):
    """A transport event: when and where something happens to the goods."""
    out = {}
    if ident:
        out["IdentificationID"] = V(ident, "The reporting party's number for this event.")
    out["OccurrenceDate"] = V(flow.date(day), why)
    if time:
        out["OccurrenceTime"] = V(time, "The local time.")
    if type_code:
        out["TransportEventTypeCode"] = V(type_code, "The kind of event, as the carriers of the world code them.")
    if description:
        out["Description"] = V(description, "What happened, in words.")
    if done is not None:
        out["CompletionIndicator"] = V("true" if done else "false", "Whether the event has taken place (true) or is "
                                                                    "still to come (false).")
    if location:
        out["Location"] = location
    out.update(more)
    return out


# the flows whose goods travel on pallets (D20, O61): the bench in three parcels, four benches to a pallet, and the
# spare frames in their cartons on a pallet of their own; the carnet's two samples and the air flow's eight frames
# travel as loose parcels (the air frames on a skid, D39)
PALLET_FLOWS = {"road", "rail", "sea", "retail", "tender", "wood"}


def pallets(flow, deal):
    """The transport handling units of a deal: the benches on pallets of four, the spare frames in their cartons on a
    pallet of their own (world/items.json, the item's pallet; D20). None for a flow that ships loose parcels."""
    units = []
    if flow.id not in PALLET_FLOWS:
        return units
    k = 0
    for d in deal:
        it = maker(d["item"])
        if not it.get("pallet"):
            continue
        q = int(Decimal(str(d["ordered"])))
        per = it["package"]["per_package"] if it["package"]["type"] == "PX" else it["pallet"]["per"]
        for start in range(0, q, per):
            k += 1
            units.append((k, it, min(per, q - start)))
    return units


def pallet_tare(flow, deal=None, iid=None):
    """The pallets' own weight in a deal (of one item's pallets, if given): the pallet, slip sheet, top cap and
    stretch film, which consignment and goods weights include (D20)."""
    return sum((Decimal(str(it["pallet"]["tare_kg"])) for _, it, _ in pallets(flow, deal or flow.deal)
                if iid is None or it is maker(iid)), Decimal(0))


def line_gross(flow, d, which):
    """The gross weight of a line of a deal: the goods in their parcels, and the pallets they travel on."""
    q = Decimal(str(d[which]))
    return q * Decimal(str(maker(d["item"]).get("gross_kg", 0))) + pallet_tare(flow, [d])


def line_gross_why(flow, d):
    if pallets(flow, [d]):
        return "The gross weight of the goods of this item, in their parcels and with the pallets they travel on."
    if maker(d["item"]).get("parcels") or maker(d["item"]).get("carton"):
        return "The gross weight of the goods of this item, in their parcels."
    if maker(d["item"]).get("package"):
        return "The gross weight of the goods of this item, with their packaging."
    return "The gross weight of the goods of this item."


def parcels(it, n):
    """The number of parcels n units of an item travel in: a bench is three parcels, a spare frame one carton."""
    return n * len(it["parcels"]) if it.get("parcels") else n


def parcel_count(flow, deal=None):
    which = "delivered" if any("delivered" in d for d in (deal or flow.deal)) else "ordered"
    return sum(parcels(maker(d["item"]), int(Decimal(str(d[which])))) for d in (deal or flow.deal))


def volume_m3(mm):
    return Decimal(mm[0]) * Decimal(mm[1]) * Decimal(mm[2]) / Decimal(10 ** 9)


def parcels_volume(flow, deal=None):
    """The volume of a deal's goods in their parcels, in m³: what the goods themselves take up."""
    out = Decimal(0)
    for d in deal or flow.deal:
        it = maker(d["item"])
        q = int(Decimal(str(d["ordered"])))
        boxes = [p["mm"] for p in it["parcels"]] if it.get("parcels") else [it["carton"]["mm"]]
        out += q * sum(volume_m3(b) for b in boxes)
    return out.quantize(Decimal("0.1"))


def goods_volume(flow, deal=None):
    """The volume of a deal's goods themselves, without packaging, in m³: the envelopes of the bench's parts (two
    side frames and five slats; the bolt set's is negligible) or of the spare frame (world/items.json)."""
    out = Decimal(0)
    for d in deal or flow.deal:
        it = maker(d["item"])
        q = int(Decimal(str(d["ordered"])))
        if it.get("parts"):
            out += q * sum(p["n"] * volume_m3(p["mm"]) for p in it["parts"] if p.get("mm"))
        elif it.get("envelope_mm"):
            out += q * volume_m3(it["envelope_mm"])
    return out.quantize(Decimal("0.1"))


def pallets_volume(flow, deal=None):
    """The volume of a deal's loaded pallets, in m³."""
    return sum((volume_m3(it["pallet"]["mm"]) for _, it, _ in pallets(flow, deal or flow.deal)),
               Decimal(0)).quantize(Decimal("0.1"))


def pallet_load(it, n_):
    """What one pallet carries, in words, and its packages: the parcels of n_ benches, or n_ frame cartons."""
    if it.get("parcels"):
        kinds = ", ".join(f"{n_} × parcel {p['no']} ({p['name'].lower()})" for p in it["parcels"])
        return n_ * len(it["parcels"]), f"{n_} benches in three parcels each: {kinds}"
    return n_, f"{n_} spare side frames, one to a frame carton"


def unit_weight(it, n_):
    """The gross weight of one loaded pallet: its goods and the pallet's own weight."""
    return n_ * Decimal(str(it["gross_kg"])) + Decimal(str(it["pallet"]["tare_kg"]))


def parcel_package(p, k=None):
    """A parcel kind on a pallet as cac:Package: what it is and holds, its size and weight (D20, O61). A bench
    parcel holds part of a bench, not an item, so it states no quantity of items."""
    two = p["lift"] == 2
    return {"PackageLevelCode": V("1", "UN/EDIFACT 7075 code 1: the inner level, below the pallet."),
            "PackagingTypeCode": V(p["type"], "UN/ECE Recommendation 21 code " + p["type"] + ": "
                                   + ("carton." if p["type"] == "CT" else "bundle.")),
            "PackagingType": V(f"{p['name']}, parcel {p['no']} of 3 of each bench: {p['contents']}",
                               "The parcel in words, as its label marks it; one of these per bench on the pallet."),
            "PackingMaterial": V(p["material"], "What the packaging is made of."),
            "ReturnableMaterialIndicator": V("false", "The parcel's packaging stays with the goods."),
            "MeasurementDimension": [
                {"AttributeID": V("LENGTH", "The parcel's size."), "Measure": V(str(p["mm"][0]), "Its length.",
                                                                                unitCode="MMT")},
                {"AttributeID": V("WIDTH", "The parcel's size."), "Measure": V(str(p["mm"][1]), "Its width.",
                                                                               unitCode="MMT")},
                {"AttributeID": V("HEIGHT", "The parcel's size."), "Measure": V(str(p["mm"][2]), "Its height.",
                                                                                unitCode="MMT")},
                {"AttributeID": V("GROSSWEIGHT", "The parcel's weight."),
                 "Measure": V(kg(p["gross_kg"]), ("Within the 25 kg one person may lift (ISO 11228-1, the world's "
                              "handling rule, D20)." if not two else "Within the limit, but 1.81 m long: two "
                              "people carry it (ISO 11228-1, the world's handling rule, D20)."), unitCode="KGM")}]}


def carton_package(it, where):
    """A spare frame's carton as cac:Package: one frame in it (D20)."""
    c = it["carton"]
    return {"Quantity": qty(1, it["unit"], "One side frame in each carton."),
            "PackageLevelCode": V("1", "UN/EDIFACT 7075 code 1: the inner level, below the pallet."),
            "PackagingTypeCode": V("CT", "UN/ECE Recommendation 21 code CT: carton."),
            "PackagingType": V(f"{c['name']}, one side frame", f"The carton in words; {where}"),
            "PackingMaterial": V(c["material"], "What the packaging is made of."),
            "ReturnableMaterialIndicator": V("false", "The carton stays with the frame.")}


def goods_packages(flow, d):
    """The packages a goods item travels in (D20, O61, worklist C12): the bench's three parcels or the frame's
    carton, on pallets where the flow ships them so; the cotton's bales where the flow lists its packages."""
    if flow_packages(flow, d["item"]):
        return containing_package(flow, d["item"])
    it = maker(d["item"])
    if it.get("parcels"):
        inner = [parcel_package(p) for p in it["parcels"]]
    elif it.get("carton"):
        inner = [carton_package(it, "the goods item's frames travel one to a carton.")]
    else:
        return {}
    units = pallets(flow, [d])
    if not units:
        return {"ContainingPackage": inner}
    per = units[0][2]
    what = "benches" if it.get("parcels") else "side frames"
    return {"ContainingPackage": {
        "Quantity": qty(per, it["unit"], f"{per} {what} to a pallet; the goods item travels on {len(units)} "
                                         f"pallet{'s' if len(units) > 1 else ''}."),
        "PackageLevelCode": V("3", "UN/EDIFACT 7075 code 3: the outer level, the pallet."),
        "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
        "ReturnableMaterialIndicator": V("true", "The pallet goes back to the party that loaded it."),
        "ContainedPackage": inner}}


def handling_units(flow, deal, owner, marks, detail=False):
    """The pallets of a deal, as transport handling units, numbered in the convention of the party that makes them
    up (unit_id). A bench pallet (1850 x 700 mm, four benches in three parcels each, 745 mm high loaded) may go two
    high; the pallet of frame cartons travels with nothing on top (world/items.json, D20)."""
    out = []
    units = pallets(flow, deal)
    for k, it, n_ in units:
        bench = bool(it.get("parcels"))
        uid = unit_id(owner, flow, k)
        count, load = pallet_load(it, n_)
        x = {"ID": uid,
             "TransportHandlingUnitTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
             "TotalGoodsItemQuantity": qty(1, "EA", "One kind of goods on the pallet."),
             "TotalPackageQuantity": qty(count, "EA", f"The parcels on the pallet: {load}."),
             "ShippingMarks": V(f"{marks} / {k:03d} of {len(units):03d}", "The marks on the pallet: the consignee's "
                                                                          "mark and the pallet's place in the count."),
             "TraceID": V(uid.value, "The pallet's barcode, scanned at each handover: it carries the same "
                                     "number.")}
        if detail:
            pal = it["pallet"]
            x["HandlingCode"] = V("STACK2" if pal["stack"] == 2 else "NOSTACK",
                                  "The carrier's handling code: two high, or nothing on top.")
            x["HandlingInstructions"] = V(
                "Fork-lift only. May be stacked two high, bench pallet on bench pallet. Unpacked, a frame carton is "
                "a one-person lift; a slat bundle, 1.81 m long, is carried by two." if bench else
                "Fork-lift only. Load on top: nothing may be stacked on the cartons. Unpacked, each carton is a "
                "one-person lift.", "The handling, in words, with the world's rule for manual handling (ISO 11228-1, "
                                    "D20).")
            L, W, H = pal["mm"]
            area = (Decimal(L) * Decimal(W) / Decimal(10 ** 6)).quantize(Decimal("0.1"))
            x["MeasurementDimension"] = [
                {"AttributeID": V("LENGTH", "The pallet's footprint."), "Measure": V(str(L), "Its length.",
                                                                                     unitCode="MMT")},
                {"AttributeID": V("WIDTH", "The pallet's footprint."), "Measure": V(str(W), "Its width.",
                                                                                    unitCode="MMT")},
                {"AttributeID": V("HEIGHT", "The height of the loaded pallet."), "Measure": V(str(H), "Its height.",
                                                                                              unitCode="MMT")},
                {"AttributeID": V("GROSSWEIGHT", "The loaded pallet's weight."),
                 "Measure": V(kg(unit_weight(it, n_)), f"The goods, {kg(n_ * Decimal(str(it['gross_kg'])))} kg, and "
                              f"the pallet's own {kg(pal['tare_kg'])} kg.", unitCode="KGM")}]
            x["FloorSpaceMeasurementDimension"] = {"AttributeID": V("FLOORSPACE", "The floor the pallet takes."),
                                                   "Measure": V(kg(area), "In square metres.", unitCode="MTK")}
            x["PalletSpaceMeasurementDimension"] = {"AttributeID": V("PALLETPLACES", "The pallet places taken on "
                                                                                      "the truck."),
                                                    "Measure": V("0.5" if pal["stack"] == 2 else "1", "Half a place "
                                                                 "when two pallets are stacked; the frame cartons' "
                                                                 "pallet takes a whole one. A number of places, not "
                                                                 "of articles, so unit C62 (one), which allows a "
                                                                 "half.", unitCode="C62")}
            if bench:
                x["Package"] = [parcel_package(p) for p in it["parcels"]]
            else:
                x["Package"] = carton_package(it, f"{n_} of them on the pallet.")
        out.append(x)
    return out


def card_account(holder, merchant):
    """The cac:CardAccount of a card payment at a merchant's till (decision ID-Q10b): the card number masked as the
    merchant's till prints it, the card scheme, the issuer's bank identifier, the chip application; no security code
    and no dates of the card, which a receipt never shows."""
    card = PARTY[holder]["identity"]["card"]
    mask = PARTY[merchant]["identity"]["card_mask"]
    pan = card["pan"]
    shown = pan[:mask["first"]] + "*" * (len(pan) - mask["first"] - mask["last"]) + pan[len(pan) - mask["last"]:]
    issuer = PARTY[card["issuer"]]["identity"]
    out = {"PrimaryAccountNumberID": V(shown, f"The card number, masked as the till prints it: {mask['note'][:-1].lower()} "
                                              "(PCI DSS allows at most the first six and the last four). The number "
                                              "itself starts with 9 and the numeric code of the issuer's country, as "
                                              "ISO/IEC 7812 provides for national use, so it is no real card's."),
           "NetworkID": V(card["scheme"], "The card scheme the card runs on."),
           "CardTypeCode": V(card["type"], f"A {card['type'].lower()} card."),
           "IssuerID": V(issuer["bic"], f"The card's issuer, {issuer['name']}, by its bank identifier.",
                         schemeID="urn:ubl-examples:world:bank-identifier")}
    if card.get("aid"):
        out["CardChipCode"] = V("Chip", "Read from the chip.")
        out["ChipApplicationID"] = V(card["aid"], "The chip application used: the card scheme's registered application "
                                                  f"provider identifier {card['aid'][:10]}, from the national category "
                                                  "D of ISO/IEC 7816-5 with the country code of the scheme, and the "
                                                  "application's own code.")
    out["HolderName"] = V(card["holder"], "The name on the card.")
    return out


def gln_location(pid, key):
    """The identifier of a place of a GS1 party: its Global Location Number (decision ID-Q7)."""
    loc = PARTY[pid]["identity"]["identification"]["locations"][key]
    return {"ID": V(loc["gln"], f"The Global Location Number of the place, {loc['name'].lower()}: "
                                f"{PARTY[pid]['identity']['name']} identifies its places the GS1 way, under its company "
                                "prefix (952, reserved for examples); world/parties.json.", schemeID="GS1 GLN")}


UNIT_SERIALS = {}       # (owner, flow, unit) -> serial in the packer's own running series


def unit_serial(owner, flow, k):
    """The next number in the running series of the party that makes the unit up (identifiers#F4): independent of
    the flow, its file numbers and the serials of the goods on the unit. The same unit keeps its number when it is
    asked for again."""
    key = (owner, flow.id, k)
    if key not in UNIT_SERIALS:
        used = sum(1 for o, _, _ in UNIT_SERIALS if o == owner)
        start = 1000 + sum(ord(c) for c in owner) * 37 % 9000
        UNIT_SERIALS[key] = start * 100 + used + 1
    return UNIT_SERIALS[key]


def unit_id(owner, flow, k, what="The number on the pallet label"):
    """The identifier of logistic unit k of a flow, in the identification convention of the party that makes the
    unit up (decision ID-Q7): an SSCC for a GS1 party, an ISO/IEC 15459 licence plate of the Codana Identification
    Agency for an ISO party, else the party's own number. The same unit has the same identifier in every document of
    the flow."""
    conv = PARTY[owner]["identity"].get("identification", {})
    serial = f"{unit_serial(owner, flow, k):09d}"
    name = PARTY[owner]["identity"]["name"]
    if conv.get("convention") == "GS1":
        return V(world_ids.sscc(conv["company_prefix"], serial), f"{what}: the unit's SSCC, which {name} gives every "
                 "logistic unit it makes up, under its GS1 company prefix (952, reserved for examples), with the check "
                 "digit.", schemeID="GS1 SSCC")
    if conv.get("convention") == "ISO":
        return V(world_ids.licence_plate(conv["codana_cin"], serial), f"{what}: the unit's licence plate in the "
                 f"structure of ISO/IEC 15459, which {name} gives every unit it makes up: the Codana Identification "
                 "Agency's issuing agency code KXU, its company number, a serial number and a check digit. The bar "
                 "code on the label adds the data identifier J, which the document leaves out.", schemeID="ISO 15459")
    return V(f"{initials(owner)}-{flow.date(0)[2:4]}-{k:03d}", f"{what}: {name}'s own number for the unit.")
