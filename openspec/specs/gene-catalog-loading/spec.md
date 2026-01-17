# gene-catalog-loading Specification

## Purpose
TBD - created by archiving change 2026-01-17-create-dna-analysis-report. Update Purpose after archive.
## Requirements
### Requirement: System SHALL Load Gene Catalog from Directory

The system SHALL be able to load all YAML gene files from the `hidden/important-genes-2/` directory structure.

#### Scenario: Load all YAML files recursively
- **WHEN** catalog loader processes `hidden/important-genes-2/` directory
- **THEN** it should recursively find all `.yaml` files in subdirectories
- **AND** it should parse each YAML file using PyYAML
- **AND** it should return a GeneCatalog object containing all genes

#### Scenario: Parse gene information from YAML
- **WHEN** catalog loader processes a gene YAML file
- **THEN** it should extract all required fields:
  - gene: Gene symbol
  - full_name: Full gene name
  - category: Category folder name
  - function: Gene function description
  - health_impact: List of health impacts
- **AND** it should extract optional fields if present:
  - common_variants: List of variant objects
  - additional_rsids: List of additional rsid values
  - ancestry_compatibility: Boolean flag
  - gene_description: Detailed gene description
  - notes: Additional information

#### Scenario: Validate required fields
- **WHEN** catalog loader processes a gene YAML file
- **THEN** it should verify all required fields are present and non-empty
- **AND** it should log an error if required fields are missing
- **AND** it should skip files with missing required fields

#### Scenario: Extract rsids from variants
- **WHEN** catalog loader processes a gene with common_variants
- **THEN** it should extract rsid from each variant object
- **AND** it should extract rsids from additional_rsids list
- **AND** it should collect all rsids for the gene

#### Scenario: Build category index
- **WHEN** catalog loader has loaded all gene files
- **THEN** it should organize genes by category folder
- **AND** it should create a dictionary mapping category names to gene lists
- **AND** it should count genes per category

#### Scenario: Build rsid-to-gene mapping
- **WHEN** catalog loader has extracted all rsids from genes
- **THEN** it should create a dictionary mapping rsids to genes
- **AND** it should support multiple genes per rsid (if rsid appears in multiple genes)
- **AND** it should enable O(1) lookup of genes by rsid

#### Scenario: Handle YAML parse errors
- **WHEN** catalog loader encounters a YAML file with invalid syntax
- **THEN** it should log an error with file path
- **AND** it should skip the problematic file
- **AND** it should continue processing remaining files

#### Scenario: Handle missing required fields
- **WHEN** catalog loader processes a gene file missing required fields
- **THEN** it should log an error with file path and missing fields
- **AND** it should skip the problematic file
- **AND** it should continue processing remaining files

#### Scenario: Handle invalid rsid format
- **WHEN** catalog loader encounters an rsid that doesn't match format `rs` followed by digits
- **THEN** it should log a warning with the invalid rsid
- **AND** it should skip the invalid variant
- **AND** it should continue processing

#### Scenario: Handle empty directory
- **WHEN** catalog loader processes an empty `hidden/important-genes-2/` directory
- **THEN** it should return an empty GeneCatalog object
- **AND** it should log a warning indicating no gene files were found

#### Scenario: Return GeneCatalog object
- **WHEN** catalog loader has completed processing all files
- **THEN** it should return a GeneCatalog object with:
  - genes: List of all Gene objects
  - genes_by_category: Dictionary mapping categories to gene lists
  - rsid_to_gene: Dictionary mapping rsids to genes
  - total_genes: Total count of genes loaded

### Requirement: System SHALL Validate Gene Catalog Structure

The system SHALL validate the structure and content of the loaded gene catalog.

#### Scenario: Validate gene count
- **WHEN** validator checks the GeneCatalog object
- **THEN** it should verify total_genes matches expected count (393)
- **AND** it should log a warning if count is unexpected

#### Scenario: Validate category coverage
- **WHEN** validator checks the genes_by_category dictionary
- **THEN** it should verify all 10 expected categories are present
- **AND** it should log a warning if any category is missing

#### Scenario: Validate rsid uniqueness
- **WHEN** validator checks the rsid_to_gene dictionary
- **THEN** it should verify all rsids are properly formatted
- **AND** it should log a warning if duplicate rsids exist within same gene

