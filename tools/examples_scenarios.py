"""Scenarios of the example flows: what a flow adds to the world's layers.

Per flow: its start date, its deal (the items and quantities it is about) and,
per document, the day it is issued and what is particular to it, each value with
its reason. The parties are placed by tools/build_examples.py from
world/documents.json; party, item and account content comes from the layers;
lines, amounts and taxes are worked out by tools/examples_kit.py.
"""
from decimal import Decimal

import examples_kit as kit
from build_examples import ITEM, PARTY, WORLD, V, amount, item, money, party, price, qty


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
        out = kit.import_declaration(f, n, doc, 15, "The customs broker declares the import for the buyer.",
                                      "The customs value in coral: the goods' value in lume at the world's reference "
                                      "rate (1 lume = 0.4 coral).",
                                      {"ID": V(f.numbers["bl"], "The bill of lading of the goods.")})
        out["ImporterParty"] = {
            "AgentParty": party("3-xl", short=True),
            "PowerOfAttorney": {"ID": V("POA-TT-2026-014", "The number of the power of attorney the buyer gave its "
                                                           "customs broker."),
                                "IssueDate": V("2026-01-05", "Given at the start of the year, for all of the year's "
                                                             "imports."),
                                "Description": V("Lodging import declarations and paying duties and taxes on behalf of "
                                                 "Velumi Trading.", "What the broker may do for the buyer."),
                                "AgentParty": party("3-xl", short=True),
                                "MandateDocumentReference": {"ID": V("MAND-2026-014", "The signed mandate kept by the "
                                                                                      "broker.")}}}
        return out
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


def ref(f, key, why):
    return {"ID": V(f.numbers[key], why)}


def period(f, start, end, why_start, why_end):
    return {"StartDate": V(f.date(start), why_start), "EndDate": V(f.date(end), why_end)}


# ---------------------------------------------------------------- the tender flow (Bayvarra, public procurement)
TENDER = kit.Flow("tender", "2026-01-12", [
    {"item": "bench-serra", "ordered": 40, "why": "The first call-off under the contract: forty benches for the "
                                                  "harbour park."}])
FOLDER = "PWD-2026-PARKS"
TENDER_QTY = 240


def tender(n, doc):
    f = TENDER
    folder = {"ContractFolderID": V(FOLDER, "The authority's file number for this procurement, the same on every "
                                            "document of the procedure.")}
    project = {"ProcurementProject": {
        "Name": V("Park benches for the city parks", "The name of the procurement project."),
        "Description": V(f"{TENDER_QTY} park benches with steel frames and hardwood slats over three years, ordered in "
                         "call-offs.", "What the authority buys."),
        "RequestedTenderTotal": {"EstimatedOverallContractAmount": amount(120000, "XBL", "The authority's estimate of "
                                                                                         "the contract value, in lume.")}}}
    appeal_why = "The independent review body for appeals and mediation in public procurement."
    if doc["doc"] == "PriorInformationNotice":
        return {"ID": V(f.number("pin", doc["from"], "PriorInformationNotice"), "The notice number."),
                "IssueDate": V(f.date(0), "Published early in the year, before the call for competition."),
                **folder, **project}
    if doc["doc"] == "ContractNotice":
        return {"ID": V(f.number("notice", doc["from"], "ContractNotice"), "The notice number."),
                "IssueDate": V(f.date(30), "The call for competition, a month after the prior information notice."),
                **folder, **project}
    if doc["doc"] == "CallForTenders":
        return {"ID": V(f.number("call", doc["from"], "CallForTenders"), "The number of the procurement documents."),
                "IssueDate": V(f.date(31), "Retrieved by the manufacturer after the notice was published."),
                **folder, **project}
    if doc["doc"] == "BusinessInformation":
        return {"ID": V(f.number("business-info", doc["from"], "BusinessInformation"), "The registry's extract number."),
                "IssueDate": V(f.date(46), "The authority checks the tenderer's registration before evaluation.")}
    if doc["doc"] == "TendererQualification":
        return {"ID": V(f.number("qualification", doc["from"], "TendererQualification"), "The tenderer's number for "
                                                                                       "its declaration."),
                "IssueDate": V(f.date(44), "Submitted with the tender."), **folder}
    if doc["doc"] == "GuaranteeCertificate":
        return {"ID": V(f.number("guarantee", doc["from"], "GuaranteeCertificate"), "The guarantee's number."),
                "IssueDate": V(f.date(43), "Issued before the tender deadline."), **folder,
                "LiabilityAmount": amount(2400, "XBL", "The bid bond: 2 % of the estimated contract value, as the "
                                                       "procurement documents ask.")}
    if doc["doc"] == "Tender":
        unit = kit.unit_price("bench-serra", "XBL")
        return {"ID": V(f.number("tender", doc["from"], "Tender"), "The tenderer's number for its tender."),
                "IssueDate": V(f.date(44), "Submitted before the deadline."), **folder,
                "TenderedProject": {"LegalMonetaryTotal": {
                    "PayableAmount": amount(unit * TENDER_QTY, "XBL", f"{TENDER_QTY} benches at {unit} lume: the bench "
                                                                      "price converted at the reference rate.")}}}
    if doc["doc"] == "ContractAwardNotice":
        return {"ID": V(f.number("award-notice", doc["from"], "ContractAwardNotice"), "The notice number."),
                "IssueDate": V(f.date(60), "Published after the standstill period."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day the authority decided the award.")}}
    if doc["doc"] == "AwardedNotification":
        return {"ID": V(f.number("awarded", doc["from"], "AwardedNotification"), "The notification number."),
                "IssueDate": V(f.date(56), "The winner is told on the day of the award decision."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day of the award decision.")}}
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 70, "The first call-off under the awarded contract.",
                         "Delivered at place, the authority's depot: the manufacturer delivers, by the carrier it "
                         "chooses; the authority clears the import.", "Public works depot, Lumeport",
                         {"Contract": {"ID": V(FOLDER, "The contract under which the call-off is made.")}},
                         currency="XBL")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 77, "The day the call-off left the 3PL.", "The gross weight loaded.")
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 77, "Declared when the goods leave for the border.",
                                      "The value of the goods, in ferra.")
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 78, "Under DAP the buyer clears the import: the authority declares "
                                                     "the benches.", "The customs value in lume, at the reference rate.")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 78, 30, "Issued on delivery.",
                           {"OrderReference": ref(f, "order", "The authority's call-off order."),
                            "ContractDocumentReference": {"ID": V(FOLDER, "The awarded contract.")}},
                           currency="XBL")
    raise SystemExit(f"tender scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the carnet flow (temporary export)
CARNET = kit.Flow("carnet", "2026-05-25", [
    {"item": "bench-serra", "ordered": 2, "why": "Two sample benches for the stand at the trade fair."}])


def carnet(n, doc):
    f = CARNET
    return {"ID": V(f.number("carnet", doc["from"], "GoodsItemPassport"), "The carnet number, given by the chamber."),
            "IssueDate": V(f.date(0), "Issued before the samples leave for the fair."),
            "ValidityPeriod": period(f, 0, 365, "Valid from issue.", "A carnet is valid for one year."),
            "Shipment": {"ID": V(f.number("shipment", doc["to"], "Shipment"), "The samples travelling under the carnet."),
                         "GoodsItem": kit.goods_items(f, "XUF", "The value of the samples, for the guarantee.")},
            "GoodsItemPassportCounterfoil": [
                {"ID": V("EXP-1", "The exportation counterfoil, stamped by Urvania's customs when the samples leave.")},
                {"ID": V("IMP-1", "The importation counterfoil, stamped by Lisavu's customs when they arrive.")}]}


# ---------------------------------------------------------------- the waste flow (Urvania, domestic)
WASTE = kit.Flow("waste", "2026-03-23")
WASTE_DESCRIPTION = "Mixed polyethylene production waste, sorted, in big bags"


def waste_shipment(f, tonnes, why):
    return {"ID": V(f.number("waste-shipment", "5-xu", "Shipment"), "The movement's shipment number."),
            "GrossWeightMeasure": qty(Decimal(tonnes) * 1000, "KGM", why),
            "Consignment": {"ID": V(f.number("waste-consignment", "5-xu", "Consignment"), "The consignment carried "
                                                                                          "by the road carrier.")},
            "GoodsItem": {"ID": V("1", "The only goods item."),
                          "Description": V(WASTE_DESCRIPTION, "What the waste is."),
                          "HazardousRiskIndicator": V("false", "Sorted polyethylene is not hazardous waste.")}}


def waste(n, doc):
    f = WASTE
    if doc["doc"] == "WasteNotification":
        return {"ID": V(f.number("notification", doc["from"], "WasteNotification"), "The notification number."),
                "IssueDate": V(f.date(0), "Notified before the movements start."),
                "Shipment": waste_shipment(f, 40, "The planned movement: about 40 tonnes in two truck loads.")}
    if doc["doc"] == "WasteMovement":
        return {"ID": V(f.number("movement", doc["from"], "WasteMovement"), "The movement document number."),
                "IssueDate": V(f.date(10), "Reported when the waste has been received."),
                "Shipment": waste_shipment(f, "38.2", "Weighed on arrival at the recovery facility.")}
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 12, 30, "Issued after the waste was collected and recovered.",
                           {"AdditionalDocumentReference": ref(f, "movement", "The waste movement document.")},
                           [{"item": "waste-recovery", "qty": "38.2", "invoice_why": "The tonnes received, from the "
                                                                                     "waste movement document."}])
    raise SystemExit(f"waste scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the utilities flow (one utility per country)
UTILITIES = kit.Flow("utilities", "2026-04-01")
BILLS = {"33-xu": [{"item": "electricity", "qty": 412800, "invoice_why": "The factory's metered consumption in March."},
                   {"item": "electricity", "qty": 18600, "invoice_why": "The warehouse's metered consumption in March; "
                                                                        "the manufacturer pays for its building."}],
         "34-xb:26-xb": [{"item": "water", "qty": 86, "invoice_why": "The shop's metered consumption in March."}],
         "34-xb:c-xb": [{"item": "water", "qty": 14, "invoice_why": "The household's metered consumption in March."}],
         "35-xl": [{"item": "telecom-line", "qty": 6, "invoice_why": "Six business lines for the month."},
                   {"item": "telecom-data", "qty": 35, "invoice_why": "Mobile data beyond the subscriptions."}]}
KIND = {"33-xu": "Electricity", "34-xb": "Water", "35-xl": "Telephone"}


def bill_key(doc):
    sup = doc["from"] if doc["doc"] != "RemittanceAdvice" else doc["to"]
    cust = doc["to"] if doc["doc"] != "RemittanceAdvice" else doc["from"]
    if sup == "34-xb":
        return f"34-xb:{cust}"
    return sup


def utilities(n, doc):
    f = UTILITIES
    if doc["doc"] == "UtilityStatement":
        sup = doc["from"]
        key = bill_key({**doc, "to": doc["parties"].get("CustomerParty", doc["to"])})
        invoice_no = f.number(f"invoice-{key}", sup, "Invoice")
        return {"ID": V(f.number(f"statement-{n}", sup, "UtilityStatement"), "The utility's statement number."),
                "IssueDate": V(f.date(1), "Issued with the bill for March."),
                "UtilityStatementTypeCode": V(KIND[sup], "The kind of utility the statement is about."),
                "DocumentCurrencyCode": kit.currency_line(kit.currency_of(sup), "the utility's currency"),
                "ParentDocumentReference": {"ID": V(invoice_no, "The invoice this statement supplements: a utility "
                                                                "statement adds the consumption behind the bill.")}}
    if doc["doc"] == "Invoice":
        key = bill_key(doc)
        return kit.invoice(f, n, doc, 1, 21, "The monthly bill, issued on the first day of the next month.", {},
                           BILLS[key], key=f"invoice-{key}")
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 18, "Paid before the due date.", key=f"invoice-{bill_key(doc)}")
    if doc["doc"] == "Reminder":
        key, cur = bill_key(doc), "XBL"
        due = f.numbers[f"invoice-{key}-amount"]
        return {"ID": V(f.number("reminder", doc["from"], "Reminder"), "The reminder number."),
                "IssueDate": V(f.date(30), "Sent a week after the due date passed without payment."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the unpaid bill"),
                "PaymentMeans": {"PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer, how the household "
                                                             "is asked to pay.", listID="UN/EDIFACT EDED 4461"),
                                 "PayeeFinancialAccount": kit.account(doc["from"], "The utility's account, where the "
                                                                                   "overdue amount is to be paid.")},
                "LegalMonetaryTotal": {"PayableAmount": amount(due, cur, "The amount still due: the whole bill.")},
                "ReminderLine": {"ID": V("1", "The unpaid bill."),
                                 "DebitLineAmount": amount(due, cur, "The amount of the unpaid invoice."),
                                 "BillingReference": {"InvoiceDocumentReference": {
                                     "ID": V(f.numbers[f"invoice-{key}"], "The invoice not paid."),
                                     "IssueDate": V(f.numbers[f"invoice-{key}-date"], "Its issue date.")}}}}
    raise SystemExit(f"utilities scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the wood flow (Bayvarra -> Urvania, and at home)
SLATS = [{"item": "slat-1800", "ordered": 4800, "why": "Slats for 960 benches: five per bench, 96 bundles of 50."}]
TIMBER = [{"item": "timber-beam", "ordered": 12, "why": "Hardwood for a month of furniture production."}]
WOOD = kit.Flow("wood", "2026-02-16", SLATS)


def quotation_lines(f, deal, cur, with_price):
    out = []
    for i, d in enumerate(deal, 1):
        li = {"ID": V(str(i), "The line number."),
              "Quantity": qty(d["ordered"], ITEM[d["item"]]["unit"], d["why"]),
              "Item": item(d["item"])}
        if with_price:
            p = kit.unit_price(d["item"], cur)
            li["LineExtensionAmount"] = amount(Decimal(str(d["ordered"])) * p, cur, "Quantity times the quoted price.")
            li["Price"] = kit.price_block(d["item"], cur)
        out.append({"LineItem": li})
    return out


def rfq(f, doc, day, why, deal):
    return {"ID": V(f.number("rfq", doc["from"], "RequestForQuotation"), "The buyer's request number."),
            "IssueDate": V(f.date(day), why),
            "IssueTime": V("10:00:00", "The time of the request; quotations refer to it."),
            "RequestForQuotationLine": quotation_lines(f, deal, None, False)}


def quotation(f, doc, day, why, deal, validity):
    cur = kit.currency_of(doc["from"])
    total = sum(Decimal(str(d["ordered"])) * kit.unit_price(d["item"], cur) for d in deal)
    return {"ID": V(f.number("quotation", doc["from"], "Quotation"), "The seller's quotation number."),
            "IssueDate": V(f.date(day), why),
            "ValidityPeriod": {"EndDate": V(f.date(day + validity), "How long the quoted prices hold.")},
            "RequestForQuotationDocumentReference": ref(f, "rfq", "The request this quotation answers."),
            "QuotedMonetaryTotal": {"LineExtensionAmount": amount(total, cur, "The sum of the quoted lines."),
                                    "PayableAmount": amount(total, cur, "The quoted total, before any tax.")},
            "QuotationLine": quotation_lines(f, deal, cur, True)}


def wood(n, doc):
    f = WOOD
    if doc["doc"] == "RequestForQuotation":
        return rfq(f, doc, 0, "The manufacturer asks for slats to its own dimensions.", SLATS)
    if doc["doc"] == "Quotation":
        return quotation(f, doc, 3, "The sawmill quotes for the slats.", SLATS, 30)
    if doc["doc"] == "Order" and doc["from"] == "5-xu":
        return kit.order(f, n, doc, 6, "The manufacturer accepts the quotation and orders.",
                         "Delivered at place, the factory: the sawmill delivers; the manufacturer clears the import.",
                         "Valdara Industries, goods-in, Ferrano",
                         {"QuotationDocumentReference": ref(f, "quotation", "The quotation accepted.")})
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 7, "Under DAP the sawmill books the truck across the border.", 10,
                               kit.gross_weight(f, "ordered"), "96 bundles of slats.")
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 10, "Declared when the truck leaves for the border.",
                                      "The value of the slats, in lume.")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 10, "The day the truck was loaded at the sawmill.",
                                   "The gross weight of the bundles.")
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 11, "The manufacturer declares the import into Urvania.",
                                      "The customs value in ferra: the value in lume at the reference rate (1 lume = 100 "
                                      "ferra).")
    if doc["doc"] == "Invoice" and doc["to"] == "5-xu":
        return kit.invoice(f, n, doc, 10, 30, "Issued when the slats leave.",
                           {"OrderReference": ref(f, "order", "The manufacturer's order.")},
                           [{"item": "slat-1800", "qty": 4800, "invoice_why": "The slats despatched."}])
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 38, "The manufacturer pays across the border.")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 20, "The furniture maker orders timber, collected with its own van.",
                         "Ex works the sawmill: the buyer collects the timber and bears every cost from the sawmill's "
                         "yard.", "Marrowdale Sawmill, timber yard", deal=TIMBER, key="order-timber")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 21, 30, "Issued when the timber was collected.",
                           {"OrderReference": ref(f, "order-timber", "The furniture maker's order.")},
                           [{"item": "timber-beam", "qty": 12, "invoice_why": "The cubic metres collected."}],
                           key="invoice-timber")
    raise SystemExit(f"wood scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the furniture flow (Bayvarra)
SETS = [{"item": "garden-set", "ordered": 20, "why": "The first delivery of the store's own garden furniture line."}]
DESKS = [{"item": "office-desk", "ordered": 6, "why": "Six desks for the new planning office."},
         {"item": "installation", "ordered": 14, "why": "Two installers for seven hours."}]
FURNITURE = kit.Flow("furniture", "2026-03-02", SETS)


def collab(f, doc, key, day, why):
    return {"ID": V(f.number(key, doc["from"], key), f"The sender's number for its {key.replace('-', ' ')}."),
            "IssueDate": V(f.date(day), why)}


def furniture(n, doc):
    f = FURNITURE
    sets = item("garden-set")
    if doc["doc"] == "RequestForQuotation":
        return rfq(f, doc, 0, "The store wants its own garden furniture line.", SETS)
    if doc["doc"] == "Quotation":
        return quotation(f, doc, 4, "The furniture maker quotes the line.", SETS, 60)
    if doc["doc"] == "ItemInformationRequest":
        return {**collab(f, doc, "info-request", 10, "Asked before the first production run."),
                "Period": period(f, 14, 70, "The season the information is wanted for.", "Its end."),
                "ItemInformationRequestLine": {
                    "Period": period(f, 14, 70, "Sales data for the season.", "Its end."),
                    "SalesItem": {"Quantity": qty(20, "SET", "The quantity of the first delivery, to compare sales "
                                                             "against."), "Item": sets}}}
    if doc["doc"] == "TradeItemLocationProfile":
        return {**collab(f, doc, "location-profile", 12, "The store sets its replenishment policy for the line."),
                "Period": period(f, 14, 180, "The policy holds for the season.", "Its end."),
                "ItemManagementProfile": {"EffectivePeriod": period(f, 14, 180, "From the first delivery.", "To the end of "
                                                                                                         "the season."),
                                          "Item": sets}}
    if doc["doc"] == "ExceptionCriteria":
        return {**collab(f, doc, "exception-criteria", 12, "Agreed together with the replenishment policy."),
                "ValidityPeriod": period(f, 14, 180, "Valid for the season.", "Its end."),
                "ExceptionCriteriaLine": {
                    "ID": V("1", "The only criterion."),
                    "ThresholdValueComparisonCode": V("LessThan", "An exception is raised when actual sales fall "
                                                                  "below the threshold."),
                    "ThresholdQuantity": qty(5, "SET", "Fewer than five sets sold in four weeks is worth a message."),
                    "SupplyItem": sets}}
    if doc["doc"] == "ProductActivity":
        return {**collab(f, doc, "activity", 49, "The store's report of the first four weeks."),
                "ActivityPeriod": period(f, 21, 49, "The four weeks reported.", "Their end."),
                "SupplyChainActivityDataLine": {
                    "ID": V("1", "The only line."),
                    "SupplyChainActivityTypeCode": V("Sales", "The activity reported: sales to consumers."),
                    "ActivityOriginLocation": {"Name": V("Brightmarket Stores, garden department, Lumeport",
                                                         "Where the sales took place.")},
                    "SalesItem": {"Quantity": qty(3, "SET", "Three sets sold in four weeks."), "Item": sets}}}
    if doc["doc"] == "ExceptionNotification":
        return {**collab(f, doc, "exception", 50, "The furniture maker sees the sales below the agreed threshold."),
                "ExceptionObservationPeriod": period(f, 21, 49, "The four weeks observed.", "Their end."),
                "ExceptionNotificationLine": {
                    "ID": V("1", "The only exception."),
                    "ComparedValueMeasure": V("5", "The agreed threshold: five sets in four weeks.", unitCode="SET"),
                    "SourceValueMeasure": V("3", "The sales the store reported: three sets.", unitCode="SET"),
                    "SupplyItem": sets}}
    if doc["doc"] == "Order" and doc["from"] == "26-xb":
        return kit.order(f, n, doc, 14, "The store orders the first delivery of its line.",
                         "Delivered at place, the store: the furniture maker delivers with its own van.",
                         "Brightmarket Stores, goods-in, Lumeport",
                         {"QuotationDocumentReference": ref(f, "quotation", "The quotation accepted.")})
    if doc["doc"] == "Invoice" and doc["to"] == "26-xb":
        return kit.invoice(f, n, doc, 20, 30, "Issued on delivery.", {"OrderReference": ref(f, "order", "The store's "
                                                                                                       "order.")},
                           [{"item": "garden-set", "qty": 20, "invoice_why": "The sets delivered."}])
    if doc["doc"] == "InstructionForReturns":
        return {**collab(f, doc, "returns", 56, "The furniture maker takes back the sets that do not sell."),
                "InstructionForReturnsLine": {"ID": V("1", "The only line."),
                                              "Quantity": qty(6, "SET", "Six of the remaining sets, to free shelf "
                                                                        "space."),
                                              "Item": sets}}
    if doc["doc"] == "CreditNote":
        return kit.credit_note(f, n, doc, 62, "Issued when the returned sets arrived back.",
                               [{"item": "garden-set", "qty": 6, "why": "The sets returned."}],
                               {"BillingReference": {"InvoiceDocumentReference": {
                                   "ID": V(f.numbers["invoice"], "The invoice of the returned sets."),
                                   "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}}})
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 30, "The public works department furnishes its new planning office.",
                         "Delivered at place, the office: the furniture maker delivers and installs.",
                         "Lumeport Public Works Department, Civic Square", deal=DESKS, key="order-desks")
    if doc["doc"] == "WorkReport":
        return {**collab(f, doc, "work-report", 38, "Reported when the installation was finished."),
                "WorkReportLine": {"ID": V("1", "The installation work."),
                                   "Quantity": qty(14, "HUR", "Two installers for seven hours, approved by the "
                                                              "department.")}}
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 38, 30, "Issued once the work report was approved.",
                           {"OrderReference": ref(f, "order-desks", "The department's order.")},
                           [{"item": "office-desk", "qty": 6, "invoice_why": "The desks delivered."},
                            {"item": "installation", "qty": 14, "invoice_why": "The hours of the approved work report."}],
                           key="invoice-desks")
    raise SystemExit(f"furniture scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the packaging flow (Bayvarra -> Urvania, and at home)
FILM = [{"item": "film-pe", "ordered": 480, "why": "Thirty rolls of 16 kg: wrapping for a month of bench pallets."}]
BAGS = [{"item": "garment-bag", "ordered": 20000, "why": "Forty boxes of 500 bags."}]
SHIRTS = [{"item": "shirt", "ordered": 600, "why": "The store's spring order of shirts."}]
PACKAGING = kit.Flow("packaging", "2026-04-27", FILM)


def packaging(n, doc):
    f = PACKAGING
    if doc["doc"] == "Order" and doc["from"] == "5-xu":
        return kit.order(f, n, doc, 0, "The manufacturer orders pallet film.",
                         "Free carrier at the packaging maker: the buyer books the road carrier that collects.",
                         "Rivermouth Packaging, dispatch, Lumeport")
    if doc["doc"] == "Invoice" and doc["to"] == "5-xu":
        return kit.invoice(f, n, doc, 5, 30, "Issued when the film was collected.",
                           {"OrderReference": ref(f, "order", "The manufacturer's order.")},
                           [{"item": "film-pe", "qty": 480, "invoice_why": "The kilograms collected."}])
    if doc["doc"] == "Order" and doc["from"] == "40-xb":
        return kit.order(f, n, doc, 2, "The textile mill orders garment bags.",
                         "Delivered at place, the mill: the packaging maker delivers.", "Lumeport Textile Mill, goods-in",
                         deal=BAGS, key="order-bags")
    if doc["doc"] == "Invoice" and doc["to"] == "40-xb":
        return kit.invoice(f, n, doc, 6, 30, "Issued on delivery.", {"OrderReference": ref(f, "order-bags",
                                                                                           "The mill's order.")},
                           [{"item": "garment-bag", "qty": 20000, "invoice_why": "The bags delivered."}],
                           key="invoice-bags")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 10, "The store orders shirts for spring.",
                         "Delivered duty paid at the store: the mill delivers and bears every cost.",
                         "Brightmarket Stores, goods-in, Lumeport", deal=SHIRTS, key="order-shirts")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 15, "The day the shirts left the mill.", "The gross weight of the cartons.",
                                   deal=SHIRTS, key="order-shirts")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 15, 30, "Issued on delivery.",
                           {"OrderReference": ref(f, "order-shirts", "The store's order.")},
                           [{"item": "shirt", "qty": 600, "invoice_why": "The shirts delivered."}], key="invoice-shirts")
    if doc["doc"] == "PurchaseReceipt":
        return kit.purchase_receipt(f, n, doc, 25, "A consumer buys two shirts.",
                                    [{"item": "shirt-r", "qty": 2, "why": "Two shirts."}], cash=True)
    raise SystemExit(f"packaging scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"tender": tender, "carnet": carnet, "waste": waste, "utilities": utilities, "wood": wood,
                  "furniture": furniture, "packaging": packaging})


# ================================================================ step 2: the document types the flows did not use yet
def nth(flow_id, n, doc):
    """Which occurrence of the same document type between the same parties this is, within the flow (1, 2, ...)."""
    same = [d for d in kit.WORLD["documents"] if d["flow"] == flow_id]
    return sum(1 for d in same[:n] if (d["doc"], d["from"], d["to"]) == (doc["doc"], doc["from"], doc["to"]))


def head(f, key, doc, day, why, doc_type=None):
    return {"ID": V(f.number(key, doc["from"], doc_type or doc["doc"]), "The sender's number for this document."),
            "IssueDate": V(f.date(day), why)}


def response(code, why, ref_id, ref_why):
    """A DocumentResponse: the response code and the document it is about."""
    return {"Response": {"ResponseCode": V(code, why)},
            "DocumentReference": {"ID": V(ref_id, ref_why)}}


_tender, _rail, _sea, _air, _retail, _road, _furniture, _carnet = tender, rail, sea, air, retail, road, furniture, carnet


def tender(n, doc):
    f, d = TENDER, doc["doc"]
    folder = {"ContractFolderID": V(FOLDER, "The authority's file number for this procurement, the same on every "
                                            "document of the procedure.")}
    if d == "ExpressionOfInterestRequest":
        return {**head(f, "eoi", doc, 33, "Sent after the contract notice was published."), **folder}
    if d == "ExpressionOfInterestResponse":
        return {**head(f, "eoi-response", doc, 34, "The authority confirms the registration the next day."), **folder}
    if d == "QualificationApplicationRequest":
        return {**head(f, "qar", doc, 32, "Sent with the procurement documents."), **folder}
    if d == "QualificationApplicationResponse":
        return {**head(f, "qar-response", doc, 38, "Returned before the tender deadline."), **folder,
                "TenderingCriterionResponse": {
                    "ID": V("SEL-1", "The response to the authority's first selection criterion."),
                    "Description": V("Annual turnover in furniture above 500,000 lume in each of the last three "
                                     "years.", "What the furniture maker declares for this criterion.")}}
    if d == "ProcurementStatusRequest":
        return {**head(f, "status-request", doc, 39, "The furniture maker asks a week before the deadline."), **folder}
    if d == "ProcurementStatus":
        return {**head(f, "procurement-status", doc, 40, "Answered the next day."), **folder,
                "TenderSubmissionDeadlinePeriod": {"EndDate": V(f.date(44), "The deadline for tenders stands.")}}
    if d == "UnsubscribeFromProcedureRequest":
        return {**head(f, "unsubscribe", doc, 41, "The sawmill decides before the deadline."), **folder}
    if d == "UnsubscribeFromProcedureResponse":
        return {**head(f, "unsubscribe-response", doc, 42, "The authority confirms the next day."), **folder}
    if d == "TenderReceipt":
        return {**head(f, "tender-receipt", doc, 44, "Sent on receipt of the tender."), **folder,
                "RegisteredDate": V(f.date(44), "The day the tender was registered, before the deadline."),
                "RegisteredTime": V("11:42:00", "The time it was registered, which proves it was on time."),
                "TenderDocumentReference": {"ID": V(f.numbers["tender"], "The tender received.")}}
    if d == "Tender" and doc["from"] == "37-xb":
        k = nth("tender", n, doc)
        price = Decimal("470.00") if k == 1 else Decimal("480.00")
        return {"ID": V(f.number(f"tender-37-{k}", doc["from"], "Tender"), "The furniture maker's number for this "
                                                                           "tender."),
                "IssueDate": V(f.date(42 if k == 1 else 43), "Submitted before the deadline." if k == 1 else
                               "The corrected tender, submitted the day after the withdrawal."),
                **folder,
                "TenderedProject": {"LegalMonetaryTotal": {
                    "PayableAmount": amount(price * TENDER_QTY, "XBL",
                                            f"{TENDER_QTY} wooden benches at {price} lume" +
                                            (": the price per bench was entered wrongly." if k == 1 else
                                             ", the corrected price."))}}}
    if d == "TenderWithdrawal":
        return {**head(f, "withdrawal", doc, 43, "Withdrawn before the deadline, which the procedure allows."),
                **folder,
                "WithdrawOfferIndicator": V("true", "The whole tender is withdrawn."),
                "TenderDocumentReference": {"ID": V(f.numbers["tender-37-1"], "The tender withdrawn.")}}
    if d == "TendererQualificationResponse":
        return {**head(f, "qualification-response", doc, 50, "After the check of the qualifications."), **folder,
                "QualificationResolution": {"AdmissionCode": V("Admitted", "The tenderer meets the selection criteria "
                                                                           "and its tender is evaluated."),
                                            "ResolutionDate": V(f.date(50), "The day of the decision.")}}
    if d == "UnawardedNotification":
        return {**head(f, "unawarded", doc, 56, "Told on the day of the award decision, as the winner is."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day the contract was awarded to another tenderer.")}}
    if d == "TenderContract":
        return {**head(f, "contract", doc, 66, "Concluded after the ten-day standstill period."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day of the award decision.")}}
    return _tender(n, doc)


def rail(n, doc):
    f, d = RAIL, doc["doc"]
    train = {"JourneyID": V("CT 4471", "The number of the container train in the hub's timetable.")}
    if d == "TransportProgressStatusRequest":
        return {**head(f, "tps-request", doc, 8, "Asked on the morning of departure."),
                "IssueTime": V("06:30:00", "Before the train leaves the hub."), "TransportMeans": train}
    if d == "TransportProgressStatus":
        return {**head(f, "tps", doc, 8, "Answered at once."), "IssueTime": V("06:45:00", "A quarter of an hour later."),
                "TransportMeans": train}
    if d == "GoodsItemItinerary":
        return {**head(f, "itinerary", doc, 8, "Sent when the containers are on the train."),
                "IssueTime": V("09:00:00", "After loading."),
                "VersionID": V("1", "The first version of the itinerary."),
                "TransportExecutionPlanReferenceID": V(f.numbers["tep"], "The transport plan the itinerary belongs to."),
                "TransportationSegment": {
                    "SequenceNumeric": V("1", "One segment: by rail from the hub to the distributor's siding."),
                    "TransportationService": {"TransportServiceCode": V("RailContainer", "The rail carrier's own code "
                                                                                         "for its container train "
                                                                                         "service.")}}}
    return _rail(n, doc)


def sea(n, doc):
    f, d = SEA, doc["doc"]
    service = {"TransportServiceCode": V("OceanContainer", "The carrier's code for its container liner service."),
               "Name": V("Weekly service Lumeport–Selanu", "The name of the service.")}
    if d == "BusinessCard":
        return head(f, "business-card", doc, 0, "Sent before the first offer to the new customer.")
    if d == "TransportServiceDescriptionRequest":
        return {**head(f, "tsd-request", doc, 4, "Asked once the order is accepted."),
                "IssueTime": V("14:00:00", "The time of the request."),
                "TransportationService": {"TransportServiceCode": V("OceanContainer", "The service asked about: a "
                                                                                      "container liner service.")}}
    if d == "TransportServiceDescription":
        return {**head(f, "tsd", doc, 5, "The carrier answers the next day."), "TransportationService": service}
    if d == "InvoiceStatusRequest":
        return {"ID": V(f.number("invoice-status-request", doc["from"], d), "The distributor's request number."),
                "RequestDate": V(f.date(25), "Two weeks after the invoice, without news from the buyer."),
                "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The invoice asked "
                                                                                                "about.")}}}
    if d == "InvoiceStatusResponse":
        return {**head(f, "invoice-status", doc, 26, "Answered the next day."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: accepted; the invoice is scheduled for "
                                                   "payment.", f.numbers["invoice"], "The invoice the status is about.")}
    return _sea(n, doc)


def air(n, doc):
    f, d = AIR, doc["doc"]
    if d == "FulfilmentCancellation":
        return {**head(f, "fulfilment-cancellation", doc, 3, "The flight left without the cargo."),
                "CancellationNote": V("The cargo missed its flight; it goes on the next day's flight under a new "
                                      "despatch advice.", "Why the despatch advice is cancelled."),
                "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice cancelled.")}}
    if d == "DespatchAdvice" and nth("air", n, doc) == 2:
        out = kit.despatch_advice(f, n, doc, 3, "Sent for the next day's flight.", "The gross weight of the boxed "
                                                                                    "frames.")
        out["ID"] = V(f.number("despatch-2", doc["from"], "DespatchAdvice"), "A new number: the first despatch "
                                                                             "advice was cancelled.")
        return out
    return _air(n, doc)


def retail(n, doc):
    f, d = RETAIL, doc["doc"]
    cat = {"ID": V(f.numbers.get("catalogue", ""), "The catalogue concerned.")} if "catalogue" in f.numbers else None
    if d == "CatalogueRequest":
        return head(f, "catalogue-request", doc, 0, "The store asks for the spring catalogue. As UBL defines it, the "
                                                     "party that sends a catalogue request is its ProviderParty.")
    if d == "CataloguePricingUpdate":
        return {**head(f, "pricing-update", doc, 30, "The distributor lowers a price during the season."),
                "RelatedCatalogueReference": cat,
                "CataloguePricingUpdateLine": {"ID": V("1", "The line of the side frame."),
                                               "RequiredItemLocationQuantity": {"Price": {
                                                   "PriceAmount": price("58.00", "XBL", "The new price of the side "
                                                                                        "frame, down from 64.00."),
                                                   "BaseQuantity": qty(1, "H87", "Per piece.")}}}}
    if d == "CatalogueItemSpecificationUpdate":
        it = item("bench-serra-b")
        it["Description"] = V("Park bench, 1800 mm, frame of cast and galvanised steel, five slats of another kiln-dried "
                              "hardwood, for bolting to the ground.", "The new description: the slats are now of a "
                                                                      "different hardwood.")
        return {**head(f, "spec-update", doc, 31, "The bench's slats changed wood."), "RelatedCatalogueReference": cat,
                "CatalogueItemSpecificationUpdateLine": {"ID": V("1", "The line of the bench."), "Item": it}}
    if d == "CatalogueDeletion":
        return {**head(f, "catalogue-deletion", doc, 60, "The spring catalogue is withdrawn before the summer one."),
                "DeletedCatalogueReference": cat}
    if d == "DocumentStatusRequest":
        return {**head(f, "status-request", doc, 6, "Asked two days after ordering."),
                "RequestedDocumentReference": {"ID": V(f.numbers["order"], "The order asked about.")}}
    if d == "DocumentStatus":
        return {**head(f, "document-status", doc, 6, "Answered the same day."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: the order is accepted and the truck is "
                                                   "booked.", f.numbers["order"], "The order the status is about.")}
    if d == "TransportationStatusRequest":
        return {**head(f, "ts-request", doc, 9, "The store asks when to expect the delivery."),
                "Consignment": {"ID": V(f.numbers["consignment"], "The consignment asked about.")}}
    return _retail(n, doc)


def road(n, doc):
    f = ROAD
    if doc["doc"] == "ApplicationResponse":
        return {**head(f, "application-response", doc, 9, "Sent automatically when the invoice was processed."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: the invoice is accepted.",
                                             f.numbers["invoice"], "The invoice responded to.")}
    return _road(n, doc)


def furniture(n, doc):
    f, d = FURNITURE, doc["doc"]
    if d == "Order" and doc["from"] == "26-xb" and nth("furniture", n, doc) == 2:
        return kit.order(f, n, doc, 45, "A second delivery, before the slow sales were clear.",
                         "Delivered at place, the store, as the first delivery.", "Brightmarket Stores, goods-in, "
                                                                                 "Lumeport", key="order-2")
    if d == "OrderCancellation":
        return {**head(f, "order-cancellation", doc, 51, "Cancelled the day after the exception notification."),
                "CancellationNote": V("Sales of the line are below the agreed threshold; the second delivery is not "
                                      "needed.", "Why the order is cancelled."),
                "OrderReference": {"ID": V(f.numbers["order-2"], "The order cancelled.")}}
    if d == "DebitNote":
        rows = kit.spec_rows([{"item": "return-transport", "qty": 1}], "26-xb", "37-xb", "XBL")
        tax, total = kit.tax_total(rows, "XBL")
        amt = rows[0][2]
        return {**head(f, "debit-note", doc, 63, "After the returned sets were collected."),
                "DocumentCurrencyCode": kit.currency_line("XBL", "the currency of the trade"),
                "BillingReference": {"CreditNoteDocumentReference": {"ID": V(next(v for k, v in f.numbers.items()
                                                                          if k.startswith("credit-")), "The credit note "
                                                                                                     "of the returned "
                                                                                                     "sets.")}},
                "TaxTotal": total,
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, "XBL", "The sum of the lines."),
                                           "PayableAmount": amount(amt + tax, "XBL", "What the furniture maker owes "
                                                                                     "the store.")},
                "DebitNoteLine": {"ID": V("1", "The return transport."),
                                  "DebitedQuantity": qty(1, "E48", "One return delivery."),
                                  "LineExtensionAmount": amount(amt, "XBL", "The store's charge for one return delivery."),
                                  "Item": item("return-transport", kit.tax_category(rows[0][3])),
                                  "Price": kit.price_block("return-transport")}}
    return _furniture(n, doc)


def carnet(n, doc):
    f, d = CARNET, doc["doc"]
    if d == "GoodsItemPassport":
        e = PARTY["5-xu"]["identity"]["employee"]
        src = "identity of Valdara Industries (world/parties.json)"
        out = _carnet(n, doc)
        out["RepresentativeParty"] = {"Person": {
            "ID": V(e["id"], f"The employee's staff number; {src}."),
            "FirstName": V(e["first"], f"The first name of the employee who travels with the samples; {src}."),
            "FamilyName": V(e["family"], f"Their family name; {src}."),
            "JobTitle": V(e["job"], f"Their job; {src}."),
            "NationalID": V(e["national_id"], "The national identity number, which customs may ask for at the border."),
            "BirthDate": V(e["birth_date"], "The birth date, as in the passport."),
            "BirthplaceName": V(e["birthplace"], "The place of birth, as in the passport."),
            "OrganizationDepartment": V(e["department"], f"The department the employee works in; {src}."),
            "CitizenshipCountry": {"IdentificationCode": V("XU", "The employee is a citizen of Urvania.")},
            "IdentityDocumentReference": {"ID": V(e["passport"], "The passport the employee travels on."),
                                          "DocumentType": V("Passport", "The kind of identity document.")}}}
        return out
    passport = {"GoodsItemPassportID": V(f.numbers.get("carnet", ""), "The carnet the samples travelled under.")}
    if d == "ProofOfReexportationRequest":
        return {**head(f, "por-request", doc, 60, "Two months after the fair the samples' re-export is not recorded."),
                **passport}
    if d == "ProofOfReexportationReminder":
        return {**head(f, "por-reminder", doc, 90, "No answer after a month."),
                "ProcedureCode": V("TemporaryAdmission", "The procedure the samples were under on the island."),
                **passport,
                "ProofOfReexportationRequestDocumentReference": {"ID": V(f.numbers["por-request"], "The request "
                                                                                                   "unanswered.")},
                "GoodsItemPassportCounterfoil": {"ID": V("IMP-1", "The importation counterfoil without a re-export "
                                                                  "stamp.")}}
    if d == "ProofOfReexportation":
        return {**head(f, "proof", doc, 95, "Urvania's chamber answers with the proof."),
                "GoodsItemPassportCounterfoil": {"ID": V("REIMP-1", "The re-importation counterfoil, stamped by "
                                                                    "Urvania's customs when the samples came home.")},
                "ReexportationEvidence": {"ID": V("REIMP-1", "The evidence is the re-importation counterfoil itself."),
                                          "Description": V("Re-importation counterfoil of the carnet, stamped by "
                                                           "Urvania's customs: the samples left the island and came "
                                                           "home.", "What the evidence shows.")}}
    return _carnet(n, doc)


SCENARIOS.update({"tender": tender, "rail": rail, "sea": sea, "air": air, "retail": retail, "road": road,
                  "furniture": furniture, "carnet": carnet})
