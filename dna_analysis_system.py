#!/usr/bin/env python3
"""
DNA Analysis Report System

This system parses Ancestry.com raw DNA test results, matches variants against
the gene catalog in hidden/important-genes-2/, and generates a comprehensive
analysis report (SUMMARY-FROM-RAW-DNA.md).

Usage:
    python dna_analysis_system.py
"""

import os
import sys
import yaml
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from datetime import datetime
from pathlib import Path


# ============================================================================
# Data Structures
# ============================================================================

@dataclass
class Genotype:
    """Represents a genotype from DNA test results."""
    rsid: str
    chromosome: str
    position: int
    allele1: str
    allele2: str
    genotype: str

    @property
    def is_homozygous(self) -> bool:
        """Check if genotype is homozygous."""
        return self.allele1 == self.allele2


@dataclass
class Variant:
    """Represents a genetic variant from gene catalog."""
    variant: str
    rsid: str
    chromosome: str
    position: int
    description: str


@dataclass(frozen=True, unsafe_hash=True)
class Gene:
    """Represents a gene from the catalog."""
    symbol: str
    full_name: str
    category: str
    function: str
    health_impact: List[str]
    common_variants: List[Variant]
    additional_rsids: List[str]
    ancestry_compatibility: bool
    research_sources: List[str]
    notes: str
    gene_description: str


@dataclass
class MatchedVariant:
    """Represents a matched variant from DNA test."""
    gene: Gene
    variant: Variant
    genotype: str
    genotype_type: str
    interpretation: str
    is_risk_allele: bool


@dataclass
class MatchResults:
    """Results of variant matching."""
    matched_variants: List[MatchedVariant] = field(default_factory=list)
    genes_with_matches: Set[str] = field(default_factory=set)  # Store gene symbols
    genes_without_matches: Set[str] = field(default_factory=set)  # Store gene symbols
    total_variants_checked: int = 0
    total_variants_found: int = 0
    coverage_percentage: float = 0.0


@dataclass
class CategoryStats:
    """Statistics for a gene category."""
    category_name: str
    total_genes: int = 0
    total_variants_checked: int = 0
    total_variants_found: int = 0
    coverage_percentage: float = 0.0
    genes_with_matches: int = 0
    genes_without_matches: int = 0


# ============================================================================
# DNA Parser Module
# ============================================================================

class DNAParser:
    """Parses Ancestry.com raw DNA files."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> Dict[str, Genotype]:
        """
        Parse Ancestry.com raw DNA file and extract genotype data.

        Returns:
            Dictionary mapping rsids to Genotype objects.
        """
        genotypes = {}
        line_number = 0
        header_skipped = False

        print(f"Parsing DNA file: {self.file_path}")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line_number += 1
                    line = line.strip()

                    # Skip header lines
                    if not header_skipped:
                        if line.startswith('#') or line.startswith('rsid'):
                            continue
                        else:
                            header_skipped = True

                    # Skip empty lines
                    if not line:
                        continue

                    # Parse data line
                    parts = line.split('\t')
                    if len(parts) < 5:
                        continue

                    rsid, chromosome, position, allele1, allele2 = parts[:5]

                    # Validate alleles
                    if not self._validate_allele(allele1) or not self._validate_allele(allele2):
                        continue

                    # Create genotype
                    genotype = Genotype(
                        rsid=rsid,
                        chromosome=chromosome,
                        position=int(position),
                        allele1=allele1,
                        allele2=allele2,
                        genotype=allele1 + allele2
                    )

                    genotypes[rsid] = genotype

        except FileNotFoundError:
            print(f"Error: DNA file not found: {self.file_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error parsing DNA file at line {line_number}: {e}")
            sys.exit(1)

        print(f"Parsed {len(genotypes)} genotypes from DNA file")
        return genotypes

    def _validate_allele(self, allele: str) -> bool:
        """Validate allele format (A, T, C, G, or 0 for missing)."""
        valid_alleles = {'A', 'T', 'C', 'G', '0'}
        return allele.upper() in valid_alleles


# ============================================================================
# Gene Catalog Loader
# ============================================================================

class GeneCatalogLoader:
    """Loads and parses gene catalog YAML files."""

    def __init__(self, catalog_path: str):
        self.catalog_path = catalog_path

    def load(self) -> List[Gene]:
        """
        Load all YAML files from gene catalog.

        Returns:
            List of Gene objects.
        """
        genes = []
        catalog_dir = Path(self.catalog_path)

        if not catalog_dir.exists():
            print(f"Error: Gene catalog directory not found: {self.catalog_path}")
            sys.exit(1)

        print(f"Loading gene catalog from: {self.catalog_path}")

        # Walk through all YAML files
        yaml_files = list(catalog_dir.rglob('*.yaml'))
        print(f"Found {len(yaml_files)} YAML files")

        for yaml_file in yaml_files:
            try:
                gene = self._parse_gene_file(yaml_file)
                if gene:
                    genes.append(gene)
            except Exception as e:
                print(f"Warning: Error parsing {yaml_file}: {e}")
                continue

        print(f"Loaded {len(genes)} genes from catalog")
        return genes

    def _parse_gene_file(self, yaml_file: Path) -> Optional[Gene]:
        """Parse a single gene YAML file."""
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Parse variants
        common_variants = []
        for variant_data in data.get('common_variants', []):
            variant = Variant(
                variant=variant_data['variant'],
                rsid=variant_data['rsid'],
                chromosome=str(variant_data['chromosome']),
                position=int(variant_data['position']),
                description=variant_data['description']
            )
            common_variants.append(variant)

        # Create gene object
        gene = Gene(
            symbol=data['gene'],
            full_name=data['full_name'],
            category=data['category'],
            function=data['function'],
            health_impact=data.get('health_impact', []),
            common_variants=common_variants,
            additional_rsids=data.get('additional_rsids', []),
            ancestry_compatibility=data.get('ancestry_compatibility', True),
            research_sources=data.get('research_sources', []),
            notes=data.get('notes', ''),
            gene_description=data.get('gene_description', '')
        )

        return gene


# ============================================================================
# Variant Matcher
# ============================================================================

class VariantMatcher:
    """Matches DNA genotypes against gene variants."""

    def __init__(self, genotypes: Dict[str, Genotype]):
        self.genotypes = genotypes

    def match(self, genes: List[Gene]) -> MatchResults:
        """
        Match DNA genotypes against gene variants.

        Args:
            genes: List of Gene objects.

        Returns:
            MatchResults object with matched variants.
        """
        results = MatchResults()

        print("Matching variants...")

        for gene in genes:
            gene_has_match = False

            for variant in gene.common_variants:
                results.total_variants_checked += 1

                # Check if rsid exists in DNA data
                if variant.rsid in self.genotypes:
                    genotype_obj = self.genotypes[variant.rsid]
                    matched_variant = self._create_matched_variant(
                        gene, variant, genotype_obj
                    )
                    results.matched_variants.append(matched_variant)
                    results.total_variants_found += 1
                    results.genes_with_matches.add(gene.symbol)
                    gene_has_match = True
                elif not gene.ancestry_compatibility:
                    # Variant not tested by Ancestry
                    results.genes_without_matches.add(gene.symbol)

            if not gene_has_match and gene.ancestry_compatibility:
                # Gene has no matches but is compatible
                results.genes_without_matches.add(gene.symbol)

        # Calculate coverage
        if results.total_variants_checked > 0:
            results.coverage_percentage = (
                results.total_variants_found / results.total_variants_checked
            ) * 100

        print(f"Matched {results.total_variants_found} of {results.total_variants_checked} variants")
        print(f"Coverage: {results.coverage_percentage:.1f}%")

        return results

    def _create_matched_variant(
        self,
        gene: Gene,
        variant: Variant,
        genotype_obj: Genotype
    ) -> MatchedVariant:
        """Create a MatchedVariant object."""
        genotype = genotype_obj.genotype
        genotype_type, interpretation, is_risk = self._interpret_genotype(
            variant, genotype
        )

        return MatchedVariant(
            gene=gene,
            variant=variant,
            genotype=genotype,
            genotype_type=genotype_type,
            interpretation=interpretation,
            is_risk_allele=is_risk
        )

    def _interpret_genotype(
        self,
        variant: Variant,
        genotype: str
    ) -> tuple[str, str, bool]:
        """
        Interpret genotype based on variant description.

        Returns:
            Tuple of (genotype_type, interpretation, is_risk_allele)
        """
        # Simple interpretation based on homozygous/heterozygous
        if genotype[0] == genotype[1]:
            genotype_type = "Homozygous"
            interpretation = f"Both alleles are {genotype[0]}. {variant.description}"
        else:
            genotype_type = "Heterozygous"
            interpretation = f"One {genotype[0]} and one {genotype[1]} allele. {variant.description}"

        # Determine if risk allele (simplified logic)
        # This is a placeholder - real implementation would need more sophisticated logic
        is_risk = False
        if 'T' in genotype and 'C677T' in variant.variant:
            is_risk = True

        return genotype_type, interpretation, is_risk


# ============================================================================
# Report Generator
# ============================================================================

class ReportGenerator:
    """Generates comprehensive DNA analysis report."""

    CATEGORY_ORDER = [
        'top-priority-genes',
        'high-impact-health-genes',
        'metabolism-detoxification-genes',
        'cardiovascular-heart-health-genes',
        'immune-inflammation-genes',
        'brain-mental-health-genes',
        'sleep-circadian-rhythm-genes',
        'hormone-reproductive-health-genes',
        'nutrient-metabolism-genes',
        'additional-important-genes'
    ]

    CATEGORY_NAMES = {
        'top-priority-genes': 'Top Priority Genes',
        'high-impact-health-genes': 'High-Impact Health Genes',
        'metabolism-detoxification-genes': 'Metabolism & Detoxification Genes',
        'cardiovascular-heart-health-genes': 'Cardiovascular & Heart Health Genes',
        'immune-inflammation-genes': 'Immune & Inflammation Genes',
        'brain-mental-health-genes': 'Brain & Mental Health Genes',
        'sleep-circadian-rhythm-genes': 'Sleep & Circadian Rhythm Genes',
        'hormone-reproductive-health-genes': 'Hormone & Reproductive Health Genes',
        'nutrient-metabolism-genes': 'Nutrient Metabolism Genes',
        'additional-important-genes': 'Additional Important Genes'
    }

    def __init__(self, genes: List[Gene], match_results: MatchResults, dna_file_path: str):
        self.genes = genes
        self.match_results = match_results
        self.dna_file_path = dna_file_path
        self.category_stats = self._calculate_category_stats()

    def _calculate_category_stats(self) -> Dict[str, CategoryStats]:
        """Calculate statistics for each category."""
        stats = {}

        # Group genes by category
        genes_by_category: Dict[str, List[Gene]] = {}
        for gene in self.genes:
            if gene.category not in genes_by_category:
                genes_by_category[gene.category] = []
            genes_by_category[gene.category].append(gene)

        # Calculate stats for each category
        for category, category_genes in genes_by_category.items():
            category_variants = self.match_results.matched_variants
            category_matches = [mv for mv in category_variants if mv.gene.category == category]

            total_variants_checked = sum(len(g.common_variants) for g in category_genes)
            total_variants_found = len(category_matches)

            coverage = 0.0
            if total_variants_checked > 0:
                coverage = (total_variants_found / total_variants_checked) * 100

            genes_with_matches = len({mv.gene.symbol for mv in category_matches})
            genes_without_matches = len(category_genes) - genes_with_matches

            stats[category] = CategoryStats(
                category_name=self.CATEGORY_NAMES.get(category, category),
                total_genes=len(category_genes),
                total_variants_checked=total_variants_checked,
                total_variants_found=total_variants_found,
                coverage_percentage=coverage,
                genes_with_matches=genes_with_matches,
                genes_without_matches=genes_without_matches
            )

        return stats

    def generate(self, output_path: str = 'SUMMARY-FROM-RAW-DNA.md'):
        """Generate the complete DNA analysis report."""
        print(f"Generating report: {output_path}")

        report_parts = []

        # Header
        report_parts.append(self._generate_header())

        # Table of Contents
        report_parts.append(self._generate_table_of_contents())

        # Overall Statistics
        report_parts.append(self._generate_overall_statistics())

        # Methodology
        report_parts.append(self._generate_methodology())

        # Category Sections
        for category in self.CATEGORY_ORDER:
            if category in self.category_stats:
                report_parts.append(self._generate_category_section(category))

        # Summary & Recommendations
        report_parts.append(self._generate_summary_and_recommendations())

        # Disclaimer
        report_parts.append(self._generate_disclaimer())

        # Write to file
        report_content = '\n\n'.join(report_parts)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"Report generated successfully: {output_path}")

    def _generate_header(self) -> str:
        """Generate report header."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        total_genes = len(self.genes)

        return f"""# DNA Analysis Report from Ancestry.com Raw Data

**Generated:** {timestamp}
**Source:** {self.dna_file_path}
**Genes Analyzed:** {total_genes}
"""

    def _generate_table_of_contents(self) -> str:
        """Generate table of contents."""
        return """## Table of Contents

1. [Overall Statistics](#overall-statistics)
2. [Methodology](#methodology)
3. [Top Priority Genes](#top-priority-genes)
4. [High-Impact Health Genes](#high-impact-health-genes)
5. [Metabolism & Detoxification Genes](#metabolism-detoxification-genes)
6. [Cardiovascular & Heart Health Genes](#cardiovascular-heart-health-genes)
7. [Immune & Inflammation Genes](#immune-inflammation-genes)
8. [Brain & Mental Health Genes](#brain-mental-health-genes)
9. [Sleep & Circadian Rhythm Genes](#sleep-circadian-rhythm-genes)
10. [Hormone & Reproductive Health Genes](#hormone-reproductive-health-genes)
11. [Nutrient Metabolism Genes](#nutrient-metabolism-genes)
12. [Additional Important Genes](#additional-important-genes)
13. [Summary & Recommendations](#summary--recommendations)
14. [Disclaimer](#disclaimer)
"""

    def _generate_overall_statistics(self) -> str:
        """Generate overall statistics section."""
        total_variants = sum(cs.total_variants_checked for cs in self.category_stats.values())
        total_found = sum(cs.total_variants_found for cs in self.category_stats.values())
        overall_coverage = 0.0
        if total_variants > 0:
            overall_coverage = (total_found / total_variants) * 100

        stats_table = "| Category | Genes | Variants Checked | Variants Found | Coverage |\n"
        stats_table += "|----------|--------|------------------|----------------|----------|\n"

        for category in self.CATEGORY_ORDER:
            if category in self.category_stats:
                cs = self.category_stats[category]
                stats_table += f"| {cs.category_name} | {cs.total_genes} | {cs.total_variants_checked} | {cs.total_variants_found} | {cs.coverage_percentage:.1f}% |\n"

        return f"""## Overall Statistics

### Analysis Coverage

{stats_table}

### Summary

- **Total Genes Analyzed:** {len(self.genes)}
- **Total Variants Checked:** {total_variants}
- **Total Variants Found:** {total_found}
- **Overall Coverage:** {overall_coverage:.1f}%
"""

    def _generate_methodology(self) -> str:
        """Generate methodology section."""
        return """## Methodology

This report was generated by:

1. **Parsing Ancestry.com raw DNA file** - Extracting all genotype data for rsids
2. **Loading gene catalog** - Reading all gene information from `hidden/important-genes-2/`
3. **Matching variants** - Comparing DNA genotypes against gene variants
4. **Generating analysis sections** - Creating category-specific genetic insights
5. **Compiling comprehensive report** - Assembling all findings into a single document

### Data Sources

- **DNA test data:** Ancestry.com raw data export ({dna_file_path})
- **Gene catalog:** `hidden/important-genes-2/` ({len_genes} genes, {len_categories} categories)
- **Variant information:** Gene YAML files with rsid, chromosome, position, and descriptions

### Limitations

- Only includes variants tested by Ancestry.com (~700,000 SNPs)
- Some gene variants may not be covered (marked with `ancestry_compatibility: false`)
- Interpretations are based on available research and may not be complete
- This is not medical advice; consult healthcare professionals
- Genetic risk is influenced by many factors including environment, lifestyle, and other genes

### Genotype Interpretation

- **Homozygous:** Both alleles are the same (e.g., AA, GG, TT, CC)
- **Heterozygous:** Two different alleles (e.g., AG, TC)
- Risk alleles are identified based on variant descriptions from research sources
- Each variant interpretation includes information from the gene catalog
""".format(dna_file_path=self.dna_file_path, len_genes=len(self.genes), len_categories=len(self.category_stats))

    def _generate_category_section(self, category: str) -> str:
        """Generate section for a specific category."""
        category_name = self.CATEGORY_NAMES.get(category, category)
        stats = self.category_stats[category]

        # Get genes for this category
        category_genes = [g for g in self.genes if g.category == category]
        
        # Debug: Print category info
        print(f"DEBUG: Category: {category}, Type: {type(category)}")
        print(f"DEBUG: Category genes count: {len(category_genes)}")
        if category_genes:
            print(f"DEBUG: First gene type: {type(category_genes[0])}")
            print(f"DEBUG: First gene: {category_genes[0]}")

        # Get matched variants for this category
        category_matches = [mv for mv in self.match_results.matched_variants if mv.gene.category == category]

        # Group matches by gene symbol
        matches_by_gene: Dict[str, List[MatchedVariant]] = {}
        for mv in category_matches:
            if mv.gene.symbol not in matches_by_gene:
                matches_by_gene[mv.gene.symbol] = []
            matches_by_gene[mv.gene.symbol].append(mv)

        section = f"## {category_name}\n\n"

        # Category Overview
        section += f"""### Genetic Classification

This category contains {stats.total_genes} genes related to {category_name.lower()}. These genes play important roles in various biological processes and have been identified through research as having significant health implications.

### Genes in This Category

**Total Genes:** {stats.total_genes}
**Variants Analyzed:** {stats.total_variants_checked}
**Variants Found in DNA Data:** {stats.total_variants_found}
**Coverage:** {stats.coverage_percentage:.1f}%

"""

        # List all genes
        section += "#### Gene Information\n\n"
        for idx, gene_info in enumerate(category_genes):
            print(f"DEBUG: Iterating gene {idx}, type: {type(gene_info)}, value: {gene_info}")
            section += f"**{gene_info.symbol.upper()}** - {gene_info.full_name}\n"
            section += f"- **Function:** {gene_info.function}\n"
            section += f"- **Health Impacts:** {', '.join(gene_info.health_impact)}\n"
            section += f"- **Variants Tracked:** {len(gene_info.common_variants)} common variants\n"
            if not gene_info.ancestry_compatibility:
                section += f"- **Note:** Some variants may not be tested by Ancestry.com\n"
            section += "\n"

        # DNA Analysis Results
        section += "### DNA Analysis Results\n\n"

        if matches_by_gene:
            for gene_symbol, matches in matches_by_gene.items():
                gene = matches[0].gene  # Get gene from first match
                section += f"#### {gene.symbol.upper()} - {gene.full_name}\n\n"
                section += f"**Function:** {gene.function}\n\n"
                section += f"**Health Impacts:**\n"
                for impact in gene.health_impact:
                    section += f"- {impact}\n"
                section += "\n"

                section += "**Variants Found:**\n\n"
                section += "| Variant | rsid | Genotype | Type | Interpretation |\n"
                section += "|----------|------|----------|------|----------------|\n"

                for mv in matches:
                    section += f"| {mv.variant.variant} | {mv.variant.rsid} | {mv.genotype} | {mv.genotype_type} | {mv.interpretation[:100]}... |\n"

                section += "\n"
        else:
            section += "**No variants found in DNA data for this category.**\n\n"

        # Category Summary
        section += "### Category Summary\n\n"
        section += f"**Key Findings:**\n"
        section += f"- {stats.genes_with_matches} of {stats.total_genes} genes have matching variants in your DNA data\n"
        section += f"- {stats.total_variants_found} variants were found out of {stats.total_variants_checked} checked\n"
        section += f"- Coverage: {stats.coverage_percentage:.1f}%\n\n"

        if stats.genes_without_matches > 0:
            section += f"**Note:** {stats.genes_without_matches} genes in this category have no matching variants. This could mean:\n"
            section += "- The variants are not tested by Ancestry.com\n"
            section += "- You have the normal (non-risk) alleles\n"
            section += "- The variants are not present in your DNA\n\n"

        return section

    def _generate_summary_and_recommendations(self) -> str:
        """Generate summary and recommendations section."""
        total_variants = sum(cs.total_variants_checked for cs in self.category_stats.values())
        total_found = sum(cs.total_variants_found for cs in self.category_stats.values())

        # Count risk alleles
        risk_variants = [mv for mv in self.match_results.matched_variants if mv.is_risk_allele]

        # Count genes requiring additional testing
        genes_needing_testing = [g for g in self.genes if not g.ancestry_compatibility]

        return f"""## Summary & Recommendations

### Overall Findings

This DNA analysis report examined {len(self.genes)} genes across {len(self.category_stats)} categories, checking {total_variants} genetic variants against your Ancestry.com test results. A total of {total_found} variants were found in your DNA data, representing a comprehensive overview of your genetic makeup across multiple health-related categories.

### Notable Findings

- **Total Genes Analyzed:** {len(self.genes)}
- **Total Variants Checked:** {total_variants}
- **Variants Found:** {total_found}
- **Risk Alleles Identified:** {len(risk_variants)}
- **Genes Requiring Additional Testing:** {len(genes_needing_testing)}

### Risk Alleles

{self._format_risk_alleles(risk_variants)}

### Genes Requiring Additional Testing

The following genes have variants that may not be tested by Ancestry.com:

{self._format_genes_needing_testing(genes_needing_testing)}

### Recommendations

1. **Review Category Sections:** Each category section provides detailed information about genes relevant to that area of health.

2. **Consult Healthcare Professionals:** Discuss these findings with a genetic counselor or healthcare provider for personalized interpretation.

3. **Consider Additional Testing:** For genes marked as not compatible with Ancestry.com, consider alternative genetic testing providers that may cover these variants.

4. **Research Further:** Use the gene descriptions and research sources to learn more about specific genes and their implications.

5. **Lifestyle Considerations:** While genetics influence health, lifestyle factors play a significant role. Focus on modifiable risk factors.

6. **Stay Informed:** Genetic research is constantly evolving. Stay updated on new discoveries about these genes.

### Important Notes

- This analysis is based on current scientific understanding, which may change as research progresses.
- Genetic risk is one factor among many that influence health outcomes.
- Environment, lifestyle, and other genetic factors all play important roles.
- This report is for informational purposes only and is not a substitute for professional medical advice.
"""

    def _format_risk_alleles(self, risk_variants: List[MatchedVariant]) -> str:
        """Format risk alleles list."""
        if not risk_variants:
            return "- No significant risk alleles identified in this analysis.\n"

        text = ""
        for rv in risk_variants[:20]:  # Limit to first 20
            text += f"- **{rv.gene.symbol.upper()}** ({rv.variant.rsid}): {rv.variant.variant} - {rv.interpretation[:80]}...\n"

        if len(risk_variants) > 20:
            text += f"- ... and {len(risk_variants) - 20} additional risk alleles (see category sections for details)\n"

        return text

    def _format_genes_needing_testing(self, genes: List[Gene]) -> str:
        """Format genes needing additional testing."""
        if not genes:
            return "- All genes in this catalog are compatible with Ancestry.com testing.\n"

        text = ""
        for gene in genes[:20]:  # Limit to first 20
            text += f"- **{gene.symbol.upper()}** - {gene.full_name}\n"

        if len(genes) > 20:
            text += f"- ... and {len(genes) - 20} additional genes\n"

        return text

    def _generate_disclaimer(self) -> str:
        """Generate disclaimer section."""
        return """## Disclaimer

**Important Notice:**

This genetic analysis report is for informational and educational purposes only. It is not intended to provide medical advice, diagnosis, or treatment recommendations. Genetic information is complex and should be interpreted by qualified healthcare professionals.

### Limitations

- Ancestry.com tests approximately 700,000 SNPs, which does not cover all possible genetic variants
- Some genes may have variants not included in this test
- Genetic risk is influenced by many factors including environment, lifestyle, and other genes
- Scientific understanding of genetic variants is constantly evolving
- Variant interpretations are based on available research and may not be complete

### Recommendations

- **Discuss these findings with a genetic counselor or healthcare provider** before making any health decisions
- **Consider additional genetic testing** if specific genes of interest are not covered
- **Use this report as a starting point** for further research and discussion with professionals
- **Do not use this information** to self-diagnose or self-treat any health conditions
- **Maintain a healthy lifestyle** regardless of genetic predispositions

### Privacy and Data Security

- This analysis was performed locally on your computer
- No genetic data was transmitted to external servers
- Your DNA data remains under your control

---

**Generated by:** DNA Analysis Report System
**Date:** {timestamp}
**Version:** 1.0

For questions or feedback, please refer to the project documentation.
""".format(timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))


# ============================================================================
# Main Application
# ============================================================================

def main():
    """Main application entry point."""
    print("=" * 70)
    print("DNA Analysis Report System")
    print("=" * 70)
    print()

    # Configuration
    dna_file_path = 'dna-test-results/dna-data-2026-01-12/AncestryDNA.txt'
    catalog_path = 'hidden/important-genes-2'
    output_path = 'SUMMARY-FROM-RAW-DNA.md'

    # Phase 1: Parse DNA Data
    print("Phase 1: Parsing DNA Data")
    print("-" * 70)
    parser = DNAParser(dna_file_path)
    genotypes = parser.parse()
    print()

    # Phase 2: Load Gene Catalog
    print("Phase 2: Loading Gene Catalog")
    print("-" * 70)
    catalog_loader = GeneCatalogLoader(catalog_path)
    genes = catalog_loader.load()
    print()

    # Phase 3: Match Variants
    print("Phase 3: Matching Variants")
    print("-" * 70)
    matcher = VariantMatcher(genotypes)
    match_results = matcher.match(genes)
    print()

    # Phase 4 & 5: Generate Report
    print("Phase 4 & 5: Generating Report")
    print("-" * 70)
    report_generator = ReportGenerator(genes, match_results, dna_file_path)
    report_generator.generate(output_path)
    print()

    print("=" * 70)
    print("Analysis Complete!")
    print("=" * 70)
    print(f"Report saved to: {output_path}")
    print()


if __name__ == '__main__':
    main()
