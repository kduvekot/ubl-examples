# LLM review: 10-DocumentStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/10-DocumentStatus.xml`, Git blob `862ae5d80ac13b0164755f867566718b3cc3bf6b` (committed)
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/10#F1 · High · The document status is issued before the request it answers
- XPath: `/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `09-DocumentStatusRequest.xml:/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `09-DocumentStatusRequest.xml:/DocumentStatusRequest/cac:RequestedDocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: this status reports on order `BS-PO-26-0224`, the document 09-DocumentStatusRequest asks about on the same day. It is issued at 11:14, before the request (11:52). As encoded the answer precedes the question.
- Condition: the document status is issued after the request it answers.
- Options: (a, preferred) a status time after 11:52 (or a request time before 11:14).
- Needs decision: no

### retail/10#F2 · Medium · Language codes in LocaleCode
- XPath: `/DocumentStatus/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/10#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/DocumentStatus/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/10#F4 · Low · Acceptance reported for Lumeway's own transport request, a document the receiver does not know
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:DocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DocumentStatus/cac:AdditionalDocumentResponse/cac:Response/cbc:ResponseCode` = `AP`
- Why: `AdditionalDocumentResponse` is "A document linked or related to the document for which the status was requested". `LD-TR-26-0227` is 11-TransportExecutionPlanRequest, which Lumeway sent to Bayforth Forwarding; Brightmarket has never received it. The response code "Accepted" says the transport request was accepted, which only Bayforth could do, and no acceptance by Bayforth exists in the flow (14-TransportationStatusRequest refers to a transport execution plan `BF-TEP-26-0227` that no example carries). The reference without any description tells Brightmarket nothing.
- Condition: an additional document response refers to a document whose status the receiver can understand, with a status that the flow supports; or it is absent.
- Options: (a, preferred) drop it, and let the note say that transport is booked; (b) keep it with a document type or description ("transport booked with the carrier") and a response code that describes Lumeway's own status of it, if the world's list has one.
- Needs decision: no

### retail/10#F5 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DocumentStatus/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. As the receiver of the status of its order, the buying office fits the role. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail (compared by script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of the contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office, or a contact fitting this role; (b) different contacts per role, if the world gives Brightmarket several.
- Needs decision: no

## Checked and consistent
- The document response refers to 08-Order (`BS-PO-26-0224`), with response code `AP` (Accepted, UN/EDIFACT 4343) and the note "Accepted and booked."; it is issued on 2026-04-26, the last day of the order's validity.
- 11-TransportExecutionPlanRequest, the referenced transport request, was issued on 2026-04-25, before this status.
- Sender and receiver are seller and buyer, described as in every retail example.
