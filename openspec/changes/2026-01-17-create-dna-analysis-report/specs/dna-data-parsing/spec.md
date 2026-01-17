# Spec: DNA Data Parsing

## Overview

This specification defines the capability to parse Ancestry.com raw DNA test files and extract genotype data for genetic analysis.

## ADDED Requirements

### Requirement: System SHALL Parse Ancestry.com Raw DNA Files

The system SHALL be able to parse Ancestry.com raw DNA export files and extract genotype information.

#### Scenario: Parse valid Ancestry.com DNA file
- **WHEN** parser processes a valid Ancestry.com raw DNA file
- **THEN** it should extract all rsid-genotype pairs
- **AND** it should validate file structure and format
- **AND** it should return a DNAData object with:
  - source_file: path to input file
  - genotypes: dictionary mapping rsids to genotypes
  - total_rsids: count of extracted rsids

#### Scenario: Handle header lines
- **WHEN** parser encounters lines starting with `#` (header lines)
- **THEN** it should skip these lines without processing

#### Scenario: Parse tab-separated data rows
- **WHEN** parser processes a data line (not starting with `#`)
- **THEN** it should split the line by tabs
- **AND** it should extract:
  - rsid (first field)
  - chromosome (second field)
  - position (third field)
  - allele1 (fourth field)
  - allele2 (fifth field)

#### Scenario: Validate allele format
- **WHEN** parser extracts allele1 and allele2 from a data row
- **THEN** it should validate that each allele is a single nucleotide (A, T, C, or G)
- **AND** it should log a warning if allele format is invalid
- **AND** it should skip the variant if alleles are invalid

#### Scenario: Create genotype from alleles
- **WHEN** parser has validated allele1 and allele2
- **THEN** it should combine them to create genotype (e.g., allele1="A", allele2="G" → genotype="AG")
- **AND** it should store genotype in DNAData.genotypes[rsid]

#### Scenario: Handle file not found error
- **WHEN** parser attempts to open a file that does not exist
- **THEN** it should raise a clear error message indicating the file was not found
- **AND** it should suggest checking the file path

#### Scenario: Handle permission denied error
- **WHEN** parser attempts to open a file without read permissions
- **THEN** it should log an error indicating permission issue
- **AND** it should suggest checking file permissions

#### Scenario: Handle malformed data lines
- **WHEN** parser encounters a data line with incorrect number of fields
- **THEN** it should log a warning with the line number
- **AND** it should skip the malformed line
- **AND** it should continue processing remaining lines

#### Scenario: Handle empty file
- **WHEN** parser processes an empty file
- **THEN** it should return an empty DNAData object
- **AND** it should log a warning indicating no data was found

#### Scenario: Build rsid index for efficient lookup
- **WHEN** parser has completed processing all lines
- **THEN** it should create an in-memory index of rsids
- **AND** the index should support O(1) genotype lookup by rsid
- **AND** it should handle rsid case insensitivity (rs429358 == RS429358)

### Requirement: System SHALL Validate Genotype Data

The system SHALL validate genotype data extracted from DNA files.

#### Scenario: Validate genotype format
- **WHEN** validator checks a genotype string
- **THEN** it should verify the genotype is exactly 2 characters
- **AND** it should verify both characters are valid nucleotides (A, T, C, G)
- **AND** it should return validation result (valid/invalid)

#### Scenario: Handle missing or null genotypes
- **WHEN** validator encounters a missing or null genotype value
- **THEN** it should log a warning indicating missing data
- **AND** it should exclude the variant from analysis

#### Scenario: Log invalid genotypes
- **WHEN** validator identifies an invalid genotype
- **THEN** it should log the rsid and genotype value
- **AND** it should indicate why the genotype is invalid
- **AND** it should continue processing with remaining data

## MODIFIED Requirements

None - this is a new capability.

## REMOVED Requirements

None - this is a new capability.

## Cross-References

This specification relates to:
- [`variant-matching`](../variant-matching/spec.md) - Defines how genotypes are matched against gene variants
- [`report-generation`](../report-generation/spec.md) - Defines how parsed data is used in report generation

## Notes

- Ancestry.com DNA files use tab-separated format with header lines starting with `#`
- Standard genotype format is two alleles combined (e.g., AA, AG, TT, CG)
- The parser should be case-insensitive for rsid lookups
- Error handling should be graceful, allowing partial results when possible
- The parser should support files with up to 1,000,000 rsids efficiently
