# Choosing and documenting values

Every value in an example document comes with the reason why it is that
value. The reason is recorded where the value is made, and a document with
a value without a reason is not built.

## Where values come from

A value in an example comes from one of these sources, and its reason says
which:

- **The world's layers.** Party names, addresses, identifiers and accounts
  come from the identity of the party; items, their identifiers, customs
  tariff codes and prices from the items layer; currencies and tax rates
  from the countries layer. These values are the same in every document
  that uses them.
- **The structure of the flow.** Which party sends the document, which
  receives it, and which other parties it names, at which place, come from
  the flow of documents, so the parties always sit where the business puts
  them.
- **The scenario of the flow.** Document numbers, dates, quantities and the
  references between documents are what a flow adds; each carries its own
  reason, in business terms.
- **Code lists.** Coded values come from the UBL default code lists or the
  world's own lists, and the reason names the list and the meaning of the
  code.
- **Calculation.** Amounts are calculated from quantities and prices and
  rounded to the minor unit of the currency; the reason states the
  calculation. Every sum is stated in the document, as UBL requires, and
  never left to the receiver.

## What a reason contains

A reason says why the value fits the element: what the element means in
UBL, in this document, and what in the business situation makes this the
value. It refers to the UBL definition and to the world's data first; a
country rule or a specific process appears only as an illustration. For
example, the quantity on an invoice for bulk ore is the weighed quantity
from the despatch advice, not the ordered quantity, and its reason says so.

## Only what UBL 2.5 endorses

The documents use only endorsed document types and elements, and they are
validated against the schemas of the endorsed document types. Where UBL 2.5
replaced an element, the examples use the replacement: a party's electronic
address, for instance, is carried in `ElectronicAddress`, because
`Party/EndpointID` is deprecated.

## Kept apart from the TC examples

The generated examples are kept in `world/examples/`, apart from the
examples of the OASIS UBL Technical Committee in `xml/`, whose history is
the base of this repository.
