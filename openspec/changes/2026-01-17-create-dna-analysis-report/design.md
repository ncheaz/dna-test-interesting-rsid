# Design: Create DNA Analysis Report System

## Overview

This document describes the architectural design for a DNA analysis system that parses Ancestry.com raw DNA test results, matches variants against the gene catalog in [`hidden/important-genes-2/`](../../hidden/important-genes-2/), and generates a comprehensive analysis report (`SUMMARY-FROM-RAW-DNA.md`) with category-specific genetic insights. The report will provide thorough, well-written analysis in clear language with good understandable detail, including diagnosis, predictive insights, and descriptive writeup of what's genetic test reveals, along with a summary of impact and things to keep in mind for every result from genes data.

## System Architecture

### High-Level Flow

```
User Input (DNA file path)
    ↓
Phase 1: DNA Data Parsing
    ↓
Phase 2: Gene Catalog Loading
    ↓
Phase 3: Variant Matching
    ↓
Phase 4: Report Generation (per category)
    ↓
Phase 5: Report Compilation
    ↓
Output: SUMMARY-FROM-RAW-DNA.md
```

### Component Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  DNA Analysis System                          │
├─────────────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐│
│  │ DNA Parser   │  │ Catalog      │  │ Variant      ││
│  │ Module       │  │ Loader       │  │ Matcher      ││
│  └──────────────┘  └──────────────┘  └──────────────┘│
│         ↓                 ↓                 ↓              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐│
│  │ Genotype     │  │ Gene Index   │  │ Matched      ││
│  │ Validator    │  │ Builder      │  │ Variants     ││
│  └──────────────┘  └──────────────┘  └──────────────┘│
│         ↓                 ↓                 ↓              │
│  ┌──────────────────────────────────────────────────────┐│
│  │              Report Generator                    ││
│  │  ┌────────────────────────────────────────┐     ││
│  │  │  Category Section Generator        │     ││
│  │  │  - Top Priority Genes          │     ││
│  │  │  - High-Impact Health Genes   │     ││
│  │  │  - Metabolism & Detox        │     ││
│  │  │  - Cardiovascular & Heart      │     ││
│  │  │  - Immune & Inflammation      │     ││
│  │  │  - Brain & Mental Health       │     ││
│  │  │  - Sleep & Circadian Rhythm   │     ││
│  │  │  - Hormone & Reproductive    │     ││
│  │  │  - Nutrient Metabolism       │     ││
│  │  │  - Additional Important       │     ││
│  │  └────────────────────────────────────────┘     ││
│  └──────────────────────────────────────────────────────┘│
│         ↓                                            │
│  ┌──────────────┐                                  │
│  │ Report       │                                  │
│  │ Compiler     │                                  │
│  └──────────────┘                                  │
│         ↓                                            │
│  SUMMARY-FROM-RAW-DNA.md                             │
└─────────────────────────────────────────────────────────────────┘
```

## Component Design

### 1. DNA Parser Module

**Purpose**: Parse Ancestry.com raw DNA file and extract genotype data

**Input**: Path to Ancestry.com raw DNA file (typically `AncestryDNA.txt`)

**Output**: Dictionary mapping rsids to genotypes

**Data Structures**:
```python
class Genotype:
    rsid: str  # e.g., "rs429358"
    chromosome: str  # e.g., "19"
    position: int  # e.g., 44908684
    allele1: str  # e.g., "T"
    allele2: str  # e.g., "C"
    genotype: str  # e.g., "TC" (allele1 + allele2)

class DNAData:
    source_file: str
    genotypes: Dict[str, Genotype]  # rsid -> Genotype
    total_rsids: int
```

**Algorithm**:
1. Open DNA file for reading
2. Skip header lines (lines starting with #)
3. For each data line:
   - Split by tabs
   - Extract rsid, chromosome, position, allele1, allele2
   - Validate allele format (single nucleotide: A, T, C, G)
   - Create Genotype object
   - Add to DNAData.genotypes dictionary
4. Close file
5. Return DNAData object

**Error Handling**:
- File not found: Raise clear error with expected path
- Malformed lines: Log warning, skip line
- Invalid alleles: Log warning, skip variant
- Empty file: Return empty DNAData object

### 2. Gene Catalog Loader

**Purpose**: Load and parse all YAML files from gene catalog

**Input**: Path to `hidden/important-genes-2/` directory

**Output**: List of Gene objects organized by category

**Data Structures**:
```python
class Variant:
    variant_name: str
    rsid: str
    chromosome: str
    position: int
    description: str

class Gene:
    symbol: str  # e.g., "MTHFR"
    full_name: str  # e.g., "Methylenetetrahydrofolate Reductase"
    category: str  # e.g., "top-priority-genes"
    function: str
    health_impact: List[str]
    common_variants: List[Variant]
    additional_rsids: List[str]
    ancestry_compatibility: bool
    gene_description: str
    notes: str

class GeneCatalog:
    genes: List[Gene]
    genes_by_category: Dict[str, List[Gene]]
    rsid_to_gene: Dict[str, List[Gene]]  # rsid -> genes containing it
    total_genes: int
```

**Algorithm**:
1. Walk `hidden/important-genes-2/` directory recursively
2. For each `.yaml` file:
   - Parse YAML content using PyYAML
   - Validate required fields present
   - Create Gene object
   - Extract all rsids from common_variants and additional_rsids
   - Add to catalog
3. Build category index (genes_by_category)
4. Build rsid index (rsid_to_gene)
5. Return GeneCatalog object

**Error Handling**:
- YAML parse error: Log error, skip file, continue
- Missing required fields: Log error, skip file, continue
- Invalid rsid format: Log warning, skip variant
- Empty directory: Return empty GeneCatalog object

### 3. Variant Matcher

**Purpose**: Match DNA genotypes against gene variants

**Input**: DNAData object, GeneCatalog object

**Output**: List of MatchedVariant objects

**Data Structures**:
```python
class MatchedVariant:
    gene: Gene
    variant: Variant
    genotype: str  # e.g., "AA", "AG", "GG"
    genotype_type: str  # "homozygous_risk", "heterozygous", "normal"
    interpretation: str
    is_risk_allele: bool

class MatchResults:
    matched_variants: List[MatchedVariant]
    genes_with_matches: List[Gene]
    genes_without_matches: List[Gene]
    total_variants_checked: int
    total_variants_found: int
    coverage_percentage: float
```

**Algorithm**:
1. Initialize empty MatchResults object
2. For each gene in GeneCatalog:
   - For each variant in gene.common_variants:
     - Check if variant.rsid exists in DNAData.genotypes
     - If found:
       - Get genotype from DNAData
       - Determine genotype_type based on alleles
       - Interpret significance based on variant description
       - Create MatchedVariant object
       - Add to results
     - If not found and gene.ancestry_compatibility == false:
       - Note as "not tested by Ancestry.com"
3. Calculate statistics:
   - Count total variants checked
   - Count variants found
   - Calculate coverage percentage
   - Identify genes with/without matches
4. Return MatchResults object

**Genotype Type Determination**:
- **Homozygous Risk**: Both alleles are risk alleles (e.g., AA for risk allele A)
- **Heterozygous**: One risk allele, one normal (e.g., AG)
- **Normal**: Both alleles are normal (e.g., GG)
- **Unknown**: Cannot determine from available data

**Error Handling**:
- Invalid genotype format: Log warning, skip variant
- Missing allele information: Use available data, note limitation
- Ambiguous interpretation: Note uncertainty in results

### 4. Category Section Generator

**Purpose**: Generate report section for each gene category

**Input**: Category name, List[Gene], MatchResults for category

**Output**: Markdown string for category section

**Section Structure**:
```markdown
## [Category Name]

### Genetic Classification

[Brief description of category's genetic significance]

### Genes in This Category

**Total Genes:** [count]
**Variants Analyzed:** [count]
**Variants Found in DNA Data:** [count]

[Table or list of all genes with key information]

### DNA Analysis Results

[For each gene with matching variants]

#### [Gene Symbol] - [Gene Full Name]

**Function:** [function]
**Health Impacts:**
- [impact 1]
- [impact 2]

**Variants Found:**

| Variant | rsid | Genotype | Type | Interpretation |
|----------|-------|-----------|-------|---------------|
| [name] | [rsid] | [genotype] | [type] | [interpretation] |

[For genes with no matching variants]

#### [Gene Symbol] - [Gene Full Name]

**Function:** [function]
**Health Impacts:**
- [impact 1]
- [impact 2]

**Note:** Variants for this gene are not tested by Ancestry.com (ancestry_compatibility: false).
Consider alternative genetic testing to analyze these variants.

### Category Summary

**Key Findings:**
- [Finding 1]
- [Finding 2]

**Notable Risk Alleles:**
- [allele 1]
- [allele 2]

**Protective Alleles Identified:**
- [allele 1]
- [allele 2]

**Recommendations:**
- [recommendation 1]
- [recommendation 2]
```

**Algorithm**:
1. Generate category overview with statistics
2. Create gene information table/list
3. For each gene with matches:
   - Generate variant analysis subsection
   - Include table of matched variants
   - Add genotype interpretations
4. For each gene without matches:
   - Generate note about ancestry compatibility
   - Suggest alternative testing if applicable
5. Generate category summary with key findings
6. Return formatted markdown string

### 5. Report Compiler

**Purpose**: Assemble all sections into final report

**Input**: List of category sections, MatchResults, metadata

**Output**: Complete markdown report file

**Report Structure**:
```markdown
# DNA Analysis Report from Ancestry.com Raw Data

**Generated:** [timestamp]
**Source:** [DNA file path]
**Genes Analyzed:** [total count]

## Table of Contents

[Links to all sections]

## Overall Statistics

### Analysis Coverage

| Category | Genes | Variants Checked | Variants Found | Coverage |
|-----------|--------|-----------------|----------------|----------|
| [category] | [count] | [count] | [count] | [percent] |
| ... | ... | ... | ... | ... |

### Summary

- **Total Genes Analyzed:** [count]
- **Total Variants Checked:** [count]
- **Total Variants Found:** [count]
- **Overall Coverage:** [percent]%

## Methodology

This report was generated by:
1. Parsing Ancestry.com raw DNA file ([path])
2. Loading gene catalog from `hidden/important-genes-2/`
3. Matching DNA genotypes against gene variants
4. Generating category-specific analysis sections
5. Compiling comprehensive report

**Data Sources:**
- DNA test data: Ancestry.com raw data export
- Gene catalog: `hidden/important-genes-2/` (393 genes, 10 categories)
- Variant information: Gene YAML files with rsid, chromosome, position

**Limitations:**
- Only includes variants tested by Ancestry.com (~700,000 SNPs)
- Some gene variants may not be covered (ancestry_compatibility: false)
- Interpretations are based on available research and may not be complete
- This is not medical advice; consult healthcare professionals

[Category sections...]

## Summary & Recommendations

### Overall Findings

[Summary of key findings across all categories]

### Notable Risk Alleles

[List of significant risk alleles identified]

### Protective Alleles

[List of protective alleles identified]

### Genes Requiring Additional Testing

[List of genes with ancestry_compatibility: false]

### Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

## Disclaimer

**Important Notice:**

This genetic analysis report is for informational and educational purposes only. It is not intended to provide medical advice, diagnosis, or treatment recommendations. Genetic information is complex and should be interpreted by qualified healthcare professionals.

**Limitations:**
- Ancestry.com tests approximately 700,000 SNPs, which does not cover all possible genetic variants
- Some genes may have variants not included in this test
- Genetic risk is influenced by many factors including environment, lifestyle, and other genes
- Scientific understanding of genetic variants is constantly evolving

**Recommendations:**
- Discuss these findings with a genetic counselor or healthcare provider
- Consider additional genetic testing if specific genes of interest are not covered
- Use this report as a starting point for further research and discussion

**Generated by:** DNA Analysis Report System
**Date:** [timestamp]
**Version:** 1.0
```

**Algorithm**:
1. Generate report header with metadata
2. Create table of contents
3. Generate overall statistics section
4. Add methodology section
5. Append all category sections in order
6. Generate summary and recommendations
7. Add disclaimer section
8. Write complete markdown to file

## Key Design Decisions

### 1. Data Structure Choice

**Decision**: Use Python dictionaries and dataclasses for in-memory data structures

**Rationale**:
- Dictionaries provide O(1) lookup for rsid matching
- Dataclasses provide type safety and clear structure
- Lists maintain order for report generation
- All structures are serializable for future enhancements

**Implementation**:
```python
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Genotype:
    rsid: str
    chromosome: str
    position: int
    allele1: str
    allele2: str
    genotype: str

@dataclass
class Gene:
    symbol: str
    full_name: str
    category: str
    function: str
    health_impact: List[str]
    common_variants: List[Variant]
    additional_rsids: List[str]
    ancestry_compatibility: bool
    gene_description: str
    notes: str
```

### 2. Genotype Interpretation Strategy

**Decision**: Use standard genetic terminology based on allele matching

**Rationale**:
- Provides clear, consistent terminology
- Aligns with genetic research standards
- Easy for users to understand
- Supports risk assessment without medical advice

**Implementation**:
- Compare alleles to known risk alleles from variant descriptions
- Classify as homozygous risk, heterozygous, or normal
- Use variant description for interpretation when available
- Note uncertainty when risk alleles are not clearly defined

### 3. Ancestry Compatibility Handling

**Decision**: Explicitly flag variants not tested by Ancestry.com

**Rationale**:
- Users need to know which variants are covered
- Enables informed decisions about additional testing
- Prevents false negatives in analysis
- Maintains transparency about test limitations

**Implementation**:
- Check `ancestry_compatibility` field in gene files
- For genes with `false` value:
  - Note in report that variants are not tested
  - Suggest alternative genetic testing
  - Include gene information for reference

### 4. Category Organization

**Decision**: Process categories in order of biological importance

**Rationale**:
- Prioritizes most impactful genes first
- Creates logical report flow
- Aligns with gene catalog structure
- Makes report easier to navigate

**Category Order**:
1. Top Priority Genes (most commonly researched)
2. High-Impact Health Genes (major health implications)
3. Metabolism & Detoxification Genes (drug metabolism)
4. Cardiovascular & Heart Health Genes (heart health)
5. Immune & Inflammation Genes (immune function)
6. Brain & Mental Health Genes (neurotransmitter systems)
7. Sleep & Circadian Rhythm Genes (sleep patterns)
8. Hormone & Reproductive Health Genes (hormone regulation)
9. Nutrient Metabolism Genes (vitamin processing)
10. Additional Important Genes (extended catalog)

### 5. Error Handling Strategy

**Decision**: Graceful degradation with informative error messages

**Rationale**:
- Prevents system crashes from bad data
- Provides clear feedback to users
- Allows partial results when possible
- Maintains data integrity

**Implementation**:
- Log all errors with context
- Continue processing when possible
- Skip problematic entries without stopping
- Include error summary in report

### 6. Performance Optimization

**Decision**: Use efficient data structures and single-pass processing

**Rationale**:
- Handles large DNA files efficiently
- Minimizes memory usage
- Reduces processing time
- Scales to larger gene catalogs

**Optimizations**:
- Load DNA data once into memory
- Index rsids for O(1) lookup
- Process categories sequentially
- Generate report in single pass
- Minimize disk I/O operations

### 7. Report Format

**Decision**: Use Markdown for human-readable output

**Rationale**:
- Widely supported format
- Easy to read and edit
- Compatible with GitHub and documentation tools
- Can be converted to other formats (HTML, PDF)

**Implementation**:
- Use markdown headers for structure
- Use tables for data presentation
- Use lists for itemized information
- Include links for navigation
- Add formatting for emphasis

## Data Flow

### Phase 1: DNA Parsing Flow

```
User provides DNA file path
    ↓
Open file for reading
    ↓
Parse header lines (skip)
    ↓
For each data line:
    ↓
Split by tabs
    ↓
Validate fields (rsid, chromosome, position, allele1, allele2)
    ↓
Create Genotype object
    ↓
Add to DNAData.genotypes[rsid]
    ↓
Close file
    ↓
Return DNAData object
```

### Phase 2: Catalog Loading Flow

```
Start at hidden/important-genes-2/
    ↓
Walk directory recursively
    ↓
For each .yaml file:
    ↓
Parse YAML content
    ↓
Validate required fields
    ↓
Create Gene object
    ↓
Extract rsids from common_variants
    ↓
Extract rsids from additional_rsids
    ↓
Add to GeneCatalog.genes
    ↓
Build genes_by_category index
    ↓
Build rsid_to_gene index
    ↓
Return GeneCatalog object
```

### Phase 3: Variant Matching Flow

```
Input: DNAData, GeneCatalog
    ↓
Initialize MatchResults object
    ↓
For each gene in GeneCatalog:
    ↓
For each variant in gene.common_variants:
    ↓
Check if variant.rsid in DNAData.genotypes
    ↓
If found:
    ↓
Get genotype from DNAData
    ↓
Determine genotype_type
    ↓
Interpret significance
    ↓
Create MatchedVariant object
    ↓
Add to MatchResults
    ↓
If not found and ancestry_compatibility == false:
    ↓
Add to genes_without_matches
    ↓
Calculate statistics
    ↓
Return MatchResults
```

### Phase 4: Report Generation Flow

```
Input: Category name, genes, MatchResults
    ↓
Generate category overview
    ↓
Create gene information table
    ↓
For each gene with matches:
    ↓
Generate variant analysis subsection
    ↓
Create variant table
    ↓
Add genotype interpretations
    ↓
For each gene without matches:
    ↓
Generate ancestry compatibility note
    ↓
Generate category summary
    ↓
Return markdown string
```

### Phase 5: Report Compilation Flow

```
Input: Category sections, MatchResults, metadata
    ↓
Generate report header
    ↓
Create table of contents
    ↓
Generate overall statistics
    ↓
Add methodology section
    ↓
Append category sections
    ↓
Generate summary & recommendations
    ↓
Add disclaimer section
    ↓
Write to SUMMARY-FROM-RAW-DNA.md
    ↓
Validate file creation
    ↓
Complete
```

## Error Handling

### DNA Parsing Errors

| Error Type | Handling |
|-------------|-----------|
| File not found | Raise clear error with expected path, suggest checking file location |
| Permission denied | Log error, suggest checking file permissions |
| Malformed line | Log warning with line number, skip line, continue |
| Invalid allele format | Log warning with rsid, skip variant, continue |
| Empty file | Return empty DNAData object, log warning |

### Catalog Loading Errors

| Error Type | Handling |
|-------------|-----------|
| Directory not found | Raise clear error, suggest checking path |
| YAML parse error | Log error with file path, skip file, continue |
| Missing required fields | Log error with file path and missing fields, skip file, continue |
| Invalid rsid format | Log warning with rsid, skip variant, continue |
| Empty directory | Return empty GeneCatalog object, log warning |

### Variant Matching Errors

| Error Type | Handling |
|-------------|-----------|
| Invalid genotype format | Log warning with rsid and genotype, skip variant, continue |
| Missing allele information | Use available data, note limitation in interpretation |
| Ambiguous interpretation | Note uncertainty in results, provide available information |
| Index not found | Log warning, treat as not found, continue |

### Report Generation Errors

| Error Type | Handling |
|-------------|-----------|
| Category not found | Log error, skip category, continue |
| Gene not found in catalog | Log error, skip gene, continue |
| Markdown generation error | Log error, use fallback format, continue |
| File write error | Raise clear error, suggest checking permissions and disk space |

## Performance Considerations

### Time Complexity

- **DNA Parsing**: O(n) where n = number of lines in DNA file
- **Catalog Loading**: O(g) where g = number of gene files (393)
- **Variant Matching**: O(v) where v = total variants across all genes
- **Report Generation**: O(c + g) where c = number of categories (10), g = genes
- **Overall**: O(n + g + v + c + g) ≈ O(n + v) for typical usage

### Space Complexity

- **DNA Data**: O(r) where r = number of rsids in DNA file (~700,000)
- **Gene Catalog**: O(g × v) where g = genes, v = average variants per gene
- **Match Results**: O(m) where m = matched variants
- **Report**: O(g) for in-memory markdown generation
- **Overall**: O(r + g × v + m + g) ≈ O(r + g × v) for typical usage

### Optimization Strategies

1. **Single-pass DNA parsing**: Load DNA data once, index for O(1) lookup
2. **Efficient data structures**: Use dictionaries for rsid lookups
3. **Lazy report generation**: Generate markdown strings, write once at end
4. **Batch processing**: Process categories sequentially, minimize context switching
5. **Memory management**: Use generators for large datasets if needed

## Testing Strategy

### Unit Tests

- **DNA Parser Tests**:
  - Test with valid Ancestry.com file
  - Test with empty file
  - Test with malformed lines
  - Test with invalid alleles
  - Test with missing fields

- **Catalog Loader Tests**:
  - Test with complete catalog
  - Test with empty directory
  - Test with invalid YAML
  - Test with missing required fields
  - Test with duplicate rsids

- **Variant Matcher Tests**:
  - Test with known genotypes
  - Test with no matches
  - Test with ancestry_compatibility: false
  - Test with ambiguous genotypes
  - Test with multiple matches per gene

- **Report Generator Tests**:
  - Test with sample data
  - Test with empty matches
  - Test with all matches
  - Test with mixed matches
  - Test markdown formatting

### Integration Tests

- **End-to-end test**:
  - Use sample Ancestry.com file
  - Load complete gene catalog
  - Generate full report
  - Verify output file exists
  - Validate report structure

- **Performance test**:
  - Test with large DNA file (700,000+ rsids)
  - Measure processing time
  - Verify memory usage
  - Check report generation time

### Validation Tests

- **Data validation**:
  - Verify all rsids extracted correctly
  - Check genotype accuracy
  - Validate variant matching
  - Confirm statistics calculations

- **Report validation**:
  - Verify all categories included
  - Check formatting consistency
  - Ensure all links work
  - Validate markdown syntax

## Security Considerations

### Input Validation

- **File path validation**: Sanitize input to prevent path traversal attacks
- **File type validation**: Ensure file is text-based, not executable
- **Size validation**: Check file size before processing (prevent DoS)
- **Content validation**: Validate data format before parsing

### Data Privacy

- **Local processing only**: No data sent to external servers
- **No data retention**: Process data in memory, discard after report generation
- **No logging of genotypes**: Log only metadata and errors
- **User control**: User provides file path and controls output location

### File Permissions

- **Read-only access**: DNA file opened for reading only
- **Write permissions**: Check write permissions for output directory
- **Hidden directory**: Ensure output respects hidden directory conventions
- **File ownership**: Maintain user ownership of generated files

## Maintenance Considerations

### Updating Gene Catalog

- Each gene is independent, can be updated individually
- YAML format is human-readable and editable
- New genes can be added to catalog without code changes
- System automatically loads all YAML files from directory

### Adding New Categories

- Add new category folder to `hidden/important-genes-2/`
- System automatically discovers and processes new categories
- No code changes required
- Report generator includes all discovered categories

### Supporting New DNA Providers

- Abstract DNA parser interface
- Implement provider-specific parsers
- Add provider detection logic
- Maintain backward compatibility with Ancestry.com format

### Schema Evolution

- Maintain backward compatibility with existing gene YAML files
- Document schema changes in version history
- Provide migration tools if needed
- Use optional fields for new features

## Future Enhancements

1. **Interactive CLI**: Command-line interface with options and progress indicators
2. **Multiple provider support**: Support 23andMe, MyHeritage, etc.
3. **Web interface**: Browser-based tool for easier use
4. **Export formats**: Support JSON, CSV, HTML, PDF
5. **Visualization**: Add charts and graphs for statistics
6. **Comparison mode**: Compare multiple DNA test results
7. **Database storage**: Cache results for faster re-analysis
8. **API endpoint**: REST API for programmatic access
9. **Custom reports**: Allow users to select specific categories or genes
10. **Integration with research**: Link to SNPedia, NIH, etc. from report
