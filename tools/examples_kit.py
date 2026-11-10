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
         "RetailEvent": "RE", "InventoryReport": "IR", "PurchaseReceipt": "PR"}


def initials(pid):
    words = [w for w in PARTY[pid]["identity"]["name"].replace("'", "").split() if w.lower() not in ("of", "and", "the")]
    return "".join(w[0] for w in words)[:4].upper()


class Flow:
    """The context of one flow: its start date, its numbering and its deal."""
    def __init__(self, flow_id, start, deal=None):
        self.id, self.start, self.deal = flow_id, datetime.date.fromisoformat(start), deal or []
        self.base = 100 + zlib.crc32(flow_id.encode()) % 800      # a stable sequence per flow
        self.numbers = {}

    def number(self, key, sender, doc_type):
        """The document number of a document, the same wherever the document is referred to."""
        if key not in self.numbers:
            self.numbers[key] = f"{initials(sender)}-{CODES.get(doc_type, 'DOC')}-26-{self.base + len(self.numbers):04d}"
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
        return ("E", 0, scheme, "A sale to a business that resells or processes the goods is exempt from the state sales "
                                "tax, which is charged only on the sale to the final consumer (category E).",
                "Sale for resale or manufacture")
    return ("O", 0, None, "Lisavu has no sales tax or value added tax: no tax applies (category O).", None)


def tax_category(rule):
    code, percent, scheme, why, exemption = rule
    out = {"ID": V(code, why), "Percent": V(str(percent), "The rate for this category." if percent else
                                            "No tax is charged in this category.")}
    if exemption:
        out["TaxExemptionReason"] = V(exemption, "Why no tax is charged, stated rather than left out (UBL rule IND6).")
    if scheme:
        out["TaxScheme"] = {"ID": V(scheme["id"], f"UN/EDIFACT 5153 code of the seller's tax: {scheme['name'].lower()}.")}
    else:
        out["TaxScheme"] = {"Name": V("No general sales tax", "Lisavu has no general tax on sales; the scheme is named "
                                      "only, as UN/EDIFACT 5153 has no code for the absence of a tax.")}
    return out


# ---------------------------------------------------------------- lines and totals
def lines(flow, seller, buyer, currency, which="ordered"):
    """The lines of a commercial document from the deal: (item, quantity, line amount, rule)."""
    out = []
    for d in flow.deal:
        q = Decimal(str(d[which]))
        p = Decimal(str(ITEM[d["item"]]["price"]["amount"]))
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


def monetary_total(base, tax, currency):
    return {"LineExtensionAmount": amount(base, currency, "The sum of the line amounts."),
            "TaxExclusiveAmount": amount(base, currency, "The total without tax: the line amounts, no allowances or "
                                                         "charges."),
            "TaxInclusiveAmount": amount(base + tax, currency, "The total without tax plus the tax."),
            "PayableAmount": amount(base + tax, currency, "What the buyer is to pay; stated, not left to be calculated "
                                                          "(UBL 2.5, 2.2.2 Manifest Values).")}


def currency_of(pid):
    return WORLD["countries"][PARTY[pid]["c"]]["currency"]["code"]


def currency_line(currency, who):
    cur = next(c for c in WORLD["countries"].values() if c["currency"]["code"] == currency)
    decimals = {0: "no minor unit", 2: "two decimals", 3: "three decimals"}[cur["currency"]["minor_units"]]
    return V(currency, f"The {cur['currency']['name'].lower()}, {who}; it has {decimals}.")


# ---------------------------------------------------------------- documents of trade
def order(flow, n, doc, day, why_date, terms_why, location, extra=None):
    buyer, seller = doc["from"], doc["to"]
    cur = currency_of(seller)
    rows = lines(flow, seller, buyer, cur)
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    out = {
        "ID": V(flow.number("order", buyer, "Order"), "The buyer's order number."),
        "IssueDate": V(flow.date(day), why_date),
        "DocumentCurrencyCode": currency_line(cur, "the seller's currency, in which the seller's prices are"),
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
            "Price": price_block(d["item"]),
            "Item": item(d["item"])}} for i, (d, q, amt, rule) in enumerate(rows, 1)],
    }
    return merge_extra(out, extra)


def order_response(flow, n, doc, day, why):
    return {"ID": V(flow.number("order-response", doc["from"], "OrderResponse"), "The seller's number for its response."),
            "IssueDate": V(flow.date(day), why),
            "OrderResponseCode": V("AP", "UN/EDIFACT 4343 code AP: accepted, the order is accepted as it stands."),
            "OrderReference": {"ID": V(flow.numbers["order"], "The order this response answers.")}}


def price_block(iid):
    it = ITEM[iid]
    return {"PriceAmount": price(it["price"]["amount"], it["price"]["currency"], "The seller's price per unit "
                                                                                 "(world/items.json)."),
            "BaseQuantity": qty(1, it["unit"], "The price is per one unit.")}


def despatch_advice(flow, n, doc, day, why, shipment_why, extra=None):
    which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
    out = {
        "ID": V(flow.number("despatch", doc["from"], "DespatchAdvice"), "The despatching party's number."),
        "IssueDate": V(flow.date(day), why),
        "OrderReference": {"ID": V(flow.numbers["order"], "The order this despatch fulfils.")},
        "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The despatching party's shipment number."),
                     "GrossWeightMeasure": qty(gross_weight(flow, which), "KGM", shipment_why),
                     "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                             "The consignment the goods travel in, as numbered when the transport "
                                             "was booked.")}},
        "DespatchLine": [{"ID": V(str(i), "The line number."),
                          "DeliveredQuantity": qty(d[which], ITEM[d["item"]]["unit"], "What was despatched."),
                          "OrderLineReference": {"LineID": V(str(i), "The order line this line fulfils.")},
                          "Item": item(d["item"])} for i, d in enumerate(flow.deal, 1)],
    }
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
                             "Item": item(d["item"])} for i, d in enumerate(flow.deal, 1)]}


def gross_weight(flow, which):
    return sum(Decimal(str(d[which])) * Decimal(str(ITEM[d["item"]].get("gross_kg", 0))) for d in flow.deal)


def invoice(flow, n, doc, day, due_days, why_date, refs, rows_spec=None, key="invoice", extra=None):
    """A commercial invoice from the seller (doc['from']) to the buyer; rows_spec overrides the deal."""
    seller, buyer = doc["from"], doc["to"]
    cur = currency_of(seller)
    if rows_spec is None:
        which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
        rows = lines(flow, seller, buyer, cur, which)
    else:
        rows = [(d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])),
                                                   cur), tax_rule(seller, buyer, d["item"])) for d in rows_spec]
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    out = {
        "ID": V(flow.number(key, seller, "Invoice"), "The seller's invoice number."),
        "IssueDate": V(flow.date(day), why_date),
        "DueDate": V(flow.date(day + due_days), f"{due_days} days after the issue date, the agreed payment term."),
        "InvoiceTypeCode": V("380", "UN/EDIFACT 1001 code 380: commercial invoice."),
        "DocumentCurrencyCode": currency_line(cur, "the seller's currency"),
        **refs,
        "PaymentMeans": {
            "PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer. The listID is the identification of "
                                        "UBL's payment means code list, which code list validation checks.",
                                  listID="UN/EDIFACT EDED 4461"),
            "PayeeFinancialAccount": account(doc["parties"].get("PayeeParty", seller), "The account to pay to.")},
        "TaxTotal": total,
        "LegalMonetaryTotal": monetary_total(base, tax, cur),
        "InvoiceLine": [{
            "ID": V(str(i), "The line number."),
            "InvoicedQuantity": qty(q, ITEM[d["item"]]["unit"], d.get("invoice_why", "The quantity delivered.")),
            "LineExtensionAmount": amount(amt, cur, f"{q} × {ITEM[d['item']]['price']['amount']}, rounded to the minor "
                                                    "unit of the currency."),
            "Item": item(d["item"], tax_category(rule)),
            "Price": price_block(d["item"])} for i, (d, q, amt, rule) in enumerate(rows, 1)],
    }
    flow.numbers[f"{key}-amount"] = base + tax
    flow.numbers[f"{key}-date"] = flow.date(day)
    flow.numbers[f"{key}-currency"] = cur
    return merge_extra(out, extra)


def remittance(flow, n, doc, day, why, key="invoice"):
    payer, payee = doc["from"], doc["to"]
    cur, paid = flow.numbers[f"{key}-currency"], flow.numbers[f"{key}-amount"]
    return {
        "ID": V(flow.number("remittance", payer, "RemittanceAdvice"), "The payer's remittance number."),
        "IssueDate": V(flow.date(day), why),
        "DocumentCurrencyCode": currency_line(cur, "the currency of the invoice paid"),
        "TotalPaymentAmount": amount(paid, cur, "The amount transferred: the payable amount of the invoice."),
        "PaymentMeans": {
            "PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer.", listID="UN/EDIFACT EDED 4461"),
            "PayerFinancialAccount": account(payer, "The account the payer pays from."),
            "PayeeFinancialAccount": account(doc["parties"].get("PayeeParty", payee), "The account stated on the invoice.")},
        "RemittanceAdviceLine": {
            "ID": V("1", "One invoice paid."),
            "DebitLineAmount": amount(paid, cur, "The amount of the invoice this payment settles: the whole payable "
                                                 "amount. Paid invoices are debits on a remittance advice, as in the "
                                                 "OASIS example UBL-RemittanceAdvice-2.0-Example."),
            "BillingReference": {"InvoiceDocumentReference": {
                "ID": V(flow.numbers[key], "The invoice this payment settles."),
                "IssueDate": V(flow.numbers[f"{key}-date"], "Its issue date, so the reference is unambiguous.")}}},
    }


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


# ---------------------------------------------------------------- customs
def rate(a, b):
    """The world's reference exchange rate: units of b for one unit of a (world/countries.json)."""
    if a == b:
        return Decimal(1)
    r = WORLD["exchange_rates"]
    return Decimal(str(r[f"{a}/{b}"])) if f"{a}/{b}" in r else 1 / Decimal(str(r[f"{b}/{a}"]))


def goods_items(flow, currency, value_why):
    """GoodsItem per line of the deal: customs value (converted to `currency` at the reference rate if needed),
    gross weight, quantity and the item with its customs tariff code and origin."""
    which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
    out = []
    for i, d in enumerate(flow.deal, 1):
        it = ITEM[d["item"]]
        q = Decimal(str(d[which]))
        value = q * Decimal(str(it["price"]["amount"])) * rate(it["price"]["currency"], currency)
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What the goods are, in words."),
                    "DeclaredCustomsValueAmount": amount(value, currency, value_why),
                    "GrossWeightMeasure": qty(q * Decimal(str(it.get("gross_kg", 0))), "KGM",
                                              "The gross weight of the goods of this item."),
                    "Quantity": qty(q, it["unit"], "The quantity declared."),
                    "Item": item(d["item"])})
    return out


def export_declaration(flow, n, doc, day, why, value_why):
    cur = currency_of(doc["from"])
    return {"ID": V(flow.number("export", doc["from"], "ExportCustomsDeclaration"), "The exporter's reference."),
            "IssueDate": V(flow.date(day), why),
            "CustomsDeclaration": {
                "ID": V(flow.number("export-declaration", doc["from"], "CustomsDeclaration"),
                        "The declaration as lodged with the customs of the exporting country."),
                "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The shipment declared."),
                             "GrossWeightMeasure": qty(gross_weight(flow, "delivered" if any("delivered" in d for d in
                                                                                         flow.deal) else "ordered"),
                                                       "KGM", "The gross weight leaving the country."),
                             "GoodsItem": goods_items(flow, cur, value_why),
                             "Consignment": {"ID": V(flow.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment carried.")}}}}


def import_declaration(flow, n, doc, day, why, value_why, refs=None):
    cur = currency_of(doc["from"])
    which = "delivered" if any("delivered" in d for d in flow.deal) else "ordered"
    out = {"ID": V(flow.number("import", doc["from"], "ImportCustomsDeclaration"), "The importer's declaration number."),
           "IssueDate": V(flow.date(day), why),
           "Shipment": {"ID": V(flow.number("shipment", doc["from"], "Shipment"), "The shipment declared."),
                        "GrossWeightMeasure": qty(gross_weight(flow, which), "KGM", "The gross weight arriving."),
                        "GoodsItem": goods_items(flow, cur, value_why)}}
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
    rows = [(d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])),
                                               cur), tax_rule(seller, buyer, d["item"])) for d in rows_spec]
    base = sum(r[2] for r in rows)
    tax, total = tax_total(rows, cur)
    return {"ID": V(flow.number(f"credit-{n}", seller, "CreditNote"), "The seller's credit note number."),
            "IssueDate": V(flow.date(day), why),
            "CreditNoteTypeCode": V("381", "UN/EDIFACT 1001 code 381: credit note."),
            "DocumentCurrencyCode": currency_line(cur, "the currency of the invoice credited"),
            **refs,
            "TaxTotal": total,
            "LegalMonetaryTotal": monetary_total(base, tax, cur),
            "CreditNoteLine": [{"ID": V(str(i), "The line number."),
                                "CreditedQuantity": qty(q, ITEM[d["item"]]["unit"], d["why"]),
                                "LineExtensionAmount": amount(amt, cur, "Quantity times price, rounded to the minor unit."),
                                "Item": item(d["item"], tax_category(rule)),
                                "Price": price_block(d["item"])} for i, (d, q, amt, rule) in enumerate(rows, 1)]}


def catalogue(flow, n, doc, day, why, items, validity_days):
    return {"ID": V(flow.number("catalogue", doc["from"], "Catalogue"), "The provider's catalogue number."),
            "Name": V(f"{PARTY[doc['from']]['identity']['name']} catalogue", "The catalogue's title."),
            "IssueDate": V(flow.date(day), why),
            "ValidityPeriod": {"StartDate": V(flow.date(day), "The prices apply from the issue date."),
                               "EndDate": V(flow.date(day + validity_days), "Until the next catalogue.")},
            "CatalogueLine": [{"ID": V(str(i), "The line number."),
                               "Item": item(iid),
                               "RequiredItemLocationQuantity": {"Price": price_block(iid)}}
                              for i, iid in enumerate(items, 1)]}


def purchase_receipt(flow, n, doc, day, why, rows_spec, cash):
    seller, buyer = doc["from"], doc["to"]
    cur = currency_of(seller)
    rows = [(d, Decimal(str(d["qty"])), money(Decimal(str(d["qty"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])),
                                               cur), tax_rule(seller, buyer, d["item"])) for d in rows_spec]
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
                                     "LineExtensionAmount": amount(amt, cur, "Quantity times the shelf price, before "
                                                                             "the sales tax."),
                                     "Item": item(d["item"], tax_category(rule)),
                                     "Price": price_block(d["item"])} for i, (d, q, amt, rule) in enumerate(rows, 1)]}
