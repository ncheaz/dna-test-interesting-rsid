# report-generation Specification

## Purpose
TBD - created by archiving change 2026-01-17-create-dna-analysis-report. Update Purpose after archive.
## Requirements
### Requirement: System SHALL Generate Category Report Sections

The system SHALL be able to generate detailed report sections for each gene category.

#### Scenario: Generate category overview
- **WHEN** report generator processes a category
- **THEN** it should create a category overview section with:
  - Category name and description
  - Total genes in category
  - Total variants analyzed
  - Number of variants found in DNA data
- **AND** it should format as markdown header with subsections

#### Scenario: Generate genetic classification section
- **WHEN** report generator creates a category section
- **THEN** it should include a genetic classification subsection with:
  - Brief description of category's genetic significance
  - Common health impacts associated with category
  - Key biological processes involved
- **AND** it should provide context for understanding category importance

#### Scenario: Generate gene information summary
- **WHEN** report generator processes a category's genes
- **THEN** it should create a gene information subsection with:
  - List of all genes in category
  - For each gene:
    - Gene symbol and full name
    - Primary function
    - Key health impacts
    - Variants tracked (rsids)
- **AND** it should format as list or table for readability

#### Scenario: Generate DNA analysis results for matched variants
- **WHEN** report generator processes a gene with matched variants
- **THEN** it should create a DNA analysis subsection with:
  - Gene symbol and full name as header
  - Function description
  - Health impacts list
  - Table of matched variants with columns:
    - Variant name
    - rsid
    - Genotype
    - Type (homozygous_risk, heterozygous, normal)
    - Interpretation
- **AND** it should include genotype interpretations for each variant

#### Scenario: Generate ancestry compatibility note
- **WHEN** report generator processes a gene with no matched variants
- **THEN** it should create a note subsection explaining:
  - Variants for this gene are not tested by Ancestry.com
  - ancestry_compatibility flag is false
  - Consider alternative genetic testing to analyze these variants
- **AND** it should include gene information for reference

#### Scenario: Generate category summary
- **WHEN** report generator has completed processing all genes in category
- **THEN** it should create a category summary subsection with:
  - Key findings from this category
  - Notable risk alleles identified
  - Protective alleles identified
  - Recommendations for further research or action
- **AND** it should synthesize insights from matched variants

### Requirement: System SHALL Generate Overall Report Structure

The system SHALL be able to compile all category sections into a complete analysis report.

#### Scenario: Generate report header
- **WHEN** report compiler starts generating final report
- **THEN** it should create a report header with:
  - Title: "DNA Analysis Report from Ancestry.com Raw Data"
  - Generation timestamp
  - Source DNA file path
  - Total genes analyzed count
- **AND** it should format as markdown level 1 header

#### Scenario: Generate table of contents
- **WHEN** report compiler creates report structure
- **THEN** it should generate a table of contents with:
  - Links to all major sections
  - Numbered list for easy navigation
  - Links to Overall Statistics, Methodology, each category, Summary & Recommendations, Disclaimer
- **AND** it should use markdown anchor links for navigation

#### Scenario: Generate overall statistics section
- **WHEN** report compiler processes MatchResults object
- **THEN** it should create an overall statistics section with:
  - Analysis coverage table with columns:
    - Category
    - Genes
    - Variants Checked
    - Variants Found
    - Coverage (percentage)
  - Summary statistics:
    - Total Genes Analyzed
    - Total Variants Checked
    - Total Variants Found
    - Overall Coverage percentage
- **AND** it should format as markdown tables

#### Scenario: Generate methodology section
- **WHEN** report compiler creates report structure
- **THEN** it should add a methodology section explaining:
  - How analysis was performed (parsing, matching, interpretation)
  - Data sources used (Ancestry.com DNA file, gene catalog)
  - Variant information sources (gene YAML files)
  - Limitations of the analysis
- **AND** it should be transparent about process and constraints

#### Scenario: Compile category sections
- **WHEN** report compiler assembles final report
- **THEN** it should append all category sections in order:
  1. Top Priority Genes
  2. High-Impact Health Genes
  3. Metabolism & Detoxification Genes
  4. Cardiovascular & Heart Health Genes
  5. Immune & Inflammation Genes
  6. Brain & Mental Health Genes
  7. Sleep & Circadian Rhythm Genes
  8. Hormone & Reproductive Health Genes
  9. Nutrient Metabolism Genes
  10. Additional Important Genes
- **AND** it should ensure consistent formatting across all sections

#### Scenario: Generate summary and recommendations section
- **WHEN** report compiler has compiled all category sections
- **THEN** it should create a summary and recommendations section with:
  - Overall findings across all categories
  - Notable risk alleles identified
  - Protective alleles identified
  - Genes requiring additional testing (ancestry_compatibility: false)
  - Recommendations for further research or action
- **AND** it should synthesize insights from all categories

#### Scenario: Add disclaimer section
- **WHEN** report compiler completes report content
- **THEN** it should add a disclaimer section with:
  - Standard genetic interpretation disclaimer
  - Note that this is not medical advice
  - Recommendation to consult healthcare professionals
  - Explanation of limitations (Ancestry.com coverage, evolving science)
- **AND** it should be clear about scope and purpose

#### Scenario: Write final report file
- **WHEN** report compiler has assembled all sections
- **THEN** it should write complete markdown to `SUMMARY-FROM-RAW-DNA.md`
- **AND** it should write to project root directory
- **AND** it should validate file creation
- **AND** it should log success or error

### Requirement: System SHALL Format Report for Readability

The system SHALL generate reports that are clear, consistent, and easy to navigate.

#### Scenario: Use markdown headers for structure
- **WHEN** report generator creates any section
- **THEN** it should use appropriate markdown header levels:
  - Level 1 (#) for main report title
  - Level 2 (##) for major sections (Statistics, Methodology, Categories, Summary)
  - Level 3 (###) for subsections (Genetic Classification, Genes in This Category)
  - Level 4 (####) for gene-specific subsections
- **AND** it should maintain consistent hierarchy

#### Scenario: Use tables for data presentation
- **WHEN** report generator presents structured data
- **THEN** it should use markdown tables with:
  - Clear column headers
  - Aligned columns for readability
  - Appropriate use of tables for variant data, statistics
- **AND** it should ensure tables are properly formatted

#### Scenario: Use lists for itemized information
- **WHEN** report generator presents lists of items
- **THEN** it should use markdown bullet lists for:
  - Health impacts
  - Key findings
  - Recommendations
- **AND** it should use numbered lists for:
  - Sequential recommendations
  - Step-by-step information

#### Scenario: Include links for navigation
- **WHEN** report generator creates table of contents
- **THEN** it should use markdown anchor links for navigation
- **AND** it should ensure all major sections have anchors
- **AND** it should verify links work correctly

#### Scenario: Add formatting for emphasis
- **WHEN** report generator presents important information
- **THEN** it should use markdown formatting for emphasis:
  - Bold (**text**) for important terms
  - Italics (*text*) for emphasis
  - Code (`text`) for gene symbols, rsids, genotypes
- **AND** it should use formatting consistently

