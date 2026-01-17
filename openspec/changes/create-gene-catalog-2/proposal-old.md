# Proposal: Create Gene Catalog v2 (important-genes-2)

## Summary

Create a comprehensive gene catalog by extracting gene information from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) and organizing it into a new directory structure `hidden/important-genes-2/` with YAML files for each gene. This will create a structured, queryable database of 300+ genes with detailed information for research against Ancestry.com raw DNA data.

## Motivation

The existing `hidden/important-genes/` directory contains only a small subset of genes (approximately 10-15 YAML files) from the 500+ genes documented in [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1). Creating a complete catalog will:

1. **Provide comprehensive coverage** of all documented genes in a structured format
2. **Enable efficient lookup** against Ancestry.com raw DNA data for research purposes
3. **Standardize gene information** using a consistent YAML schema
4. **Support future analysis** and automation tools for genetic data processing
5. **Create a complete summary document** for easy reference

## Goals

1. Extract all unique genes from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) and organize them by category
2. Create directory structure `hidden/important-genes-2/` with category folders (lowercase, hyphenated)
3. Create YAML files for each gene following the established schema from existing YAML files
4. Research and populate complete gene information using browser MCP when needed
5. Create a comprehensive summary file `hidden/SUMMARY-2.md` documenting all genes
6. Manage context efficiently by compacting after each gene is completed

## Non-Goals

1. Creating automated tools for gene lookup (future work)
2. Integrating with external APIs or databases
3. Modifying the existing `hidden/important-genes/` directory
4. Creating web interfaces or visualization tools

## Success Criteria

- [ ] All 300+ unique genes from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) have corresponding YAML files
- [ ] Directory structure follows the pattern: `hidden/important-genes-2/<category>/<gene>.yaml`
- [ ] All YAML files follow the established schema with complete information
- [ ] Summary file `hidden/SUMMARY-2.md` is created with all gene information
- [ ] Each gene has at least basic information (name, function, health impact)
- [ ] Common variants include rsids, chromosome, and position when available
- [ ] All category folder names are lowercase and hyphenated

## Proposed Approach

### Phase 1: Analysis and Planning
1. Parse [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) to extract all unique genes and their categories
2. Identify duplicate genes that appear in multiple categories
3. Create a master list of genes to process
4. Determine category folder names (lowercase, hyphenated)

### Phase 2: Directory Structure Creation
1. Create `hidden/important-genes-2/` directory
2. Create category subdirectories based on the categories in [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1)

### Phase 3: Gene File Creation
For each gene:
1. Create YAML file in appropriate category folder
2. Populate with basic information from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1)
3. Use browser MCP to research additional information (rsids, chromosome, position, etc.)
4. Follow the established YAML schema
5. Verify completeness and accuracy
6. Compact context to save memory before moving to next gene

### Phase 4: Summary Creation
1. Create `hidden/SUMMARY-2.md` with:
   - Directory structure overview
   - Category breakdown with gene counts
   - Links to all gene files
   - YAML format documentation
   - Usage instructions
   - Total gene statistics

## Categories Identified

From [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1), the following categories will be created:

1. **top-priority-genes** - Top Priority Genes (Most Commonly Researched)
2. **high-impact-health-genes** - High-Impact Health Genes
3. **metabolism-detoxification-genes** - Metabolism & Detoxification Genes
4. **cardiovascular-heart-health-genes** - Cardiovascular & Heart Health Genes
5. **immune-inflammation-genes** - Immune & Inflammation Genes
6. **brain-mental-health-genes** - Brain & Mental Health Genes
7. **sleep-circadian-rhythm-genes** - Sleep & Circadian Rhythm Genes
8. **hormone-reproductive-health-genes** - Hormone & Reproductive Health Genes
9. **nutrient-metabolism-genes** - Nutrient Metabolism Genes
10. **additional-important-genes** - Additional Important Genes
11. **additional-genes-selfdecode** - Additional Genes from SelfDecode's 350+ Gene Reports
12. **additional-genes-research** - Additional Genes from Research Sources

## YAML Schema

All gene files will follow this schema (based on existing YAML files):

```yaml
---
gene: GENE_SYMBOL
full_name: Full Gene Name
category: gene-category-folder
function: Brief description of gene function
health_impact:
  - Health impact 1
  - Health impact 2
primary_rsid: rs##### (required)
  The most common/significant rsid for this gene
chromosome: # (required)
  Chromosome number where the gene is located (1-22, X, Y, or MT)
position: ####### (required)
  Genomic position of the primary rsid
common_variants:
  - variant: Variant name
    rsid: rs#####
    chromosome: #
    position: #######
    description: Brief description
additional_rsids:
  - rs#####
  - rs#####
ancestry_compatibility: true/false
notes: |
  Additional information about the gene
gene_description: |
  Detailed text description of the gene, its function, and significance
```

## File Naming Convention

YAML files shall be named using the pattern: `<gene-symbol>-<primary-rsid>.yaml`

**Examples:**
- `mthfr-rs1801133.yaml` (for MTHFR gene with primary variant rs1801133)
- `apoe-rs429358.yaml` (for APOE gene with primary variant rs429358)
- `bdnf-rs6265.yaml` (for BDNF gene with primary variant rs6265)

**Rules:**
1. Use lowercase gene symbol
2. Include the primary_rsid value (required field) after a hyphen
3. For genes with multiple equally important variants, use the first listed variant as primary_rsid
4. Maintain `.yaml` extension
5. The primary_rsid, chromosome, and position fields are required for all genes

## Open Questions

1. **Duplicate genes**: Some genes appear in multiple categories (e.g., COMT appears in both "Top Priority Genes" and "Brain & Mental Health Genes"). Should we:
   - Create one file per unique gene and reference it from multiple categories?
   - Create duplicate files in each category?
   - Choose the primary category and note cross-category relevance in notes?

2. **Gene pairs**: Some entries list multiple genes together (e.g., "MTNR1A & MTNR1B", "BRCA1 & BRCA2"). Should we:
   - Create separate YAML files for each gene?
   - Create a combined file for the pair?

3. **Research depth**: For genes with limited information in [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1), how much research should be done via browser MCP?
   - Minimum: basic name, function, health impact
   - Standard: add common variants with rsids when available
   - Comprehensive: full research including all known variants

4. **File naming for multi-variant genes**: For genes with multiple equally important variants (e.g., MTHFR has both rs1801133 and rs1801131), which rsid should be used in the file name?
   - Use the first listed variant
   - Use the most clinically significant variant
   - Create multiple files (one per variant)
   - Use a generic name without rsid

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Context exhaustion due to processing 300+ genes | Compact context after each gene completion |
| Incomplete or inaccurate gene information from research | Cross-reference multiple sources (SNPedia, NIH, Genetic Lifehacks) |
| Inconsistent YAML schema across files | Create a template and validate each file against it |
| Browser MCP rate limits or unavailability | Have fallback sources (existing YAML files, DNA-GENES.md) |
| Time required to process all genes | Process genes in batches, prioritize by category importance |

## Alternatives Considered

1. **Automated script generation**: Could write a script to parse and generate YAML files, but would lack the research depth and accuracy of manual curation
2. **Using existing important-genes directory**: Could extend existing directory, but would mix old and new formats; creating separate directory allows for clean slate
3. **Database instead of YAML files**: Could use SQLite or JSON, but YAML files are more human-readable and align with existing project structure

## Dependencies

- Browser MCP for gene research
- Existing YAML files in `hidden/important-genes/` as schema reference
- [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) as source data
- [`openspec/AGENTS.md`](../AGENTS.md:1) for proposal conventions

## Timeline Estimate

- Phase 1 (Analysis): 30 minutes
- Phase 2 (Directory creation): 10 minutes
- Phase 3 (Gene file creation): 8-12 hours (300+ genes × 1-2 minutes each)
- Phase 4 (Summary creation): 30 minutes

**Total estimated time**: 10-13 hours

## Related Work

- Existing `hidden/important-genes/` directory with partial gene catalog
- [`hidden/SUMMARY.md`](../../hidden/SUMMARY.md:1) documenting existing catalog
- [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) source document with 500+ genes
