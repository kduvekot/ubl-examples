# Checking the examples

The world is checked automatically every time the site is built. A build
with a problem stops. The checks are layered like the world itself.

## The world against the UBL 2.5 model

Every document in the world is checked against the UBL 2.5 semantic model:

- every place where a party is mentioned exists in the structure of that
  document type;
- the sender fills a sender element of the document and the receiver a
  receiver element, or the document says on whose behalf they act, as a
  customs broker does for an importer;
- every mandatory party element at document level is filled;
- every party of the world takes part in at least one document.

## Only what UBL 2.5 endorses

The examples use only document types, associations and properties that
UBL 2.5 endorses. Anything the model marks as deprecated is rejected. A
transport service, for example, is invoiced with the Invoice, because the
Freight Invoice is deprecated.

## Nothing empty, nothing implied

Two rules of the UBL specification shape the data the world needs:

- **No empty elements (IND5).** A UBL document never contains an element
  without content: an aggregate needs a child, a basic element a value, and
  a value of only spaces counts as empty. Every party element must
  therefore hold at least one of its parts, even though none of them is
  mandatory in the schema. The identity of every party makes sure there is
  always something to put in it.
- **One text per language (IND7, IND8).** Two sibling text elements of the
  same name never have the same `languageID`, and never both lack one. A
  text element repeats only to give the same text in another language, as
  the bilingual notes do; several keywords of an item therefore go in one
  search string. The text elements are the basic properties whose data type
  in the UBL 2.5 model is Text or Name: their schema types derive from the
  CCTS text type, which carries `languageID`.
- **No empty attributes (IND9).** Every attribute that is present has a
  value.
- **An absence carries no meaning (IND6).** Leaving an element out never
  says anything; the sender states every value that matters, and every sum
  (section 2.2.2, "Manifest Values"). An order without a carrier does not
  say that the seller arranges the transport: its delivery terms must say
  so. The world therefore requires values that would otherwise be implied,
  such as the delivery terms of every order.

## The parties

The identity of every party is checked: every party has a name and every
organisation an identifier; tax numbers and account numbers carry valid
check digits; the city in the address is the nearest town or locality of
the party's own country and state; every account is held at a bank of the
world in the same country; and a bank named in a document is the bank where
that party keeps its account. The ISIN of a listed company has the
structure and check digit of ISO 6166 and starts with its country's code.

## The items

Units and packaging types must be codes of the UBL default lists; world
item numbers carry a valid check digit and are unique; prices are positive
and in the seller's currency; gross
weight is at least net weight. Every party that bills or offers in a
document has items to put on its lines, and every party with items bills
or offers them. The exchange rates between the currencies agree with each
other.

## The map and the code lists

The map is checked as a structure: one connected road network per
landmass, houses on streets, nothing built on roads or water, believable
terrain, and customs posts where roads cross a border. The world's code
lists are checked to hold exactly the codes of the countries layer.

## The example documents

The build checks that a reference to another document of the same flow
quotes that document's UUID wherever it gives one. Every example document is
validated in the two phases UBL prescribes:

- **Phase 1:** against the UBL 2.5 runtime schema of its document type,
  from the endorsed set.
- **Phase 2:** its coded values against the code lists, using UBL's
  context/value associations (CVA). It runs twice. First UBL's own phase 2,
  unchanged, with the UBL default code lists: it must object to exactly the
  world's country and currency codes and to nothing else. Then the same
  associations with the world's code lists in place of the defaults: here
  every value, and the list identifier where a document gives one, must
  pass.

The committed examples must also be up to date: they are generated again
from the world's layers and compared, so a change in the world cannot leave
an example behind.

## Still to come

Later layers add their own checks: document lines with items and
quantities, amounts and taxes that add up, dates in a believable order, references between documents,
and quantities that agree from order to invoice. These apply to the
example documents as they are generated for every flow.
