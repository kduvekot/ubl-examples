# LLM review: 08-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/08-Order.xml`, Git blob `4b9ab738473f9a4b2d8102ca056f226654c8875b` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/08#F1 · High · Emission factor times base does not give the emission
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor (see F5).
- Options: drop the emission from the order (preferred), or correct the factor.
- Needs decision: no

### retail/08#F2 · Medium · DataSendingCapability used for the e-invoicing network
- XPath: `/Order/cac:SellerSupplierParty/cbc:DataSendingCapability` = `UBL 2.5 over the trade accord network`
- Why: DataSendingCapability is "Text describing the supplier's ability to send invoice data via a
  purchase card provider (e.g., VISA, MasterCard, American Express)". The order is paid by credit
  transfer (PaymentMeansCode `30`); no purchase card is involved. The value describes the exchange
  network the supplier uses, which the parties' ElectronicAddress already gives.
- Condition: DataSendingCapability describes purchase-card data capability, or is absent.
- Options: drop it (preferred).
- Needs decision: no

### retail/08#F3 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples). LocaleCode is "A
  code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is a language
  code (213 examples; both counts with `grep -l` over `*.xml`).
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; `en-XB` or no LocaleCode.
- Needs decision: no

### retail/08#F4 · Low · "Third-party" account ID that is the buyer's own
- XPath: `/Order/cac:BuyerCustomerParty/cbc:AdditionalAccountID` = `BM-LUM-01`
- Why: in CustomerParty, AdditionalAccountID is "An identifier for the customer's account, assigned by
  a third party". `BM-LUM-01` follows Brightmarket's own numbering (`BM-`, as the buyer-assigned
  `BM-6120`) and names Lumeway; no third party appears in the order. It reads as a second
  buyer-assigned account number.
- Condition: AdditionalAccountID is an account ID assigned by a third party named in the story, or is
  absent.
- Options: drop it (preferred), or make it a third party's ID (e.g. of the factor in 18-Invoice.xml)
  with a reason.
- Needs decision: no

### retail/08#F5 · Low · The order carries the item's full catalogue description and the parties' master data
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the order identifies the bench by four identifiers and the catalogue line; the footprint,
  circularity profile, load test, dimensions with tolerances and customs codes are the seller's own
  catalogue data, which the order does nothing with. The parties carry share capital, a customs trader
  number (domestic order) and social media.
- Condition: item and parties carry what an order uses.
- Options: reduce the item to identifiers, name and the ordered variant; drop the master data.
- Needs decision: no

### retail/08#F6 · Low · No requested delivery date in an order placed for a promotion
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `/Order/cac:AdditionalDocumentReference/cbc:ID` = `BS-RE-26-0222`
- Why: the order is placed for the spring promotion (it refers to the retail event, which starts on
  2026-05-11 and needs shelf stock beforehand) but its Delivery has only a location and a party, no
  requested delivery period. The supplier learns when the benches are needed only from the event.
- Condition: the order says by when the goods are wanted, or the story says the date is agreed
  elsewhere.
- Options: a RequestedDeliveryPeriod before the promotion (e.g. ending 2026-05-04) (preferred).
- Needs decision: no

### retail/08#F7 · Low · Substitute line item with the same line ID as the ordered item
- XPath: `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cbc:ID` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: LineItem ID is "An identifier for this line item, assigned by the buyer". The proposed
  substitute (the moss green variant) is a different line item but has the same ID as the ordered
  grey bench, so a response cannot tell them apart by ID.
- Condition: the substitute has its own line item ID.
- Options: e.g. `1.1` or `2` for the substitute.
- Needs decision: no

### retail/08#F8 · Low · Signature without anything that signs
- XPath: `/Order/cac:Signature/cbc:ID` = `BM-SIG-26-0424`
- Why: only an ID and a signatory, no method or attachment; it records no signature.
- Condition: a signature with data, or none.
- Options: drop it.
- Needs decision: no

## Checked and consistent
- CatalogueReference and the item's CatalogueDocumentReference resolve to 02-Catalogue.xml;
  CatalogueLineReference `1` is the bench line; price 520 XBL is the catalogue price.
- Quantity 24 = six pallets of four, within the catalogue's 4–192 and increments of 4.
- 24 × 520 = 12480.00; 5 % of 12480.00 = 624.00; 12480.00 − 624.00 = 11856.00.
- The additional reference `BS-RE-26-0222` resolves to 06-RetailEvent.xml.
- BuyerContact, DeliveryContact and AccountingContact, and the seller's despatch, accounting and
  seller contacts, fit their roles.
- TransactionConditions `LD-TC-01` with ActionCode "Accepted" is the buyer accepting the seller's
  conditions named in the catalogue.

## Considered and refuted
- `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID`:
  a moss green variant `GRN` that the catalogue does not list — refuted because a buyer may propose an
  alternative the catalogue does not carry; the seller can decline it.
- `/Order/cac:ValidityPeriod/cbc:EndDate`: the order is valid until 2026-04-26 while delivery is on
  the 30th — refuted because the validity period is the period in which the order may be accepted
  (10-DocumentStatus.xml reports it accepted on the 26th), not the delivery period.
