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
| Items | `world/items.json` | what the parties sell: goods and services, with prices |
| UBL model | `world/ubl-model.json` | extracted from the UBL 2.5 semantic model |
| Code lists | `world/codelists/` | UBL default code lists with the world's codes added |

## Countries

The world has three countries: Urvania, Bayvarra and Lisavu, whose
initials spell UBL. Two share a land border on the mainland; the third is
an island overseas. They differ on purpose, so that the
examples show how UBL carries different national arrangements in the same
structure:

- **Urvania (XU)** has a value added tax in the style of the EU VAT:
  charged at every stage, deducted by businesses, not charged on exports.
- **Bayvarra (XB)** is a federal country whose states levy a retail sales
  tax, charged once, on the sale to the final consumer. Sales for resale,
  exports and sales to public bodies are exempt.
- **Lisavu (XL)** has no general sales tax. Customs collects a customs
  duty and an import consumption tax when goods enter the island.

The tax schemes are identified with UN/EDIFACT 5153 codes: `VAT`, `STT`
(state or provincial sales tax), `CUD` (customs duty) and `IMP` (import
tax). Because 5153 has no code for a national sales tax, Bayvarra levies
its sales tax at state level, which also gives the state in its addresses a
purpose.

XU, XB and XL are ISO 3166-1 user-assigned codes, which exist for exactly
this purpose; each follows the initial of its country's name. ISO 4217 has
no such range for currencies. The world's currencies follow the ISO 4217
convention of the country code plus the initial of the currency's name:
the ferra of Urvania (`XUF`), the lume of Bayvarra (`XBL`) and the coral of
Lisavu (`XLC`). The convention limits the names: ISO 4217 already uses
`XUA` and `XBA` to `XBD`, so Urvania's currency cannot start with an A and
Bayvarra's not with A to D. Each code is checked against the current
ISO 4217 list, so that none is a real code.

The three currencies also differ in their minor unit, because currencies
do: the ferra has none (amounts are whole ferra, as with the Japanese yen),
the lume has two decimals, and the coral three (as with the Bahraini or
Kuwaiti dinar). An example that only ever shows two decimals hides a case
that software must handle. Neither the countries nor
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

## Items

Every party that sells has items. Goods carry what the documents along
their way need: a seller's item identifier, a world item number issued by
the identifier issuing agency (twelve digits with a check digit, a scheme of
the world, not a GTIN), a Harmonized System customs tariff code, the country
of origin, dimensions, net and gross weight, and the packaging. Services
have a unit and a price. Units of measure and packaging types are UN/ECE
Recommendation 20 and 21 codes from the UBL default code lists. Prices are
in the seller's currency. A unit price may be finer than the currency, as
an electricity tariff of 27.3 ferra per kilowatt hour is, but every amount
to pay is rounded to the currency's minor unit.

Items connect the chains. The park bench is made with slats from the
sawmill and film from the packaging maker; the distributor resells the
bench, and its own item points to the manufacturer's, so the maker's
identifiers travel along. A component or a resold item is only possible
if the maker or reseller orders it from that seller somewhere in the flows.

The maker's facts travel with the item wherever it appears: brand and
model, properties with their test method and accepted range, certificates,
the carbon footprint and the circularity profile. What belongs to one
delivery is added only where the goods move: a despatch advice names the
production lot, or the serial number of every casting, which stays the same
when a cancelled despatch advice is replaced. A catalogue line adds the
seller's terms (lead time, minimum and maximum quantity, the price list and
its validity), and a till receipt during a promotion shows the discount on
the shelf price.

## Flows of documents

The parties do business in flows. Each country has its own raw material
and industry: Urvania mines ore and makes park benches, recovering its
production waste as recycled plastic; Bayvarra saws timber, makes furniture,
packaging and clothing, and distributes and retails; the island Lisavu grows
and gins cotton, its export. Goods cross the land border by road, rail and
river barge and go overseas by sea and air in both directions; there is a
public tender, a temporary export with an ATA carnet, and a utility in each
country. Each flow starts from the business: who buys
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
