<?xml version="1.0" encoding="UTF-8"?>
<!--
  HTML for the note while it is a proposal, not an OASIS work product.

  Imports the OASIS Committee Note stylesheet unchanged and replaces only
  the OASIS logo on the cover page with a draft banner, so the page cannot
  be mistaken for an OASIS publication. Remove this override (build with
  oasis-2025-spec-note-html.xsl directly) once the note is a TC document.
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:import href="../../.oasis/db/spec-0.9/stylesheets/oasis-2025-spec-note-html.xsl"/>

  <!-- Hook left empty by the OASIS stylesheet:
       - make the page readable on phones and tablets (the OASIS HTML has no
         viewport declaration);
       - style the draft banner and the bar back to the site;
       - a dark theme when the reader's system is set to dark. The OASIS
         stylesheet only defines a light look; this follows its structure
         (one heading colour, a tinted background for code) with darker
         colours, and leaves the light look and print unchanged. -->
  <xsl:template name="user.head.content.extension">
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="color-scheme" content="light dark"/>
    <style type="text/css">
      body { overflow-wrap: anywhere; }
      pre, .informaltable, .table-contents { overflow-x: auto; max-width: 100%; }
      img { max-width: 100%; height: auto; }

      .site-bar { font: 14px/1.4 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
        border-bottom: 1px solid #d1d9e0; padding: 0.4em 0; margin-bottom: 1em; }
      .site-bar a { text-decoration: none; }
      .draft-banner { border: 2px solid #b45309; background: #fffbeb; color: #78350f;
        padding: 0.6em 1em; font-weight: bold; }

      @media screen and (prefers-color-scheme: dark) {
        html, body { background: #0e1116; color: #d7dbe2; }
        /* OASIS navy (#446CAA), lightened for a dark background */
        h1, h2, h3, h4, h5, h6, div.section h1.title, div.article h1.title,
        .docid-heading, .uri-heading, .loc-heading, .abstract-heading, .status-heading,
        .thisver-heading, .prevver-heading, .editor-heading, .author-heading,
        .contrib-heading, .notices-heading { color: #8fb0ec; }
        a:link { color: #7ea2ff; }
        a:visited { color: #b49cff; }
        a[href]:hover { background: #3a3720; }
        hr { border: 0; border-top: 1px solid #2f3742; }
        /* OASIS lilac code background (#E7DEEF), as a dark purple */
        pre.programlisting, div.informalexample pre { background-color: #231d2e; color: #e3dcef; }
        code, tt, .literal { color: #e3dcef; }
        table, tr, td, th, col, colgroup, tbody, thead, tfoot { border-color: #3a414c; }
        th { background: #151a21; }
        .site-bar { border-bottom-color: #2f3742; }
        .draft-banner { border-color: #d97706; background: #2a1f0e; color: #fcd9a8; }
      }
    </style>
  </xsl:template>

  <!-- A thin bar back to the site, above the cover page; the OASIS layout
       below it stays as it is (the note has its own table of contents). -->
  <xsl:template name="user.header.content">
    <div class="site-bar">
      <a href="../index.html">&#8592; UBL Example Documents</a>
    </div>
  </xsl:template>

  <!-- The OASIS footer states "Copyright OASIS Open"; that does not apply
       to a draft that is not an OASIS work product. Same layout, no claim. -->
  <xsl:template name="user.footer.content">
    <table style="font-size:80%" width="100%">
      <tr>
        <td>
          <xsl:value-of select="/*/articleinfo/productname"/>
          <xsl:for-each select="/*/articleinfo/productnumber">
            <xsl:text/>-<xsl:value-of select="."/>
          </xsl:for-each>
          <br/>
          <xsl:value-of select="/*/articleinfo/releaseinfo[@role='track']"/>
        </td>
        <td style="text-align:center">
          <br/>
          <xsl:text>Proposal draft, not an OASIS document.</xsl:text>
        </td>
        <td style="text-align:right">
          <xsl:value-of select="/*/articleinfo/pubdate"/>
        </td>
      </tr>
    </table>
  </xsl:template>

  <xsl:template name="article.titlepage.before.recto">
    <p class="draft-banner">
      Proposal draft. Not an OASIS document: not contributed to, reviewed by or
      approved by the OASIS UBL TC.
    </p>
  </xsl:template>
</xsl:stylesheet>
