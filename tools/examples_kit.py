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

from build_examples import ITEM, PARTY, WORLD, V, account, amount, item, money, price, qty

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
    words = [w for w in PARTY[pid]["identity"]["name"].replace("'", "").split() if w.lower() not in ("of", "and", "the")]
    return "".join(w[0] for w in words)[:4].upper()


class Flow:
    """The context of one flow: its start date, its numbering and its deal."""
    def __init__(self, flow_id, start, deal=None):
        self.id, self.start, self.deal = flow_id, datetime.date.fromisoformat(start), deal or []
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


def tax_rule(seller, buyer, iid):
    """The tax category of a supply: (code, percent, scheme, reason, exemption reason or None).

    Category codes are UN/EDIFACT 5305: S standard rate, E exempt, G free export item (tax not
    charged), O not subject to tax (outside the scope)."""
    s, b, it = PARTY[seller], PARTY[buyer], ITEM[iid]
    c = WORLD["countries"][s["c"]]
    scheme = c["tax"]["schemes"][0]
    if it.get("levy"):
        return ("O", 0, scheme, f"A public levy the seller collects for {PARTY[it['levy']]['identity']['name']}: not a "
                                "supply, so outside the scope of the sales tax (category O).", "Levy collected for a "
                                                                                               "public body")
    if s["c"] == "XU":
        if b["c"] == "XU":
            return ("S", c["tax"]["schemes"][0]["rates"]["standard"], scheme,
                    "A domestic supply in Urvania: its value added tax applies at the standard rate (category S).", None)
        if it["kind"] == "goods":
            return ("G", 0, scheme, "Goods exported from Urvania: no value added tax is charged on an export "
                                    "(category G, free export item).", "Export of goods outside Urvania")
        return ("O", 0, scheme, "A service to a business abroad is supplied where the customer is, outside the scope of "
                                "Urvania's value added tax (category O).", "Service to a business established outside Urvania")
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
        return ("E", 0, scheme, "A sale to a business that resells or processes the goods is exempt from the state sales "
                                "tax, which is charged only on the sale to the final consumer (category E).",
                "Sale for resale or manufacture")
    return ("O", 0, None, "Lisavu has no sales tax or value added tax: no tax applies (category O).", None)


def tax_category(rule, kind=None):
    code, percent, scheme, why, exemption = rule
    out = {"ID": V(code, why), "Percent": V(str(percent), "The rate for this category." if percent else
                                            "No tax is charged in this category.")}
    if exemption:
        codes = next((c["tax"].get("exemption_codes", {}) for c in WORLD["countries"].values()
                      if exemption in c["tax"].get("exemption_codes", {})), {})
        if exemption in codes:
            out["TaxExemptionReasonCode"] = V(codes[exemption], "The world's code for the exemption reason "
                                                                "(world/countries.json).")
        out["TaxExemptionReason"] = V(exemption, "Why no tax is charged, stated rather than left out (UBL rule IND6).")
    if kind:
        out["SupplyTypeCode"] = V("Goods" if kind == "goods" else "Services", "Whether the category applies to goods "
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


def payment_terms(flow, seller, buyer, day, due_days, total, cur, number):
    """The seller country's payment practice (world/countries.json) applied to this invoice."""
    c = WORLD["countries"][PARTY[seller]["c"]]
    pay = c["payment"]
    out = {"ID": V(f"{PARTY[seller]['c']}-STD", f"The standard terms of {c['name']}."),
           "Note": V(pay["terms"], pay["note"]),
           "PaymentDueDate": V(flow.date(day + due_days), "The day the amount is due."),
           "PaymentMeansID": V("1", "The payment means these terms apply to: the credit transfer below.")}
    if pay.get("discount"):
        dsc = pay["discount"]
        out["SettlementDiscountPercent"] = V(dsc["percent"], "The cash discount for early payment.")
        out["SettlementDiscountAmount"] = amount(total * Decimal(dsc["percent"]) / 100, cur, "The discount on the "
                                                 "amount payable, if paid in time.")
        out["SettlementPeriod"] = {"StartDate": V(flow.date(day), "From the invoice date."),
                                   "EndDate": V(flow.date(day + dsc["days"]), f"For {dsc['days']} days.")}
    if pay.get("penalty_surcharge"):
        pen = pay["penalty_surcharge"]
        out["PenaltySurchargePercent"] = V(pen["percent"], f"The surcharge per {pen['per']} of late payment.")
        out["PenaltyAmount"] = amount(total * Decimal(pen["percent"]) / 100, cur, "The surcharge for the first month "
                                                                                  "late.")
        out["PenaltyPeriod"] = {"StartDate": V(flow.date(day + due_days + 1), "From the day after the due date."),
                                "DurationMeasure": V("1", "Per month.", unitCode="MON")}
    if pay.get("penalty_interest"):
        pi = pay["penalty_interest"]
        out["PenaltyInterestRate"] = {"InterestRatePercent": V(pi["percent"], "The interest on late payment."),
                                      "TimeBasisCode": V(pi["basis"], "A yearly rate."),
                                      "CalculationMethodCode": V("Simple", "Simple interest, per day late.")}
    if PARTY[seller]["identity"].get("website"):
        out["PaymentTermsDetailsURI"] = V(PARTY[seller]["identity"]["website"] + "/terms", "The seller's general "
                                                                                           "terms of payment.")
    return out


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
           "PaymentChannelCode": V("IBAN", "Paid to an account identified in the format of ISO 13616."),
           "PaymentRailID": V(system, "The payment system the transfer runs over: "
                              + ("the trade accord's link between the countries." if border else
                                 "the domestic clearing.")),
           "PaymentID": V(rf_reference(number), "The structured creditor reference of ISO 11649 to quote with the "
                                                "payment, made from the invoice number with its check digits."),
           "InstructionNote": V(f"Quote {rf_reference(number)}", "What the payer writes in the transfer.")}
    if border:
        out["ChargeBearerCode"] = V(WORLD["payment_cross_border"]["charge_bearer"], "ISO 20022 SHAR: each side pays "
                                                                                     "its own bank's charges.")
    out["PayeeFinancialAccount"] = account(payee, why_account, note=f"Invoice {number}")
    return out


def cost_centre(pid, why):
    """The buyer's accounting cost, as code and text, from its identity."""
    cc = PARTY[pid]["identity"].get("cost_centre")
    if not cc:
        return {}
    return {"AccountingCostCode": V(cc["code"], why), "AccountingCost": V(cc["name"], "The cost centre in words.")}


# ---------------------------------------------------------------- lines and totals
def unit_price(iid, currency):
    """The item's price in `currency`: its own price, or converted at the world's reference rate."""
    it = ITEM[iid]
    p = Decimal(str(it["price"]["amount"]))
    if it["price"]["currency"] == currency:
        return p
    return money(p * rate(it["price"]["currency"], currency), currency)


def lines(flow, seller, buyer, currency, which="ordered", deal=None):
    """The lines of a commercial document from the deal: (item, quantity, line amount, rule)."""
    out = []
    for d in (deal or flow.deal):
        q = Decimal(str(d[which]))
        p = unit_price(d["item"], currency)
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
        **cost_centre(buyer, "The buyer's cost centre, to be quoted on the invoice."),
        "LineCountNumeric": V(str(len(rows)), "The number of order lines."),
        "DeliveryTerms": {"ID": V(doc["values"]["DeliveryTerms/ID"], terms_why, schemeID="INCOTERMS"),
                          "DeliveryLocation": {"Description": V(location, "Where the delivery terms place the "
                                                                          "handover of the goods.")}},
        "TaxTotal": total,
        "AnticipatedMonetaryTotal": {
            "LineExtensionAmount": amount(base, cur, "The sum of the line amounts."),
            "PayableAmount": amount(base + tax, cur, "What the buyer expects to pay, tax included.")},
        "OrderLine": [{"LineItem": {
            "ID": V(str(i), "The line number."),
            "Quantity": qty(q, ITEM[d["item"]]["unit"], d.get("why", "The quantity ordered.")),
            "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
            "Price": price_block(d["item"], cur),
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


def price_block(iid, currency=None):
    it = ITEM[iid]
    if currency and currency != it["price"]["currency"]:
        r = rate(it["price"]["currency"], currency)
        return {"PriceAmount": price(unit_price(iid, currency), currency,
                                     f"The seller's price of {it['price']['amount']} {it['price']['currency']}, converted "
                                     f"to the buyer's currency at the world's reference rate, as the contract provides."),
                "BaseQuantity": qty(1, it["unit"], "The price is per one unit."),
                "PricingExchangeRate": {
                    "SourceCurrencyCode": V(it["price"]["currency"], "The currency of the seller's price list."),
                    "TargetCurrencyCode": V(currency, "The currency of the order."),
                    "SourceCurrencyBaseRate": V("1", "The rate is for one unit of the seller's currency."),
                    "TargetCurrencyBaseRate": V("1", "Given in single units of the order's currency."),
                    "ExchangeMarketID": V("World reference rate", "The rate the world's central banks publish "
                                                                  "(world/countries.json)."),
                    "CalculationRate": V(f"{r.normalize():f}", "The world's reference rate (world/countries.json)."),
                    "MathematicOperatorCode": V("Multiply", "The seller's price times the rate gives the order price."),
                    "Date": V("2026-01-02", "The reference rate of the first working day of the year, fixed in the "
                                            "contract.")}}
    out = {"PriceAmount": price(it["price"]["amount"], it["price"]["currency"], "The seller's price per unit "
                                                                                "(world/items.json)."),
           "BaseQuantity": qty(1, it["unit"], "The price is per one unit.")}
    if it.get("pack") and it["unit"] == "H87":
        out["OrderableUnitFactorRate"] = V(it["pack"]["size"], f"The item is priced per piece and ordered in packs: "
                                                               f"one pack holds {it['pack']['size']} pieces.")
    return out


def instances(flow, d, which, day):
    """ItemInstance for a despatched line: the production lot of the maker, or one instance per serial number."""
    it = ITEM[d["item"]]
    while it.get("resale_of"):         # a resold item keeps the maker's lot and serial numbers
        it = ITEM[it["resale_of"]]
    made = flow.date(day - 3)
    if it.get("serials"):
        q = int(Decimal(str(d[which])))
        first = flow.base * 10          # a stable range per flow: the same castings keep their numbers
        out = []
        for s in range(first, first + q):
            x = {"ManufactureDate": V(made, "The day the casting was poured and inspected."),
                 "SerialID": V(f"{it['serials']}{s:05d}", "The serial number cast into the frame; every casting is "
                                                         "traceable to its melt.")}
            if it.get("made_time"):
                x["ManufactureTime"] = V(it["made_time"], "The time the melt was poured.")
            if it.get("trace"):
                x["ProductTraceID"] = V(f"{it['trace']}{s:05d}", "The trace code on the casting's label, for the "
                                                               "maker's tracing system.")
            if it.get("registration"):
                x["RegistrationID"] = V(f"{it['registration']}{s:05d}", "The casting's entry in the maker's quality "
                                                                      "register, with its inspection result.")
            if it.get("instance_props"):
                x["AdditionalItemProperty"] = [{"Name": V(n_, "A fact about this one casting."),
                                                "Value": V(v, "Its value.")} for n_, v in it["instance_props"]]
            out.append(x)
        return out
    if it.get("lot_prefix"):
        lot = f"{it['lot_prefix']}{flow.date(day - 3).replace('-', '')[4:]}"
        x = {"ManufactureDate": V(made, "The day the lot was produced."),
             "LotIdentification": {"LotNumberID": V(lot, "The production lot, from the maker's prefix and the "
                                                         "production day; a recall names the lot.")}}
        if it.get("best_before_months"):
            m = it["best_before_months"]
            d0 = datetime.date.fromisoformat(made)
            until = d0.replace(year=d0.year + (d0.month - 1 + m) // 12, month=(d0.month - 1 + m) % 12 + 1).isoformat()
            x["BestBeforeDate"] = V(until, f"Best used within {m} months: the granulate takes up moisture in storage.")
            x["LotIdentification"]["ExpiryDate"] = V(until, "The lot's quality data apply until then.")
        if it.get("lot_props"):
            x["LotIdentification"]["AdditionalItemProperty"] = [{"Name": V(n_, "A fact about this lot."),
                                                                 "Value": V(v, "Its value for this lot.")}
                                                                for n_, v in it["lot_props"]]
        return [x]
    return None


def despatch_advice(flow, n, doc, day, why, shipment_why, extra=None, deal=None, key="order"):
    deal = deal or flow.deal
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = {
        "ID": V(flow.number(f"despatch-{key}", doc["from"], "DespatchAdvice"), "The despatching party's number."),
        "IssueDate": V(flow.date(day), why),
        "OrderReference": {"ID": V(flow.numbers[key], "The order this despatch fulfils.")},
        "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The despatching party's shipment number."),
                     "GrossWeightMeasure": qty(gross_weight(flow, which, deal), "KGM", shipment_why),
                     "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                             "The consignment the goods travel in, as numbered when the transport "
                                             "was booked.")}},
        "DespatchLine": [{"ID": V(str(i), "The line number."),
                          "DeliveredQuantity": qty(d[which], ITEM[d["item"]]["unit"], "What was despatched."),
                          "OrderLineReference": {"LineID": V(str(i), "The order line this line fulfils.")},
                          "Item": item(d["item"], buyer=doc["to"], instance=instances(flow, d, which, day))}
                         for i, d in enumerate(deal, 1)],
    }
    flow.numbers["despatch"] = flow.numbers[f"despatch-{key}"]
    return merge_extra(out, extra)


def receipt_advice(flow, n, doc, day, why):
    which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
    return {"ID": V(flow.number("receipt", doc["from"], "ReceiptAdvice"), "The receiving party's number."),
            "IssueDate": V(flow.date(day), why),
            "OrderReference": {"ID": V(flow.numbers["order"], "The order the goods were delivered for.")},
            "DespatchDocumentReference": {"ID": V(flow.numbers["despatch"], "The despatch advice this receipt answers.")},
            "ReceiptLine": [{"ID": V(str(i), "The line number."),
                             "ReceivedQuantity": qty(d.get("received", d[which]), ITEM[d["item"]]["unit"],
                                                     d.get("received_why", "Counted at the goods-in and found as "
                                                                           "announced.")),
                             "Item": item(d["item"], buyer=doc["from"])} for i, d in enumerate(flow.deal, 1)]}


def gross_weight(flow, which, deal=None):
    return sum(Decimal(str(d[which])) * Decimal(str(ITEM[d["item"]].get("gross_kg", 0))) for d in (deal or flow.deal))


def invoice(flow, n, doc, day, due_days, why_date, refs, rows_spec=None, key="invoice", extra=None, charges=None,
            currency=None):
    """A commercial invoice from the seller (doc['from']) to the buyer; rows_spec overrides the deal."""
    seller, buyer = doc["from"], doc["to"]
    cur = currency or currency_of(seller)
    if rows_spec is None:
        which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
        rows = lines(flow, seller, buyer, cur, which)
    else:
        rows = [(d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * unit_price(d["item"], cur), cur),
                 tax_rule(seller, buyer, d["item"])) for d in rows_spec]
    rows, gross = line_allowances(rows, cur)
    base = sum(r[2] for r in rows)
    charge_rows = [({"item": c["like"]}, None, money(Decimal(str(c["amount"])), cur), tax_rule(seller, buyer, c["like"]))
                   for c in (charges or [])]
    tax, total = tax_total(rows + charge_rows, cur)
    out = {
        "ID": V(flow.number(key, seller, "Invoice"), "The seller's invoice number."),
        "IssueDate": V(flow.date(day), why_date),
        "DueDate": V(flow.date(day + due_days), f"{due_days} days after the issue date, the agreed payment term."),
        "InvoiceTypeCode": V("380", "UN/EDIFACT 1001 code 380: commercial invoice."),
        "DocumentCurrencyCode": currency_line(cur, "the seller's currency" if cur == currency_of(seller)
                                              else "the buyer's currency, agreed in the contract"),
        **cost_centre(buyer, "The buyer's cost centre, quoted in its order, so the invoice is booked without "
                            "asking."),
        "LineCountNumeric": V(str(len(rows)), "The number of invoice lines, as a check on the transfer."),
        "DefaultLanguageCode": V(WORLD["countries"][PARTY[seller]["c"]]["languages"][0], "The language the texts "
                                 "of the invoice are in: the seller's country's language."),
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
        "PaymentTerms": payment_terms(flow, seller, buyer, day, due_days, base + tax +
                                      sum(r[2] for r in charge_rows), cur, flow.number(key, seller, "Invoice")),
        "TaxTotal": total,
        "LegalMonetaryTotal": monetary_total(base, tax, cur, sum(r[2] for r in charge_rows)),
        "InvoiceLine": [{
            "ID": V(str(i), "The line number."),
            "InvoicedQuantity": qty(q, ITEM[d["item"]]["unit"], d.get("invoice_why", "The quantity delivered.")),
            "LineExtensionAmount": amount(amt, cur, f"{q} × {unit_price(d['item'], cur)}, rounded to the minor unit of "
                                                    "the currency."),
            "Item": item(d["item"], tax_category(rule, ITEM[d["item"]]["kind"])),
            "Price": price_block(d["item"], cur)} for i, (d, q, amt, rule) in enumerate(rows, 1)],
    }
    line_features(rows, out["InvoiceLine"], cur, gross)
    if rows_spec is None and "OrderReference" in refs:      # the lines of the deal are the lines of the order
        for i, line in enumerate(out["InvoiceLine"], 1):
            line["OrderLineReference"] = {"LineID": V(str(i), "The order line this invoice line bills.")}
    if "TaxPointDate" not in out and PARTY[seller]["c"] == "XU":
        out["TaxPointDate"] = V(flow.date(day), "Urvania's value added tax becomes due on the invoice date.")
    if charges:
        out["AllowanceCharge"] = [{"ChargeIndicator": V("true", "A charge, not an allowance: it adds to the amount."),
                                   "AllowanceChargeReason": V(c["reason"], c["why"]),
                                   "Amount": amount(c["amount"], cur, c["amount_why"]),
                                   "TaxCategory": tax_category(r[3])} for c, r in zip(charges, charge_rows)]
    flow.numbers[f"{key}-amount"] = base + sum(r[2] for r in charge_rows) + tax
    flow.numbers[f"{key}-date"] = flow.date(day)
    flow.numbers[f"{key}-currency"] = cur
    return merge_extra(out, extra)


def remittance(flow, n, doc, day, why, key="invoice", discount=None, credit=None):
    """credit: (number, date, amount) of a credit note the payer deducts."""
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
        "PayerReference": V(f"{initials(payer)}-{flow.base:04d}", "The payer's own reference for this payment run."),
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
            "PaymentPurposeCode": V("SUPP", "ISO 20022 purpose code SUPP: payment to a supplier."),
            "InvoicingPartyReference": V(rf_reference(flow.numbers[key]), "The reference the invoicing party asked "
                                                                          "to quote."),
            "BalanceAmount": amount(0, cur, "Nothing remains open on the invoice after this payment."),
            "AccountingSupplierParty": {"Party": party_short(payee)},
            "AccountingCustomerParty": {"Party": party_short(payer)},
            "DocumentReference": {"ID": V(flow.numbers[key], "The invoice paid, as a document reference."),
                                  "DocumentTypeCode": V("380", "UN/EDIFACT 1001 code 380: commercial invoice."),
                                  "IssueDate": V(flow.numbers[f"{key}-date"], "Its issue date.")},
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
def tep_request(flow, n, doc, day, why, start_day, weight, why_weight):
    return {"ID": V(flow.number("tep-request", doc["from"], "TransportExecutionPlanRequest"),
                    "The transport user's request number."),
            "IssueDate": V(flow.date(day), why),
            "ServiceStartTimePeriod": {"StartDate": V(flow.date(start_day), "The day the goods should be collected.")},
            "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                    "The transport user's number for this consignment, quoted along the chain."),
                            "GrossWeightMeasure": qty(weight, "KGM", why_weight)}}


def tep(flow, n, doc, day, why, start_day, weight):
    return {"ID": V(flow.number("tep", doc["from"], "TransportExecutionPlan"), "The carrier's number for the agreed plan."),
            "IssueDate": V(flow.date(day), why),
            "DocumentStatusCode": V("Confirmed", "The carrier confirms the plan as requested. A value of UBL's document "
                                                 "status code list (2.1: Document has been confirmed)."),
            "TransportExecutionPlanRequestDocumentReference": {"ID": V(flow.numbers["tep-request"],
                                                                       "The request this plan answers.")},
            "ServiceStartTimePeriod": {"StartDate": V(flow.date(start_day), "Collection, as requested.")},
            "Consignment": {"ID": V(flow.numbers["consignment"], "The consignment of the request."),
                            "GrossWeightMeasure": qty(weight, "KGM", "The weight the plan is made for.")}}


def waybill(flow, n, doc, day, why, weight, why_weight, extra=None):
    out = {"ID": V(flow.number("waybill", doc["from"], "Waybill"), "The consignment note number."),
           "IssueDate": V(flow.date(day), why),
           "Shipment": {"ID": V(flow.numbers.get("shipment") or flow.number("shipment", doc["from"], "Shipment"),
                                "The shipment as the despatching party numbered it."),
                        "GrossWeightMeasure": qty(weight, "KGM", why_weight),
                        "Consignment": {"ID": V(flow.numbers.get("consignment") or
                                                flow.number("consignment", doc["from"], "Consignment"),
                                                "The consignment of the transport booking.")}}}
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


HS_SECTION = {"26": "V", "39": "VII", "44": "IX", "52": "XI", "62": "XI", "73": "XV", "94": "XX"}


def customs_item(iid):
    """The item as goods declared or carried: its classification also says the nature and the kind of cargo."""
    out = item(iid)
    cc = out.get("CommodityClassification")
    maker = ITEM[iid]
    while maker.get("resale_of"):
        maker = ITEM[maker["resale_of"]]
    hs = maker.get("hs")
    if cc and hs:
        cc["NatureCode"] = V(HS_SECTION[hs[:2]], "The section of the Harmonized System the goods fall in, the "
                                                 "highest level of the World Customs Organization's classification.")
        cc["CargoTypeCode"] = V("BULK" if ITEM[iid]["unit"] in ("TNE",) and hs[:2] == "26" else "GEN",
                                "The kind of cargo as the parties code it: bulk, or general cargo in packages.")
    return out


def goods_items(flow, currency, value_why, deal=None):
    """GoodsItem per line of the deal: customs value (converted to `currency` at the reference rate if needed),
    gross weight, quantity and the item with its customs tariff code and origin."""
    deal = deal or flow.deal
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = []
    for i, d in enumerate(deal, 1):
        it = ITEM[d["item"]]
        q = Decimal(str(d[which]))
        value = q * Decimal(str(it["price"]["amount"])) * rate(it["price"]["currency"], currency)
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What the goods are, in words."),
                    "DeclaredCustomsValueAmount": amount(value, currency, value_why),
                    "GrossWeightMeasure": qty(q * Decimal(str(it.get("gross_kg", 0))), "KGM",
                                              "The gross weight of the goods of this item."),
                    "Quantity": qty(q, it["unit"], "The quantity declared."),
                    "Item": customs_item(d["item"])})
    return out


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
                             "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment carried.")}}}}


def import_declaration(flow, n, doc, day, why, value_why, refs=None, deal=None):
    cur = currency_of(doc["from"])
    deal = deal or flow.deal
    which = "delivered" if any("delivered" in d for d in deal) else "ordered"
    out = {"ID": V(flow.number("import", doc["from"], "ImportCustomsDeclaration"), "The importer's declaration number."),
           "IssueDate": V(flow.date(day), why),
           "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The shipment declared."),
                        "GrossWeightMeasure": qty(gross_weight(flow, which, deal), "KGM", "The gross weight arriving."),
                        "GoodsItem": goods_items(flow, cur, value_why, deal)}}
    if refs:
        out["AdditionalDocumentReference"] = refs
    return out


def transportation_status(flow, n, doc, day, event_why, description, location, extra=None):
    out = {"ID": V(flow.number(f"status-{n}", doc["from"], "TransportationStatus"), "The sender's status report number."),
           "IssueDate": V(flow.date(day), event_why),
           "TransportEvent": {"OccurrenceDate": V(flow.date(day), "The day the event took place."),
                              "Description": V(description, "What happened, in words."),
                              "Location": {"Name": V(location, "Where it happened.")}},
           "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                   "The consignment the report is about.")}}
    return merge_extra(out, extra)


# ---------------------------------------------------------------- credit, retail and collaboration
def credit_note(flow, n, doc, day, why, rows_spec, refs):
    seller, buyer = doc["from"], doc["to"]
    cur = currency_of(seller)
    rows, gross = line_allowances(spec_rows(rows_spec, seller, buyer, cur), cur)
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    out = {"ID": V(flow.number(f"credit-{n}", seller, "CreditNote"), "The seller's credit note number."),
            "IssueDate": V(flow.date(day), why),
            "CreditNoteTypeCode": V("381", "UN/EDIFACT 1001 code 381: credit note."),
            "DocumentCurrencyCode": currency_line(cur, "the currency of the invoice credited"),
            **cost_centre(buyer, "The buyer's cost centre, as on the invoice credited."),
            "LineCountNumeric": V(str(len(rows)), "The number of lines."),
            "DefaultLanguageCode": V(WORLD["countries"][PARTY[seller]["c"]]["languages"][0], "The language of the "
                                                                                              "texts."),
            "PaymentTerms": {"Note": V("Settled against the next payment to the seller, unless refunded.",
                                       "How a credit note is settled in the world.")},
            **refs,
            "TaxTotal": total,
            "LegalMonetaryTotal": monetary_total(base, tax, cur),
            "CreditNoteLine": [{"ID": V(str(i), "The line number."),
                                "CreditedQuantity": qty(q, ITEM[d["item"]]["unit"], d["why"]),
                                "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
                                "Item": item(d["item"], tax_category(rule, ITEM[d["item"]]["kind"])),
                                "Price": line_price(d, cur)} for i, (d, q, amt, rule) in enumerate(rows, 1)]}
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
        p = Decimal(str(d.get("unit_price", ITEM[d["item"]]["price"]["amount"])))
        out.append((d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * p, cur), tax_rule(seller, buyer, d["item"])))
    return out


def line_price(d, cur):
    if "unit_price" in d:
        return {"PriceAmount": price(d["unit_price"], cur, d["unit_price_why"]),
                "BaseQuantity": qty(1, ITEM[d["item"]]["unit"], "The price is per one unit.")}
    return price_block(d["item"])


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


def catalogue_terms(flow, doc, day, validity_days, iid, alternative=None):
    """The terms a catalogue line is offered on: lead time, minimum quantity, where it is sold, the price and
    the price list it belongs to."""
    it = ITEM[iid]
    seller = PARTY[doc["from"]]
    p = price_block(iid)
    p["ValidityPeriod"] = {"StartDate": V(flow.date(day), "The price applies from the catalogue's issue date."),
                           "EndDate": V(flow.date(day + validity_days), "And until the catalogue ends.")}
    p["PriceList"] = {"ID": V(f"{seller['identity'].get('short', doc['from']).upper()}-PL-{flow.date(day)[:4]}",
                              "The seller's price list this price is taken from."),
                      "StatusCode": V("Active", "The price list is in force.")}
    out = {"LeadTimeMeasure": V(it.get("lead_days", 5), "The days between order and despatch.", unitCode="DAY"),
           "MinimumQuantity": qty(it.get("min_order", 1), it["unit"], "The smallest quantity the seller accepts on an "
                                                                       "order."),
           "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V(PARTY[doc["from"]]["c"], "The catalogue "
                                                                              "is offered for buyers in the seller's "
                                                                              "country.")}},
           "Price": p}
    p["PriceTypeCode"] = V("TRD", "The seller's code for its trade price.")
    p["PriceType"] = V("Trade price", "A price for resellers, before sales tax.")
    if alternative:
        p["AlternativeCurrencyPrice"] = {
            "PriceAmount": price(unit_price(iid, alternative), alternative, "The same price in the buyer's currency, "
                                 "at the world's reference rate on the catalogue's issue day; for information only."),
            "BaseQuantity": qty(1, it["unit"], "Per one unit.")}
    if it.get("max_order"):
        out["MaximumQuantity"] = qty(it["max_order"], it["unit"], "The most one order can take from stock: two "
                                                                   "containers.")
    if it.get("conditions"):
        out["TradingRestrictions"] = V("Not sold to consumers.", "The bench is sold through retailers.")
        out["DeliveryUnit"] = {"BatchQuantity": qty(4, it["unit"], "The benches are delivered per pallet of four."),
                               "ConsumerUnitQuantity": qty(1, it["unit"], "One bench is one consumer unit.")}
        out["Package"] = {"ID": V("PAL-4", "The pallet the price is for."),
                          "Quantity": qty(4, it["unit"], "Four benches to a pallet."),
                          "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet.")}
        out["AllowanceCharge"] = {"ChargeIndicator": V("false", "A discount."),
                                  "AllowanceChargeReasonCode": V("78", "UN/EDIFACT 5189 code 78: volume discount.",
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
    if it.get("resale_of") and ITEM[it["resale_of"]].get("serials"):     # the spare frame, priced after the bench
        bench = next(i for i in WORLD["items"] if i["seller"] == it["seller"] and i.get("conditions"))
        out["DependentPriceReference"] = {"Percent": V(str(round(Decimal(str(it["price"]["amount"])) * 100 /
                                                                 Decimal(str(bench["price"]["amount"])), 2)),
                                                       "The spare frame costs this share of the bench's price, "
                                                       "as the distributor's price rule sets it."),
                                          "DependentLineReference": {"LineID": V("1", "The catalogue line of the "
                                                                                      "bench.")}}
    out["ApplicableTaxCategory"] = tax_category(tax_rule(doc["from"], doc["to"], iid))
    return out


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
            "AllowanceChargeReasonCode": V("75", "UN/EDIFACT 5189 code 75: promotion discount.",
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
                                     "Item": item(d["item"], tax_category(rule, ITEM[d["item"]]["kind"])),
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
           "DefaultLanguageCode": V(WORLD["countries"][PARTY[supplier]["c"]]["languages"][0], "The language of the "
                                                                                               "texts."),
           **refs,
           "TaxTotal": total,
           "LegalMonetaryTotal": monetary_total(base, tax, cur),
           line: [{"ID": V(str(i), "The line number."),
                   qname: qty(q, ITEM[d["item"]]["unit"], d["why"]),
                   "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
                   "Item": item(d["item"], tax_category(rule, ITEM[d["item"]]["kind"])),
                   "Price": line_price(d, cur)} for i, (d, q, amt, rule) in enumerate(rows, 1)]}
    if not credit:
        out["InvoiceTypeCode"] = V("389", "UN/EDIFACT 1001 code 389: self-billed invoice.")
        number = flow.numbers[f"self-billed-{n}"]
        due = WORLD["countries"][PARTY[supplier]["c"]]["payment"]["due_days"]
        out["DueDate"] = V(flow.date(day + due), "The supplier's usual term, which the customer applies to itself.")
        out["PaymentMeans"] = payment_means(flow, supplier, customer, supplier, day, due, number,
                                            "The supplier's account, where the customer pays what it billed itself.")
        out["PaymentTerms"] = payment_terms(flow, supplier, customer, day, due, base + tax, cur, number)
    else:
        out["CreditNoteTypeCode"] = V("261", "UN/EDIFACT 1001 code 261: self-billed credit note.")
    flow.numbers[f"self-billed-{n}-amount"] = base + tax
    flow.numbers[f"self-billed-{n}-date"] = flow.date(day)
    return out


# ---------------------------------------------------------------- containers
def container_number(owner, serial):
    """An ISO 6346 container number: owner code, U (freight container), six digits and the check digit."""
    values = {c: v for c, v in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25,
                                                                   26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38])}
    code = f"{owner}U{serial:06d}"
    total = sum((values[c] if c.isalpha() else int(c)) * 2 ** i for i, c in enumerate(code))
    return f"{code}{total % 11 % 10}"


# ---------------------------------------------------------------- transport: places, means, events, units
PLACES = {"XUFER": ("Ferrano", "XU"), "XUSRV": ("Serravona", "XU"), "XBMRW": ("Marrowdale", "XB"),
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
        out["DirectionCode"] = V(direction, "The direction of the journey, as the carrier codes its services.")
    out["TransportMeansTypeCode"] = V(f.get("type", f["kind"].upper()), f"The carrier's code for the kind of means: "
                                                                          f"{f['name'].lower()}; {src}.")
    if f["kind"] == "road":
        out["RoadTransport"] = {"LicensePlateID": V(f["plate"], f"The registration plate of the truck; {src}.")}
        if f.get("trailer"):
            out["RoadTransport"]["TrailerLicensePlateID"] = V(f["trailer"], "The trailer's own plate.")
        if f.get("loading_m"):
            out["MeasurementDimension"] = {"AttributeID": V("Loading length", "The length of the loading floor."),
                                           "Measure": V(f["loading_m"], f"Room for {f['pallets']} pallets.",
                                                        unitCode="MTR")}
    if f["kind"] == "rail":
        out["RailTransport"] = {"TrainID": V(f["ore_train"] if ore else f["train"], f"The train number; {src}.")}
    if f["kind"] in ("inland", "sea"):
        m = {"VesselID": V(f["vessel_id"], "The vessel's number in its country's register of ships; a number of the "
                                           "world, not an IMO number.", schemeID="urn:ubl-examples:world:vessel"),
             "VesselName": V(f["name"], f"The vessel's name; {src}."),
             "RadioCallSignID": V(f["call_sign"], "The radio call sign, with the world's country code."),
             "MMSIRegistrationID": V(f["mmsi"], "The Maritime Mobile Service Identity, nine digits; 999 is no real "
                                                "country's maritime identification digits."),
             "GrossTonnageMeasure": V(f["gross_t"], "The gross tonnage of the vessel, a number without a unit.", unitCode="C62"),
             "NetTonnageMeasure": V(f["net_t"], "Its net tonnage, also without a unit.", unitCode="C62"),
             "ShipConfigurationCode": V(f["config"], "The kind of vessel."),
             "RegistryPortLocation": {"Name": V(f["registry"], "The port the vessel is registered in.")}}
        if f.get("ballast"):
            m["SegregatedBallastMeasure"] = V(f["ballast"], "The capacity of the tanks for ballast water only.",
                                              unitCode="TNE")
            m["ShipsRequirements"] = V("Shore power at the container quay.", "What the ship needs in port.")
            m["RegistryCertificateDocumentReference"] = {"ID": V(f"REG-{f['vessel_id']}", "The ship's certificate "
                                                                 "of registry.")}
        out["MaritimeTransport"] = m
    if f["kind"] == "air":
        out["AirTransport"] = {"AircraftID": V(f["aircraft"], "The aircraft's registration, with the world's country "
                                                              "code as its nationality mark.")}
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


def pallets(flow, deal):
    """The transport handling units of a deal: the benches on pallets of four, the castings boxed on one pallet."""
    units = []
    k = 0
    for d in deal:
        it = ITEM[d["item"]]
        while it.get("resale_of"):
            it = ITEM[it["resale_of"]]
        q = int(Decimal(str(d["ordered"])))
        per = it["package"]["per_package"] if it["package"]["type"] == "PX" else q
        for start in range(0, q, per):
            k += 1
            n_ = min(per, q - start)
            units.append((k, it, n_))
    return units


def handling_units(flow, deal, prefix, marks, detail=False):
    """The pallets of a deal, as transport handling units. Bench pallets (1850 x 650 mm, four benches) may go two
    high; the pallet of boxed castings (1200 x 800 mm) carries nothing on top."""
    out = []
    units = pallets(flow, deal)
    for k, it, n_ in units:
        pal = it["package"]["type"] == "PX"
        x = {"ID": V(f"{prefix}{k:03d}", "The number on the pallet label."),
             "TransportHandlingUnitTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
             "TotalGoodsItemQuantity": qty(1, "H87", "One kind of goods on the pallet."),
             "TotalPackageQuantity": qty(n_, "H87", f"{n_} benches on the pallet, each wrapped in film." if pal
                                         else f"{n_} boxed side frames on the pallet."),
             "ShippingMarks": V(f"{marks} / {k:03d} of {len(units):03d}", "The marks on the pallet: the consignee's "
                                                                          "mark and the pallet's place in the count."),
             "TraceID": V(f"{prefix}{k:03d}", "The pallet's barcode, scanned at each handover.")}
        if detail:
            x["HandlingCode"] = V("Stack2" if pal else "NoStack", "The carrier's handling code: two high, or "
                                                                  "nothing on top.")
            x["HandlingInstructions"] = V("May be stacked two high, steel frames on steel frames." if pal else
                                          "Load on top: nothing may be stacked on the boxes.", "The handling, in words.")
            x["MeasurementDimension"] = [
                {"AttributeID": V("Length", "The pallet's footprint."),
                 "Measure": V("1850" if pal else "1200", "Its length.", unitCode="MMT")},
                {"AttributeID": V("Width", "The pallet's footprint."),
                 "Measure": V("650" if pal else "800", "Its width.", unitCode="MMT")},
                {"AttributeID": V("Height", "The height of the loaded pallet."),
                 "Measure": V("1650" if pal else "900", "Its height.", unitCode="MMT")}]
            x["FloorSpaceMeasurementDimension"] = {"AttributeID": V("Floor space", "The floor the pallet takes."),
                                                   "Measure": V("1.2" if pal else "0.96", "In square metres.",
                                                                unitCode="MTK")}
            x["PalletSpaceMeasurementDimension"] = {"AttributeID": V("Pallet places", "The pallet places taken on "
                                                                                      "the truck."),
                                                    "Measure": V("0.5" if pal else "1", "Half a place when two pallets "
                                                                 "are stacked; the castings take a whole one.",
                                                                 unitCode="C62")}
            x["Package"] = {"ID": V(f"{prefix}{k:03d}-1", "The packages on the pallet."),
                            "Quantity": qty(n_, "H87", "The packages of this kind on the pallet."),
                            "PackagingTypeCode": V("SW" if pal else "BX", "UN/ECE Recommendation 21: "
                                                   + ("shrinkwrapped, each bench in film" if pal else "box") + "."),
                            "PackagingType": V("Bench in stretch film" if pal else "Cardboard box",
                                               "The packaging in words."),
                            "PackingMaterial": V("Recycled PE stretch film" if pal else "Corrugated cardboard",
                                                 "What the packaging is made of."),
                            "ReturnableMaterialIndicator": V("false", "The packaging is not returned."),
                            "PackageLevelCode": V("1", "The inner packaging, below the pallet.")}
            x["ActualPackage"] = {"ID": V(f"{prefix}{k:03d}", "The pallet itself, as packed."),
                                  "Quantity": qty(1, "H87", "One pallet."),
                                  "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
                                  "ReturnableMaterialIndicator": V("true", "The pallet is exchanged with the "
                                                                           "carrier and goes back.")}
        out.append(x)
    return out
