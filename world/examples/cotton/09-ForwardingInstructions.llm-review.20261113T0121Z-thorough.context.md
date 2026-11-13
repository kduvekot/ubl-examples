# LLM review: 09-ForwardingInstructions.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/09-ForwardingInstructions.xml`, Git blob `f8e65d13a83ffc42dbb2cdb364ae14e78a2f0b46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/09#F1 · Medium · The forwarding instructions do not describe the goods or say from where to where
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the bales to Bayvarra.`
- Why: Forwarding Instructions is "A document issued to a forwarder, giving instructions regarding
  the action to be taken for the forwarding of goods described therein". The shipment carries only
  an ID, a gross weight and a consignment with its consignee: no goods item, no description of the
  goods, no number of bales or packages, no place of loading or discharge, no delivery, no transport
  mode, no dates. "The bales to Bayvarra" in the description is all the forwarder learns of what to
  carry and where. The bill of lading 13 and the export declaration 11 describe the goods, the 27
  bales and the ports; the instructions that start that chain do not.
- Condition: the forwarding instructions state what is to be forwarded (goods description and
  number of bales), from where (the port of Selanu or the gin) and to where (the mill at Lumeport),
  and when.
- Options: (a, preferred) add a goods item with the lint and the 27 bales, the delivery terms FOB
  Port of Selanu from the order, and the loading and destination places; (b) keep it short but
  refer to a booking or packing document that does describe them.
- Needs decision: no

### cotton/09#F2 · Medium · The ginnery's shipment ID used as the shipping order number
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `SCG-SH-26-0200`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: ShippingOrderID is "Reference number to identify a Shipping Order"; Shipment/ID is "An
  identifier for this shipment". The same value is used for both: the ginnery's identifier of the
  shipment (prefix SCG, used as Shipment/ID in 10, 11, 12, 13 and 15) is given as the number of a
  shipping order, in a document issued by the mill (ID prefix LTM, signed by the mill). No shipping
  order exists in the flow. An identifier of one kind is used as another.
- Condition: ShippingOrderID, if present, is the number of a shipping order (issued by the party
  that places it), distinct from the shipment's own ID.
- Options: (a, preferred) leave ShippingOrderID out; (b) give it a number of its own if the story has
  a shipping order (e.g. the forwarder's booking request).
- Needs decision: no

### cotton/09#F3 · Low · Ad valorem indicator used for the declared carriage value, while its definition is about ad valorem duties
- XPath: `/ForwardingInstructions/cbc:AdValoremIndicator` = `true`
- XPath: `/ForwardingInstructions/cbc:DeclaredCarriageValueAmount` = `6055.452`
- Why: AdValoremIndicator is "A term used in commerce in reference to certain duties, called ad
  valorem duties, which are levied on commodities at certain rates per centum on their value".
  In a forwarding instruction placed next to a declared carriage value, the indicator reads in the
  shipping sense of "ad valorem freight" (the carrier's liability raised to the declared value),
  which is not the UBL definition. Under the UBL definition the value says the goods are subject to
  ad valorem duties; the import declaration 15 only notes that "Duties paid by the importer's
  account at customs", without saying they are ad valorem. Semantic conformance asks for the UBL
  meaning (UBL 2.5 §4.7/§7.2). The same pair is in the bill of lading 13.
- Condition: AdValoremIndicator is present only to state whether ad valorem duties apply to the
  goods, and the story agrees with it.
- Options: (a, preferred) leave AdValoremIndicator out and let DeclaredCarriageValueAmount alone
  express the higher liability; (b) keep it if Bayvarra's duty on cotton lint is ad valorem, and let
  15 show it.
- Needs decision: yes (whether the indicator states a duty fact of the world)

### cotton/09#F4 · Low · An exchange rate no amount uses, a distribution list naming the addressee, and a status that states none
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/ForwardingInstructions/cbc:DocumentStatusCode` = `NoStatus`
- Why: ExchangeRate is "Information about the rate of exchange (conversion) between two currencies";
  the only amount of the document, the declared carriage value, is in coral, so the Lume–coral rate
  converts nothing. DocumentDistribution is "A list of interested parties to whom this document is
  distributed"; it names only the forwarder, to whom the instructions are addressed anyway.
  DocumentStatusCode "No status on document" gives no status. None of the three is used (UBL IND5).
- Condition: each is present only with a business use (an amount in another currency, a third party
  receiving a copy, a real status).
- Options: (a, preferred) leave all three out.
- Needs decision: no

## Checked and consistent
- Under FOB (order 08) the buyer arranges the main carriage, so the mill instructing its own
  forwarder, with the ginnery as consignor and the mill as consignee, fits.
- DocumentReference LTM-PO-26-0198 resolves to the order 08; the declared carriage value 6,055.452
  XLC is the order value.
- "Send the bill of lading to the forwarder" fits the forwarder being the B/L's freight forwarder
  party in 13.
- Gross weight 6,190.29 kg against 6,129 kg net: 61.29 kg of bale packaging (1 %, about 2.3 kg per
  bale of 27), plausible for bale wrapping and ties.

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `false`: suspected as a filler — refuted because it
  tells the forwarder to have a straight (named consignee) bill of lading issued, which fits the B/L
  13 naming the mill.
