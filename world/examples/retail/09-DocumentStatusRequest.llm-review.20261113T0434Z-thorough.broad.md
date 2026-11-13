# LLM review: 09-DocumentStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/09-DocumentStatusRequest.xml`, Git blob `68cae595b7754cc365ebfdb3b09245cd84b8e2fc` (committed)
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

### retail/09#F1 · High · The status request is issued after the status that answers it
- XPath: `/DocumentStatusRequest/cbc:IssueDate` = `2026-04-26`
- XPath: `/DocumentStatusRequest/cbc:IssueTime` = `11:52:00`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cbc:IssueTime` = `11:14:00`
- XPath: `10-DocumentStatus.xml:/DocumentStatus/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: the request asks "Has the order been accepted?" about order `BS-PO-26-0224`. The document status that answers it, 10-DocumentStatus (same order, same day), was issued at 11:14, 38 minutes before this request at 11:52. Either the status was not a response to this request, or one of the times is wrong; as encoded the answer precedes the question.
- Condition: the request is issued before the document status that answers it.
- Options: (a, preferred) a request time before 11:14 (or a status time after 11:52); (b) if the status was sent unprompted, the request has no reason to exist in the flow.
- Needs decision: no

### retail/09#F2 · Medium · Language codes in LocaleCode
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/09#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/DocumentStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/09#F4 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DocumentStatusRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. As the sender asking about its order, the buying office fits the role. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail (compared by script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of the contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office, or a contact fitting this role; (b) different contacts per role, if the world gives Brightmarket several.
- Needs decision: no

## Checked and consistent
- The requested document `BS-PO-26-0224` resolves to 08-Order, issued two days earlier by the same sender to the same receiver; the order's validity ends on 2026-04-26, the day of the request, which explains the question.
- Sender and receiver are the order's buyer and seller, described as in every retail example.

## Considered and refuted
- `/DocumentStatusRequest/cbc:TrackingID` = `BS-PO-26-0224`: suspected an order number misused as a tracking ID — refuted: UBL defines it as "An identifier for tracking status of the business process", and the business process here is identified by the order.
