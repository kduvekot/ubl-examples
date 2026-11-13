# LLM review: 03-CataloguePricingUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/03-CataloguePricingUpdate.xml`, Git blob `fa746f7555ca2bc6ffeef41cf02e3ca5ac1ffe9d` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/03#F1 · High · Revision time after the issue time
- XPath: `/CataloguePricingUpdate/cbc:IssueDate` = `2026-05-20`
- XPath: `/CataloguePricingUpdate/cbc:IssueTime` = `13:10:00`
- XPath: `/CataloguePricingUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- Why: `RevisionDate`/`RevisionTime` are "The date/time, assigned by the seller, on which the Catalogue was revised". The update is issued on 2026-05-20 at 13:10 and reports a revision at 14:00 the same day, 50 minutes after it was sent: two values of this document contradict each other in their order. If 14:00 is meant as the time from which the new price applies, that is the validity period's job (`/CataloguePricingUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`, which could carry a `StartTime`).
- Condition: the revision date and time are not later than the issue date and time.
- Options: (a, preferred) a revision time at or before 13:10 (or none); (b) if the change takes effect at 14:00, a `StartTime` in the validity period and the revision time when the revision was made.
- Needs decision: no
- From: broad (High), logistics (Medium), context (Medium)

### retail/03#F2 · High · Reference to the catalogue gives an issue time and a revision that are not the catalogue's, one of them in the future
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionDate` = `2026-04-20`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionTime` = `09:00:00`
- Why: the reference resolves to 02-Catalogue (same ID and UUID), and in a CatalogueReference `IssueTime` is "The time at which the catalogue was issued" and `RevisionDate` "The date on which the information in the catalogue was last revised". Verified against 02: the catalogue was issued at 17:28; 09:00 is its revision time. The reference's last revision, 2026-05-21 14:00, is neither 02's revision (2026-04-20 09:00) nor possible here: it is the day after this update was issued (2026-05-20 13:10), and the issue date of the next update, 04 (issued 2026-05-21 09:01, so 14:00 is after 04 as well). The same reference values recur in 04 and 20 (verified: `grep -l 'RevisionDate>2026-05-21'` finds 03, 04 and 20).
- Condition: the reference's issue date and time equal 02's, and its revision date and time are 02's revision (or the last revision before this document's issue), never later than this document's issue.
- Options: (a, preferred) `IssueTime` 17:28:00, revision 2026-04-20 09:00:00, copied from 02; (b) drop the dates and times and keep ID, UUID and version, since they identify the catalogue.
- Needs decision: no
- From: broad, logistics, context

### retail/03#F3 · High · The update line points to the bench line, but the update is for the side frame
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cbc:ID` = `1`
- XPath: `/CataloguePricingUpdate/cbc:Name` = `Price change of the side frame`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Name` = `Bench side frame casting`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `64`
- Why: `CataloguePricingUpdateLine/ID` is "An identifier for the catalogue line to be updated", and the line carries no item, so the ID is the only link. Line 1 of LD-CAT-26-0218 is the bench at 520; the side frame is line 2 at 64. As encoded the update sets the bench's price to 58, an 89 % cut (recomputed: 58 / 520 = 0.1115), while name and description announce a change of the side frame (64 → 58, −9.4 %).
- Condition: the pricing update line identifies line 2 of LD-CAT-26-0218, so that the price of 58 lands on the side frame.
- Options: (a, preferred, all parts) line ID `2`; (b) a bench price change, implausible at 58.
- Needs decision: no
- From: broad, money, logistics, context

### retail/03#F4 · Medium · A language code in LocaleCode
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats `Language/cbc:ID`. 362 occurrences in 213 files (verified).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a locale list (context's preference).
- Needs decision: no
- From: broad, parties, context

### retail/03#F5 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is a vehicle access detail, not a street name. 79 occurrences in 76 files (verified).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address; (b) record it in Bayvarra's address format.
- Needs decision: no
- From: broad, parties

### retail/03#F6 · Low · Signature without anything that signs
- XPath: `/CataloguePricingUpdate/cac:Signature/cbc:ID` = `LD-SIG-26-1.1`
- Why: the signature has only an ID and a signatory (no method, no attachment), so it records nothing a receiver could check, and the update has no story reason for a signature (IND5/IND6). 137 of 147 signatures in the world have this shape (lxml). The ID is built from this document's version number `1.1` rather than a signature numbering of Lumeway's own (compare `LD-SIG-26-0420` in 02).
- Condition: either a signature with a reason and its data, or none; a signature ID is the signer's own.
- Options: (a, preferred) drop it; (b) method and attachment with a reason, and an ID from Lumeway's numbering.
- Needs decision: yes (world-wide convention, as in the air and utilities merges)
- From: context (signature part of its F8)

### retail/03#F7 · Low · Party master data the pricing update does nothing with
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- Why: a domestic price change uses neither a customs trader number, nor the share capital, the logo, consumer web shop and social-media profile, nor the tax registrations (the update states no tax category); they are the parties' master data (section 4.8). `CorporateStockAmount` is defined as "The number of shares in the capital stock of a corporation" but holds the share capital: a definition/data type conflict for the TC write-up.
- Condition: the parties carry only what a pricing update uses.
- Options: (a, preferred) leave these values out; (b) keep share capital only where company law needs it and record the conflict for the TC.
- Needs decision: no
- From: parties (F3, F4, F5), context (F8, master-data part)

### retail/03#F8 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: name and e-mail fit the buyer receiving a price change; job title and department are a seller's customer service and contradict them. Same contact in 41 files (verified).
- Condition: name, job title and department agree with each other and with the buying role.
- Options: (a, preferred) buyer's job title in purchasing.
- Needs decision: no
- From: broad, parties

### retail/03#F9 · Low · Trading terms that say only "Unchanged."
- XPath: `/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`
- Why: `TradingTerms` are "The trading terms associated with the Catalogue" and `Information` "Text describing the terms of a trade agreement". "Unchanged." describes no term; it says that the catalogue's terms (`02-Catalogue.xml:/Catalogue/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store; 30 days net.`) still apply. Money and context: an update without trading terms already leaves them as they are, so the aggregate has no content (no-filler rule). Broad refuted: saying so explicitly avoids implying it by absence (IND6). Both readings of the agreed rules are possible, and the value occurs only in 03 and 04 (verified), so the convention is to be settled once.
- Condition: the update either has no `TradingTerms` or carries the terms that apply; the choice is documented as the reading of IND5/IND6 for updates.
- Options: (a, preferred) remove `TradingTerms` (money, context); (b) repeat the actual terms with the reference LD-GTC-2026, if the update is meant to be read alone; (c) keep "Unchanged." as the explicit statement (broad).
- Needs decision: yes
- From: money, context (broad refuted)

### retail/03#F10 · Low · Header contract parties repeated on the line
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: they are the parties responsible for the contract of the line, which is the header's one contract `LD-BM-SUPPLY-2026` with the same parties; repeating them adds nothing.
- Condition: line-level contract parties only where they differ from the header.
- Options: (a, preferred) drop them.
- Needs decision: no
- From: broad, context

### retail/03#F11 · Low · The side frame's dependent price percentage no longer matches its new price
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`
- Why: in the catalogue the side frame's price is also expressed as 12.31 % of the bench's (recomputed: 64 / 520 = 12.31 %). With the new price of 58 and the bench at 520 the relation is 58 / 520 = 11.15 %. The update changes the absolute price but says nothing about the dependent price reference, so after it the catalogue states two prices for the side frame (58, and 12.31 % × 520 = 64.01). Broad refuted it (an update may replace a dependent price by a fixed one); then the update should say so, because the reference stays in the catalogue line otherwise. (This holds once F3 is fixed; as encoded, the bench line is changed and the percentage gives 12.31 % × 58 = 7.14.)
- Condition: after the update, the side frame's price and its dependent price reference agree (11.15 % of 520 = 58), or the reference no longer applies.
- Options: (a, preferred) carry a `DependentPriceReference` with 11.15 % in the update line; (b) remove the reference from the catalogue if the frame's price does not follow the bench's.
- Needs decision: no
- From: money (broad refuted)

### retail/03#F12 · Low · The whole price list LD-PL-2026 is marked replaced, though the bench keeps its price on it
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cac:PreviousPriceList/cbc:ID` = `LD-PL-2026`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cac:PreviousPriceList/cbc:StatusCode` = `REPLACED`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`
- Why: the update marks `LD-PL-2026` as replaced by `LD-PL-2026-2`. In 02 that list holds both prices, and only the side frame's changes; after the update the bench's price sits on a list said to be replaced, and nothing says `LD-PL-2026-2` carries it.
- Condition: after the update it is clear which active price list holds each catalogue price.
- Options: (a, preferred) state that `LD-PL-2026-2` is a revision covering the whole range (or give the previous list no status); (b) keep `LD-PL-2026` active and give the new price its own list without declaring the old one replaced.
- Needs decision: no
- From: broad, money, context

## Checked and consistent
- `RelatedCatalogueReference` ID `LD-CAT-26-0218`, UUID `f5163e36-0159-5b9f-b172-a86137e369e6`, issue date 2026-04-20, `VersionID` 1.0 and `PreviousVersionID` 0.9 match 02; this update's `VersionID` 1.1 follows, and 04 continues with 1.2.
- Validity 2026-05-20 to 2026-07-19 starts on the issue date, lies within the catalogue's validity and equals the new price list's validity.
- `LineCountNumeric` `1` matches the single line; contract `LD-BM-SUPPLY-2026` and the parties match 02; the parties are described as in every retail example; GLN check digits correct.
- The order (2026-04-24) and invoice (2026-04-30) predate the change; no later document of the flow had to use the new price.
- New price 58 per 1 EA (base quantity given).

## Considered and refuted
- `/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`: filler — refuted by broad (explicit statement avoids implying by absence); not followed alone, kept as the Low/yes F9 with both readings (from broad).
- `/CataloguePricingUpdate/cbc:Description` = `Price change of the side frame`: repeats the name — refuted, a harmless repetition of a short name (from broad, context).
- `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`: conflicts with the dependent price of 02 — refuted by broad (an update may replace a dependent price by a fixed one); not followed, F11 (from broad).
- `/CataloguePricingUpdate/cbc:IssueDate` = `2026-05-20`: out of order after the order and invoice of April — refuted, a price change during the catalogue's validity is a later event of the same collaboration (from logistics).
- `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:PreviousVersionID`: repeats 02's `0.9` — refuted here, the reference faithfully copies 02; whether 02 may have a previous version is 02#F2 (from context).
- `/CataloguePricingUpdate/cac:ProviderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: misuse — refuted, a business park fits the definition (from parties).

## Changed in the merge
- broad/F2 (High), logistics/F3 (Medium), context/F3 (Medium) → F1: High, because two values of this document contradict each other in their order (section 6: a contradiction with another value in this example), as the road merges did for a despatch time after the issue time.
- broad/F3, logistics/F2, context/F2 → F2: combined; the link to 04's issue time added.
- broad/F1, money/F1, logistics/F1, context/F1 → F3; numbered after F1/F2 by position in the document.
- context/F8 split: the signature → F6 ("Needs decision" no → yes, aligned with the air and utilities merges; the ID built from the version number added by the merge); the master data → F7 with parties/F3, F4 (Low/yes → no, see 01#F6) and F5.
- money/F4 (no), context/F6 (no) → F9: "Needs decision" no → yes, because broad's IND6 refutation is a possible reading of the agreed rules.
- broad/F7, context/F7 → F10; broad/F8, money/F3, context/F5 → F12: combined.
- broad/F4, parties/F1, context/F4 → F4; broad/F5, parties/F2 → F5; broad/F6, parties/F6 → F8: combined.
