"""Scenarios of the example flows: what a flow adds to the world's layers.

A scenario gives, for the n-th document of a flow, the values that are not
in the world's layers: document numbers, dates, quantities, references and
the lines. The parties are placed by tools/build_examples.py from
world/documents.json; party, item and account content comes from the layers.
Every value carries its reason.
"""
from decimal import Decimal

from build_examples import ITEM, WORLD, V, account, amount, item, money, price, qty, tax_category

# ---------------------------------------------------------------- the ore flow (Urvania, domestic)
# One monthly call-off of ore: one train of 30 wagons, ordered as 1,800 tonnes, weighed at loading at
# 1,788.4 tonnes. Everything is invoiced on the weighed quantity. Ferra has no minor unit, so every
# amount to pay is a whole number of ferra, while the unit prices may be finer.
ORE = {
    "order": "VI-PO-26-0412", "tep_request": "VI-TR-26-0087", "tep": "FRC-TEP-26-1193",
    "consignment": "VI-CN-26-0412", "despatch": "SM-DA-26-0311", "shipment": "SM-SH-26-0311",
    "waybill": "FRC-WB-26-5521", "rail_invoice": "FRC-INV-26-2207", "ore_invoice": "SM-INV-26-0311",
    "remittance": "VI-RA-26-0398",
    "ordered": Decimal("1800"), "weighed": Decimal("1788.4"),
    # the standard rate of Urvania's value added tax, from the countries layer
    "vat": Decimal(str(WORLD["countries"]["XU"]["tax"]["schemes"][0]["rates"]["standard"])),
}
CUR = "XUF"
VAT_WHY = ("A domestic supply in Urvania: Urvania's value added tax applies at the standard rate. "
           "UN/EDIFACT 5305 code S, standard rate.")


def vat(base, why):
    """TaxTotal with one standard-rate subtotal; the tax is rounded to whole ferra."""
    tax = money(base * ORE["vat"] / 100, CUR)
    return tax, {"TaxAmount": amount(tax, CUR, f"{why} Rounded to whole ferra, which have no minor unit."),
                 "TaxSubtotal": {
                     "TaxableAmount": amount(base, CUR, "The sum of the line amounts at the standard rate."),
                     "TaxAmount": amount(tax, CUR, f"{ORE['vat']} % of the taxable amount, rounded to whole ferra."),
                     "TaxCategory": tax_category("S", ORE["vat"], VAT_WHY)}}


def invoice(n, number, date, due, iid, refs, why_line):
    it = ITEM[iid]
    base = money(ORE["weighed"] * Decimal(str(it["price"]["amount"])), CUR)
    tax, total = vat(base, "The value added tax of the invoice.")
    seller = it["seller"]
    content = {
        "ID": V(number, "The seller's invoice number."),
        "IssueDate": V(date, "Issued the day after the goods were despatched and weighed."),
        "DueDate": V(due, "Thirty days after the issue date, the payment term of the world's domestic trade."),
        "InvoiceTypeCode": V("380", "UN/EDIFACT 1001 code 380: commercial invoice."),
        "DocumentCurrencyCode": V(CUR, "The ferra, the seller's currency, in the world's currency code list."),
        **refs,
        "PaymentMeans": {
            "PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer, how businesses in Urvania pay. The listID "
                                  "is the identification of UBL's payment means code list, which code list validation "
                                  "checks.",
                                  listID="UN/EDIFACT EDED 4461"),
            "PayeeFinancialAccount": account(seller, "The seller's account, where the buyer is to pay.")},
        "TaxTotal": total,
        "LegalMonetaryTotal": {
            "LineExtensionAmount": amount(base, CUR, "The sum of the line amounts."),
            "TaxExclusiveAmount": amount(base, CUR, "The total without tax: the sum of the line amounts, no allowances "
                                                    "or charges."),
            "TaxInclusiveAmount": amount(base + tax, CUR, "The total without tax plus the value added tax."),
            "PayableAmount": amount(base + tax, CUR, "What the buyer is to pay; stated, not left to be calculated "
                                                     "(UBL 2.5, 2.2.2 Manifest Values).")},
        "InvoiceLine": {
            "ID": V("1", "The first and only line."),
            "InvoicedQuantity": qty(ORE["weighed"], it["unit"], why_line),
            "LineExtensionAmount": amount(base, CUR, f"{ORE['weighed']} × {it['price']['amount']} ferra, rounded to "
                                                     "whole ferra."),
            "Item": item(iid, tax_category("S", ORE["vat"], VAT_WHY)),
            "Price": {"PriceAmount": price(it["price"]["amount"], CUR, "The seller's price per unit "
                                                                       "(world/items.json)."),
                      "BaseQuantity": qty(1, it["unit"], "The price is per one unit.")}},
    }
    return content


def ore(n, doc):
    o = ORE
    if doc["doc"] == "Order":
        it = ITEM["ore-lump"]
        base = money(o["ordered"] * Decimal(str(it["price"]["amount"])), CUR)
        tax, total = vat(base, "The value added tax the buyer expects to pay.")
        return {
            "ID": V(o["order"], "The buyer's order number."),
            "IssueDate": V("2026-03-02", "The first working day of the month: the monthly ore call-off."),
            "Note": V("Monthly call-off, one train.", "Says in words what the order is for."),
            "DocumentCurrencyCode": V(CUR, "The ferra, the currency of the domestic trade in Urvania."),
            "Delivery": {
                "RequestedDeliveryPeriod": {
                    "StartDate": V("2026-03-09", "The week in which the factory wants the ore."),
                    "EndDate": V("2026-03-13", "The end of that week.")}},
            "DeliveryTerms": {
                "ID": V("FCA", "Free carrier at the mine: the buyer arranges and pays the main transport, so the order "
                               "names the carrier the buyer has booked. Stated, because leaving it out would carry no "
                               "meaning (UBL rule IND6).", schemeID="INCOTERMS"),
                "DeliveryLocation": {"Description": V("Mine siding, Serravona", "Where the seller hands the ore to "
                                                                                "the carrier under FCA.")}},
            "TaxTotal": total,
            "AnticipatedMonetaryTotal": {
                "LineExtensionAmount": amount(base, CUR, f"{o['ordered']} tonnes × {it['price']['amount']} ferra."),
                "PayableAmount": amount(base + tax, CUR, "What the buyer expects to pay, value added tax included.")},
            "OrderLine": {"LineItem": {
                "ID": V("1", "The first and only line."),
                "Quantity": qty(o["ordered"], "TNE", "One train: 30 wagons of about 60 tonnes. Tonne is UN/ECE Rec 20 "
                                                     "code TNE."),
                "LineExtensionAmount": amount(base, CUR, "Quantity times price."),
                "Price": {"PriceAmount": price(it["price"]["amount"], CUR, "The mine's price per tonne "
                                                                           "(world/items.json)."),
                          "BaseQuantity": qty(1, "TNE", "The price is per tonne.")},
                "Item": item("ore-lump")}},
        }
    if doc["doc"] == "TransportExecutionPlanRequest":
        return {
            "ID": V(o["tep_request"], "The transport user's request number."),
            "IssueDate": V("2026-03-03", "The day after the order: the buyer books the train it named in its order."),
            "ServiceStartTimePeriod": {"StartDate": V("2026-03-10", "The day the ore should be loaded at the mine.")},
            "Consignment": {
                "ID": V(o["consignment"], "The buyer's number for this consignment, quoted along the chain."),
                "GrossWeightMeasure": qty(o["ordered"], "TNE", "The expected weight: the ordered quantity.")},
        }
    if doc["doc"] == "TransportExecutionPlan":
        return {
            "ID": V(o["tep"], "The rail carrier's number for the agreed plan."),
            "IssueDate": V("2026-03-04", "The day after the request."),
            "DocumentStatusCode": V("Confirmed", "The carrier confirms the plan as requested. A value of UBL's document status "
                                                 "code list (2.1: Document has been confirmed)."),
            "TransportExecutionPlanRequestDocumentReference": {
                "ID": V(o["tep_request"], "The request this plan answers.")},
            "ServiceStartTimePeriod": {"StartDate": V("2026-03-10", "Loading at the mine, as requested.")},
            "Consignment": {
                "ID": V(o["consignment"], "The consignment of the request."),
                "GrossWeightMeasure": qty(o["ordered"], "TNE", "The weight the plan is made for.")},
        }
    if doc["doc"] == "DespatchAdvice":
        return {
            "ID": V(o["despatch"], "The mine's despatch advice number."),
            "IssueDate": V("2026-03-10", "The day the train was loaded and weighed."),
            "OrderReference": {"ID": V(o["order"], "The order this despatch fulfils.")},
            "Shipment": {
                "ID": V(o["shipment"], "The mine's number for the shipment."),
                "GrossWeightMeasure": qty(o["weighed"], "TNE", "Weighed on the weighbridge at loading: 30 wagons."),
                "Consignment": {"ID": V(o["consignment"], "The buyer's consignment, quoted back.")}},
            "DespatchLine": {
                "ID": V("1", "The first and only line."),
                "DeliveredQuantity": qty(o["weighed"], "TNE", "What was loaded, weighed; slightly less than ordered, "
                                                              "as with every bulk load."),
                "OrderLineReference": {"LineID": V("1", "The order line this line fulfils.")},
                "Item": item("ore-lump")},
        }
    if doc["doc"] == "Waybill":
        return {
            "ID": V(o["waybill"], "The rail consignment note number."),
            "IssueDate": V("2026-03-10", "Issued when the carrier takes over the loaded train."),
            "Shipment": {
                "ID": V(o["shipment"], "The shipment as the mine numbered it."),
                "GrossWeightMeasure": qty(o["weighed"], "TNE", "The weight the carrier takes over, from the weighbridge."),
                "Consignment": {"ID": V(o["consignment"], "The consignment of the transport plan.")}},
            "DocumentReference": {"ID": V(o["tep"], "The transport plan under which the carriage is performed.")},
        }
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        return invoice(n, o["rail_invoice"], "2026-03-12", "2026-04-11", "rail-ore",
                       {"AdditionalDocumentReference": [
                           {"ID": V(o["tep"], "The transport plan with the agreed price.")},
                           {"ID": V(o["waybill"], "The consignment note of the carriage invoiced.")}]},
                       "The weight carried, from the consignment note: the freight is per tonne.")
    if doc["doc"] == "Invoice":
        return invoice(n, o["ore_invoice"], "2026-03-11", "2026-04-10", "ore-lump",
                       {"OrderReference": {"ID": V(o["order"], "The buyer's order.")},
                        "DespatchDocumentReference": {"ID": V(o["despatch"], "The despatch advice of the goods invoiced.")}},
                       "The weighed quantity from the despatch advice, not the ordered quantity.")
    if doc["doc"] == "RemittanceAdvice":
        it = ITEM["ore-lump"]
        base = money(o["weighed"] * Decimal(str(it["price"]["amount"])), CUR)
        paid = base + money(base * o["vat"] / 100, CUR)
        return {
            "ID": V(o["remittance"], "The buyer's remittance number."),
            "IssueDate": V("2026-04-09", "The day the payment is made, one day before the due date."),
            "DocumentCurrencyCode": V(CUR, "The ferra."),
            "TotalPaymentAmount": amount(paid, CUR, "The amount transferred: the payable amount of the invoice."),
            "PaymentMeans": {
                "PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer.", listID="UN/EDIFACT EDED 4461"),
                "PayerFinancialAccount": account("5-xu", "The account the manufacturer pays from."),
                "PayeeFinancialAccount": account("4-xu", "The mine's account, as stated on its invoice.")},
            "RemittanceAdviceLine": {
                "ID": V("1", "One invoice paid."),
                "DebitLineAmount": amount(paid, CUR, "The amount of the invoice that this payment settles: the whole "
                                                     "payable amount. The line amounts of a remittance advice are debits "
                                                     "for invoices, as in the OASIS example UBL-RemittanceAdvice-2.0-Example."),
                "BillingReference": {"InvoiceDocumentReference": {
                    "ID": V(o["ore_invoice"], "The invoice this payment settles."),
                    "IssueDate": V("2026-03-11", "The issue date of that invoice, so the reference is unambiguous.")}}},
        }
    raise SystemExit(f"ore scenario: no document {n} {doc['doc']}")


SCENARIOS = {"ore": ore}
