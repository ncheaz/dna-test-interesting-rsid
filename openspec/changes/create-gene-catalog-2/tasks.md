# Tasks: Create Gene Catalog v2 (important-genes-2)

**Note**: This work will be divided into manageable chunks for piecemeal implementation. Each chunk is a discrete, completable unit that can be requested and implemented independently.

## Phase 1: Analysis and Planning

- [ ] **T1.1**: Parse [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) to extract all unique genes and their categories
  - Create a mapping of gene symbol to category(ies)
  - Identify duplicate genes across categories
  - Count total unique genes to process
  - Output: Master gene list with categories (500+ genes)

- [ ] **T1.2**: Determine category folder names (lowercase, hyphenated)
  - Convert each category from DNA-GENES.md to folder-safe naming
  - Validate no naming conflicts
  - Output: Category name mapping table

- [ ] **T1.3**: Create gene processing plan
  - Decide on duplicate gene handling strategy
  - Decide on gene pair handling strategy
  - Determine research depth for each category
  - Output: Processing guidelines document

- [ ] **T1.4**: Perform data cleanup on source document
  - Parse DNA-GENES.md and identify all unique gene symbols
  - Remove duplicates from the master gene list
  - Document actual unique gene count
  - Note which genes appear in multiple categories
  - Output: Cleaned gene list with category mapping

## Phase 2: Directory Structure Creation

- [ ] **T2.1**: Create main directory `hidden/important-genes-2/`
  - Verify directory doesn't exist
  - Create with proper permissions

- [ ] **T2.2**: Create category subdirectories
  - Create 12 category folders based on T1.2 output
  - Verify all folders created successfully
  - Output: Directory structure listing

## Phase 3: Gene File Creation

**Note**: File naming uses descriptive format: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`

### Phase 3a: Top Priority Genes (5 genes)

- [ ] **T3.1**: Create `mthfr-methylenetetrahydrofolate-reductase-c677t-rs1801133.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.2**: Create `apoe-apolipoprotein-e-e4-rs429358.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.3**: Create `fto-fat-mass-and-obesity-associated-rs9939609.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.4**: Create `brca1-breast-cancer-1-rs799917.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.5**: Create `brca2-breast-cancer-2-rs206115.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.6**: Create `comt-catechol-o-methyltransferase-val158met-rs4680.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3b: High-Impact Health Genes (8 genes)

- [ ] **T3.7**: Create `cyp2d6-cytochrome-p450-2d6-rs3892097.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.8**: Create `cyp2c19-cytochrome-p450-2c19-rs4244285.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.9**: Create `vdr-vitamin-d-receptor-rs1544410.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.10**: Create `ace-angiotensin-converting-enzyme-rs4343.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.11**: Create `nos3-nitric-oxide-synthase-3-rs1799983.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.12**: Create `fut2-fucosyltransferase-2-rs601338.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.13**: Create `sod2-superoxide-dismutase-2-rs4880.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.14**: Create `maoa-monoamine-oxidase-a-rs6323.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3c: Metabolism & Detoxification Genes (7 genes)

- [ ] **T3.15**: Create `cyp1a1-cytochrome-p450-1a1-rs1048943.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.16**: Create `nat2-n-acetyltransferase-2-rs1801280.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.17**: Create `gstp1-glutathione-s-transferase-p1-rs1695.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.18**: Create `aldh2-aldehyde-dehydrogenase-2-rs671.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.19**: Create `pparg-peroxisome-proliferator-activated-receptor-gamma-rs1801282.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.20**: Create `ucp1-uncoupling-protein-1-rs1800592.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.21**: Create `slc2a2-solute-carrier-family-2-member-2-rs5400.yaml` in `metabolism-detoxification-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3d: Cardiovascular & Heart Health Genes (5 genes)

- [ ] **T3.22**: Create `apoa1-apolipoprotein-a1-rs670.yaml` in `cardiovascular-heart-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.23**: Create `apob-apolipoprotein-b-rs693.yaml` in `cardiovascular-heart-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.24**: Create `cetp-cholesteryl-ester-transfer-protein-rs708272.yaml` in `cardiovascular-heart-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.25**: Create `lpl-lipoprotein-lipase-rs1800590.yaml` in `cardiovascular-heart-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.26**: Create `pcsk9-proprotein-convertase-subtilisin-kexin-9-rs505151.yaml` in `cardiovascular-heart-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3e: Immune & Inflammation Genes (5 genes)

- [ ] **T3.27**: Create `il1b-interleukin-1-beta-rs1143634.yaml` in `immune-inflammation-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.28**: Create `il6-interleukin-6-rs1800795.yaml` in `immune-inflammation-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.29**: Create `tnf-tumor-necrosis-factor-rs1800629.yaml` in `immune-inflammation-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.30**: Create `crp-c-reactive-protein-rs1205.yaml` in `immune-inflammation-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.31**: Create `hla-drb1-human-leukocyte-antigen-drb1-rs660895.yaml` in `immune-inflammation-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3f: Brain & Mental Health Genes (5 genes)

- [ ] **T3.32**: Create `bdnf-brain-derived-neurotrophic-factor-val66met-rs6265.yaml` in `brain-mental-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.33**: Create `drd2-dopamine-receptor-d2-rs1800497.yaml` in `brain-mental-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.34**: Create `slc6a4-serotonin-transporter-5-httlpr-rs25531.yaml` in `brain-mental-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.35**: Handle COMT and MAOA (already created in T3.6 and T3.14)
  - Note cross-category relevance in existing files
  - Update notes if needed

### Phase 3g: Sleep & Circadian Rhythm Genes (3 genes)

- [ ] **T3.36**: Create `clock-circadian-locomotor-output-cycles-kaput-rs1801260.yaml` in `sleep-circadian-rhythm-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.37**: Create `per2-period-circadian-regulator-2-rs2304672.yaml` in `sleep-circadian-rhythm-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.38**: Create `mtnr1a-melatonin-receptor-1a-rs2119882.yaml` and `mtnr1b-melatonin-receptor-1b-rs10830963.yaml` in `sleep-circadian-rhythm-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3h: Hormone & Reproductive Health Genes (3 genes)

- [ ] **T3.39**: Create `esr1-estrogen-receptor-1-rs2234693.yaml` in `hormone-reproductive-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.40**: Create `shbg-sex-hormone-binding-globulin-rs6259.yaml` in `hormone-reproductive-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.41**: Create `cyp19a1-aromatase-rs10046.yaml` in `hormone-reproductive-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3i: Nutrient Metabolism Genes (7 genes)

- [ ] **T3.42**: Create `mtr-methionine-synthase-rs1805087.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.43**: Create `mtrr-methionine-synthase-reductase-rs1801394.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.44**: Create `cbs-cystathionine-beta-synthase-rs234706.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.45**: Create `bhmt-betaine-homocysteine-s-methyltransferase-rs3733890.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.46**: Create `tcn2-transcobalamin-2-rs1801198.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.47**: Create `slc19a1-solute-carrier-family-19-member-1-rs1051266.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.48**: Create `folh1-folate-hydrolase-1-rs202676.yaml` in `nutrient-metabolism-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3j: Additional Important Genes (12 genes)

- [ ] **T3.49**: Create `adrb2-beta-2-adrenergic-receptor-rs1042713.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.50**: Create `adrb3-beta-3-adrenergic-receptor-rs4994.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.51**: Create `lepr-leptin-receptor-rs1137101.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.52**: Create `mc4r-melanocortin-4-receptor-rs17782313.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.53**: Create `adipoq-adiponectin-rs1501299.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.54**: Create `ppargc1a-pparg-coactivator-1-alpha-rs8192678.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.55**: Create `gckr-glucokinase-regulator-rs780094.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.56**: Create `tcf7l2-transcription-factor-7-like-2-rs7903146.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.57**: Create `pnpla3-patatin-like-phospholipase-3-rs738409.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.58**: Create `slc30a8-zinc-transporter-8-rs13266634.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.59**: Create `hfe-hemochromatosis-rs1799945.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.60**: Create `tas2r38-taste-receptor-rs713598.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [ ] **T3.61**: Create `adrb1-beta-1-adrenergic-receptor-rs1801253.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.62**: Create `adipor1-adiponectin-receptor-1-rs7539542.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.63**: Create `agxt-alanine-glyoxylate-aminotransferase-rs34116584.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.64**: Create `akt1-akt-serine-threonine-kinase-rs1130233.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.65**: Create `alad-aminolevulinate-dehydratase-rs1805312.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.66**: Create `alas2-aminolevulinate-synthase-2-rs16954073.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.67**: Create `amy1a-amylase-1a-rs4248129.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.68**: Create `ank3-ankyrin-3-rs10994336.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

### Phase 3k: Additional Important Genes from Source.md (~320 genes)

- [ ] **T3.69**: Create `4-1bb-tumor-necrosis-factor-receptor-superfamily-member-9.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.70**: Create `4-1bbl-tumor-necrosis-factor-ligand-superfamily-member-4.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.71**: Create `5-httlpr-serotonin-transporter-linked-polymorphic-region.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.72**: Create `aanat-arylalkylamine-n-acetyltransferase-rs4446909.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.73**: Create `abcb1-atp-binding-cassette-subfamily-b-member-1-rs1045642.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.74**: Create `abcc1-atp-binding-cassette-subfamily-c-member-1-rs35592.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.75**: Create `abcc2-atp-binding-cassette-subfamily-c-member-2-rs717620.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.76**: Create `abcc8-atp-binding-cassette-subfamily-c-member-8-rs757110.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.77**: Create `abo-abo-blood-group-rs8176719.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.78**: Create `acadm-acyl-coa-dehydrogenase-medium-chain-rs779312.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.79**: Create `acadvl-acyl-coa-dehydrogenase-very-long-chain-rs2119502.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.80**: Create `ada-adenosine-deaminase-rs73598374.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.81**: Create `adamts4-adam-metallopeptidase-with-thrombospondin-type-4-rs4233367.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.82**: Create `adamts5-adam-metallopeptidase-with-thrombospondin-type-5-rs2830585.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.83**: Create `adh1b-alcohol-dehydrogenase-1b-rs1229984.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.84**: Create `adh1c-alcohol-dehydrogenase-1c-rs698.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.85**: Create `adoa2a-adenosine-a2a-receptor-rs5751876.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.86**: Create `adra1a-adrenergic-receptor-alpha-1a-rs1048101.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.87**: Create `adra2a-adrenergic-receptor-alpha-2a-rs1800544.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.88**: Create `ahcy-s-adenosylhomocysteine-hydrolase-rs1128457.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.89**: Create `aldh1b1-aldehyde-dehydrogenase-1-family-member-b1-rs2073478.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.90**: Create `aldob-aldolase-b-fructose-bisphosphate-rs174082.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [ ] **T3.91-T3.388**: Create remaining ~298 genes from source.md (genes 91-388)
   - Process in batches of 10 genes
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP when available
   - Validate YAML schema
   - Compact context after each batch

### Phase 3l: Additional Genes from SelfDecode (~340 genes)

- [ ] **T3.389-T3.728**: Create YAML files for all ~340 SelfDecode genes (61-400)
   - Process in batches of 10 genes
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP when available
   - Validate YAML schema
   - Compact context after each batch

### Phase 3m: Additional Genes from Research (~100 genes)

- [ ] **T3.729-T3.828**: Create YAML files for all ~100 research genes (401-500)
  - Process in batches of 10 genes
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP when available
  - Validate YAML schema
  - Compact context after each batch

## Phase 4: Summary Creation

- [ ] **T4.1**: Create `hidden/SUMMARY-2.md` with directory structure overview
  - List all 12 categories
  - Show folder structure
  - Include gene count per category

- [ ] **T4.2**: Add category breakdown with gene listings
  - For each category, list all genes with links to YAML files
  - Include gene symbols and full names

- [ ] **T4.3**: Add YAML format documentation
  - Document the schema used
  - Provide examples
  - Explain field meanings

- [ ] **T4.4**: Add usage instructions
  - How to use with AncestryDNA data
  - Example searches
  - Tips for interpretation

- [ ] **T4.5**: Add statistics and metadata
  - Total gene count
  - Category breakdown table
  - Last updated date
  - Sources referenced

- [ ] **T4.6**: Review and finalize SUMMARY-2.md
  - Verify all links work
  - Check for completeness
  - Ensure consistent formatting

## Validation Tasks

- [ ] **T5.1**: Validate directory structure
  - Verify all 12 category folders exist
  - Check folder names are lowercase and hyphenated
  - Verify no naming conflicts

- [ ] **T5.2**: Validate YAML files
  - Check all YAML files follow the schema
  - Verify required fields are present
  - Validate YAML syntax using `yamllint` or Python script
  - Verify rsid format (rs followed by digits)
  - Verify chromosome values are valid (1-22, X, Y, MT)
  - Verify position values are positive integers

- [ ] **T5.3**: Verify gene completeness
  - Cross-reference with DNA-GENES.md
  - Ensure all genes have corresponding YAML files
  - Handle duplicates appropriately
  - Verify no duplicate gene files across categories

- [ ] **T5.4**: Test summary file
  - Verify all links in SUMMARY-2.md work
  - Check statistics are accurate
  - Ensure formatting is consistent

- [ ] **T5.5**: Validate proposal using `openspec validate`
  - Run `openspec validate` on proposal documents
  - Ensure proposal follows OpenSpec conventions
  - Address any validation errors

## Dependencies

- T1.1 must complete before T1.2
- T1.2 must complete before T1.3
- T1.3 must complete before T1.4
- T1.4 must complete before T2.1
- T2.1 must complete before T2.2
- T2.2 must complete before any T3.x tasks
- All T3.x tasks must complete before T4.1
- T4.1-T4.5 must complete in order
- T4.6 must complete before any T5.x tasks
- T5.1-T5.4 must complete in order
- T5.5 can run in parallel with T5.1-T5.4

**Chunking Approach**: Each Phase 3 sub-phase (3a through 3m) can be requested and implemented independently. This allows for piecemeal implementation of the 386+ gene catalog.

## Notes

**Chunking Strategy**:
- **Primary Chunk**: Each Phase 3 sub-phase (3a through 3m) is a primary chunk
- **Sub-Chunk**: Process genes in batches of 10 genes per sub-chunk
- **Context Compaction**: Perform context compaction after each sub-chunk (10 genes)
- This approach balances manageable context size with efficient processing

**Gene Processing**:
- Each gene creation task should include context compaction to prevent memory exhaustion
- Browser MCP research should prioritize SNPedia, NIH, and Genetic Lifehacks sources
- For genes with limited available information, focus on at least basic name, function, and health impact
- Duplicate genes across categories should be noted in the gene's notes field
- Gene pairs (e.g., MTNR1A & MTNR1B) should be created as separate files
- Phase 3k covers the remaining ~298 genes from source.md (genes 91-388) that are not in the original 60 specific tasks
- These genes should be processed systematically to ensure all 386 genes from source.md are covered
