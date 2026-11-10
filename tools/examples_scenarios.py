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


# ---------------------------------------------------------------- the sea flow (Bayvarra -> Lisavu, CIF)
SEA = kit.Flow("sea", "2026-05-04", [
    {"item": "bench-serra-b", "ordered": 96, "why": "One 40-foot container: 24 pallets of 4 benches."},
    {"item": "bench-casting-b", "ordered": 12, "why": "Spare side frames for the buyer's own service stock."}])
CONTAINER = kit.container_number("TWL", 412087)       # Tidewell Ocean Lines' container (ISO 6346, with check digit)
SEA_FREIGHT, INSURANCE = Decimal("2950.00"), Decimal("140.00")


def cif_value(f):
    goods = sum(Decimal(str(d["ordered"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])) for d in f.deal)
    return goods + SEA_FREIGHT + INSURANCE


def container(f, gross_why):
    return {"TransportHandlingUnit": {"TransportEquipment": {
        "ID": V(CONTAINER, "The container's number: the owner code of the ocean carrier, U for a freight container, six "
                           "digits and the ISO 6346 check digit.", schemeID="ISO6346"),
        "GrossWeightMeasure": qty(kit.gross_weight(f, "ordered") + 3750, "KGM", gross_why),
        "TareWeightMeasure": qty(3750, "KGM", "The empty container's own weight, as marked on its door.")}}}


def sea(n, doc):
    f = SEA
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Catalogue":
        return kit.catalogue(f, n, doc, 0, "The export catalogue for the island customer.",
                             ["bench-serra-b", "bench-casting-b"], 180)
    if doc["doc"] == "DigitalAgreement":
        return {"ID": V(f.number("agreement", doc["from"], "DigitalAgreement"), "The agreement's number."),
                "IssueDate": V(f.date(1), "Signed before the first order."),
                "VersionID": V("1.0", "The first version of the agreement."),
                "DigitalProcess": [{"ID": V(p, "A process the parties agree to exchange electronically."),
                                    "Description": V(d, "What the process covers.")}
                                   for p, d in (("ordering", "Order, order response and order change."),
                                                ("billing", "Invoice, credit note, statement and remittance advice."))]}
    if doc["doc"] == "DigitalCapability":
        return {"ID": V(f.number("capability", doc["from"], "DigitalCapability"), "The governor's number."),
                "IssueDate": V(f.date(1), "Sent when the buyer joins the agreement."),
                "DigitalProcess": [{"ID": V(p, "A process the distributor supports."),
                                    "Description": V(d, "What it covers.")}
                                   for p, d in (("ordering", "Receives orders and order changes, sends order "
                                                             "responses."),
                                                ("billing", "Sends invoices and statements, receives remittance "
                                                            "advices."))]}
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 3, "The island buyer orders benches for its city's parks.",
                         "Cost, insurance and freight to the port of Selanu: the seller pays the sea freight and insures "
                         "the cargo; the risk passes when the goods are on board in Lumeport.", "Port of Selanu",
                         {"Delivery": {"DeliveryLocation": {"Description": V("Lanoro warehouse, Selanu",
                                                                             "The buyer's 3PL, where the goods go after "
                                                                             "customs clearance.")}}})
    if doc["doc"] == "OrderResponse":
        return kit.order_response(f, n, doc, 4, "The distributor accepts the order the next day.")
    if doc["doc"] == "ForwardingInstructions" and doc["from"] == "6-xb":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The distributor's "
                                                                                       "instruction number."),
                "IssueDate": V(f.date(5), "The distributor instructs its forwarder once the order is accepted."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the goods."),
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment to be shipped.")},
                             "InsurancePolicy": {
                                 "InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                              "CIF requires insurance of at least 110 % of the value; "
                                                              "the CIF value is the goods, freight and insurance."),
                                 "InsuranceTypeDescription": V("Cargo insurance, all risks", "The cover the forwarder "
                                                                                            "is to arrange.")}}}
    if doc["doc"] == "PackingList":
        return {"ID": V(f.number("packing", doc["from"], "PackingList"), "The distributor's packing list number."),
                "IssueDate": V(f.date(8), "Made when the container is packed."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment packed."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the goods."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")},
                             "GoodsItem": kit.goods_items(f, "XBL", "The value of the goods, in lume."),
                             **container(f, "The verified gross mass: cargo and the container's own weight of 3,750 "
                                            "kg.")}}
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 8, "The forwarder, as customs agent, declares the export at the "
                                                    "seaport.", "The value of the goods at export, in lume.")
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions-carrier", doc["from"], "ForwardingInstructions"),
                        "The forwarder's booking number with the ocean carrier."),
                "IssueDate": V(f.date(6), "The forwarder books the container."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the goods."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")}}}
    if doc["doc"] == "TransportationStatus" and doc["from"] == "16-xb":
        return kit.transportation_status(f, n, doc, 10, "Reported when the container is on board.",
                                         f"Container {CONTAINER} loaded on board.", "Port of Lumeport, container quay",
                                         {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The sea leg.")}}})
    if doc["doc"] == "BillOfLading":
        return {"ID": V(f.number("bl", doc["from"], "BillOfLading"), "The bill of lading number."),
                "IssueDate": V(f.date(10), "Issued when the goods are shipped on board."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment carried."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the cargo."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")},
                             "InsurancePolicy": {"InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                                              "The insured value, 110 % of the CIF "
                                                                              "value.")},
                             **container(f, "The container's gross mass as declared.")}}
    if doc["doc"] == "Manifest":
        return {"ID": V(f.number("manifest", doc["from"], "Manifest"), "The carrier's cargo manifest number."),
                "IssueDate": V(f.date(11), "Sent to the island's customs before arrival."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment on the manifest."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of this shipment.")}}
    if doc["doc"] == "CommonTransportationReport":
        return {"ID": V(f.number("ctr", doc["from"], "CommonTransportationReport"), "The carrier's report number."),
                "IssueDate": V(f.date(12), "Sent before the ship enters the port of Selanu."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment the report is for."),
                             "ShipmentStage": {"ID": V("1", "The sea leg to Selanu."),
                                               "ISPSRequirements": {
                                                   "ID": V("ISSC-XL-2026-0117", "The number of the ship's International "
                                                                                 "Ship Security Certificate."),
                                                   "ValidISSCIndicator": V("true", "The ship holds a valid security "
                                                                                   "certificate."),
                                                   "ISSCExpiryDate": V("2028-09-30", "The certificate is valid for five "
                                                                                     "years from its issue."),
                                                   "CurrentOperatingSecurityLevelCode": V("1", "Security level 1, the "
                                                                                              "normal level.")}}}}
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 14, "Reported when the container is discharged.",
                                         f"Container {CONTAINER} discharged and available for customs clearance.",
                                         "Port of Selanu", {"Consignment": {"MainCarriageShipmentStage": {
                                             "ID": V("1", "The sea leg.")}}})
    if doc["doc"] == "Invoice" and doc["from"] == "10-xb":
        return kit.invoice(f, n, doc, 15, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading.")}},
                           [{"item": "sea-freight", "qty": 1, "invoice_why": "One 40-foot container."},
                            {"item": "export-clearance", "qty": 1, "invoice_why": "One export declaration."},
                            {"item": "cargo-insurance", "qty": 1, "invoice_why": "Insurance of this shipment."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment shipped.")}}}})
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 15, "The customs broker declares the import for the buyer.",
                                      "The customs value in coral: the goods' value in lume at the world's reference "
                                      "rate (1 lume = 0.4 coral).",
                                      {"ID": V(f.numbers["bl"], "The bill of lading of the goods.")})
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 9, "Sent to the delivery party named in the order when the container "
                                                 "leaves.", "The gross weight of the goods.")
    if doc["doc"] == "ReceiptAdvice":
        return kit.receipt_advice(f, n, doc, 17, "The buyer's 3PL confirms what arrived.")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 10, 45, "Issued when the goods are on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
                           charges=[{"like": "bench-serra-b", "reason": "Sea freight", "amount": SEA_FREIGHT,
                                     "why": "Under CIF the seller pays the sea freight and charges it on the invoice.",
                                     "amount_why": "The freight the forwarder charged for the container."},
                                    {"like": "bench-serra-b", "reason": "Cargo insurance", "amount": INSURANCE,
                                     "why": "Under CIF the seller insures the cargo and charges the insurance.",
                                     "amount_why": "The premium of the cargo insurance."}])
    if doc["doc"] == "Statement":
        cur, total = "XBL", f.numbers["invoice-amount"]
        return {"ID": V(f.number("statement", doc["from"], "Statement"), "The factor's statement number."),
                "IssueDate": V(f.date(40), "The monthly statement of account."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the invoices"),
                "StatementLine": {"ID": V("1", "The open invoice."),
                                  "DebitLineAmount": amount(total, cur, "The amount of the invoice, owed to the factor."),
                                  "BalanceAmount": amount(total, cur, "Still open: nothing paid yet."),
                                  "BillingReference": {"InvoiceDocumentReference": {
                                      "ID": V(f.numbers["invoice"], "The distributor's invoice, which the factor "
                                                                    "bought."),
                                      "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}}}}
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 52, "The buyer pays the factor, before the due date.")
    raise SystemExit(f"sea scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the air flow (an urgent part, CPT airport)
AIR = kit.Flow("air", "2026-05-11", [
    {"item": "bench-casting-b", "ordered": 8, "why": "Eight side frames, needed before the ship arrives."}])


def air(n, doc):
    f = AIR
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "OrderChange":
        order = kit.order(f, n, doc, 0, "The buyer needs eight side frames urgently.",
                          "Carriage paid to the island's airport for the urgent frames: the distributor pays the air "
                          "freight; the rest of the order stays CIF by sea.", "Selanu airport, cargo terminal")
        for k in ("TaxTotal", "AnticipatedMonetaryTotal"):
            order.pop(k)
        return {**order, "ID": V(f.number("order-change", doc["from"], "OrderChange"), "The number of this change."),
                "SequenceNumberID": V("1", "The first change to the order."),
                "OrderReference": {"ID": V(SEA.numbers["order"], "The order of the sea flow that this change "
                                                                 "extends.")}}
    if doc["doc"] == "OrderResponse":
        out = kit.order_response(f, n, doc, 1, "The distributor accepts the change.")
        out["OrderReference"] = {"ID": V(f.numbers["order-change"], "The order change this response answers.")}
        return out
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The instruction number."),
                "IssueDate": V(f.date(1), "The distributor asks its forwarder to book air freight."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the eight boxed frames."),
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment.")}}}
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 2, "The air waybill, issued when the airline accepts the cargo.", w,
                           "The gross weight of the cargo.")
    if doc["doc"] == "TransportationStatus" and doc["from"] == "17-xb":
        return kit.transportation_status(f, n, doc, 2, "Reported when the cargo is built up for the flight.",
                                         "Cargo accepted and built up for the flight.", "Lumeport airport, cargo "
                                                                                        "terminal",
                                         {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The flight.")}}})
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 2, "Sent to the buyer's 3PL when the cargo leaves.",
                                   "The gross weight of the boxed frames.")
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 3, "Reported when the cargo has landed.",
                                         "Cargo arrived and ready for customs clearance.", "Selanu airport, cargo "
                                                                                          "terminal",
                                         {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The flight.")}}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 4, 30, "Issued after the flight.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The air waybill.")}},
                           [{"item": "air-freight", "qty": w, "invoice_why": "The chargeable weight: the gross weight "
                                                                             "of the boxed frames."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment flown.")}}}})
    raise SystemExit(f"air scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the cotton flow (Lisavu -> Bayvarra, FOB)
COTTON = kit.Flow("cotton", "2026-02-02", [
    {"item": "cotton-bale", "ordered": 6129, "why": "27 bales of about 227 kg: one container of lint."}])
SEED_KG = 18000


def cotton(n, doc):
    f = COTTON
    w = kit.gross_weight(f, "ordered")
    farm_rows = [{"item": "seed-cotton", "qty": SEED_KG, "why": "The weighed seed cotton of three trailer loads."}]
    if doc["doc"] == "Forecast":
        return {"ID": V(f.number("forecast", doc["from"], "Forecast"), "The mill's forecast number."),
                "IssueDate": V(f.date(0), "Sent at the start of the ginning season."),
                "IssueTime": V("09:00:00", "The time is stated, because a revision refers to the forecast by its issue "
                                           "date and time."),
                "ForecastPurposeCode": V("Order", "A forecast of what the mill will order, so the ginnery can plan."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The season's shipping period."),
                                   "EndDate": V(f.date(120), "Its end.")},
                "ForecastLine": {"ID": V("1", "The only line."),
                                 "ForecastTypeCode": V("Total", "The total expected purchase in the period."),
                                 "SalesItem": {"Quantity": qty(24000, "KGM", "About four containers of lint."),
                                               "Item": item("cotton-bale")}}}
    if doc["doc"] == "DeliveryNote":
        return {"ID": V(f.number("delivery", doc["from"], "DeliveryNote"), "The farm's delivery note number."),
                "IssueDate": V(f.date(3), "The day the trailers were weighed at the gin."),
                "DespatchLine": {"ID": V("1", "The only line."),
                                 "DeliveredQuantity": qty(SEED_KG, "KGM", "Weighed at the gin's weighbridge."),
                                 "OrderLineReference": {"LineID": V("1", "The line of the season agreement between farm "
                                                                         "and ginnery under which the cotton is "
                                                                         "delivered.")},
                                 "Item": item("seed-cotton")}}
    if doc["doc"] == "SelfBilledInvoice":
        return kit.self_billed(f, n, doc, 5, "The ginnery bills itself for the delivery, as the self-billing agreement "
                                             "provides.", farm_rows,
                               {"DespatchDocumentReference": {"ID": V(f.numbers["delivery"], "The farm's delivery "
                                                                                             "note.")}})
    if doc["doc"] == "SelfBilledCreditNote":
        return kit.self_billed(f, n, doc, 12, "Issued after classing showed part of the delivery a grade lower.",
                               [{"item": "seed-cotton", "qty": 2500, "unit_price": "0.030",
                                 "unit_price_why": "The price difference between the agreed grade and the lower grade, "
                                                   "per kilogram.", "why": "The part of the delivery classed lower."}],
                               {"BillingReference": {"SelfBilledInvoiceDocumentReference": {
                                   "ID": V(f.numbers["self-billed-3"], "The self-billed invoice this corrects."),
                                   "IssueDate": V(f.numbers["self-billed-3-date"], "Its issue date.")}}}, credit=True)
    if doc["doc"] == "RemittanceAdvice" and doc["from"] == "39-xl":
        inv, cn = f.numbers["self-billed-3-amount"], f.numbers["self-billed-4-amount"]
        return {"ID": V(f.number("remittance-farm", doc["from"], "RemittanceAdvice"), "The ginnery's remittance number."),
                "IssueDate": V(f.date(14), "The ginnery pays the farm after classing."),
                "DocumentCurrencyCode": kit.currency_line("XLC", "the island's currency"),
                "TotalPaymentAmount": amount(inv - cn, "XLC", "The invoice minus the credit note."),
                "PaymentMeans": {"PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer.",
                                                       listID="UN/EDIFACT EDED 4461"),
                                 "PayerFinancialAccount": kit.account("39-xl", "The ginnery's account."),
                                 "PayeeFinancialAccount": kit.account("38-xl", "The farm's account.")},
                "RemittanceAdviceLine": [
                    {"ID": V("1", "The self-billed invoice."),
                     "DebitLineAmount": amount(inv, "XLC", "The amount of the self-billed invoice."),
                     "BillingReference": {"SelfBilledInvoiceDocumentReference": {
                         "ID": V(f.numbers["self-billed-3"], "The self-billed invoice paid.")}}},
                    {"ID": V("2", "The self-billed credit note."),
                     "CreditLineAmount": amount(cn, "XLC", "The amount credited, deducted from the payment."),
                     "BillingReference": {"SelfBilledCreditNoteDocumentReference": {
                         "ID": V(f.numbers["self-billed-4"], "The self-billed credit note set off.")}}}]}
    if doc["doc"] == "ForecastRevision":
        return {"ID": V(f.number("forecast-revision", doc["from"], "ForecastRevision"), "The revision's number."),
                "IssueDate": V(f.date(20), "Demand for clothing has risen."),
                "SequenceNumberID": V("1", "The first revision of the forecast."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The same period."), "EndDate": V(f.date(120), "Its end.")},
                "ForecastRevisionLine": {"ID": V("1", "The only line."),
                                         "RevisedForecastLineID": V("1", "The forecast line revised."),
                                         "SourceForecastIssueDate": V(f.date(0), "The issue date of the forecast "
                                                                                 "revised."),
                                         "SourceForecastIssueTime": V("09:00:00", "Its issue time."),
                                         "SalesItem": {"Quantity": qty(30000, "KGM", "Raised to five containers."),
                                                       "Item": item("cotton-bale")}}}
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 22, "The mill orders the first container of the season.",
                         "Free on board at the port of Selanu: the buyer books and pays the sea freight; the risk "
                         "passes when the bales are on board.", "Port of Selanu")
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The mill's instruction "
                                                                                       "number."),
                "IssueDate": V(f.date(23), "Under FOB the buyer instructs the forwarder for the main carriage."),
                "Shipment": {"ID": V(f.number("shipment", "39-xl", "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the bales."),
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment.")}}}
    if doc["doc"] == "GoodsCertificate":
        return {"ID": V(f.number("goods-certificate", doc["from"], "GoodsCertificate"), "The chamber's certificate "
                                                                                       "number."),
                "IssueDate": V(f.date(26), "Issued before shipment, at the ginnery's application."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment certified."),
                             "GoodsItem": kit.goods_items(f, "XLC", "The value of the bales, in coral.")}}
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 27, "The island's export: declared before loading.",
                                      "The value of the bales, in coral.")
    if doc["doc"] == "WeightStatement":
        return {"ID": V(f.number("vgm", doc["from"], "WeightStatement"), "The shipper's weight statement number."),
                "IssueDate": V(f.date(27), "Declared before the container is loaded, as required for every packed "
                                           "container."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment weighed."),
                             "TransportHandlingUnit": {"TransportEquipment": {
                                 "ID": V(kit.container_number("TWL", 412311), "The container, with its ISO 6346 check "
                                                                              "digit.", schemeID="ISO6346"),
                                 "GrossWeightMeasure": qty(w + 3750, "KGM", "The verified gross mass: the bales and the "
                                                                            "container's own weight, weighed on the "
                                                                            "port's weighbridge."),
                                 "TareWeightMeasure": qty(3750, "KGM", "The empty container's own weight.")}}}}
    if doc["doc"] == "BillOfLading":
        return {"ID": V(f.number("bl", doc["from"], "BillOfLading"), "The bill of lading number."),
                "IssueDate": V(f.date(28), "Issued when the bales are on board."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment carried."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the bales."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")}}}
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 32, "The mill declares the bales in Bayvarra.",
                                      "The customs value in lume: the value in coral at the world's reference rate "
                                      "(1 lume = 0.4 coral, so 1 coral = 2.5 lume).",
                                      {"ID": V(f.numbers["bl"], "The bill of lading.")})
    if doc["doc"] == "Invoice" and doc["from"] == "10-xb":
        return kit.invoice(f, n, doc, 30, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading.")}},
                           [{"item": "sea-freight", "qty": 1, "invoice_why": "One 40-foot container, booked for the "
                                                                             "mill under FOB."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment shipped.")}}}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 28, 30, "Issued when the bales are on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The mill's order.")}})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 55, "The mill pays the ginnery: money flows to the island.")
    raise SystemExit(f"cotton scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"sea": sea, "air": air, "cotton": cotton})
