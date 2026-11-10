# The UBL example world

All examples take place in one fictional world. It is built in layers.
Each layer adds one kind of data, is kept in its own file, and is checked
before the next layer builds on it.

| Layer | File | What it holds |
|---|---|---|
| Countries | `world/countries.json` | names, currencies, tax schemes, identifier and address schemes |
| Parties | `world/parties.json` | the organisations: place on the map, role, identity |
| Map | `world/map.json` | routes, towns and localities |
| Documents | `world/documents.json` | the flows of documents between the parties |
| UBL model | `world/ubl-model.json` | extracted from the UBL 2.5 semantic model |
| Code lists | `world/codelists/` | UBL default code lists with the world's codes added |

## Countries

The world has three countries. Two share a land border on the mainland;
the third is an island overseas. They differ on purpose, so that the
examples show how UBL carries different national arrangements in the same
structure:

- **Country A (XA)** has a value added tax in the style of the EU VAT:
  charged at every stage, deducted by businesses, not charged on exports.
- **Country B (XB)** is a federal country whose states levy a retail sales
  tax, charged once, on the sale to the final consumer. Sales for resale,
  exports and sales to public bodies are exempt.
- **Country C (XC)** has no general sales tax. Customs collects a customs
  duty and an import consumption tax when goods enter the island.

The tax schemes are identified with UN/EDIFACT 5153 codes: `VAT`, `STT`
(state or provincial sales tax), `CUD` (customs duty) and `IMP` (import
tax). Because 5153 has no code for a national sales tax, Country B levies
its sales tax at state level, which also gives the state in its addresses a
purpose.

XA, XB and XC are ISO 3166-1 user-assigned codes, which exist for exactly
this purpose. ISO 4217 has no such range for currencies, so the world's
currencies (`XAW`, `XBW`, `XCW`) are invented and checked against the
current ISO 4217 list, so that none is a real code. Neither the countries nor
the currencies are in the UBL default code lists. UBL lets trading partners
use their own code lists in the second phase of validation, so the world
has its own: copies of the UBL 2.5 default lists, unchanged, with the
world's codes added and their own identification.

## Parties

The parties are the organisations of the world, chosen so that every party
role in every UBL document type can be filled (see the party cover
analysis). Each party has:

- a **role**, such as manufacturer, road carrier or contracting authority;
- a **place** on the map, in a town or a locality;
- an **identity**: a name, the identifiers of its country's schemes, a
  postal address in its country's format, an electronic address, a contact,
  and, where it is paid, an account at one of the world's banks.

Names are invented and checked against real organisations. E-mail
addresses use the reserved domain `.example` (RFC 2606), so that none can
reach a real organisation. Account numbers follow the structure of ISO 13616
with its check digits, using the world's country codes, but they are not
called IBANs, because the world's countries are not registered IBAN
countries.

## Flows of documents

The parties do business in flows: an ore delivery, goods by road, rail and
river across the land border, a retail chain, an overseas shipment by sea
and by air, a public tender, a temporary export with an ATA carnet, and the
removal of production waste. Each flow starts from the business: who buys
from whom, on which delivery terms, and therefore who arranges and pays the
transport. A distributor that buys free carrier (FCA) books the truck
itself and names the carrier in its order; a retailer that buys delivered
duty paid (DDP) leaves the transport to its supplier, who then needs an
outgoing waybill.

Every document in a flow records:

- the document type, its sender and its receiver;
- why it is sent, in business terms;
- every party it mentions, at its place in the UBL structure, for example
  the road carrier at `Order/Delivery/Despatch/CarrierParty`.

## Who sends and who receives

Who sends and who receives a document type comes from the UBL 2.5 semantic
model first: the elements `SenderParty` and `ReceiverParty`, or a definition
of the document or of one of its party elements, such as "The Party who
submits this Tender". Where the model does not say it, the party role table
of the UBL specification is used. Where neither says it, the choice is
marked as inferred, with the definitions it rests on. Every quote is checked
word for word against its source.
