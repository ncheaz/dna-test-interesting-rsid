
import re
import os
import json

def parse_dna_genes(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    categories = {}
    current_category = None
    
    # Regex patterns
    category_pattern = re.compile(r'^##\s+(.+)$')
    gene_pattern = re.compile(r'^###\s+\d+\.\s+\*\*(.+?)\*\*\s*(?:\((.+?)\))?')
    gene_pair_pattern = re.compile(r'^###\s+\d+\.\s+\*\*(.+?)\*\*\s+&\s+\*\*(.+?)\*\*\s*(?:\((.+?)\))?')
    
    # Special handling for "Additional Genes from Source.md" if it were there, but here we have sections.
    # Note: The file has section headers like "## Top Priority Genes..."
    
    all_genes = []
    
    for line in lines:
        line = line.strip()
        
        # Check for category
        match_cat = category_pattern.match(line)
        if match_cat:
            cat_name = match_cat.group(1).split('(')[0].strip()
            # Normalize category name for folder
            folder_name = cat_name.lower().replace(' & ', '-').replace(' ', '-').replace('--', '-')
            if 'selfdecode' in folder_name:
                 folder_name = 'additional-genes-selfdecode'
            
            current_category = {
                'name': cat_name,
                'folder': folder_name,
                'genes': []
            }
            categories[cat_name] = current_category
            continue
            
        if not current_category:
            continue
            
        # Check for gene pair first
        match_pair = gene_pair_pattern.match(line)
        if match_pair:
            gene1_symbol = match_pair.group(1).strip()
            gene2_symbol = match_pair.group(2).strip()
            desc = match_pair.group(3).strip() if match_pair.group(3) else ""
            
            # Treat as two separate entries
            all_genes.append({
                'symbol': gene1_symbol,
                'full_name': desc, # Shared description usually
                'category': current_category['folder']
            })
            all_genes.append({
                'symbol': gene2_symbol,
                'full_name': desc,
                'category': current_category['folder']
            })
            continue

        # Check for single gene
        match_gene = gene_pattern.match(line)
        if match_gene:
            gene_symbol = match_gene.group(1).strip()
            full_name = match_gene.group(2).strip() if match_gene.group(2) else ""
            
            if "already listed above" in gene_symbol.lower() or "already listed above" in full_name.lower():
                continue
                
            all_genes.append({
                'symbol': gene_symbol,
                'full_name': full_name,
                'category': current_category['folder']
            })

    return all_genes, categories

file_path = '/home/ncheaz/Projects/glm/dna-test-interesting-rsid/hidden/DNA-GENES.md'
all_genes, categories = parse_dna_genes(file_path)

# Handle duplicates: keep first occurrence, or maybe list all?
# Proposal says: "Duplicate genes: Create one YAML file per unique gene, note cross-category relevance in the notes field"

unique_genes = {}
duplicates = {}

for gene in all_genes:
    symbol = gene['symbol']
    if '/' in symbol: # Handle cases like FADS1/2
        parts = symbol.split('/')
        # This acts like a pair but written with slash
        # Actually usually it implies FADS1 and FADS2
        # Let's split them
        for part in parts:
             # If part is just a number (like '2' in FADS1/2), append to prefix
             if part.isdigit():
                 # assume prefix is from previous part
                 # This is tricky without more logic.
                 # Let's look at specific cases visually found.
                 # FADS1/2 -> FADS1 and FADS2?
                 pass 
             
    if symbol in unique_genes:
        if symbol not in duplicates:
            duplicates[symbol] = []
        duplicates[symbol].append(gene['category'])
    else:
        unique_genes[symbol] = gene

# Print stats
print(f"Total entries found: {len(all_genes)}")
print(f"Unique genes: {len(unique_genes)}")
print("Categories:")
for cat in categories.values():
    print(f"- {cat['name']} -> {cat['folder']}")

# Output to JSON
with open('gene_list.json', 'w') as f:
    json.dump(list(unique_genes.values()), f, indent=2)

with open('categories.json', 'w') as f:
    json.dump(categories, f, indent=2)
    
