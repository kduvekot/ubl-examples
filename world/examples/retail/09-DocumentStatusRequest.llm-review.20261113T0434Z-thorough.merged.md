# LLM review: 09-DocumentStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/09-DocumentStatusRequest.xml`, Git blob `68cae595b7754cc365ebfdb3b09245cd84b8e2fc` (committed)
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

### retail/09#F1 · High · The status request is issued after the status that answers it
- XPath: `/DocumentStatusRequest/cbc:IssueDate` = `2026-04-26`
- XPath: `/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `/DocumentStatusRequest/cbc:Note` = `Has the order been accepted?`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cbc:IssueDate` = `2026-04-26`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: a DocumentStatusRequest is "A document used to request the status of a collaboration/process associated with a document". This one asks "Has the order been accepted?" about `BS-PO-26-0224`; 10-DocumentStatus answers it ("Accepted and booked.", same order, same day), but is issued at 11:14, 38 minutes before this request at 11:52. The merge tried the reading that 10 was sent unprompted and the two crossed: then the buyer would ask about a status it had already received 38 minutes earlier, and 09 would have no reason in the flow. The times are the only link between the two documents (DocumentStatus has no reference to the request).
- Condition: the request is issued before the document status that answers it (date and time).
- Options: (a, preferred) a request time before 11:14, or a status time after 11:52 in 10 (either works: 10 also refers to the transport request 11 of 2026-04-25 10:28); (b) if the status is meant to be unprompted, drop the request from the flow.
- Needs decision: no
- From: broad, context, logistics

### retail/09#F2 · Medium · Language codes in LocaleCode
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code `Language/cbc:ID` already holds and names no locale. 362 such elements in 213 XML files (recounted in the merge, see 08-Order's merged review).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as English as used in Bayvarra from a locale list (context preferred this; aligned with all merges on dropping).
- Needs decision: no
- From: broad, context, parties

### retail/09#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; "Gate 3" is an entrance of the distribution centre, which matters only to vehicles, not a street name. 79 occurrences in 76 XML files (recounted).
- Condition: no `AdditionalStreetName` of Lumeway holds the gate.
- Options: (a, preferred) drop it from the postal address (party master data); (b) if Bayvarra's address format makes the gate part of the postal address, record that and dismiss the finding.
- Needs decision: no
- From: broad, parties

### retail/09#F4 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: the name (and e-mail) is the buying office, the job title and department are those of a seller's customer service; they contradict each other. As the sender asking about its order, the buying office fits the role. The same contact is used for Brightmarket in every role in the flow.
- Condition: name, job title and department agree with each other and with Brightmarket's role here.
- Options: (a, preferred) a buyer's job title in purchasing for the buying office; role-specific contacts elsewhere.
- Needs decision: no
- From: broad, parties

### retail/09#F5 · Low · Party master data a status request does nothing with
- XPath: `/DocumentStatusRequest/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: a one-line question about an order's status uses neither Brightmarket's logo, web shop and social-media profile, nor the parties' share capital and tax registrations, nor Lumeway's customs trader number (no example of this domestic flow is a customs document). They are the parties' master data, identical in every example (IND5/IND6). The parties part also notes that `CorporateStockAmount` is defined as "The number of shares in the capital stock of a corporation" while the world uses it for the share capital (an amount): a candidate for the TC write-up, which does not change what this document should carry.
- Condition: the parties carry only what the request uses (identification, name, electronic address, contact).
- Options: (a, preferred) drop them from this document; keep logo, shop and social media for the consumer documents and the customs number for customs flows; record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context (with the signature, split in the merge), parties

### retail/09#F6 · Low · Signature with an ID and a signatory only
- XPath: `/DocumentStatusRequest/cac:Signature/cbc:ID` = `BM-SIG-26-DSR`
- Why: the signature has no method, no attachment and no date: it records no signature, and a status question needs none. World-wide convention (137 of 147 `Signature` aggregates hold only ID and signatory, lxml count of the air merge), so changing it is a decision.
- Condition: a signature carries what makes it one, or is absent.
- Options: (a, preferred) drop it.
- Needs decision: yes
- From: context (Needs decision no there; set to yes, aligned with retail merges a and c, air and utilities)

## Checked and consistent
- `RequestedDocumentReference` `BS-PO-26-0224` resolves to 08-Order, issued two days earlier by the same sender to the same receiver; the order's validity ends on 2026-04-26, the day of the request, which gives the question a reason.
- `TrackingID` `BS-PO-26-0224` identifies the business process by the order number.
- Sender and receiver are the order's buyer and seller, described identically in every retail example (parties part, leaf by leaf); register IDs agree with `CompanyID` and the endpoint IDs; GLN check digits correct.

## Considered and refuted
- `/DocumentStatusRequest/cbc:TrackingID` = `BS-PO-26-0224`: suspected an order number misused as tracking ID — refuted because UBL defines it as "An identifier for tracking status of the business process", and the process here is identified by the order (from broad; context and logistics listed it as consistent).
- `/DocumentStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse for a business park — refuted because the definition fits a business park, and "Plot 14" is the land parcel (from parties).

## Changed in the merge
- broad/F1, context/F1, logistics/F1 → F1: combined; the merge's check of the "unprompted status" reading added.
- broad/F2, context/F2, parties/F1 → F2: combined; context's preferred option (en-XB) made option (b), aligned with all merges.
- broad/F3, parties/F2 → F3; broad/F4, parties/F5 → F4: combined.
- context/F3 → split into F5 (master data) and F6 (signature); parties/F3, F4, F6 folded into F5. parties/F4 (CorporateStockAmount) Needs decision yes → no, with its TC note, aligned with retail a/c and earlier flows. The tax schemes, named in context's Why without an XPath, given their XPaths.
- F6: Needs decision no → yes (world-wide convention).
