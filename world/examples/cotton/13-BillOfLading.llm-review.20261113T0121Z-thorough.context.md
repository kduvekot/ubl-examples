# LLM review: 13-BillOfLading.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/13-BillOfLading.xml`, Git blob `c90a3571519a90b3221ab1bd12b871dc2751864d` (committed)
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

### cotton/13#F1 · High · The original bill of lading goes to a bank, while the forwarding instructions ask for it to be sent to the forwarder
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `/BillOfLading/cac:DocumentReference/cbc:ID` = `LTM-FI-26-0199`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- Why: The bill of lading refers to the forwarding instructions 09, which instruct "Send the bill of
  lading to the forwarder". The B/L's distribution list sends the original by courier to the Bank of
  Selanu and a scanned copy to the mill; the forwarder, Bayforth Forwarding, receives nothing. The
  B/L does not follow the instruction it cites, and nothing explains the change.
- Condition: the distribution of the original bill of lading agrees with the forwarding
  instructions, or the story explains why the original goes elsewhere.
- Options: (a, preferred) distribute the original to the forwarder, as instructed; (b) if the
  original must go to a bank (documentary collection), change the instruction in 09 and the payment
  terms of the invoice 16 to match (see F2).
- Needs decision: yes (whether the sale is settled through a bank is part of the story)

### cotton/13#F2 · Medium · A bank as mortgage holder of the consignment of an open-account sale
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MortgageHolderParty/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `16-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `16-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- Why: MortgageHolderParty is "The Party who holds the mortgage for this Consignment". The sale of
  the lint is invoiced on open account: credit transfer within 45 days (invoice 16), with no letter
  of credit or documentary collection anywhere in the flow. A bank holding a security interest in
  the goods (and receiving the original B/L, F1) would fit a documentary credit or a financed
  export; nothing in the flow shows one. The bank is also the ginnery's own bank (the payee account
  of 16 is at the Bank of Selanu), which would make the ginnery's goods pledged to it; the story
  does not say so. A straight bill of lading (ToOrderIndicator false in 09, the mill as consignee)
  is moreover not the document a bank takes as security (own knowledge of trade finance).
- Condition: the consignment names a mortgage holder only if the flow shows the financing that
  gives it one (and then the payment terms and the B/L's transferability agree with it).
- Options: (a, preferred) leave MortgageHolderParty out; (b) add the financing to the story
  (documentary collection or pre-export finance) and let 09, 13 and 16 show it consistently.
- Needs decision: yes

### cotton/13#F3 · Medium · The bill of lading does not describe the goods, the container, the vessel or the ports
- XPath: `/BillOfLading/cbc:Description` = `Shipped on board.`
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- Why: A Bill of Lading "evidences a contract of carriage by sea and the acceptance of responsibility
  for the goods by the carrier, by which the carrier undertakes to deliver the goods against
  surrender of the document" (UBL definition). It says "Shipped on board", but the shipment carries
  only an ID, a gross weight and a consignment with consignee and mortgage holder: no goods item or
  description of the goods, no number of bales, no container (the VGM 12 gives TWLU4123110), no
  vessel or voyage, no port of loading or discharge, no shipped-on-board date. The carrier's
  acknowledgement of what it received and where it will deliver, the core of a B/L, is missing.
- Condition: the bill of lading states the goods and their packages as received, the container,
  the vessel and voyage, the ports of loading and discharge, and the on-board date.
- Options: (a, preferred) add a goods item (lint, 27 bales), the transport handling unit with the
  container of 12, and a main-carriage shipment stage with vessel, ports and loading date that fit
  the map's sea route Selanu–Lumeport and the report 14.
- Needs decision: no

### cotton/13#F4 · Low · Ad valorem indicator used for the declared carriage value; an exchange rate no amount uses
- XPath: `/BillOfLading/cbc:AdValoremIndicator` = `true`
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- Why: AdValoremIndicator is, by its UBL definition, about "ad valorem duties, which are levied on
  commodities at certain rates per centum on their value"; here it stands next to
  DeclaredCarriageValueAmount in the shipping sense of ad valorem freight (same as in 09). The
  Lume–coral ExchangeRate converts nothing: the only amount is the declared value in coral.
- Condition: AdValoremIndicator is present only to state whether ad valorem duties apply; an
  exchange rate is present only when an amount needs converting.
- Options: (a, preferred) leave both out.
- Needs decision: yes for the indicator (whether it states a duty fact of the world), as in 09

## Checked and consistent
- "Freight collect" fits FOB Port of Selanu (08): the buyer pays the main carriage.
- Carrier Tidewell Ocean Lines is the receiver of the VGM 12 and signs the B/L; the forwarder
  Bayforth is the one the mill instructed in 09; consignor and consignee are those of 09.
- DocumentReference LTM-FI-26-0199 resolves to 09; the declared carriage value 6,055.452 XLC is
  the one of 09.
- Issued 2026-03-02, after the export declaration (2026-03-01) and the VGM (2026-03-01).

## Considered and refuted
- `/BillOfLading/cbc:DocumentStatusCode` = `Confirmed`: a status on a first issue suspected as a
  filler — refuted because "Document has been confirmed" states that the carrier has confirmed the
  booking it was issued against, a real status.

## Outside this review
- Whether the voyage of 13/14 (dates, vessel, route) fits the map and the other flows using the same
  vessel is a cross-flow timeline question.
