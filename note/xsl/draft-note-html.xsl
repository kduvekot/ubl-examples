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

  <!-- Hook left empty by the OASIS stylesheet: make the page readable on
       phones and tablets (the OASIS HTML has no viewport declaration). -->
  <xsl:template name="user.head.content.extension">
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <style type="text/css">
      body { overflow-wrap: anywhere; }
      pre, .informaltable, .table-contents { overflow-x: auto; max-width: 100%; }
      img { max-width: 100%; height: auto; }
    </style>
  </xsl:template>

  <!-- A thin bar back to the site, above the cover page; the OASIS layout
       below it stays as it is (the note has its own table of contents). -->
  <xsl:template name="user.header.content">
    <div class="site-bar"
         style="font:14px/1.4 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; border-bottom:1px solid #d1d9e0; padding:0.4em 0; margin-bottom:1em;">
      <a href="../index.html" style="text-decoration:none;">&#8592; UBL Example Documents</a>
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
    <p class="draft-banner"
       style="border:2px solid #b45309; background:#fffbeb; color:#78350f; padding:0.6em 1em; font-weight:bold;">
      Proposal draft. Not an OASIS document: not contributed to, reviewed by or
      approved by the OASIS UBL TC.
    </p>
  </xsl:template>
</xsl:stylesheet>
