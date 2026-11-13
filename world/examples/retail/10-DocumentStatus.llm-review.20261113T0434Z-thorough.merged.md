# LLM review: 10-DocumentStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/10-DocumentStatus.xml`, Git blob `862ae5d80ac13b0164755f867566718b3cc3bf6b` (committed)
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

### retail/10#F1 · High · The document status is issued before the request it answers
- XPath: `/DocumentStatus/cbc:IssueDate` = `2026-04-26`
- XPath: `/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `/DocumentStatus/cbc:Note` = `Accepted and booked.`
- XPath: `09-DocumentStatusRequest.xml:/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `09-DocumentStatusRequest.xml:/DocumentStatusRequest/cac:RequestedDocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: a DocumentStatus is "A document used to provide information about the status of a collaboration/process associated with a document". In this flow it answers 09-DocumentStatusRequest ("Has the order been accepted?", same order `BS-PO-26-0224`, same day), but it is issued at 11:14, 38 minutes before the request (11:52). Read as an unprompted status, the request that follows it would have no reason (see 09's merged review).
- Condition: the document status is issued after the request it answers.
- Options: (a, preferred) a status time after 11:52 (e.g. 12:14), or the request in 09 before 11:14; both fit the rest of the timeline (the transport request 11 is of 2026-04-25 10:28).
- Needs decision: no
- From: broad, context, logistics

### retail/10#F2 · Medium · Language codes in LocaleCode
- XPath: `/DocumentStatus/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is a language code and names no locale. 362 such elements in 213 XML files (recounted in the merge).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as English as used in Bayvarra from a locale list.
- Needs decision: no
- From: broad, context, parties

### retail/10#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/DocumentStatus/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; "Gate 3" is a vehicle entrance of the distribution centre, not a street name. 79 occurrences in 76 XML files (recounted).
- Condition: no `AdditionalStreetName` of Lumeway holds the gate.
- Options: (a, preferred) drop it from the postal address (party master data); (b) if Bayvarra's address format makes the gate part of the postal address, record that and dismiss the finding.
- Needs decision: no
- From: broad, parties

### retail/10#F4 · Low · "Accepted" reported to the buyer for Lumeway's own transport request
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:DocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:Response/cbc:ResponseCode` = `AP`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `AdditionalDocumentResponse` is "A document linked or related to the document for which the status was requested". `LD-TR-26-0227` is 11-TransportExecutionPlanRequest, which Lumeway sent to Bayforth; Brightmarket never received it, and the reference has no type or description. "Accepted" can only be Bayforth's answer, but the response does not say who accepted it, and no acceptance by Bayforth exists in the flow: the plan `BF-TEP-26-0227` that 14-TransportationStatusRequest refers to is in no example (see 14's merged review). Read literally, Lumeway reports that its own request is accepted. Not High: the note's "booked" is possible at this time (11 was issued the day before), and the missing plan is 14's finding.
- Condition: the status reports only on documents the buyer can place, or the response about the transport request says what the document is and who accepted it, consistent with what the flow shows.
- Options: (a, preferred) drop the additional response and keep "booked" in the note (the buyer asked only about its order); (b) refer to Bayforth's plan once it exists in the flow, with a document type and Bayforth as `IssuerParty` of the response; (c) keep the reference with a document type ("Transport booking") and a response description.
- Needs decision: no
- From: broad, context, logistics, parties

### retail/10#F5 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: name and e-mail are the buying office, job title and department those of a seller's customer service; they contradict each other. As receiver of its order's status the buying office fits the role. Same contact in every role in the flow.
- Condition: name, job title and department agree with each other and with Brightmarket's role here.
- Options: (a, preferred) a buyer's job title in purchasing for the buying office; role-specific contacts elsewhere.
- Needs decision: no
- From: broad, parties

### retail/10#F6 · Low · Party master data a status message does nothing with
- XPath: `/DocumentStatus/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/DocumentStatus/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/DocumentStatus/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/DocumentStatus/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- Why: a status message uses neither Brightmarket's logo, web shop and social media, nor the parties' share capital and tax registrations, nor Lumeway's customs trader number in a domestic flow without customs documents (IND5/IND6); they are the parties' master data. `CorporateStockAmount` is defined as "The number of shares in the capital stock of a corporation" while the world uses it for the share capital: a candidate for the TC write-up (parties part).
- Condition: the parties carry only what the status message uses.
- Options: (a, preferred) drop them here; record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context (with the signature, split in the merge), parties

### retail/10#F7 · Low · Signature with an ID and a signatory only
- XPath: `/DocumentStatus/cac:Signature/cbc:ID` = `LD-SIG-26-DS`
- Why: no method, no attachment, no date: the aggregate records no signature. World-wide convention (137 of 147 `Signature` aggregates, lxml count of the air merge).
- Condition: a signature carries what makes it one, or is absent.
- Options: (a, preferred) drop it.
- Needs decision: yes
- From: context (Needs decision no there; set to yes, aligned with retail merges a and c, air and utilities)

## Checked and consistent
- `DocumentResponse` refers to 08-Order (`BS-PO-26-0224`) with response code `AP` (UNTDID 4343 "Accepted"), matching the note; issued on 2026-04-26, the last day of the order's validity.
- `LD-TR-26-0227` resolves to 11-TransportExecutionPlanRequest, issued 2026-04-25 10:28, before this status, so "booked" is possible at this time.
- Sender and receiver are seller and buyer of the order, described identically in every retail example (parties part); register IDs agree with `CompanyID` and endpoint IDs.

## Considered and refuted
- `/DocumentStatus/cac:SenderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse for a business park — refuted because the definition fits a business park, and "Plot 14" is the land parcel (from parties).

## Changed in the merge
- broad/F1, context/F1, logistics/F1 → F1; broad/F2, context/F2, parties/F1 → F2; broad/F3, parties/F2 → F3; broad/F5, parties/F6 → F5: combined.
- broad/F4, context/F3, logistics/F2, parties/F7 → F4: four parts' findings about the same response combined; their options kept as (a)–(c).
- context/F4 → split into F6 (master data) and F7 (signature); parties/F3, F4, F5 folded into F6; parties/F4 (CorporateStockAmount) Needs decision yes → no with its TC note, aligned with retail a/c and earlier flows. Tax-scheme XPaths added.
- F7: Needs decision no → yes (world-wide convention).
