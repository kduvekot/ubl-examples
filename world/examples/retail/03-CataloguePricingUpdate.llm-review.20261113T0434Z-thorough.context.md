# LLM review: 03-CataloguePricingUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/03-CataloguePricingUpdate.xml`, Git blob `fa746f7555ca2bc6ffeef41cf02e3ca5ac1ffe9d` (committed)
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

### retail/03#F1 · High · The pricing update line points at the bench, not the side frame
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cbc:ID` = `1`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- XPath: `/CataloguePricingUpdate/cbc:Name` = `Price change of the side frame`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Name` = `Bench side frame casting`
- Why: the line's ID is "An identifier for the catalogue line to be updated". In the catalogue
  being updated (02-Catalogue.xml, `LD-CAT-26-0218`) line `1` is the park bench at 520 XBL and line
  `2` the side frame at 64 XBL. The update line carries no item, so by its ID it sets the bench's
  price to 58 XBL, while the document's name and description say the side frame's price changes (and
  58 is a plausible new price for a 64 XBL part, not for a 520 XBL bench).
- Condition: the update line identifies the side frame's catalogue line (and, if an item is given,
  the side frame).
- Options: (a) preferred: line ID `2`, matching the catalogue line, optionally with the item's
  seller's identification `LD-10443` so the receiver can check it; (b) keep the ID and change the
  story to a bench price change (implausible at 58 XBL).
- Needs decision: no

### retail/03#F2 · High · Reference to the catalogue gives an issue time and a revision that are not the catalogue's
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CataloguePricingUpdate/cbc:IssueDate` = `2026-05-20`
- Why: in the CatalogueReference, IssueTime is "The time at which the catalogue was issued" and
  RevisionDate "The date on which the information in the catalogue was last revised". The catalogue
  was issued at 17:28; 09:00 is its RevisionTime
  (`02-Catalogue.xml:/Catalogue/cbc:RevisionTime` = `09:00:00`). The last revision is dated
  2026-05-21, the day after this update was issued (2026-05-20) and the issue date of the next
  update, 04-CatalogueItemSpecificationUpdate.xml; a document cannot know of a revision made the day
  after it was sent.
- Condition: the reference's issue date and time are those of 02-Catalogue.xml, and its revision
  date/time are not later than this document's issue.
- Options: issue time 17:28:00; revision date/time either the catalogue's own revision (2026-04-20
  09:00) or left out, since this update itself is the revision.
- Needs decision: no

### retail/03#F3 · Medium · Catalogue revised after the document announcing the revision was issued
- XPath: `/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `/CataloguePricingUpdate/cbc:IssueTime` = `13:10:00`
- Why: RevisionDate/RevisionTime are "The date/time, assigned by the seller, on which the Catalogue was
  revised". The update was issued at 13:10 and says the catalogue was revised at 14:00 the same day,
  i.e. in the future. A revision that takes effect later is expressed by the validity period, which
  here already starts on the issue date.
- Condition: the revision time is not later than the issue time.
- Options: a revision time before 13:10 (preferred), or no revision time.
- Needs decision: no

### retail/03#F4 · Medium · A language code in LocaleCode
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value is the
  ISO 639 language code (listID `ISO 639`). Same pattern in 213 examples (`grep -l` over `*.xml`).
- Condition: LocaleCode holds a locale code or is absent.
- Options: a locale such as `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/03#F5 · Low · The whole previous price list is marked replaced by a list that holds one price
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cac:PreviousPriceList/cbc:StatusCode` = `REPLACED`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`
- Why: PreviousPriceList is "The previous price list"; its status says price list `LD-PL-2026` is
  replaced. That list also carries the bench price of catalogue line 1, which this update leaves
  untouched. After the update the bench price would belong to a price list marked replaced.
- Condition: the status of the previous price list fits what happens to the other prices on it.
- Options: (a) preferred: the new list `LD-PL-2026-2` as a revision covering both prices, or no
  status on the previous list; (b) also update line 1 to the new list.
- Needs decision: no

### retail/03#F6 · Low · Trading terms that say only "Unchanged."
- XPath: `/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`
- Why: TradingTerms are "The trading terms associated with the Catalogue", and Information is "Text
  describing the terms of a trade agreement". "Unchanged." describes no term; an update that does not
  touch the terms simply leaves them out (nothing is implied by absence of a change element).
- Condition: TradingTerms carries terms, or is absent.
- Options: drop it (preferred).
- Needs decision: no

### retail/03#F7 · Low · Line-level contract parties repeat the header
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: they are the customer and seller "responsible for the contract associated with the catalogue
  line being updated"; the one contract is the header's `LD-BM-SUPPLY-2026` with the same parties.
- Condition: line-level contract parties only where they differ from the header.
- Options: drop them.
- Needs decision: no

### retail/03#F8 · Low · Signature and master data the update does nothing with
- XPath: `/CataloguePricingUpdate/cac:Signature/cbc:ID` = `LD-SIG-26-1.1`
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the signature has only an ID and a signatory (no method, no attachment), so it signs nothing;
  a domestic price change uses neither a customs trader number nor a social-media profile, nor the
  share capital and tax registrations the parties carry. They look copied from master data
  (IND5/IND6).
- Condition: everything in the parties and the signature has a use in a pricing update.
- Options: drop the signature and the master-data detail.
- Needs decision: no

## Checked and consistent
- RelatedCatalogueReference ID, UUID, IssueDate, VersionID `1.0` and Description match
  02-Catalogue.xml; this update's VersionID `1.1` follows it.
- The validity period (2026-05-20 to 2026-07-19) ends with the catalogue's validity.
- ReferencedContract `LD-BM-SUPPLY-2026` and the parties match 02-Catalogue.xml.
- The order 08-Order.xml (2026-04-24) predates the change, so its prices are not affected.

## Considered and refuted
- `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:PreviousVersionID`: repeats the
  catalogue's own `0.9` — refuted here because the reference faithfully copies 02; the question
  whether 02 may have a previous version at all belongs to 02's review.
- `/CataloguePricingUpdate/cbc:Description`: repeats the Name — refuted because a short description
  identical to the name is harmless.
