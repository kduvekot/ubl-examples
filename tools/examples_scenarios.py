"""Scenarios of the example flows: what a flow adds to the world's layers.

Per flow: its start date, its deal (the items and quantities it is about) and,
per document, the day it is issued and what is particular to it, each value with
its reason. The parties are placed by tools/build_examples.py from
world/documents.json; party, item and account content comes from the layers;
lines, amounts and taxes are worked out by tools/examples_kit.py.
"""
from decimal import Decimal

import examples_kit as kit
from build_examples import ITEM, PARTY, WORLD, V, amount, item, money, party, qty


def rate(a, b):
    """The world's reference exchange rate: units of b for one unit of a (world/countries.json)."""
    return Decimal(str(WORLD["exchange_rates"][f"{a}/{b}"]))


# ---------------------------------------------------------------- the ore flow (Urvania, domestic)
ORE = kit.Flow("ore", "2026-03-02", [
    {"item": "ore-lump", "ordered": 1800, "delivered": "1788.4",
     "why": "One train: 30 wagons of about 60 tonnes.",
     "invoice_why": "The weighed quantity from the despatch advice, not the ordered quantity."}])


def ore(n, doc):
    f = ORE
    weighed_kg = Decimal("1788.4") * 1000
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The first working day of the month: the monthly ore call-off.",
                         "Free carrier at the mine: the buyer arranges and pays the main transport, so the order names "
                         "the carrier the buyer has booked. Stated, because leaving it out would carry no meaning "
                         "(UBL rule IND6).", "Mine siding, Serravona",
                         {"Note": V("Monthly call-off, one train.", "Says in words what the order is for."),
                          "Delivery": {"RequestedDeliveryPeriod": {
                              "StartDate": V(f.date(7), "The week in which the factory wants the ore."),
                              "EndDate": V(f.date(11), "The end of that week.")}}})
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 1, "The day after the order: the buyer books the train it named in its order.",
                               8, 1800000, "The expected weight: the ordered quantity.")
    if doc["doc"] == "TransportExecutionPlan":
        return kit.tep(f, n, doc, 2, "The day after the request.", 8, 1800000)
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 8, "The day the train was loaded and weighed.",
                                   "Weighed on the weighbridge at loading: 30 wagons.",
                                   {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                         "The buyer's consignment, quoted back.")}}})
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 8, "Issued when the carrier takes over the loaded train.", weighed_kg,
                           "The weight the carrier takes over, from the weighbridge.")
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        return kit.invoice(f, n, doc, 10, 30, "Issued after the carriage was performed.",
                           {"AdditionalDocumentReference": [
                               {"ID": V(f.numbers["tep"], "The transport plan with the agreed price.")},
                               {"ID": V(f.numbers["waybill"], "The consignment note of the carriage invoiced.")}]},
                           [{"item": "rail-ore", "qty": "1788.4",
                             "invoice_why": "The weight carried, from the consignment note: the freight is per tonne."}],
                           key="freight-invoice")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 9, 30, "Issued the day after the goods were despatched and weighed.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"],
                                                                  "The despatch advice of the goods invoiced.")}})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 38, "The day the payment is made, one day before the due date.")
    raise SystemExit(f"ore scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the road flow (Urvania -> Bayvarra)
ROAD = kit.Flow("road", "2026-03-16", [
    {"item": "bench-serra", "ordered": 96, "why": "24 pallets of 4 benches: one full truck."},
    {"item": "bench-casting", "ordered": 12, "why": "Spare side frames, for the distributor's service stock."}])
DISTANCE_KM = 186     # the carrier's route from the 3PL in Ferrano to the distributor in Marrowdale


def goods_items(f, currency, value_why, convert=None):
    """GoodsItem per line of the deal, with the customs value and the item (HS code, origin)."""
    out = []
    for i, d in enumerate(f.deal, 1):
        it = ITEM[d["item"]]
        value = Decimal(str(d["ordered"])) * Decimal(str(it["price"]["amount"]))
        if convert:
            value = value * rate(it["price"]["currency"], currency)
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What the goods are, in words."),
                    "DeclaredCustomsValueAmount": amount(value, currency, value_why),
                    "GrossWeightMeasure": qty(Decimal(str(d["ordered"])) * Decimal(str(it["gross_kg"])), "KGM",
                                              "The gross weight of the goods of this item."),
                    "Quantity": qty(d["ordered"], it["unit"], "The quantity declared."),
                    "Item": item(d["item"])})
    return out


def road(n, doc):
    f = ROAD
    weight = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The distributor orders for its spring stock.",
                         "Free carrier at the seller's warehouse: the buyer arranges and pays the main transport, so the "
                         "order names the warehouse where the goods are collected and the carrier that collects them "
                         "(UBL rule IND6: the delivery terms are stated, not implied).",
                         "Castrano Logistics warehouse, Ferrano")
    if doc["doc"] == "OrderResponse":
        return kit.order_response(f, n, doc, 1, "The manufacturer answers the next day.")
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 1, "The distributor books the truck once the order is accepted.", 7, weight,
                               "The gross weight of the order: benches and castings with their packaging.")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 7, "The day the 3PL loaded the truck.",
                                   "The gross weight loaded, packaging included.",
                                   {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                         "The distributor's consignment for the truck.")}}})
    if doc["doc"] == "ExportCustomsDeclaration":
        return {"ID": V(f.number("export", doc["from"], "ExportCustomsDeclaration"), "The exporter's reference."),
                "IssueDate": V(f.date(7), "Declared the day the goods leave the warehouse for the border."),
                "CustomsDeclaration": {
                    "ID": V(f.number("export-declaration", doc["from"], "CustomsDeclaration"),
                            "The declaration as lodged with Urvania's customs."),
                    "Shipment": {"ID": V(f.numbers["shipment"], "The shipment of the despatch advice."),
                                 "GrossWeightMeasure": qty(weight, "KGM", "The gross weight leaving the country."),
                                 "GoodsItem": goods_items(f, "XUF", "The value at the frontier: the invoice value, in "
                                                                     "ferra."),
                                 "Consignment": {"ID": V(f.numbers["consignment"], "The consignment of the truck.")}}}}
    if doc["doc"] == "CertificateOfOrigin":
        chamber, exporter = "20-xu", "5-xu"
        endorsed = doc["from"] == chamber
        signer = {"RoleCode": V("Chamber", "The endorser is the chamber of commerce of the exporting country."),
                  "SequenceNumeric": V("1", "The first and only endorsement."),
                  "Party": party(chamber),
                  "SignatoryContact": {"Name": V("Certificates office", "The office of the chamber that signs "
                                                 "certificates of origin.")}}
        return {
            "EndorserParty": {k: v for k, v in signer.items() if k != "Party"},
            "ID": V(f.number("certificate", chamber, "CertificateOfOrigin"), "The number of the certificate, given by "
                                                                            "the chamber."),
            "IssueDate": V(f.date(6 if endorsed else 4), "The day the chamber endorsed the certificate." if endorsed
                           else "The day the exporter applies, before the goods leave."),
            "Description": V("Certificate of origin for park benches and castings made in Urvania.",
                             "What the certificate is for."),
            "CertificateOfOriginApplication": {
                "ReferenceID": V(f.number("certificate-application", exporter, "Application"),
                                 "The exporter's reference for its application."),
                "CertificateType": V("Preferential", "The goods qualify for the preferential duty rate in Bayvarra; "
                                                     "the importer needs this certificate to claim it."),
                "ApplicationStatusCode": V("Approved" if endorsed else "Submitted",
                                           "The chamber has approved the application." if endorsed
                                           else "The exporter submits the application."),
                "OriginalJobID": V(f.numbers["order"], "The order the goods are for."),
                "Shipment": {"ID": V(f.number("shipment", "8-xu", "Shipment"), "The shipment the certificate covers."),
                             "GoodsItem": goods_items(f, "XUF", "The value of the goods, in ferra.")},
                "EndorserParty": signer,
                "PreparationParty": party(exporter),
                "IssuerParty": party(chamber),
                "IssuingCountry": {"IdentificationCode": V("XU", "The goods were made in Urvania, and the certificate is "
                                                                 "issued there.")}},
            "IssuerEndorsement": {
                "DocumentID": V(f.numbers["certificate"], "The certificate this endorsement belongs to."),
                "ApprovalStatus": V("Approved" if endorsed else "Pending", "The chamber has endorsed the certificate."
                                    if endorsed else "Not yet endorsed: the application is with the chamber."),
                "EndorserParty": signer}}
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 7, "Issued when the carrier collects the goods at the warehouse.", weight,
                           "The gross weight the carrier takes over.")
    if doc["doc"] == "TransportationStatus":
        return {"ID": V(f.number("status", doc["from"], "TransportationStatus"), "The carrier's status report number."),
                "IssueDate": V(f.date(8), "The morning after collection, when the truck has crossed the border."),
                "TransportEvent": {
                    "OccurrenceDate": V(f.date(8), "The day the truck crossed the land border."),
                    "Description": V("Border crossing passed; customs cleared on both sides.",
                                     "What happened, in words."),
                    "Location": {"Name": V("Land border crossing Urvania–Bayvarra",
                                           "The road border crossing between the customs posts of both countries.")}},
                "Consignment": {"ID": V(f.numbers["consignment"], "The consignment the report is about.")}}
    if doc["doc"] == "ImportCustomsDeclaration":
        return {"ID": V(f.number("import", doc["from"], "ImportCustomsDeclaration"), "The importer's declaration "
                                                                                    "number."),
                "IssueDate": V(f.date(8), "Declared when the goods arrive in Bayvarra."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment of the despatch advice."),
                             "GrossWeightMeasure": qty(weight, "KGM", "The gross weight arriving."),
                             "GoodsItem": goods_items(f, "XBL", "The customs value in lume, Bayvarra's currency: the "
                                                                "invoice value in ferra at the world's reference rate "
                                                                "(1 ferra = 0.01 lume).", convert=True)},
                "AdditionalDocumentReference": {"ID": V(f.numbers["certificate"], "The certificate of origin, to claim "
                                                                                  "the preferential duty rate.")}}
    if doc["doc"] == "ReceiptAdvice":
        return kit.receipt_advice(f, n, doc, 9, "The day the truck was unloaded at the distribution centre.")
    if doc["doc"] == "Invoice" and doc["from"] == "13-xu":
        return kit.invoice(f, n, doc, 9, 30, "Issued after delivery.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note of the "
                                                                                          "carriage invoiced.")}},
                           [{"item": "road-transport", "qty": DISTANCE_KM,
                             "invoice_why": "The kilometres driven loaded, from Ferrano to Marrowdale."}],
                           key="freight-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {
                               "ID": V(f.numbers["consignment"], "The consignment carried, as the distributor numbered "
                                                                 "it when booking the truck.")}}}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 8, 30, "Issued when the goods have left the warehouse.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice of the "
                                                                                         "goods invoiced.")}})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 37, "The day the payment is made across the border, before the due date.")
    raise SystemExit(f"road scenario: no document {n} {doc['doc']}")


SCENARIOS = {"ore": ore, "road": road}


# ---------------------------------------------------------------- the rail flow (Urvania -> Bayvarra, DAP, transit)
RAIL = kit.Flow("rail", "2026-04-06", [
    {"item": "bench-serra", "ordered": 192, "why": "Two containers of 24 pallets, 4 benches on each pallet."}])


def rail(n, doc):
    f = RAIL
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "Full container loads for the summer season.",
                         "Delivered at place, the distributor's rail siding: the seller arranges and pays the carriage, "
                         "so the order names no carrier (UBL rule IND6: the terms say who transports, not a missing "
                         "carrier).", "Rail siding of Lumeway Distribution, Marrowdale")
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 1, "Under DAP the manufacturer is the transport user and books the train.",
                               8, w, "Two containers of benches.")
    if doc["doc"] == "TransportExecutionPlan":
        return kit.tep(f, n, doc, 2, "The rail carrier confirms the slots on the container train.", 8, w)
    if doc["doc"] == "TransitCustomsDeclaration":
        return {"ID": V(f.number("transit", doc["from"], "TransitCustomsDeclaration"), "The transit declaration "
                                                                                       "number."),
                "IssueDate": V(f.date(8), "Lodged at the office of departure before the train leaves."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment under transit."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight under transit."),
                             "GoodsItem": kit.goods_items(f, "XUF", "The value of the goods, in ferra, for the transit "
                                                                    "guarantee."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment on the train.")}}}
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 8, "Reported when the containers are on the train.",
                                         "Two containers loaded on the container train.",
                                         "Ferrano Intermodal Hub",
                                         {"Consignment": {"MainCarriageShipmentStage": {
                                             "ID": V("1", "The main carriage, by rail.")}}})
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 8, "Issued when the carrier takes over the containers.", w,
                           "The gross weight of the two containers' cargo.")
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        return kit.invoice(f, n, doc, 11, 30, "Issued after delivery at the siding.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "rail-container", "qty": 2, "invoice_why": "Two container slots."}],
                           key="freight-invoice")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 11, 30, "Issued on delivery at the distributor's siding.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
                           extra={"Note": V("Delivered at place: the price includes the carriage to the siding.",
                                            "Why the invoice has no separate freight line.")})
    raise SystemExit(f"rail scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the plastics flow (Urvania -> Bayvarra, barge, CPT)
PLASTICS = kit.Flow("plastics", "2026-04-13", [
    {"item": "granulate-pe", "ordered": 120, "why": "One barge load of recycled granulate in jumbo bags."}])


def plastics(n, doc):
    f = PLASTICS
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The packaging maker orders for the next production run.",
                         "Carriage paid to the river quay: the seller books and pays the barge, the buyer bears the "
                         "risk once the goods are on board.", "River quay, Lumeport")
    if doc["doc"] == "OrderResponse":
        return kit.order_response(f, n, doc, 1, "The waste processor confirms the lot.")
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 1, "Under CPT the seller is the transport user and books the barge.", 6, w,
                               "120 jumbo bags of one tonne, with their bags.")
    if doc["doc"] == "TransportExecutionPlan":
        return kit.tep(f, n, doc, 2, "The barge operator confirms the sailing.", 6, w)
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 6, "Declared the day the barge is loaded.",
                                      "The value of the granulate, in ferra.")
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 6, "Issued when the barge is loaded.", w, "The gross weight on board.")
    if doc["doc"] == "Invoice" and doc["from"] == "15-xu":
        return kit.invoice(f, n, doc, 9, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "barge-freight", "qty": 120, "invoice_why": "The tonnes carried."}],
                           key="freight-invoice")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 6, "The day the barge was loaded.", "The gross weight loaded.")
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 9, "Declared when the barge arrives at the coast.",
                                      "The customs value in lume: the invoice value in ferra at the world's reference "
                                      "rate (1 ferra = 0.01 lume).")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 7, 30, "Issued once the granulate is on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}},
                           extra={"Note": V("Carriage paid to: the price includes the barge to the river quay.",
                                            "Why the invoice has no separate freight line.")})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 36, "The packaging maker pays across the border, before the due date.")
    raise SystemExit(f"plastics scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the retail flow (Bayvarra, DDP)
RETAIL = kit.Flow("retail", "2026-04-20", [
    {"item": "bench-serra-b", "ordered": 24, "why": "Six pallets for the garden department's spring promotion.",
     "received": 23, "received_why": "One bench arrived in a damaged carton and was refused."}])


def retail(n, doc):
    f = RETAIL
    w = kit.gross_weight(f, "ordered")
    store = {"Name": V("Garden department", "The department of the store that sells the benches.")}
    if doc["doc"] == "Catalogue":
        return kit.catalogue(f, n, doc, 0, "The spring catalogue for the store.", ["bench-serra-b", "bench-casting-b"], 90)
    if doc["doc"] == "Forecast":
        return {"ID": V(f.number("forecast", doc["from"], "Forecast"), "The store's forecast number."),
                "IssueDate": V(f.date(2), "Sent after the catalogue arrived."),
                "ForecastPurposeCode": V("Sales", "A forecast of the store's sales, so the distributor can plan its "
                                                  "stock."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The forecast covers the next six weeks."),
                                   "EndDate": V(f.date(56), "The end of the forecast period.")},
                "ForecastLine": {"ID": V("1", "The first and only line."),
                                 "ForecastTypeCode": V("Total", "The total expected sales of the item in the period."),
                                 "SalesItem": {"Quantity": qty(40, "H87", "Forty benches over six weeks, promotion "
                                                                          "included."),
                                               "Item": item("bench-serra-b")}}}
    if doc["doc"] == "RetailEvent":
        return {"ID": V(f.number("event", doc["from"], "RetailEvent"), "The store's event number."),
                "IssueDate": V(f.date(2), "Announced with the forecast."),
                "RetailEventName": V("Spring garden promotion", "The name of the promotion."),
                "RetailEventStatusCode": V("Confirmed", "The promotion is decided, not only planned."),
                "Description": V("Ten per cent off garden furniture for two weeks.", "What the promotion is."),
                "Period": {"StartDate": V(f.date(21), "The promotion starts in three weeks."),
                           "EndDate": V(f.date(34), "It lasts two weeks.")}}
    if doc["doc"] == "InventoryReport":
        return {"ID": V(f.number("inventory", doc["from"], "InventoryReport"), "The store's inventory report number."),
                "IssueDate": V(f.date(3), "The weekly stock report."),
                "InventoryReportLine": {"ID": V("1", "The first and only line."),
                                        "Quantity": qty(3, "H87", "Three benches left in the garden department."),
                                        "Item": item("bench-serra-b")}}
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 4, "The store replenishes before the promotion.",
                         "Delivered duty paid at the store: the distributor arranges and pays the transport and every "
                         "cost, so the order names only where to deliver.", "Brightmarket Stores, goods-in, Lumeport",
                         {"Delivery": {"DeliveryLocation": {"Description": V("Goods-in, garden department",
                                                                             "Where the truck unloads.")}}})
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 5, "Because it sold delivered duty paid, the distributor books the truck.", 9,
                               w, "Six pallets of benches.")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 9, "The day the truck was loaded at the distribution centre.",
                                   "The gross weight loaded.")
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 9, "Issued when the carrier collects at the distribution centre.", w,
                           "The gross weight taken over.")
    if doc["doc"] == "Invoice" and doc["from"] == "13-xu":
        return kit.invoice(f, n, doc, 10, 30, "Issued after delivery.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "road-transport", "qty": 38, "invoice_why": "The kilometres from Marrowdale to the "
                                                                                 "store in Lumeport."}],
                           key="freight-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment carried.")}}}})
    if doc["doc"] == "ReceiptAdvice":
        return kit.receipt_advice(f, n, doc, 10, "The day the goods were unloaded at the store.")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 10, 30, "Issued on delivery.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The store's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}},
                           [{"item": "bench-serra-b", "qty": 24, "invoice_why": "The benches despatched."}])
    if doc["doc"] == "CreditNote":
        return kit.credit_note(f, n, doc, 12, "Issued after the receipt advice reported the refused bench.",
                               [{"item": "bench-serra-b", "qty": 1, "why": "The bench refused at delivery."}],
                               {"BillingReference": {"InvoiceDocumentReference": {
                                   "ID": V(f.numbers["invoice"], "The invoice this credit note corrects."),
                                   "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}},
                                "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The receipt advice that "
                                                                                           "reported the damage.")}})
    if doc["doc"] == "PurchaseReceipt":
        return kit.purchase_receipt(f, n, doc, 25, "A consumer buys a bench during the promotion week.",
                                    [{"item": "bench-serra-r", "qty": 1, "why": "One bench."}], cash=True)
    raise SystemExit(f"retail scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"rail": rail, "plastics": plastics, "retail": retail})
