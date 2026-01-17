# DNA Gene Analysis via RSID

An OpenSpec proposal-based system for analyzing the most common genes from DNA test results (e.g., Ancestry.com, 23andMe) using RSID (Reference SNP ID) lookups.

## Overview

This project provides a comprehensive approach to catalog and analyze genetic variants from consumer DNA tests. It uses the OpenSpec framework to:

1. **Create and maintain a gene catalog** with detailed information about 393 genes across 10 categories
2. **Automate DNA analysis** by parsing raw DNA test results and matching variants against the gene catalog
3. **Generate detailed reports** with personalized insights, genetic classifications, and actionable findings

The system includes:

- Gene symbols and full names
- Chromosome locations
- RSID (Reference SNP ID) values
- Health implications
- Scientific references
- Automated variant matching
- Comprehensive analysis reports

## Project Structure

```
dna-test-interesting-rsid/
├── openspec/                    # OpenSpec proposal framework
│   ├── changes/                 # Active change proposals
│   │   └── 2026-01-17-create-dna-analysis-report/
│   │       ├── proposal.md      # DNA Analysis Report System proposal
│   │       ├── tasks.md        # Detailed task breakdown
│   │       ├── design.md       # Design decisions
│   │       └── specs/          # Technical specifications
│   ├── changes/archive/        # Archived proposals
│   │   └── 2026-01-17-create-gene-catalog-2/
│   │       └── (Gene catalog creation proposal)
│   ├── specs/                  # Active specifications
│   │   ├── dna-data-parsing/
│   │   ├── gene-catalog-loading/
│   │   ├── variant-matching/
│   │   └── report-generation/
│   └── AGENTS.md               # Agent instructions
├── hidden/                     # Data and source files
│   ├── source.md               # List of 386 unique genes
│   ├── DNA-GENES.md          # Original gene data
│   └── important-genes-2/      # Gene catalog with 393 genes
│       ├── top-priority-genes/
│       ├── high-impact-health-genes/
│       ├── metabolism-detoxification-genes/
│       ├── cardiovascular-heart-health-genes/
│       ├── immune-inflammation-genes/
│       ├── brain-mental-health-genes/
│       ├── sleep-circadian-rhythm-genes/
│       ├── hormone-reproductive-health-genes/
│       ├── nutrient-metabolism-genes/
│       └── additional-important-genes/
├── dna-test-results/          # Your DNA test results
│   └── dna-data-2026-01-12/
│       └── AncestryDNA.txt    # Example AncestryDNA data
├── dna_analysis_system.py     # DNA analysis script
└── SUMMARY-FROM-RAW-DNA.md    # Generated analysis report
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

### 3. Review the OpenSpec Proposals

This project has two main OpenSpec proposals:

**Gene Catalog Creation** (Archived - Completed):
- Location: [`openspec/changes/archive/2026-01-17-create-gene-catalog-2/proposal.md`](openspec/changes/archive/2026-01-17-create-gene-catalog-2/proposal.md:1)
- Status: Completed - Gene catalog with 393 genes across 10 categories

**DNA Analysis Report System** (Active):
- Location: [`openspec/changes/2026-01-17-create-dna-analysis-report/proposal.md`](openspec/changes/2026-01-17-create-dna-analysis-report/proposal.md:1)
- Purpose: Automate analysis of DNA test results against the gene catalog
- Generates: `SUMMARY-FROM-RAW-DNA.md` with personalized insights

### 4. Run DNA Analysis

The DNA analysis system automatically processes your raw DNA data and generates a comprehensive report:

```bash
# Run the DNA analysis system
python dna_analysis_system.py dna-test-results/AncestryDNA.txt
```

This will:
- Parse your Ancestry.com raw DNA file
- Match variants against the 393-gene catalog
- Generate `SUMMARY-FROM-RAW-DNA.md` with:
  - Overall statistics
  - Category-by-category analysis
  - Genetic classifications
  - Personalized variant interpretations
  - Health impact summaries
  - Recommendations

### 5. (Optional) Gene Catalog Implementation

The gene catalog has already been created and contains 393 genes. If you need to understand how it was built or extend it:

```bash
# Review the archived gene catalog proposal
cat openspec/changes/archive/2026-01-17-create-gene-catalog-2/proposal.md
cat openspec/changes/archive/2026-01-17-create-gene-catalog-2/tasks.md
```

The gene catalog is fully implemented in `hidden/important-genes-2/` with all 393 genes across 10 categories.

## Gene Catalog Structure

The gene catalog is organized as:

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

## DNA Analysis Report System

The DNA Analysis Report System provides automated analysis of your raw DNA test results against the gene catalog.

### Features

- **Automated Parsing**: Reads Ancestry.com raw DNA files
- **Variant Matching**: Matches your variants against 393 genes
- **Category Analysis**: Analyzes genes across 10 health categories
- **Personalized Insights**: Provides genotype interpretations
- **Health Impact Summaries**: Explains significance of findings
- **Comprehensive Reporting**: Generates detailed markdown reports

### Running the Analysis

```bash
# Basic usage
python dna_analysis_system.py dna-test-results/AncestryDNA.txt

# The report will be generated as SUMMARY-FROM-RAW-DNA.md
```

### Report Contents

The generated report includes:

1. **Overall Statistics**
   - Total genes analyzed
   - Variants found vs. not found
   - Coverage by category

2. **Category-by-Category Analysis**
   - Genetic classification overview
   - Gene information summary
   - DNA analysis results with variant details
   - Category-specific findings and recommendations

3. **Detailed Variant Analysis**
   - RSID and genotype information
   - Chromosome and position data
   - Genotype interpretation (homozygous/heterozygous)
   - Health impact and significance

4. **Summary & Recommendations**
   - Key findings across all categories
   - Notable risk alleles
   - Protective alleles
   - Actionable insights

### Example Report Sections

For each gene category, the report provides:

- **Genetic Classification**: Overview of the category's biological significance
- **Genes in Category**: List of all genes with key information
- **DNA Analysis Results**: Detailed breakdown of matched variants
- **Category Summary**: Key findings and recommendations

### Understanding Your Results

The report uses standard genetic terminology:

- **Homozygous**: Both alleles are the same (e.g., AA or aa)
- **Heterozygous**: Two different alleles (e.g., Aa)
- **Risk Allele**: Variant associated with increased risk
- **Protective Allele**: Variant associated with decreased risk

### Limitations

- Based on Ancestry.com test data (may not include all variants)
- Not medical advice - consult healthcare professionals
- Some gene variants may not be tested by Ancestry.com
- Results should be validated with clinical testing when appropriate

## Genes Covered

The catalog includes **393 unique genes** organized into categories:

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

1. Review the active DNA Analysis Report proposal in `openspec/changes/2026-01-17-create-dna-analysis-report/`
2. Review the archived gene catalog proposal in `openspec/changes/archive/2026-01-17-create-gene-catalog-2/`
3. Implement specific tasks or phases
4. Validate your changes
5. Submit your improvements

## License

This project is licensed under the GNU General Public License v3.0.

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2026 DNA Gene Analysis Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

For the full license text, see [LICENSE](LICENSE) or visit <https://www.gnu.org/licenses/gpl-3.0.txt>.

## Support

For questions or issues:
- Review the OpenSpec documentation
- Check the task breakdown in `tasks.md`
- Examine existing gene files for examples

## Acknowledgments

- Data sources: SNPedia, NIH, Genetic Lifehacks
- OpenSpec framework for structured proposal management
