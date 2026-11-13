# LLM review: 08-TransportServiceDescription.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/08-TransportServiceDescription.xml`, Git blob `3b64d9a508af69f9f2be5711a0061f17a39e8741` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/08#F1 · Medium · A language code in LocaleCode
- XPath: `/TransportServiceDescription/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/08#F2 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/08#F3 · Low · Lumeway Distribution’s sales customer-service contact used in a transport role
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportServiceDescription/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: In this example Lumeway Distribution is the receiver of the carrier’s service description, i.e. the shipper choosing a sailing. Its only contact is the sales department’s customer service, the same as in the catalogue and the order documents. For the questions this document raises (cargo, pickup, export formalities) the carrier, forwarder or authority needs Lumeway’s shipping or despatch contact; the checklist asks that a contact fit the party’s role in the document.
- Condition: The contact given for Lumeway Distribution in this example is one that handles the shipment (despatch, shipping or export), or there is none.
- Options: Preferred: give Lumeway Distribution a despatch or shipping contact for its transport roles. Alternative: leave the contact out of the transport documents where nobody needs to reach Lumeway about the shipment.
- Needs decision: no

## Checked and consistent
- Sender, signatory, transport service provider and responsible transport service provider are all Tidewell Ocean Lines; the receiver is Lumeway Distribution, the sender of the request this document answers (07-TransportServiceDescriptionRequest.xml), so the parties of request and response match.
