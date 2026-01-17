# Proposal: Create Gene Catalog v2 (important-genes-2)

## Summary

Create a comprehensive gene catalog by extracting gene information from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) and organizing it into a new directory structure `hidden/important-genes-2/` with YAML files for each gene. This will create a structured, queryable database of 386 unique genes with detailed information for research against Ancestry.com raw DNA data.

## Motivation

The `hidden/DNA-GENES.md` file contains a wealth of information about 386 unique genes, but it is currently in a flat Markdown format that is difficult to query or process programmatically. Creating a complete catalog will transform this data into a structured format, processing all genes in manageable chunks for piecemeal implementation.

1. **Provide comprehensive coverage** of all documented genes in a structured format
2. **Enable efficient lookup** against Ancestry.com raw DNA data for research purposes
3. **Standardize gene information** using a consistent YAML schema
4. **Support future analysis** and automation tools for genetic data processing
5. **Create a complete summary document** for easy reference

## Goals

1. Extract all 386 unique genes from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) and organize them by category
2. Create directory structure `hidden/important-genes-2/` with category folders (lowercase, hyphenated)
3. Create YAML files for each gene following the established schema
4. Research and populate complete gene information using browser MCP when needed
5. Create a comprehensive summary file `hidden/SUMMARY-2.md` documenting all genes
6. Manage context efficiently by compacting after each gene is completed
7. Process genes in manageable chunks for piecemeal implementation with clear labels

## Non-Goals

1. Creating automated tools for gene lookup (future work)
2. Integrating with external APIs or databases
3. Creating web interfaces or visualization tools

## Success Criteria

- [ ] All 386 unique genes from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) have corresponding YAML files
- [ ] Directory structure follows the pattern: `hidden/important-genes-2/<category>/<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`
- [ ] All YAML files follow the established schema with complete information
- [ ] Summary file `hidden/SUMMARY-2.md` is created with all gene information
- [ ] Each gene has at least basic information (name, function, health impact)
- [ ] Common variants include rsids, chromosome, and position when available
- [ ] All category folder names are lowercase and hyphenated
- [ ] All file names follow the pattern: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml` (or `<gene-symbol>-<full-name>-<short-description>.yaml` if no rsid)

## Proposed Approach

### Phase 1: Analysis and Planning
1. Parse [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) to extract all unique genes and their categories
2. Identify duplicate genes that appear in multiple categories
3. Create a master list of genes to process
4. Determine category folder names (lowercase, hyphenated)
5. Perform data cleanup to remove duplicates and document actual unique gene count

### Phase 2: Directory Structure Creation
1. Create `hidden/important-genes-2/` directory
2. Create category subdirectories based on the categories in [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1)

### Phase 3: Gene File Creation
For each gene:
1. Create YAML file in appropriate category folder
2. Populate with basic information from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1)
3. Use browser MCP to research additional information (rsids, chromosome, position, gene description)
4. Follow the established YAML schema (rsid, chromosome, position nested in common_variants)
5. Verify completeness and accuracy
6. Compact context to save memory before moving to next one

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

All gene files will follow this schema:

```yaml
---
gene: GENE_SYMBOL
full_name: Full Gene Name
category: gene-category-folder
function: Brief description of gene function
health_impact:
  - Health impact 1
  - Health impact 2
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
research_sources:
  - SNPedia
  - NIH Genetics Home Reference
  - Genetic Lifehacks
notes: |
  Additional information about the gene
gene_description: |
  Detailed text description of the gene, its function, and significance
```

**Schema Notes:**
- rsid, chromosome, and position are nested within `common_variants` objects (not top-level fields)
- Each variant object in `common_variants` must include all four fields: variant, rsid, chromosome, position, description
- `additional_rsids` is a top-level list for supplementary rsid references
- `gene_description` is optional for all genes, but required for Tier 1 genes (Top Priority, High-Impact)
- For Tier 2 and Tier 3 genes, include `gene_description` if readily available from research sources
- `ancestry_compatibility`: Boolean indicating whether the gene's variants are included in Ancestry.com's ~700,000 SNP test
  - Default to `true` unless research shows otherwise
  - Set to `false` if gene's variants are not tested by Ancestry.com
- `research_sources`: Optional list of sources used for gene information (e.g., SNPedia, NIH, Genetic Lifehacks)

## File Naming Convention

YAML files shall be named using the standardized long format pattern: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`

**Components:**
- `<gene-symbol>`: Lowercase gene symbol (e.g., mthfr, apoe, bdnf)
- `<full-name>`: Lowercase full gene name with spaces replaced by hyphens (e.g., methylenetetrahydrofolate-reductase, apolipoprotein-e, brain-derived-neurotrophic-factor)
- `<short-description>`: Lowercase brief description of the primary variant or function with spaces replaced by hyphens (e.g., c677t, e4, val66met)
- `<rsid>`: The primary rsid for the variant (e.g., rs1801133, rs429358, rs6265)

**Examples:**
- `mthfr-methylenetetrahydrofolate-reductase-c677t-rs1801133.yaml` (for MTHFR gene)
- `apoe-apolipoprotein-e-e4-rs429358.yaml` (for APOE gene)
- `bdnf-brain-derived-neurotrophic-factor-val66met-rs6265.yaml` (for BDNF gene)

**Rules:**
1. All components must be in lowercase for cross-platform compatibility
2. Use hyphens to separate all components
3. Maintain `.yaml` extension
4. If no rsid is available, use fallback format: `<gene-symbol>-<full-name>-<short-description>.yaml`
5. The file name provides comprehensive information at a glance, making files self-documenting

## Decisions Made

The following decisions have been made and are documented in [`design.md`](./design.md:1):

1. **Duplicate genes**: Create one YAML file per unique gene, note cross-category relevance in the `notes` field. Example: COMT appears in both "Top Priority" and "Brain & Mental Health" - create in Top Priority, reference in Brain & Mental Health notes.

2. **Gene pairs**: Create separate YAML files for each gene in a pair. Parse gene pairs (e.g., "MTNR1A & MTNR1B") and create `mtnr1a-melatonin-receptor-1a-rs2119882.yaml` and `mtnr1b-melatonin-receptor-1b-rs10830963.yaml` files.

3. **Research depth**: Use tiered research approach based on gene prominence:
   - **Tier 1** (Top Priority, High-Impact): Full research with all variants
   - **Tier 2** (Brain, Cardiovascular, Immune, etc.): Research top 2-3 variants
   - **Tier 3** (Additional, SelfDecode, Research): Basic research (name, function, available rsids)

4. **File naming**: Use descriptive format `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml` for all genes. All variant information is also stored within the YAML file's `common_variants` field.

5. **Implementation approach**: Process genes in manageable chunks with clear labels for piecemeal implementation. Each chunk will be a discrete, completable unit that can be requested separately.


## Implementation Requirements

1. **DNA Test Results**: The request for implementation must point to the DNA test results, which is the ancestry.com DNA test result raw data.

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Context exhaustion due to processing 386 genes | Compact context after each gene completion |
| Incomplete or inaccurate gene information from research | Cross-reference multiple sources (SNPedia, NIH, Genetic Lifehacks) |
| Inconsistent YAML schema across files | Create a template and validate each file against it |
| Browser MCP rate limits or unavailability | Have fallback sources (DNA-GENES.md); implement delay between browser MCP requests (2-3 seconds); cache research results to avoid redundant searches; if rate limit hit, wait and retry; document rate limit errors in gene's `notes` field |
| Time required to process all genes | Process genes in batches, prioritize by category importance |

## Alternatives Considered

1. **Automated script generation**: Could write a script to parse and generate YAML files, but would lack the research depth and accuracy of manual curation
2. **Using `hidden/important-genes/` directory**: Could create files in `hidden/important-genes/`, but using a versioned directory `hidden/important-genes-2/` ensures a clean structure without potential conflicts
3. **Database instead of YAML files**: Could use SQLite or JSON, but YAML files are more human-readable and align with existing project structure

## Dependencies

- Browser MCP for gene research
- [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) as source data
- [`openspec/AGENTS.md`](../AGENTS.md:1) for proposal conventions

## Timeline Estimate

- Phase 1 (Analysis): 30 minutes
- Phase 2 (Directory creation): 10 minutes
- Phase 3 (Gene file creation): 12-15 hours (386 genes × 1-2 minutes each)
- Phase 4 (Summary creation): 30 minutes

**Total estimated time**: 14-17 hours

**Note**: Due to the large scope (386 unique genes), this work will be divided into manageable chunks for piecemeal implementation. Each chunk will be labeled clearly (e.g., "Phase 3a: Top Priority Genes", "Phase 3b: High-Impact Genes", etc.) so that implementation can be requested and completed incrementally.

## Related Work

- [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) source document with 386 unique genes
