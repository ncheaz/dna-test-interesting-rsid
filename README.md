# DNA Gene Analysis via RSID

An OpenSpec proposal-based system for analyzing the most common genes from DNA test results (e.g., Ancestry.com, 23andMe) using RSID (Reference SNP ID) lookups.

## Overview

This project provides a structured approach to catalog and analyze genetic variants from consumer DNA tests. It uses the OpenSpec framework to create a comprehensive gene catalog with detailed information about each gene, including:

- Gene symbols and full names
- Chromosome locations
- RSID (Reference SNP ID) values
- Health implications
- Scientific references

## Project Structure

```
dna-test-interesting-rsid/
├── openspec/                    # OpenSpec proposal framework
│   ├── changes/                 # Change proposals
│   │   └── create-gene-catalog-2/
│   │       ├── proposal.md       # Main proposal document
│   │       ├── tasks.md         # Detailed task breakdown
│   │       └── specs/          # Technical specifications
│   └── AGENTS.md               # Agent instructions
├── hidden/                     # Data and source files
│   ├── source.md               # List of 386 unique genes
│   └── DNA-GENES.md          # Original gene data
└── dna-test-results/          # Your DNA test results
    └── dna-data-2026-01-12/
        └── AncestryDNA.txt    # Example AncestryDNA data
```

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd dna-test-interesting-rsid
```

### 2. Add Your DNA Test Results

Place your DNA test results in the `dna-test-results/` directory:

**For Ancestry.com:**
- Download your raw DNA data from Ancestry.com
- Save as `dna-test-results/AncestryDNA.txt`

**For 23andMe:**
- Download your raw DNA data from 23andMe
- Save as `dna-test-results/23andMe.txt`

**Supported Formats:**
- AncestryDNA format (tab-separated with rsid columns)
- 23andMe format (tab-separated with rsid columns)
- Any format containing RSID values in the first column

### 3. Review the OpenSpec Proposal

The gene catalog creation is managed through an OpenSpec proposal located at:

[`openspec/changes/create-gene-catalog-2/proposal.md`](openspec/changes/create-gene-catalog-2/proposal.md:1)

This proposal defines:
- The gene catalog structure
- Processing methodology
- Validation requirements
- Implementation phases

### 4. Apply the Proposal

To implement the gene catalog proposal, follow these steps:

#### Step 1: Review the Tasks

Examine the detailed task breakdown:

```bash
cat openspec/changes/create-gene-catalog-2/tasks.md
```

The tasks are organized into phases:
- **Phase 1**: Analysis and Planning
- **Phase 2**: Directory Structure Creation
- **Phase 3**: Gene File Creation (divided into sub-phases 3a-3m)
- **Phase 4**: Summary Creation
- **Phase 5**: Validation

#### Step 2: Implement the Proposal

You can implement the proposal in two ways:

**Option A: Full Implementation**
Execute all tasks sequentially from Phase 1 through Phase 5.

**Option B: Piecemeal Implementation**
Implement specific phases independently:
- Phase 3a: Top Priority Genes (6 genes)
- Phase 3b: High-Impact Health Genes (8 genes)
- Phase 3c: Metabolism & Detoxification Genes (7 genes)
- Phase 3d: Cardiovascular & Heart Health Genes (5 genes)
- Phase 3e: Immune & Inflammation Genes (5 genes)
- Phase 3f: Brain & Mental Health Genes (5 genes)
- Phase 3g: Sleep & Circadian Rhythm Genes (3 genes)
- Phase 3h: Hormone & Reproductive Health Genes (3 genes)
- Phase 3i: Nutrient Metabolism Genes (7 genes)
- Phase 3j: Additional Important Genes (12 genes)
- Phase 3k: Additional Genes from Source.md (~298 genes)
 - Phase 3k: Additional Genes from `hidden/source.md` (remaining genes from the curated source list)
 - Optional: Additional external gene lists (SelfDecode, research). These are not included in `hidden/DNA-GENES.md` and must be curated before processing.

#### Step 3: Validate the Implementation

After implementation, run validation tasks:

```bash
# Validate directory structure
# Validate YAML files
# Verify gene completeness
# Test summary file
# Validate proposal compliance
```

## Gene Catalog Structure

Once implemented, the gene catalog will be organized as:

```
hidden/important-genes-2/
├── top-priority-genes/           # MTHFR, APOE, FTO, BRCA1, BRCA2, COMT
├── high-impact-health-genes/      # CYP2D6, CYP2C19, VDR, ACE, NOS3, etc.
├── metabolism-detoxification-genes/ # CYP1A1, NAT2, GSTP1, ALDH2, etc.
├── cardiovascular-heart-health-genes/ # APOA1, APOB, CETP, LPL, PCSK9
├── immune-inflammation-genes/      # IL1B, IL6, TNF, CRP, HLA-DRB1
├── brain-mental-health-genes/      # BDNF, DRD2, SLC6A4
├── sleep-circadian-rhythm-genes/  # CLOCK, PER2, MTNR1A, MTNR1B
├── hormone-reproductive-health-genes/ # ESR1, SHBG, CYP19A1
├── nutrient-metabolism-genes/      # MTR, MTRR, CBS, BHMT, TCN2, etc.
└── additional-important-genes/     # All remaining genes
```

## Gene File Format

Each gene is documented in a YAML file with the following structure:

```yaml
gene:
  symbol: GENE_SYMBOL
  full_name: Full Gene Name
  short_description: Brief description
  rsid: rs1234567
  chromosome: 1
  position: 12345678
  function: |
    Detailed description of gene function
  health_impact: |
    Health implications of genetic variants
  references:
    - SNPedia: https://snpedia.com/index.php/Gene
    - NIH: https://www.ncbi.nlm.nih.gov/gene/1234
```

## Using the Gene Catalog

### Find Your Variants

After implementing the catalog, you can:

1. **Search by RSID**: Look up specific variants found in your DNA test
2. **Browse by Category**: Explore genes organized by health category
3. **Cross-reference**: Compare your results against the catalog

### Example Workflow

```bash
# 1. Extract RSIDs from your DNA test
grep -E "^rs" dna-test-results/AncestryDNA.txt > my-rsids.txt

# 2. Check which genes you have variants for
while read rsid; do
  find hidden/important-genes-2 -name "*${rsid}*.yaml"
done < my-rsids.txt

# 3. Read the gene information
cat hidden/important-genes-2/category/gene-symbol-full-name-rsid.yaml
```

## Genes Covered

The catalog includes **386 unique genes** organized into categories:

- **Top Priority**: 6 genes (MTHFR, APOE, FTO, BRCA1, BRCA2, COMT)
- **High-Impact Health**: 8 genes (CYP enzymes, VDR, ACE, etc.)
- **Metabolism & Detoxification**: 7 genes (CYP1A1, NAT2, GSTP1, etc.)
- **Cardiovascular & Heart Health**: 5 genes (APOA1, APOB, CETP, etc.)
- **Immune & Inflammation**: 5 genes (IL1B, IL6, TNF, CRP, HLA-DRB1)
- **Brain & Mental Health**: 5 genes (BDNF, DRD2, SLC6A4)
- **Sleep & Circadian Rhythm**: 3 genes (CLOCK, PER2, MTNR1A/B)
- **Hormone & Reproductive Health**: 3 genes (ESR1, SHBG, CYP19A1)
- **Nutrient Metabolism**: 7 genes (MTR, MTRR, CBS, BHMT, TCN2, etc.)
- **Additional Important**: 12+ genes (ADRB2, ADRB3, LEPR, MC4R, etc.)
- **Additional Genes**: ~298 more genes from source.md

## OpenSpec Framework

This project uses the OpenSpec framework for structured change proposals:

- **Proposal**: Defines what will be created and why
- **Tasks**: Breaks down the work into manageable chunks
- **Specs**: Provide technical specifications for implementation
- **Validation**: Ensures quality and completeness

For more information on OpenSpec, see:
- [`openspec/AGENTS.md`](openspec/AGENTS.md:1) - Agent instructions
- [`openspec/project.md`](openspec/project.md:1) - Project documentation

## Contributing

To contribute to this project:

1. Review the OpenSpec proposal in `openspec/changes/create-gene-catalog-2/`
2. Implement specific tasks or phases
3. Validate your changes
4. Submit your improvements

## License

[Add your license here]

## Support

For questions or issues:
- Review the OpenSpec documentation
- Check the task breakdown in `tasks.md`
- Examine existing gene files for examples

## Acknowledgments

- Data sources: SNPedia, NIH, Genetic Lifehacks
- OpenSpec framework for structured proposal management
