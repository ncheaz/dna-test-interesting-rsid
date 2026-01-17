# Tasks: Create DNA Analysis Report System

## Phase 1: DNA Data Parsing

- [ ] **T1.1**: Create DNA file parser module
  - Implement parser for Ancestry.com raw DNA format
  - Extract rsid-genotype pairs
  - Validate file structure and format
  - Handle parsing errors gracefully
  - Output: Dictionary mapping rsids to genotypes

- [ ] **T1.2**: Implement genotype validation
  - Validate allele format (e.g., AA, AG, GG, etc.)
  - Handle missing data or null values
  - Log invalid genotypes
  - Output: Cleaned genotype data

- [ ] **T1.3**: Create rsid index
  - Build efficient lookup structure for rsids
  - Support O(1) genotype lookup
  - Handle case sensitivity (rsids are case-insensitive)
  - Output: In-memory rsid index

## Phase 2: Gene Catalog Loading

- [ ] **T2.1**: Implement YAML file loader
  - Recursively load all YAML files from `hidden/important-genes-2/`
  - Parse gene information using PyYAML
  - Validate YAML schema compliance
  - Handle missing or malformed files
  - Output: List of gene objects

- [ ] **T2.2**: Create gene variant index
  - Extract all rsids from common_variants and additional_rsids
  - Map rsids to genes and categories
  - Handle multiple rsids per gene
  - Output: Rsid-to-gene mapping

- [ ] **T2.3**: Organize genes by category
  - Group genes by category folder
  - Count genes per category
  - Handle cross-category references
  - Output: Category-to-genes mapping

## Phase 3: Variant Matching

- [ ] **T3.1**: Implement variant matcher
  - For each gene, check if variant rsids exist in DNA data
  - Match genotypes from DNA data to variants
  - Record matched variants with allele information
  - Handle ancestry_compatibility flags
  - Output: List of matched variants per gene

- [ ] **T3.2**: Create genotype interpreter
  - Interpret genotypes (homozygous risk, heterozygous, normal)
  - Use gene file descriptions for variant significance
  - Map genotypes to risk levels where applicable
  - Output: Interpreted variant data

- [ ] **T3.3**: Generate match statistics
  - Count total variants checked
  - Count variants found vs. not found
  - Calculate coverage percentage
  - Identify genes with no matching variants
  - Output: Statistics summary

## Phase 4: Report Generation

### Phase 4a: Top Priority Genes (6 genes)

- [ ] **T4.1**: Generate top-priority-genes section
  - Create category overview with statistics
  - List all 6 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4b: High-Impact Health Genes (8 genes)

- [ ] **T4.2**: Generate high-impact-health-genes section
  - Create category overview with statistics
  - List all 8 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4c: Metabolism & Detoxification Genes (7 genes)

- [ ] **T4.3**: Generate metabolism-detoxification-genes section
  - Create category overview with statistics
  - List all 7 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4d: Cardiovascular & Heart Health Genes (5 genes)

- [ ] **T4.4**: Generate cardiovascular-heart-health-genes section
  - Create category overview with statistics
  - List all 5 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4e: Immune & Inflammation Genes (5 genes)

- [ ] **T4.5**: Generate immune-inflammation-genes section
  - Create category overview with statistics
  - List all 5 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4f: Brain & Mental Health Genes (3 genes)

- [ ] **T4.6**: Generate brain-mental-health-genes section
  - Create category overview with statistics
  - List all 3 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4g: Sleep & Circadian Rhythm Genes (4 genes)

- [ ] **T4.7**: Generate sleep-circadian-rhythm-genes section
  - Create category overview with statistics
  - List all 4 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4h: Hormone & Reproductive Health Genes (3 genes)

- [ ] **T4.8**: Generate hormone-reproductive-health-genes section
  - Create category overview with statistics
  - List all 3 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4i: Nutrient Metabolism Genes (7 genes)

- [ ] **T4.9**: Generate nutrient-metabolism-genes section
  - Create category overview with statistics
  - List all 7 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

### Phase 4j: Additional Important Genes (345 genes)

- [ ] **T4.10**: Generate additional-important-genes section
  - Create category overview with statistics
  - List all 345 genes with information
  - Analyze matched variants for each gene
  - Provide genotype interpretations
  - Include category summary and insights

## Phase 5: Report Compilation

- [ ] **T5.1**: Create report header
  - Add title and generation date
  - Include source DNA file path
  - Add total genes analyzed count
  - Create table of contents

- [ ] **T5.2**: Generate overall statistics section
  - Create summary tables:
    - Total genes analyzed
    - Total variants checked
    - Variants found vs. not found
    - Coverage by category
  - Add visual summary if possible

- [ ] **T5.3**: Add methodology section
  - Explain analysis approach
  - Describe data sources
  - Document limitations
  - Explain genotype interpretation

- [ ] **T5.4**: Compile category sections
  - Assemble all category sections in order
  - Ensure consistent formatting
  - Verify all links work
  - Add section dividers

- [ ] **T5.5**: Create summary and recommendations section
  - Summarize key findings across all categories
  - Highlight notable risk alleles
  - Identify protective alleles
  - Provide recommendations for further research
  - Note any genes requiring additional testing

- [ ] **T5.6**: Add disclaimer section
  - Include standard genetic interpretation disclaimer
  - Note that this is not medical advice
  - Recommend consultation with healthcare professionals
  - Explain limitations of genetic testing

- [ ] **T5.7**: Write final report
  - Compile all sections into `SUMMARY-FROM-RAW-DNA.md`
  - Write to project root directory
  - Validate file creation
  - Verify report completeness

## Validation Tasks

- [ ] **T6.1**: Validate DNA parsing
  - Test with sample Ancestry.com file
  - Verify all rsids extracted correctly
  - Check genotype accuracy
  - Handle edge cases

- [ ] **T6.2**: Validate gene catalog loading
  - Test with complete `hidden/important-genes-2/` directory
  - Verify all YAML files loaded
  - Check variant extraction accuracy
  - Handle missing files gracefully

- [ ] **T6.3**: Validate variant matching
  - Test with known genotypes
  - Verify correct matches
  - Check ancestry compatibility handling
  - Validate genotype interpretation

- [ ] **T6.4**: Validate report generation
  - Test report with sample data
  - Verify all categories included
  - Check formatting consistency
  - Ensure all links work

- [ ] **T6.5**: Validate overall statistics
  - Verify counts are accurate
  - Check percentages
  - Ensure coverage calculations correct
  - Validate category breakdowns

- [ ] **T6.6**: Test with real DNA data
  - Run analysis with actual Ancestry.com file
  - Verify report generates correctly
  - Check for runtime errors
  - Validate output quality

- [ ] **T6.7**: Validate proposal using `openspec validate`
  - Run `openspec validate` on proposal documents
  - Ensure proposal follows OpenSpec conventions
  - Address any validation errors

## Dependencies

- T1.1 must complete before T1.2
- T1.2 must complete before T1.3
- T1.3 must complete before T2.1
- T2.1 must complete before T2.2
- T2.2 must complete before T2.3
- T2.3 must complete before T3.1
- T3.1 must complete before T3.2
- T3.2 must complete before T3.3
- T3.3 must complete before any T4.x tasks
- All T4.x tasks must complete before T5.1
- T5.1-T5.6 must complete in order
- T5.7 must complete before any T6.x tasks
- T6.1-T6.6 must complete in order
- T6.7 can run in parallel with T6.1-T6.6

## Notes

**Implementation Language**: Python 3.x will be used for this implementation due to:
- Excellent YAML parsing support (PyYAML library)
- Strong text processing capabilities
- Easy file I/O operations
- Good performance for data processing

**Data Structures**:
- Use dictionaries for efficient rsid lookups
- Use lists for gene collections
- Use sets for uniqueness checks
- Use dataclasses or namedtuples for structured data

**Error Handling**:
- Gracefully handle missing YAML files
- Log parsing errors without crashing
- Provide informative error messages
- Continue processing when possible

**Performance Considerations**:
- Load DNA data into memory once
- Index rsids for O(1) lookup
- Process categories sequentially
- Write report in single pass
- Minimize disk I/O operations

**Testing Strategy**:
- Use sample Ancestry.com file for unit tests
- Test edge cases (empty file, malformed data)
- Validate with real DNA data
- Check report output manually
- Verify statistics calculations

**Chunking Approach**:
- Each Phase 4 sub-phase (4a through 4j) can be implemented and tested independently
- This allows for incremental development and validation
- Large category (additional-important-genes with 345 genes) may need sub-chunking

**Ancestry.com DNA File Format**:
```
# AncestryDNA raw data export
# Data provided for testing purposes
# Format: rsid chromosome position allele1 allele2
rs429358	19	44908684	T	C
rs440446	1	11183527	A	A
rs4477212	1	224045022	C	T
...
```
- Header lines start with #
- Data rows: tab-separated (rsid, chromosome, position, allele1, allele2)
- Genotype = allele1 + allele2 (e.g., AA, AG, TT)
- Some rows may have missing data
