# Spec: Variant Matching

## Overview

This specification defines the capability to match DNA genotypes against gene variants and interpret genetic findings. The interpretation will be thorough, well-written in clear language with good understandable detail, providing diagnosis, predictive insights, and descriptive writeup of what's genetic test reveals, along with a summary of impact and things to keep in mind for every result from genes data.

## ADDED Requirements

### Requirement: System SHALL Match DNA Genotypes to Gene Variants

The system SHALL be able to match extracted DNA genotypes against gene variants from the catalog.

#### Scenario: Match variant rsids in DNA data
- **WHEN** matcher processes a gene variant with an rsid
- **THEN** it should check if rsid exists in DNAData.genotypes
- **AND** if found, it should retrieve the genotype from DNA data
- **AND** it should create a MatchedVariant object with:
  - gene: The gene containing the variant
  - variant: The variant object from gene file
  - genotype: The genotype from DNA data (e.g., "AA", "AG", "GG")
  - is_risk_allele: Boolean indicating if genotype contains risk allele

#### Scenario: Determine genotype type
- **WHEN** matcher has a genotype and variant information
- **THEN** it should classify genotype as one of:
  - "homozygous_risk": Both alleles are risk alleles (e.g., AA for risk allele A)
  - "heterozygous": One risk allele, one normal allele (e.g., AG)
  - "normal": Both alleles are normal (e.g., GG)
- **AND** it should set genotype_type accordingly in MatchedVariant

#### Scenario: Interpret genotype significance
- **WHEN** matcher has classified a genotype
- **THEN** it should use variant description to interpret significance
- **AND** it should create an interpretation string explaining the genotype's meaning
- **AND** it should add interpretation to MatchedVariant object

#### Scenario: Handle variants not in DNA data
- **WHEN** matcher checks a variant rsid that doesn't exist in DNAData.genotypes
- **THEN** it should note that variant was not found in test data
- **AND** it should not create a MatchedVariant for this variant

#### Scenario: Handle ancestry compatibility flag
- **WHEN** matcher processes a gene with ancestry_compatibility: false
- **THEN** it should flag gene as "not tested by Ancestry.com"
- **AND** it should add gene to genes_without_matches list
- **AND** it should not attempt to match variants for this gene

#### Scenario: Process all genes in catalog
- **WHEN** matcher processes all genes from GeneCatalog
- **THEN** it should iterate through each gene
- **AND** it should check each variant in gene.common_variants
- **AND** it should collect all matched variants

#### Scenario: Generate match statistics
- **WHEN** matcher has completed processing all genes and variants
- **THEN** it should calculate:
  - total_variants_checked: Count of all variants examined
  - total_variants_found: Count of variants with matches in DNA data
  - coverage_percentage: (total_variants_found / total_variants_checked) × 100
- **AND** it should identify genes_with_matches: List of genes with at least one matched variant
- **AND** it should identify genes_without_matches: List of genes with no matched variants

#### Scenario: Handle invalid genotype format
- **WHEN** matcher encounters an invalid genotype from DNA data
- **THEN** it should log a warning with rsid and genotype value
- **AND** it should skip the variant
- **AND** it should continue processing remaining variants

#### Scenario: Handle missing allele information
- **WHEN** matcher has a genotype but variant description lacks risk allele information
- **THEN** it should use available data for matching
- **AND** it should note limitation in interpretation
- **AND** it should set genotype_type to "unknown" if cannot determine

#### Scenario: Return MatchResults object
- **WHEN** matcher has completed all processing and calculations
- **THEN** it should return a MatchResults object with:
  - matched_variants: List of MatchedVariant objects
  - genes_with_matches: List of Gene objects
  - genes_without_matches: List of Gene objects
  - total_variants_checked: Integer count
  - total_variants_found: Integer count
  - coverage_percentage: Float value

### Requirement: System SHALL Interpret Genetic Findings

The system SHALL provide meaningful interpretations of matched genetic variants.

#### Scenario: Interpret homozygous risk genotype
- **WHEN** interpreter processes a homozygous_risk genotype
- **THEN** it should explain that both alleles are risk alleles
- **AND** it should indicate this may have stronger health impact
- **AND** it should reference variant description for specific implications

#### Scenario: Interpret heterozygous genotype
- **WHEN** interpreter processes a heterozygous genotype
- **THEN** it should explain that one allele is a risk allele
- **AND** it should indicate this may have moderate health impact
- **AND** it should note that one normal allele may provide some protection

#### Scenario: Interpret normal genotype
- **WHEN** interpreter processes a normal genotype
- **THEN** it should explain that both alleles are normal
- **AND** it should indicate this is not a risk genotype
- **AND** it should note that this is the common or protective form

#### Scenario: Provide variant-specific interpretation
- **WHEN** interpreter has variant description from gene file
- **THEN** it should incorporate variant-specific information into interpretation
- **AND** it should explain what the variant affects (e.g., enzyme activity, receptor function)
- **AND** it should reference known health impacts from gene file

## MODIFIED Requirements

None - this is a new capability.

## REMOVED Requirements

None - this is a new capability.

## Cross-References

This specification relates to:
- [`dna-data-parsing`](../dna-data-parsing/spec.md) - Defines how DNA genotypes are extracted
- [`gene-catalog-loading`](../gene-catalog-loading/spec.md) - Defines how gene variants are loaded
- [`report-generation`](../report-generation/spec.md) - Defines how matched variants are presented in report

## Notes

- Genotype classification should use standard genetic terminology
- Risk allele determination should be based on variant descriptions from gene files
- The matcher should handle cases where risk alleles are not clearly defined
- Ancestry compatibility flag is critical for accurate reporting
- Statistics should provide clear overview of analysis coverage
- The matcher should be efficient for processing hundreds of variants
- Interpretations should be informative but not provide medical advice
- The matcher should support multiple variants per gene
- Cross-category gene references should be handled appropriately
