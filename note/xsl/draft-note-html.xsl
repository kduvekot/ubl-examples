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

  <xsl:template name="article.titlepage.before.recto">
    <p class="draft-banner"
       style="border:2px solid #b45309; background:#fffbeb; color:#78350f; padding:0.6em 1em; font-weight:bold;">
      Proposal draft. Not an OASIS document: not contributed to, reviewed by or
      approved by the OASIS UBL TC.
    </p>
  </xsl:template>
</xsl:stylesheet>
