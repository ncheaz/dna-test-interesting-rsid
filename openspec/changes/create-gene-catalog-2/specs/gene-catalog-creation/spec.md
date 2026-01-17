# Spec: Gene Catalog Creation

## Overview

This specification defines the capability to create a comprehensive gene catalog from source documentation into a structured YAML-based directory system.

## ADDED Requirements

### Requirement: System SHALL Parse Gene Source Document

The system SHALL be able to parse a markdown source document containing gene information and extract structured data.

#### Scenario: Extract genes from DNA-GENES.md
- **WHEN** the parser processes the file `hidden/DNA-GENES.md`
- **THEN** it should extract all unique genes with their:
  - Gene symbol
  - Full name
  - Category
  - Function
  - Health impacts
  - Common variants (if listed)

#### Scenario: Handle gene pairs
- **WHEN** the parser encounters a gene entry listing multiple genes (e.g., "MTNR1A & MTNR1B")
- **THEN** it should create separate entries for each gene in the pair

#### Scenario: Identify duplicate genes
- **WHEN** the parser processes the document and a gene appears in multiple categories
- **THEN** it should identify the gene as a duplicate and note all categories where it appears

#### Scenario: Generate gene list
- **WHEN** the parser has extracted all gene information and parsing is complete
- **THEN** it should generate a master list mapping gene symbols to categories

### Requirement: System SHALL Create Directory Structure

The system SHALL create a hierarchical directory structure for organizing gene files by category.

#### Scenario: Create main catalog directory
- **WHEN** the directory manager creates the catalog and the project root directory exists
- **THEN** it should create `hidden/important-genes-2/` directory

#### Scenario: Create category subdirectories
- **WHEN** the directory manager creates category folders and the main catalog directory exists
- **THEN** it should create 12 subdirectories with lowercase, hyphenated names:
- `top-priority-genes/`
- `high-impact-health-genes/`
- `metabolism-detoxification-genes/`
- `cardiovascular-heart-health-genes/`
- `immune-inflammation-genes/`
- `brain-mental-health-genes/`
- `sleep-circadian-rhythm-genes/`
- `hormone-reproductive-health-genes/`
- `nutrient-metabolism-genes/`
- `additional-important-genes/`
- `additional-genes-selfdecode/`
- `additional-genes-research/`

#### Scenario: Validate directory creation
- **WHEN** validation is performed after the directory manager has created all directories
- **THEN** all 13 directories (1 main + 12 categories) should exist and be accessible

### Requirement: System SHALL Create Gene YAML Files

The system SHALL create YAML files for each gene following a standardized schema.

#### Scenario: Create YAML file with required fields
- **WHEN** a YAML file is created and gene information is available
- **THEN** it must contain all required fields:
- `gene`: Gene symbol (required)
- `full_name`: Full gene name (required)
- `category`: Category folder name (required)
- `function`: Brief description of gene function (required)
- `health_impact`: List of health impacts (required)
- `gene_description`: Detailed text description of gene, its function, and significance (optional)

#### Scenario: Include variant information when available
- **WHEN** a YAML file is created and the gene has known variants
- **THEN** it should include:
- `common_variants`: List of variant objects with `variant`, `rsid`, `chromosome`, `position`, `description`
- `additional_rsids`: List of additional rsid values

#### Scenario: Set ancestry compatibility
- **WHEN** the `ancestry_compatibility` field is set in a gene file
- **THEN** it should default to `true` unless specifically set to `false`

#### Scenario: Add notes field
- **WHEN** a YAML file is created and additional information about a gene is available
- **THEN** it should include a `notes` field with multi-line text

#### Scenario: Handle duplicate genes
- **WHEN** processing a gene that has already been created in another category
- **THEN** it should add a reference note in the category's gene file pointing to the primary file

#### Scenario: Create file with rsid in name
- **WHEN** a YAML file is created and a gene symbol, full name, short description, and primary rsid are available
- **THEN** it should use naming pattern: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`
- **THEN** all components should be lowercase
- **THEN** hyphens should separate all components

#### Scenario: Create file without rsid
- **WHEN** a YAML file is created and the gene has no available rsid
- **THEN** it should use naming pattern: `<gene-symbol>-<full-name>-<short-description>.yaml` as fallback
- **THEN** all components should be lowercase
- **THEN** hyphens should separate all components

### Requirement: System SHALL Research Gene Information

The system SHALL gather additional gene information from external sources via browser MCP.

#### Scenario: Research rsid information
- **WHEN** research is performed via browser MCP and a gene symbol is provided
- **THEN** it should search SNPedia for rsid information and extract:
- rsid values
- Chromosome number
- Genomic position
- Variant descriptions

#### Scenario: Research gene function
- **WHEN** research is performed via browser MCP and a gene symbol is provided
- **THEN** it should search NIH Genetics Home Reference for authoritative gene function information

#### Scenario: Research health impacts
- **WHEN** research is performed via browser MCP and a gene symbol is provided
- **THEN** it should search Genetic Lifehacks for practical health impact information

#### Scenario: Handle research unavailability
- **WHEN** research cannot be performed because browser MCP is unavailable or search fails
- **THEN** it should use information from the source document and document the limitation in the gene's `notes` field

### Requirement: System SHALL Validate YAML Schema

The system SHALL validate that all YAML files conform to the established schema.

#### Scenario: Validate required fields
- **WHEN** schema validation is performed on a YAML file
- **THEN** it should verify all required fields are present and non-empty

#### Scenario: Validate YAML syntax
- **WHEN** syntax validation is performed on a YAML file
- **THEN** it should verify the file is valid YAML syntax

#### Scenario: Validate field types
- **WHEN** type validation is performed on a YAML file
- **THEN** it should verify:
- `gene` is a string
- `full_name` is a string
- `category` is a string
- `function` is a string
- `health_impact` is a list
- `common_variants` is a list (if present)
- `additional_rsids` is a list (if present)
- `ancestry_compatibility` is a boolean
- `notes` is a string (if present)

### Requirement: System SHALL Manage Context

The system SHALL manage context efficiently to prevent memory exhaustion during long-running tasks.

#### Scenario: Compact context after gene creation
- **WHEN** context compaction is triggered after a gene YAML file has been successfully created and validated
- **THEN** it should discard:
- Previous gene details
- Browser MCP search results
- Research notes
And retain only:
- Current gene being processed
- Category mapping
- YAML schema template

#### Scenario: Maintain essential state
- **WHEN** processing continues to the next gene after context compaction is performed
- **THEN** it should maintain:
- Master gene list
- Category folder mapping
- YAML schema template
- Processing guidelines

### Requirement: System SHALL Generate Summary Document

The system SHALL create a comprehensive summary document documenting all genes in the catalog.

#### Scenario: Create summary with directory structure
- **WHEN** the summary document is generated and all gene files have been created
- **THEN** it should include an overview of the directory structure with all 12 categories

#### Scenario: Include category breakdown
- **WHEN** the summary document is generated and all gene files have been created
- **THEN** it should list all genes in each category with links to their YAML files

#### Scenario: Document YAML format
- **WHEN** the format section is generated while the summary document is being created
- **THEN** it should document the YAML schema with examples and field explanations

#### Scenario: Include usage instructions
- **WHEN** the usage section is generated while the summary document is being created
- **THEN** it should provide instructions for using the catalog with AncestryDNA data

#### Scenario: Add statistics
- **WHEN** the summary document is generated and all gene files have been created
- **THEN** it should include:
- Total gene count
- Gene count per category
- Last updated date
- Sources referenced

### Requirement: System SHALL Handle Errors Gracefully

The system SHALL handle errors without halting the entire process.

#### Scenario: Handle parse errors
- **WHEN** the parser encounters an error because a gene entry is malformed in the source document
- **THEN** it should log the error, skip the gene, and continue processing

#### Scenario: Handle research errors
- **WHEN** research cannot be performed because browser MCP is unavailable or search fails
- **THEN** it should use available information and document the limitation

#### Scenario: Handle YAML creation errors
- **WHEN** the error occurs and a YAML file cannot be created
- **THEN** it should log the error, check permissions, and retry

#### Scenario: Handle directory creation errors
- **WHEN** the error occurs and a directory cannot be created
- **THEN** it should log the error and abort if critical, or continue if non-critical

## MODIFIED Requirements

None - this is a new capability.

## REMOVED Requirements

None - this is a new capability.

## Cross-References

This specification relates to:
- [`gene-information-management`](../gene-information-management/spec.md) - Defines how gene information is structured and managed
- [`directory-structure-management`](../directory-structure-management/spec.md) - Defines how the directory structure is created and maintained

## Notes

- All gene symbols should be validated against standard HGNC nomenclature
- Category folder names must be lowercase and hyphenated
- The system should process genes in batches to optimize performance
- Context compaction is critical for processing 300+ genes without memory exhaustion
- Research depth should be tiered based on gene prominence (Tier 1: Top Priority, Tier 2: Health Impact, Tier 3: Additional)
- File names use standardized long format: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`
  - `<gene-symbol>`: Lowercase gene symbol (e.g., mthfr, apoe, bdnf)
  - `<full-name>`: Lowercase full gene name with spaces replaced by hyphens (e.g., methylenetetrahydrofolate-reductase, apolipoprotein-e, brain-derived-neurotrophic-factor)
  - `<short-description>`: Lowercase brief description of primary variant or function with spaces replaced by hyphens (e.g., c677t, e4, val66met)
  - `<rsid>`: The primary rsid for variant (e.g., rs1801133, rs429358, rs6265)
- All components are lowercase to ensure case-insensitive file systems work correctly
- Hyphens separate all components
- If no rsid is available, file names use fallback format: `<gene-symbol>-<full-name>-<short-description>.yaml`
