# Spec: Gene Information Management

## Overview

This specification defines the data structure and management of gene information in YAML format for the gene catalog.

## ADDED Requirements

### Requirement: System SHALL Define Gene YAML Schema

The system SHALL define and enforce a standardized YAML schema for gene information.

#### Scenario: Validate gene symbol format
- **WHEN** the `gene` field is set in a gene YAML file
- **THEN** it should be a valid HGNC gene symbol (uppercase letters, numbers, optional hyphen)

#### Scenario: Validate full name format
- **WHEN** the `full_name` field is set in a gene YAML file
- **THEN** it should be the official gene name from authoritative sources

#### Scenario: Validate category format
- **WHEN** the `category` field is set in a gene YAML file
- **THEN** it should match one of the 12 valid category folder names

#### Scenario: Validate function field
- **WHEN** the `function` field is set in a gene YAML file
- **THEN** it should be a concise description of the gene's biological function

#### Scenario: Validate health impact list
- **WHEN** the `health_impact` field is set in a gene YAML file
- **THEN** it should be a list of health conditions or traits influenced by the gene

#### Scenario: Validate common variants structure
- **WHEN** the field is validated in a gene YAML file that has `common_variants` field
- **THEN** each variant should contain:
- `variant`: Variant name or identifier
- `rsid`: rsid value in format "rs" followed by digits
- `chromosome`: Chromosome number (1-22, X, Y, or MT)
- `position`: Genomic position as integer
- `description`: Brief description of variant impact

#### Scenario: Validate additional rsids format
- **WHEN** the field is validated in a gene YAML file that has `additional_rsids` field
- **THEN** each rsid should be in format "rs" followed by digits

#### Scenario: Validate ancestry compatibility
- **WHEN** the `ancestry_compatibility` field is set in a gene YAML file
- **THEN** it should be a boolean value indicating if gene is testable by Ancestry.com

#### Scenario: Validate notes field
- **WHEN** the field is validated in a gene YAML file that has `notes` field
- **THEN** it should be multi-line text providing additional context about the gene

### Requirement: System SHALL Manage Gene Metadata

The system SHALL track metadata for each gene in the catalog.

#### Scenario: Track gene creation date
- **WHEN** metadata is recorded after a gene YAML file is created
- **THEN** it should include the date the file was created

#### Scenario: Track gene source
- **WHEN** metadata is recorded after a gene YAML file is created
- **THEN** it should reference the source document (DNA-GENES.md)

#### Scenario: Track research sources
- **WHEN** metadata is recorded in a gene YAML file that includes researched information
- **THEN** it should list the sources used (SNPedia, NIH, Genetic Lifehacks, etc.)

#### Scenario: Include detailed gene description
- **WHEN** research is performed after a gene YAML file is created
- **THEN** it should gather detailed text description of the gene, its function, and significance from authoritative sources

#### Scenario: Track last update
- **WHEN** metadata is updated after a gene YAML file is modified
- **THEN** it should include the date of last modification

### Requirement: System SHALL Handle Gene Relationships

The system SHALL manage relationships between genes and categories.

#### Scenario: Track primary category
- **WHEN** the gene file is created and a gene appears in multiple categories
- **THEN** it should be placed in the primary category (first occurrence or most relevant)

#### Scenario: Note cross-category references
- **WHEN** the gene file is created and a gene appears in multiple categories
- **THEN** the `notes` field should list all categories where the gene is relevant

#### Scenario: Handle gene families
- **WHEN** gene files are created and genes belong to a family (e.g., CYP450 family)
- **THEN** the `notes` field should indicate family relationships

#### Scenario: Handle gene pathways
- **WHEN** gene files are created and genes participate in biological pathways
- **THEN** the `notes` field should note pathway participation if relevant

### Requirement: System SHALL Support Gene Lookup

The system SHALL enable efficient lookup of genes by various criteria.

#### Scenario: Lookup by gene symbol
- **WHEN** lookup is performed and a user provides a gene symbol
- **THEN** it should return the corresponding YAML file path

#### Scenario: Lookup by rsid
- **WHEN** lookup is performed and a user provides an rsid
- **THEN** it should return all genes containing that rsid

#### Scenario: Lookup by category
- **WHEN** lookup is performed and a user provides a category
- **THEN** it should return all genes in that category

#### Scenario: Lookup by health impact
- **WHEN** lookup is performed and a user provides a health condition
- **THEN** it should return all genes affecting that condition

#### Scenario: Validate file name format
- **WHEN** a gene file is created or accessed
- **THEN** it should validate that the file name follows the standardized long format pattern
- **THEN** it should verify all components are lowercase
- **THEN** it should verify hyphens separate all components
- **THEN** it should verify the pattern: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml` or `<gene-symbol>-<full-name>-<short-description>.yaml` (fallback)

### Requirement: System SHALL Maintain Data Consistency

The system SHALL ensure consistency across all gene files.

#### Scenario: Enforce consistent naming
- **WHEN** consistency is checked and multiple gene files exist
- **THEN** all gene symbols in file names should use consistent capitalization (lowercase)
- **WHEN** consistency is checked and multiple gene files exist
- **THEN** all gene symbols in the YAML `gene` field should use consistent capitalization (uppercase)

#### Scenario: Enforce consistent category names
- **WHEN** consistency is checked and multiple gene files exist
- **THEN** all `category` fields should match valid folder names

#### Scenario: Enforce consistent rsid format
- **WHEN** consistency is checked and multiple gene files exist
- **THEN** all rsids should use "rs" prefix with digits

#### Scenario: Enforce consistent chromosome format
- **WHEN** consistency is checked and multiple gene files exist
- **THEN** all chromosome values should use consistent format (numbers 1-22, X, Y, MT)

### Requirement: System SHALL Support Data Migration

The system SHALL support migration of gene information between formats or versions.

#### Scenario: Migrate from old format
- **WHEN** migration is performed and gene information exists in old format
- **THEN** it should convert to new YAML schema

#### Scenario: Handle missing fields
- **WHEN** migration is performed and a gene file is missing optional fields
- **THEN** it should use appropriate defaults or leave fields empty

#### Scenario: Preserve data integrity
- **WHEN** migration is performed and a gene file is being migrated
- **THEN** all existing data should be preserved without loss

#### Scenario: Validate migrated data
- **WHEN** validation is performed after a gene file has been migrated
- **THEN** it should conform to the current schema

## MODIFIED Requirements

None - this is a new capability.

## REMOVED Requirements

None - this is a new capability.

## Cross-References

This specification relates to:
- [`gene-catalog-creation`](../gene-catalog-creation/spec.md) - Defines how gene catalog is created
- [`directory-structure-management`](../directory-structure-management/spec.md) - Defines how gene files are organized in directories

## Notes

- Gene symbols should follow HGNC (HUGO Gene Nomenclature Committee) guidelines
- The YAML schema is designed to be human-readable and easily editable
- Optional fields should be omitted rather than set to empty values
- The schema supports future extensions without breaking existing files
- Metadata can be stored in a separate metadata field or as comments in YAML
- File names use standardized long format: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`
  - `<gene-symbol>`: Lowercase gene symbol (e.g., mthfr, apoe, bdnf)
  - `<full-name>`: Lowercase full gene name with spaces replaced by hyphens (e.g., methylenetetrahydrofolate-reductase, apolipoprotein-e, brain-derived-neurotrophic-factor)
  - `<short-description>`: Lowercase brief description of primary variant or function with spaces replaced by hyphens (e.g., c677t, e4, val66met)
  - `<rsid>`: The primary rsid for variant (e.g., rs1801133, rs429358, rs6265)
- All components are lowercase to ensure case-insensitive file systems work correctly
- Hyphens separate all components
- If no rsid is available, file names use fallback format: `<gene-symbol>-<full-name>-<short-description>.yaml`
