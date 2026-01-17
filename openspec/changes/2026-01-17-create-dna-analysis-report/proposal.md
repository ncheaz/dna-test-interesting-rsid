# Proposal: Create DNA Analysis Report System

## Summary

Create a comprehensive DNA analysis system that takes Ancestry.com raw DNA test results and generates a detailed report (`SUMMARY-FROM-RAW-DNA.md`) analyzing genetic variants across all gene categories in `hidden/important-genes-2/`. The system will parse raw DNA data, match variants against the gene catalog, and produce category-specific summaries with genetic classifications, gene information, and personalized analysis based on test results.

## Motivation

The gene catalog in `hidden/important-genes-2/` contains structured information about 393 genes across 10 categories, but there is currently no automated way to analyze individual DNA test results against this catalog. Users must manually search through raw DNA data and cross-reference with gene files, which is time-consuming and error-prone.

1. **Automate genetic analysis** by parsing Ancestry.com raw DNA files and matching variants against the gene catalog
2. **Generate comprehensive reports** that provide personalized insights for each gene category
3. **Improve accessibility** of genetic information through structured, readable summaries
4. **Enable efficient research** by consolidating analysis results in a single document
5. **Support multiple test formats** by handling standard Ancestry.com raw data format

## Goals

1. Parse Ancestry.com raw DNA test files to extract genotype data for all rsids
2. Match extracted rsids against gene variants in `hidden/important-genes-2/` catalog
3. Generate `SUMMARY-FROM-RAW-DNA.md` with category-specific analysis sections
4. Include genetic classification, gene information, and personalized variant analysis for each category
5. Provide clear, actionable insights based on genetic test results
6. Write thorough, well-written analysis in clear language with good understandable detail
7. Include diagnosis, predictive insights, and descriptive writeup of what's genetic test reveals
8. Provide summary of impact and things to keep in mind for every result from genes data
9. Handle edge cases (missing data, unknown variants, ancestry compatibility issues)
10. Support future expansion to other DNA testing providers

## Non-Goals

1. Creating automated tools for gene lookup beyond this analysis system
2. Integrating with external APIs or databases beyond existing gene catalog
3. Creating web interfaces or visualization tools
4. Providing medical advice or clinical interpretations
5. Supporting DNA test formats other than Ancestry.com raw data (future work)

## Success Criteria

- [ ] System accepts Ancestry.com raw DNA file path as input
- [ ] All rsids from raw DNA file are extracted and cataloged
- [ ] Extracted rsids are matched against all gene variants in `hidden/important-genes-2/`
- [ ] `SUMMARY-FROM-RAW-DNA.md` is generated with sections for each of the 10 gene categories
- [ ] Each category section includes:
  - Genetic classification overview
  - Summary of genes in the category
  - Analysis of matched variants from DNA test results
  - Interpretation of genetic findings
- [ ] Report clearly identifies which genes/variants were found vs. not found in test data
- [ ] Report handles genes with no matching variants (ancestry_compatibility: false)
- [ ] Report includes statistics (total genes analyzed, variants found, categories covered)
- [ ] Report format is consistent and easy to read

## Proposed Approach

### Phase 1: DNA Data Parsing

1. Accept file path to Ancestry.com raw DNA file (typically `AncestryDNA.txt`)
2. Parse file to extract all rsid-genotype pairs
3. Validate data format and handle parsing errors
4. Create in-memory index of rsids to genotypes for efficient lookup

### Phase 2: Gene Catalog Loading

1. Load all YAML files from `hidden/important-genes-2/` directory structure
2. Parse gene information including common_variants, rsids, chromosome, position
3. Create lookup structure mapping rsids to genes and categories
4. Handle duplicate genes and cross-category references

### Phase 3: Variant Matching

1. For each gene in catalog, check if its variants' rsids exist in DNA data
2. Match genotypes from DNA data to gene variants
3. Record matched variants with allele information
4. Flag genes where variants are not in DNA data (ancestry compatibility issues)

### Phase 4: Report Generation

For each category directory:

1. **Category Overview Section**
   - Category name and description
   - Total genes in category
   - Total variants analyzed
   - Number of variants found in DNA data

2. **Gene Classification Section**
   - Brief description of category's genetic significance
   - Common health impacts associated with category
   - Key biological processes

3. **Gene Information Summary**
   - List all genes in category
   - For each gene:
     - Gene symbol and full name
     - Primary function
     - Key health impacts
     - Variants tracked (rsids)

4. **DNA Analysis Section**
   - For each gene with matching variants:
     - Variant found (rsid, alleles)
     - Chromosome and position
     - Genotype interpretation (e.g., homozygous risk, heterozygous, normal)
     - Brief significance of this genotype
   - For genes with no matching variants:
     - Note that variants not tested by Ancestry.com
     - Alternative testing recommendations (if applicable)

5. **Category Summary**
   - Key findings from this category
   - Notable risk alleles identified
   - Protective alleles identified
   - Recommendations for further research or action

### Phase 5: Report Compilation

1. Create `SUMMARY-FROM-RAW-DNA.md` in project root
2. Include overall statistics section:
   - Total genes analyzed
   - Total variants checked
   - Variants found vs. not found
   - Coverage by category
3. Add table of contents for easy navigation
4. Include methodology section explaining analysis approach
5. Add disclaimer about genetic interpretation limitations

## Categories to Analyze

Based on `hidden/important-genes-2/` structure, the following 10 categories will be analyzed:

1. **top-priority-genes** (6 genes) - Most commonly researched genes with significant health impacts
2. **high-impact-health-genes** (8 genes) - Genes with major health implications
3. **metabolism-detoxification-genes** (7 genes) - Drug metabolism and detoxification pathways
4. **cardiovascular-heart-health-genes** (5 genes) - Heart health and lipid metabolism
5. **immune-inflammation-genes** (5 genes) - Immune system function and inflammation
6. **brain-mental-health-genes** (3 genes) - Neurotransmitter systems and brain function
7. **sleep-circadian-rhythm-genes** (4 genes) - Sleep patterns and circadian biology
8. **hormone-reproductive-health-genes** (3 genes) - Hormone regulation and reproductive health
9. **nutrient-metabolism-genes** (7 genes) - Vitamin and nutrient processing
10. **additional-important-genes** (345 genes) - Extended gene catalog with diverse health impacts

## Report Structure

```markdown
# DNA Analysis Report from Ancestry.com Raw Data

**Generated:** [Date]
**Source:** [DNA file path]
**Genes Analyzed:** [Total count]

## Table of Contents

1. [Overall Statistics](#overall-statistics)
2. [Methodology](#methodology)
3. [Top Priority Genes](#top-priority-genes)
4. [High-Impact Health Genes](#high-impact-health-genes)
5. [Metabolism & Detoxification Genes](#metabolism-detoxification-genes)
6. [Cardiovascular & Heart Health Genes](#cardiovascular-heart-health-genes)
7. [Immune & Inflammation Genes](#immune-inflammation-genes)
8. [Brain & Mental Health Genes](#brain-mental-health-genes)
9. [Sleep & Circadian Rhythm Genes](#sleep-circadian-rhythm-genes)
10. [Hormone & Reproductive Health Genes](#hormone-reproductive-health-genes)
11. [Nutrient Metabolism Genes](#nutrient-metabolism-genes)
12. [Additional Important Genes](#additional-important-genes)
13. [Summary & Recommendations](#summary-recommendations)

## Overall Statistics

[Tables and charts showing analysis coverage]

## Methodology

[Explanation of how analysis was performed]

## [Category Name]

### Genetic Classification

[Category overview and significance]

### Genes in This Category

[Summary of all genes]

### DNA Analysis Results

[Detailed variant-by-variant analysis]

### Category Summary

[Key findings and insights]

## Summary & Recommendations

[Overall findings and actionable insights]

## Disclaimer

[Standard genetic interpretation disclaimer]
```

## Decisions Made

The following decisions will be documented in [`design.md`](./design.md:1):

1. **Genotype Interpretation**: Use standard genetic terminology (homozygous, heterozygous) based on allele matching from DNA data

2. **Ancestry Compatibility Handling**: Clearly indicate when gene variants are not tested by Ancestry.com (ancestry_compatibility: false) and suggest alternative testing

3. **Variant Priority**: Report primary variants first, followed by additional_rsids if present

4. **Category Organization**: Process categories in order of importance (Top Priority → Additional) for logical report flow

5. **Missing Data Handling**: Gracefully handle cases where DNA data doesn't contain expected rsids, noting this in report

## Implementation Requirements

1. **DNA Test Results**: User must provide path to Ancestry.com raw DNA file (typically `AncestryDNA.txt`)
2. **Gene Catalog**: System requires `hidden/important-genes-2/` directory with complete YAML files
3. **Python Environment**: Implementation will use Python for file parsing and YAML processing
4. **Output Location**: Report will be generated as `SUMMARY-FROM-RAW-DNA.md` in project root

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| DNA file format variations | Support standard Ancestry.com format; validate structure before processing |
| Missing rsids in DNA data | Clearly document which variants were not found; suggest alternative testing |
| Large file processing time | Use efficient data structures; provide progress indicators |
| Gene catalog inconsistencies | Validate YAML files before processing; handle missing fields gracefully |
| Incorrect genotype interpretation | Use standard genetic terminology; cross-reference with gene file descriptions |
| Ancestry compatibility issues | Check ancestry_compatibility field; flag variants not tested |

## Alternatives Considered

1. **Web-based interface**: Could create interactive web app, but command-line tool is simpler and more accessible
2. **Database storage**: Could use SQLite for gene data, but YAML files are already structured and human-readable
3. **Multiple provider support**: Could support 23andMe, MyHeritage, etc., but starting with Ancestry.com focuses on immediate need
4. **Real-time analysis**: Could analyze on-demand, but batch report generation is more efficient for comprehensive analysis

## Dependencies

- Python 3.x with PyYAML library for YAML parsing
- [`hidden/important-genes-2/`](../../hidden/important-genes-2/) directory with complete gene catalog
- Ancestry.com raw DNA file (user-provided)
- [`openspec/AGENTS.md`](../AGENTS.md:1) for proposal conventions
- Existing gene catalog structure and YAML schema

## Timeline Estimate

- Phase 1 (DNA Parsing): 1-2 hours
- Phase 2 (Catalog Loading): 1 hour
- Phase 3 (Variant Matching): 1-2 hours
- Phase 4 (Report Generation): 2-3 hours
- Phase 5 (Report Compilation): 1 hour
- Testing and Validation: 1-2 hours

**Total estimated time**: 7-11 hours

## Related Work

- [`hidden/important-genes-2/`](../../hidden/important-genes-2/) - Gene catalog with 393 genes across 10 categories
- [`hidden/SUMMARY-2.md`](../../hidden/SUMMARY-2.md) - Usage instructions for gene catalog
- [`openspec/changes/archive/2026-01-17-create-gene-catalog-2/`](../archive/2026-01-17-create-gene-catalog-2/) - Previous work creating gene catalog
