# About this project

The UBL World is a fictional world made to show the Universal Business Language (UBL 2.5, an OASIS
Standard and ISO/IEC 19845) in use. Three countries, their companies and their public bodies exchange
the documents a real economy would exchange, and every value in every document comes with the reason
why it is that value: why this element, why this code, why this date, and how it agrees with the other
documents of the same trade.

It is meant for people who implement, teach or maintain UBL: a coherent set of examples in which a
value is never a filler, every element is used as its UBL definition says, and the documents of one
flow tell one consistent story.

## How it is made

The world is kept as data: its countries, parties, items, map and flows of trade. The example
documents are generated from that data, so a party, an address, a price or a tax rate is the same in
every document that carries it. Every build checks the documents against the UBL 2.5 schemas and the
world's code lists, and checks the world itself: the transport legs run on the map's routes, the
calendar and the issue order of the documents hold, and amounts, quantities and stock add up.

## How much of UBL 2.5 it covers

[Element coverage](coverage.html) counts the endorsed elements of UBL 2.5 that the documents use,
per document type, and lists every element that has no example yet. An element is added only through a
real business situation in the world, never as a filler, so some stay out on purpose.

## The OASIS sample documents

Next to the world, the repository holds the sample documents the OASIS UBL Technical Committee
published with each release of UBL, with their history reconstructed one document per commit:
[the releases and their changes](releases.html) and [how the history was built](history.html).

## The Encyclopedia

The [Encyclopedia](wiki/index.html) is the world's own reference work: its countries, towns, companies and
institutions, with their history, each article made from the world's data. It is being written; the first
articles are there.

## The method note

A longer description of the principles, the world and the checks, written in the layout of an OASIS
note: [UBL example documents: method and rationale](note/ubl-examples-method.html) (a draft).

## Status

Work in progress. Not an OASIS publication. The data, the generators and the checks are on
[GitHub](https://github.com/kduvekot/ubl-examples).
