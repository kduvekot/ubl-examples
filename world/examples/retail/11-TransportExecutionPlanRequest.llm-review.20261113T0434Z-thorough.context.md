# LLM review: 11-TransportExecutionPlanRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/11-TransportExecutionPlanRequest.xml`, Git blob `43f5b79071571e3db0185c905bab61bd7c25ec4c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/11#F1 · Medium · The transport request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `996`
- Why: a TransportExecutionPlanRequest is "A document sent by a transport user to request a
  transport service from a transport service provider". Its consignment has only an ID, a gross
  weight and the two parties: no goods description, no number or kind of packages or handling units
  (six pallets of benches, according to 12-DespatchAdvice.xml), no dimensions. The forwarder cannot
  plan loading or price the service from a weight alone.
- Condition: the consignment states what is carried: at least the goods description and the number
  and type of transport handling units (pallets).
- Options: add the six pallets (count and type) and a goods description such as "park benches,
  palletised" (preferred); dimensions or loading metres if the truck is planned on them.
- Needs decision: no

### retail/11#F2 · Medium · A language code in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/11#F3 · Low · Document status "No status"
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "A code signifying the status of the Transport Execution Plan Request";
  `NoStatus` ("No status on document") states that there is nothing to state. A first, ordinary
  request (VersionID `1`) needs no status code; the value is a filler (IND5/IND6).
- Condition: DocumentStatusCode only when the request is cancelled, revised or disputed.
- Options: drop it.
- Needs decision: no

### retail/11#F4 · Low · Transport locations named after companies, and the destination without the goods-in point
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Lumeway Distribution`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Brightmarket Stores`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: FromLocation and ToLocation are "The location of origin" and "The destination location for the
  transport service". Their names are the companies, not places, and the destination is the
  retailer's business address, without the goods-in point the order names (GLN `9522610900019`,
  "Goods-in, garden department"). The forwarder is not told where at the store to unload.
- Condition: the locations are named as places, and the destination identifies the goods-in point of
  the order.
- Options: "Marrowdale distribution centre" / "Brightmarket Lumeport, goods-in" with the GLN of the
  delivery location (preferred).
- Needs decision: no

### retail/11#F5 · Low · A gate in AdditionalStreetName
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a
  gate is not a street. For a pickup the gate matters, but as a detail of the location (its
  description or a sub-location), not as a street name.
- Condition: the gate is not in a street-name element.
- Options: put "Gate 3" in the location's Description (preferred) or in a sub-location.
- Needs decision: no

### retail/11#F6 · Low · Master data the transport request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: a domestic truck booking uses neither share capital nor tax schemes, the consignee's
  social-media profile and online shop, nor a customs trader number (IND5/IND6).
- Condition: the parties carry what the booking uses (identification, name, address, contact).
- Options: drop them.
- Needs decision: no

## Checked and consistent
- SenderParty and TransportUserParty are Lumeway, ReceiverParty and TransportServiceProviderParty
  Bayforth, BillToParty Lumeway; this matches 16-Invoice.xml, where Bayforth invoices Lumeway.
- The service period (start 2026-04-29, end by 2026-05-02) follows the order of 2026-04-24 and the
  response deadline 2026-04-26 follows the issue date 2026-04-25.
- From and to addresses are the business addresses of Lumeway (Marrowdale) and Brightmarket
  (Lumeport) as given in the other examples.
- The consignment ID `LD-CS-26-0228` is the one used in 12-DespatchAdvice.xml.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode`: a full
  truck load for six pallets of about one tonne — refuted because a dedicated truck for a delivery to
  a store is a plausible commercial choice; the code describes the service booked, not the load factor.
