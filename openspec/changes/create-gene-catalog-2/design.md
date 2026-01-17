# Design: Create Gene Catalog v2 (important-genes-2)

## Overview

This document describes the architectural design for creating a comprehensive gene catalog from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) into a structured YAML-based directory system at `hidden/important-genes-2/`. The work will be divided into manageable chunks for piecemeal implementation.

## System Architecture

### Directory Structure

```
hidden/important-genes-2/
├── top-priority-genes/
│   ├── mthfr-methylenetetrahydrofolate-reductase-c677t-rs1801133.yaml
│   ├── apoe-apolipoprotein-e-e4-rs429358.yaml
│   ├── fto-fat-mass-and-obesity-associated-rs9939609.yaml
│   ├── brca1-breast-cancer-1-rs799917.yaml
│   ├── brca2-breast-cancer-2-rs206115.yaml
│   └── comt-catechol-o-methyltransferase-val158met-rs4680.yaml
├── high-impact-health-genes/
│   ├── cyp2d6-cytochrome-p450-2d6-rs3892097.yaml
│   ├── cyp2c19-cytochrome-p450-2c19-rs4244285.yaml
│   ├── vdr-vitamin-d-receptor-rs1544410.yaml
│   ├── ace-angiotensin-converting-enzyme-rs4343.yaml
│   ├── nos3-nitric-oxide-synthase-3-rs1799983.yaml
│   ├── fut2-fucosyltransferase-2-rs601338.yaml
│   ├── sod2-superoxide-dismutase-2-rs4880.yaml
│   └── maoa-monoamine-oxidase-a-rs6323.yaml
├── metabolism-detoxification-genes/
│   ├── cyp1a1-cytochrome-p450-1a1-rs1048943.yaml
│   ├── nat2-n-acetyltransferase-2-rs1801280.yaml
│   ├── gstp1-glutathione-s-transferase-p1-rs1695.yaml
│   ├── aldh2-aldehyde-dehydrogenase-2-rs671.yaml
│   ├── pparg-peroxisome-proliferator-activated-receptor-gamma-rs1801282.yaml
│   ├── ucp1-uncoupling-protein-1-rs1800592.yaml
│   └── slc2a2-solute-carrier-family-2-member-2-rs5400.yaml
├── cardiovascular-heart-health-genes/
│   ├── apoa1-apolipoprotein-a1-rs670.yaml
│   ├── apob-apolipoprotein-b-rs693.yaml
│   ├── cetp-cholesteryl-ester-transfer-protein-rs708272.yaml
│   ├── lpl-lipoprotein-lipase-rs1800590.yaml
│   └── pcsk9-proprotein-convertase-subtilisin-kexin-9-rs505151.yaml
├── immune-inflammation-genes/
│   ├── il1b-interleukin-1-beta-rs1143634.yaml
│   ├── il6-interleukin-6-rs1800795.yaml
│   ├── tnf-tumor-necrosis-factor-rs1800629.yaml
│   ├── crp-c-reactive-protein-rs1205.yaml
│   └── hla-drb1-human-leukocyte-antigen-drb1-rs660895.yaml
├── brain-mental-health-genes/
│   ├── bdnf-brain-derived-neurotrophic-factor-val66met-rs6265.yaml
│   ├── drd2-dopamine-receptor-d2-rs1800497.yaml
│   ├── slc6a4-serotonin-transporter-5-httlpr-rs25531.yaml
│   └── notes.yaml (references COMT, MAOA from other categories)
├── sleep-circadian-rhythm-genes/
│   ├── clock-circadian-locomotor-output-cycles-kaput-rs1801260.yaml
│   ├── per2-period-circadian-regulator-2-rs2304672.yaml
│   ├── mtnr1a-melatonin-receptor-1a-rs2119882.yaml
│   └── mtnr1b-melatonin-receptor-1b-rs10830963.yaml
├── hormone-reproductive-health-genes/
│   ├── esr1-estrogen-receptor-1-rs2234693.yaml
│   ├── shbg-sex-hormone-binding-globulin-rs6259.yaml
│   └── cyp19a1-aromatase-rs10046.yaml
├── nutrient-metabolism-genes/
│   ├── mtr-methionine-synthase-rs1805087.yaml
│   ├── mtrr-methionine-synthase-reductase-rs1801394.yaml
│   ├── cbs-cystathionine-beta-synthase-rs234706.yaml
│   ├── bhmt-betaine-homocysteine-s-methyltransferase-rs3733890.yaml
│   ├── tcn2-transcobalamin-2-rs1801198.yaml
│   ├── slc19a1-solute-carrier-family-19-member-1-rs1051266.yaml
│   └── folh1-folate-hydrolase-1-rs202676.yaml
├── additional-important-genes/
│   ├── adrb2-beta-2-adrenergic-receptor-rs1042713.yaml
│   ├── adrb3-beta-3-adrenergic-receptor-rs4994.yaml
│   ├── lepr-leptin-receptor-rs1137101.yaml
│   ├── mc4r-melanocortin-4-receptor-rs17782313.yaml
│   ├── adipoq-adiponectin-rs1501299.yaml
│   ├── ppargc1a-pparg-coactivator-1-alpha-rs8192678.yaml
│   ├── gckr-glucokinase-regulator-rs780094.yaml
│   ├── tcf7l2-transcription-factor-7-like-2-rs7903146.yaml
│   ├── pnpla3-patatin-like-phospholipase-3-rs738409.yaml
│   ├── slc30a8-zinc-transporter-8-rs13266634.yaml
│   ├── hfe-hemochromatosis-rs1799945.yaml
│   └── tas2r38-taste-receptor-rs713598.yaml
├── additional-genes-selfdecode/
│   ├── sod1-superoxide-dismutase-1-rs2070424.yaml
│   ├── sod3-superoxide-dismutase-3-rs699473.yaml
│   ├── gpx4-glutathione-peroxidase-4-rs713041.yaml
│   ├── cat-catalase-rs1001179.yaml
│   └── ... (130+ more genes)
└── additional-genes-research/
    ├── hbb-hemoglobin-beta-rs334.yaml
    ├── hba1-hemoglobin-alpha-1-rs3888188.yaml
    ├── hba2-hemoglobin-alpha-2-rs3888188.yaml
    ├── g6pd-glucose-6-phosphate-dehydrogenase-rs1050828.yaml
    └── ... (100+ more genes)
```

### Data Flow

```
DNA-GENES.md (Source)
    ↓
Parse & Extract
    ↓
Gene List (Gene Symbol → Category Mapping)
    ↓
Create Directory Structure
    ↓
For Each Gene:
    1. Create YAML file
    2. Populate basic info from DNA-GENES.md
    3. Research via Browser MCP (rsids, chromosome, position)
    4. Validate YAML schema
    5. Compact context
    ↓
SUMMARY-2.md (Documentation)
```

## Component Design

### 1. Gene Parser

**Purpose**: Extract gene information from [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1)

**Input**: Markdown file with gene listings organized by category

**Output**: Structured data mapping:
- Gene symbol → Category
- Gene symbol → Full name
- Gene symbol → Function
- Gene symbol → Health impacts
- Gene symbol → Common variants (if listed)

**Algorithm**:
1. Scan document for category headers (## or ###)
2. Extract gene entries under each category
3. Parse gene symbol, full name, function, and health impacts
4. Handle special cases (gene pairs, duplicates, "already listed" notes)
5. Generate unique gene list with category mapping

### 2. Directory Manager

**Purpose**: Create and manage directory structure

**Responsibilities**:
- Create main directory `hidden/important-genes-2/`
- Create category subdirectories with lowercase, hyphenated names
- Validate directory creation
- Handle naming conflicts

**Category Name Mapping**:
| Original Category | Folder Name |
|-------------------|-------------|
| Top Priority Genes | top-priority-genes |
| High-Impact Health Genes | high-impact-health-genes |
| Metabolism & Detoxification Genes | metabolism-detoxification-genes |
| Cardiovascular & Heart Health Genes | cardiovascular-heart-health-genes |
| Immune & Inflammation Genes | immune-inflammation-genes |
| Brain & Mental Health Genes | brain-mental-health-genes |
| Sleep & Circadian Rhythm Genes | sleep-circadian-rhythm-genes |
| Hormone & Reproductive Health Genes | hormone-reproductive-health-genes |
| Nutrient Metabolism Genes | nutrient-metabolism-genes |
| Additional Important Genes | additional-important-genes |
| Additional Genes from SelfDecode | additional-genes-selfdecode |
| Additional Genes from Research | additional-genes-research |

### 3. Gene File Generator

**Purpose**: Create YAML files for each gene

**Input**: Gene information from parser and research from browser MCP

**Output**: YAML file following established schema

**Process**:
1. Create file with descriptive naming pattern `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`
2. Populate required fields from DNA-GENES.md
3. Research additional information via browser MCP:
   - rsids for common variants
   - Chromosome number
   - Genomic position
   - Additional variant details
4. Validate against schema
5. Write to appropriate category folder

**YAML Schema**:
```yaml
---
gene: GENE_SYMBOL (required)
full_name: Full Gene Name (required)
category: gene-category-folder (required)
function: Brief description of gene function (required)
health_impact: (required, list)
  - Health impact 1
  - Health impact 2
common_variants: (optional, list)
  - variant: Variant name
    rsid: rs#####
    chromosome: #
    position: #######
    description: Brief description
additional_rsids: (optional, list)
  - rs#####
  - rs#####
ancestry_compatibility: true/false (default: true)
  - Boolean indicating whether the gene's variants are included in Ancestry.com's ~700,000 SNP test
  - Default to `true` unless research shows otherwise
  - Set to `false` if gene's variants are not tested by Ancestry.com
research_sources: (optional, list)
  - SNPedia
  - NIH Genetics Home Reference
  - Genetic Lifehacks
notes: | (optional)
  Additional information about the gene
gene_description: | (optional, required for Tier 1 genes)
  Detailed text description of the gene, its function, and significance
```

### 4. Research Module

**Purpose**: Gather additional gene information via browser MCP

**Research Sources (Priority Order)**:
1. **SNPedia** (https://www.snpedia.com/) - rsid information, variant details
2. **NIH Genetics Home Reference** (https://ghr.nlm.nih.gov/) - authoritative gene information
3. **Genetic Lifehacks** (https://www.geneticlifehacks.com/) - practical health implications
4. **SelfDecode** (https://selfdecode.com/) - comprehensive gene reports

**Research Strategy**:
- For well-known genes (MTHFR, APOE, etc.): Full research including all common variants
- For moderately-known genes: Research top 2-3 variants
- For less-known genes: Basic research (name, function, any available rsids)

**Fallback Strategy**:
- If browser MCP unavailable, use information from DNA-GENES.md only
- If no rsid information found, leave `common_variants` empty or use placeholder
- Document research limitations in `notes` field

### 5. Context Manager

**Purpose**: Manage context to prevent memory exhaustion

**Strategy**:
- Compact context after each gene file is completed
- Retain only essential information for next gene:
  - Current gene being processed
  - Category mapping
  - YAML schema template
- Discard:
  - Previous gene details
  - Browser MCP search results
  - Research notes

**Compaction Trigger**:
- After successful YAML file creation
- After validation
- Before moving to next gene

### 6. Summary Generator

**Purpose**: Create comprehensive documentation in `hidden/SUMMARY-2.md`

**Structure**:
```markdown
# DNA Gene Information Summary v2

## Directory Structure
[Category listings with gene counts]

## Category Breakdown
[Detailed gene listings with links]

## YAML File Format
[Schema documentation]

## Using with AncestryDNA Data
[Usage instructions]

## Total Genes Documented
[Statistics table]

## Resources
[External references]
```

## Key Design Decisions

### 1. Duplicate Gene Handling

**Decision**: Create one YAML file per unique gene, note cross-category relevance

**Rationale**:
- Avoids data duplication
- Single source of truth for each gene
- Easier to maintain and update
- Cross-category references can be documented in `notes` field

**Implementation**:
- Track genes already processed
- When encountering duplicate, add reference to existing file in `notes`
- Example: COMT appears in "Top Priority" and "Brain & Mental Health" - create in Top Priority, reference in Brain & Mental Health

### 2. Gene Pair Handling

**Decision**: Create separate YAML files for each gene in a pair

**Rationale**:
- Each gene is a distinct entity
- May have different variants and health impacts
- Enables independent lookup and analysis

**Implementation**:
- Parse gene pairs (e.g., "MTNR1A & MTNR1B")
- Create `mtnr1a-melatonin-receptor-1a-rs2119882.yaml` and `mtnr1b-melatonin-receptor-1b-rs10830963.yaml`
- Extract relevant information for each from DNA-GENES.md
- Research primary rsid for each gene separately

**Gene Pair Examples**:
- `MTNR1A & MTNR1B` → Create `mtnr1a-melatonin-receptor-1a-rs2119882.yaml` and `mtnr1b-melatonin-receptor-1b-rs10830963.yaml`
- `GCLC & GCLM` → Create `gclc-glutamate-cysteine-ligase-catalytic-rs17883901.yaml` and `gclm-glutamate-cysteine-ligase-modifier-rs1050828.yaml`
- `BRCA1 & BRCA2` → Already handled separately in source (no parsing needed)

### 3. File Naming Convention

**Decision**: Use descriptive file names with gene symbol, full name, short description, and rsid (long format)

**Rationale**:
- Provides comprehensive information at a glance
- Makes files self-documenting
- Easier to identify specific variants without opening files
- Facilitates searching and filtering by variant
- More informative for research purposes

**Implementation**:
- Use pattern: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`

**Components:**
- `<gene-symbol>`: Lowercase gene symbol (e.g., mthfr, apoe, bdnf)
- `<full-name>`: Lowercase full gene name with spaces replaced by hyphens (e.g., methylenetetrahydrofolate-reductase, apolipoprotein-e, brain-derived-neurotrophic-factor)
- `<short-description>`: Lowercase brief description of primary variant or function with spaces replaced by hyphens (e.g., c677t, e4, val66met)
- `<rsid>`: The primary rsid for variant (e.g., rs1801133, rs429358, rs6265)

**Examples:**
  - `mthfr-methylenetetrahydrofolate-reductase-c677t-rs1801133.yaml` (MTHFR gene)
  - `apoe-apolipoprotein-e-e4-rs429358.yaml` (APOE gene)
  - `bdnf-brain-derived-neurotrophic-factor-val66met-rs6265.yaml` (BDNF gene)

**Rules:**
- All components are lowercase for cross-platform compatibility
- Use hyphens to separate all components
- If no rsid is available, use fallback format: `<gene-symbol>-<full-name>-<short-description>.yaml`

### 4. Research Depth Strategy

**Decision**: Tiered research approach based on gene prominence

**Rationale**:
- Optimizes time investment
- Focuses research on most impactful genes
- Provides complete information where it matters most

**Tiers**:
- **Tier 1** (Top Priority, High-Impact): Full research with all variants, required `gene_description`
- **Tier 2** (Brain, Cardiovascular, Immune, etc.): Research top 2-3 variants, include `gene_description` if readily available
- **Tier 3** (Additional, SelfDecode, Research): Basic research (name, function, available rsids), include `gene_description` if readily available

**Field Requirements by Tier**:
- **Tier 1**: All required fields including `gene_description`
- **Tier 2**: Required fields, `gene_description` optional (include if available)
- **Tier 3**: Required fields, `gene_description` optional (include if available)

### 4. Context Management

**Decision**: Aggressive context compaction after each gene

**Rationale**:
- Processing 386 genes will exceed context limits
- Each gene is independent after creation
- Prevents memory exhaustion during long-running task

**Implementation**:
- Compact context after each gene completion
- Maintain only essential state (gene list, current gene, schema)
- Document compaction in task notes

### 5. Validation Strategy

**Decision**: Multi-level validation throughout process

**Rationale**:
- Catches errors early
- Ensures data quality
- Maintains consistency across all files

**Validation Levels**:
1. **Parse validation**: Ensure all genes extracted correctly
2. **Directory validation**: Verify folder structure created
3. **YAML validation**: Check schema compliance
4. **Link validation**: Verify all links in summary work
5. **Completeness validation**: Cross-reference with source document

**Validation Tools**:
1. **openspec validate**: Use `openspec validate` for proposal validation (per AGENTS.md)
2. **YAML schema validation**: Use `yamllint` or a Python script to validate gene YAML files against the schema
3. **Manual review**: Visual inspection of generated files for completeness and accuracy

**Validation Criteria**:
- All required fields present (gene, full_name, category, function, health_impact)
- Correct YAML syntax and formatting
- Valid rsid format (rs followed by digits)
- Chromosome values are valid (1-22, X, Y, MT)
- Position values are positive integers
- Category folder names match expected pattern (lowercase, hyphenated)
- File names follow `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml` pattern (or `<gene-symbol>-<full-name>-<short-description>.yaml` if no rsid)
- No duplicate gene files across categories
- All genes from source document have corresponding YAML files

## Error Handling

### Parse Errors
- **Issue**: Malformed gene entries in DNA-GENES.md
- **Handling**: Log error, skip gene, document in error report
- **Recovery**: Continue with next gene

### Research Errors
- **Issue**: Browser MCP unavailable or search fails
- **Handling**: Use available information from DNA-GENES.md
- **Recovery**: Document research limitation in gene's `notes` field
- **Rate Limit Handling**:
  - Implement delay between browser MCP requests (2-3 seconds)
  - Cache research results to avoid redundant searches
  - If rate limit hit, wait and retry
  - Document rate limit errors in gene's `notes` field

### YAML Errors
- **Issue**: Invalid YAML syntax or missing required fields
- **Handling**: Log error, fix manually, re-validate
- **Recovery**: Continue with next gene

### Directory Errors
- **Issue**: Cannot create directory or file
- **Handling**: Log error, check permissions, retry
- **Recovery**: Abort if critical, continue if non-critical

## Performance Considerations

### Time Complexity
- Parsing: O(n) where n = lines in DNA-GENES.md
- Directory creation: O(c) where c = number of categories (12)
- Gene file creation: O(g) where g = number of genes (386)
- Research: O(g × r) where r = research time per gene (1-2 min)

### Space Complexity
- In-memory gene list: O(g)
- Context per gene: O(1) after compaction
- Total disk space: O(g × f) where f = average file size (~1KB)

### Implementation Approach
Due to the scope (386 genes), work will be divided into manageable chunks for piecemeal implementation:

**Chunking Strategy**:
- **Primary Chunk**: One phase (e.g., Phase 3a = Top Priority Genes, Phase 3b = High-Impact Genes)
- **Sub-Chunk**: 10 genes per sub-chunk for context management
- **Context Compaction**: After each sub-chunk (10 genes) to prevent memory exhaustion

**Chunk Structure**:
- Each chunk is a discrete, completable unit
- Chunks will be labeled clearly (e.g., "Phase 3a: Top Priority Genes", "Phase 3b: High-Impact Genes")
- Chunks can be requested and implemented independently
- Each sub-chunk includes context compaction after completion
  - Primary chunks can span multiple sub-chunks (e.g., Phase 3k with ~298 genes would have ~30 sub-chunks)

### Optimization Strategies
1. Process genes in batches to minimize context switching
2. Cache research results for commonly referenced genes
3. Use efficient YAML parsing and generation
4. Parallelize independent research (if supported)

## Security Considerations

### Input Validation
- Validate gene symbols against standard nomenclature
- Sanitize folder names to prevent path traversal
- Validate rsid format (rs followed by digits)

### External Research
- Use trusted sources (SNPedia, NIH, Genetic Lifehacks)
- Verify information from multiple sources when possible
- Document source URLs in gene notes

### File Permissions
- Create files with appropriate read/write permissions
- Ensure hidden directory is not publicly accessible
- Consider file ownership and group settings

## Testing Strategy

### Unit Tests
- Test gene parser with various entry formats
- Test directory creation with edge cases
- Test YAML schema validation
- Test research module with mock browser MCP

### Integration Tests
- Test full pipeline from DNA-GENES.md to YAML files
- Test context compaction and recovery
- Test summary generation

### Validation Tests
- Verify all genes from source have YAML files
- Verify all YAML files are valid
- Verify all links in summary work
- Verify gene counts match expectations

## Maintenance Considerations

### Updating Gene Information
- Each gene is independent, can be updated individually
- YAML format is human-readable and editable
- Schema can be extended without breaking existing files

### Adding New Genes
- Add to DNA-GENES.md source
- Re-run gene parser
- Create new YAML files
- Update summary

### Schema Evolution
- Maintain backward compatibility
- Document schema changes in version history
- Provide migration tools if needed

## Future Enhancements

1. **Automated Validation Tool**: Script to validate all YAML files against schema
2. **Gene Lookup Tool**: CLI tool to search genes by symbol, rsid, or health impact
3. **AncestryDNA Integration**: Automated matching against raw data files
4. **Web Interface**: Browser-based gene catalog with search and filtering
5. **API Endpoint**: REST API for programmatic access to gene data
6. **Export Formats**: Support JSON, CSV, and database exports
7. **Version Control**: Track changes to gene information over time
8. **Collaboration Features**: Allow community contributions and updates
