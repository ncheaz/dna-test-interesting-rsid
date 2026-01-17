# directory-structure-management Specification

## Purpose
TBD - created by archiving change create-gene-catalog-2. Update Purpose after archive.
## Requirements
### Requirement: System SHALL Create Main Catalog Directory

The system SHALL create the main catalog directory for gene files.

#### Scenario: Create hidden catalog directory
- **WHEN** the catalog directory is created and the project root directory exists
- **THEN** it should create `hidden/important-genes-2/` directory

#### Scenario: Set appropriate permissions
- **WHEN** permissions are set after the catalog directory is created
- **THEN** it should have read/write permissions for owner

#### Scenario: Verify directory creation
- **WHEN** verification is performed and the catalog directory should exist
- **THEN** it should confirm the directory is accessible

### Requirement: System SHALL Create Category Subdirectories

The system SHALL create category subdirectories for organizing gene files.

#### Scenario: Create top-priority-genes directory
- **WHEN** the top-priority-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/top-priority-genes/`

#### Scenario: Create high-impact-health-genes directory
- **WHEN** the high-impact-health-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/high-impact-health-genes/`

#### Scenario: Create metabolism-detoxification-genes directory
- **WHEN** the metabolism-detoxification-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/metabolism-detoxification-genes/`

#### Scenario: Create cardiovascular-heart-health-genes directory
- **WHEN** the cardiovascular-heart-health-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/cardiovascular-heart-health-genes/`

#### Scenario: Create immune-inflammation-genes directory
- **WHEN** the immune-inflammation-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/immune-inflammation-genes/`

#### Scenario: Create brain-mental-health-genes directory
- **WHEN** the brain-mental-health-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/brain-mental-health-genes/`

#### Scenario: Create sleep-circadian-rhythm-genes directory
- **WHEN** the sleep-circadian-rhythm-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/sleep-circadian-rhythm-genes/`

#### Scenario: Create hormone-reproductive-health-genes directory
- **WHEN** the hormone-reproductive-health-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/hormone-reproductive-health-genes/`

#### Scenario: Create nutrient-metabolism-genes directory
- **WHEN** the nutrient-metabolism-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/nutrient-metabolism-genes/`

#### Scenario: Create additional-important-genes directory
- **WHEN** the additional-important-genes directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/additional-important-genes/`

#### Scenario: Create additional-genes-selfdecode directory
- **WHEN** the additional-genes-selfdecode directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/additional-genes-selfdecode/`

#### Scenario: Create additional-genes-research directory
- **WHEN** the additional-genes-research directory is created and the main catalog directory exists
- **THEN** it should create `hidden/important-genes-2/additional-genes-research/`

### Requirement: System SHALL Enforce Naming Conventions

The system SHALL enforce consistent naming conventions for directories and files.

#### Scenario: Use lowercase for directory names
- **WHEN** a directory is created and a category name is provided
- **THEN** the directory name should be all lowercase

#### Scenario: Use hyphens for directory names
- **WHEN** a directory is created and a category name contains spaces or special characters
- **THEN** spaces should be replaced with hyphens

#### Scenario: Use lowercase for gene file names
- **WHEN** a gene file is created and a gene symbol is provided
- **THEN** the file name should be all lowercase

#### Scenario: Include rsid in file names
- **WHEN** a gene file is created and a gene symbol, full name, short description, and primary rsid are provided
- **THEN** the file name should follow pattern: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`

#### Scenario: Use .yaml extension
- **WHEN** the file is saved after a gene file is created
- **THEN** it should have `.yaml` extension

#### Scenario: Handle genes without rsid
- **WHEN** a gene file is created and a gene has no available rsid
- **THEN** the file name should use pattern: `<gene-symbol>-<full-name>-<short-description>.yaml` as fallback

#### Scenario: Validate file name components
- **WHEN** a gene file name is created
- **THEN** it should validate that all components are lowercase
- **THEN** it should validate that hyphens separate all components
- **THEN** it should validate that the file name follows the standardized long format pattern

### Requirement: System SHALL Validate Directory Structure

The system SHALL validate that the directory structure is complete and correct.

#### Scenario: Verify all category directories exist
- **WHEN** validation is performed and the catalog directory structure is created
- **THEN** all 12 category directories should exist

#### Scenario: Verify directory names match specification
- **WHEN** validation is performed and the catalog directory structure is created
- **THEN** all directory names should match the specification

#### Scenario: Verify directory accessibility
- **WHEN** validation is performed and the catalog directory structure is created
- **THEN** all directories should be readable and writable

#### Scenario: Verify no naming conflicts
- **WHEN** validation is performed and the catalog directory structure is created
- **THEN** there should be no duplicate or conflicting directory names

### Requirement: System SHALL Manage Directory Permissions

The system SHALL manage appropriate permissions for directories and files.

#### Scenario: Set owner read/write permissions
- **WHEN** permissions are set after a directory is created
- **THEN** the owner should have read and write permissions

#### Scenario: Set group read permissions
- **WHEN** permissions are set after a directory is created
- **THEN** the group should have read permissions

#### Scenario: Set other read permissions
- **WHEN** permissions are set after a directory is created
- **THEN** others should have read permissions

#### Scenario: Verify file permissions
- **WHEN** permissions are verified after a gene file is created
- **THEN** the file should have read and write permissions for owner

### Requirement: System SHALL Handle Directory Conflicts

The system SHALL handle conflicts when directories or files already exist.

#### Scenario: Handle existing directory
- **WHEN** attempting to create a directory that already exists
- **THEN** the system should verify it matches the specification and continue

#### Scenario: Handle existing file
- **WHEN** attempting to create a file that already exists
- **THEN** the system should prompt for overwrite or skip

#### Scenario: Handle permission denied
- **WHEN** an error occurs and a directory cannot be created due to permissions
- **THEN** the system should log the error and provide guidance

#### Scenario: Handle disk space issues
- **WHEN** an error occurs and a directory cannot be created due to disk space
- **THEN** the system should log the error and provide guidance

### Requirement: System SHALL Support Directory Cleanup

The system SHALL support cleanup of the directory structure if needed.

#### Scenario: Remove empty directory
- **WHEN** cleanup is requested and a directory is empty
- **THEN** the directory should be removed

#### Scenario: Remove directory with files
- **WHEN** cleanup is requested and a directory contains files
- **THEN** the system should prompt for confirmation before removing

#### Scenario: Preserve directory structure
- **WHEN** the main catalog directory is removed during cleanup
- **THEN** the system should confirm before removing all subdirectories

### Requirement: System SHALL Document Directory Structure

The system SHALL document the directory structure for reference.

#### Scenario: Generate directory tree
- **WHEN** documentation is generated and the catalog directory structure exists
- **THEN** it should produce a tree view of the structure

#### Scenario: Count files per directory
- **WHEN** documentation is generated and the catalog directory structure exists
- **THEN** it should count files in each directory

#### Scenario: List directories with descriptions
- **WHEN** documentation is generated and the catalog directory structure exists
- **THEN** it should list directories with their purpose

