# Tasks: Create Gene Catalog v2 (important-genes-2)

**Note**: This work will be divided into manageable chunks for piecemeal implementation. Each chunk is a
discrete, completable unit that can be requested and implemented independently.

## Phase 1: Analysis and Planning

- [x] **T1.1**: Parse [`hidden/DNA-GENES.md`](../../hidden/DNA-GENES.md:1) to extract all unique genes and their categories
  - Create a mapping of gene symbol to category(ies)
  - Identify duplicate genes across categories
  - Count total unique genes to process
  - Output: Master gene list with categories (386 unique genes)

- [x] **T1.2**: Determine category folder names (lowercase, hyphenated)
  - Convert each category from DNA-GENES.md to folder-safe naming
  - Validate no naming conflicts
  - Output: Category name mapping table

- [x] **T1.3**: Create gene processing plan
  - Decide on duplicate gene handling strategy
  - Decide on gene pair handling strategy
  - Determine research depth for each category
  - Output: Processing guidelines document

- [x] **T1.4**: Perform data cleanup on source document
  - Parse DNA-GENES.md and identify all unique gene symbols
  - Remove duplicates from the master gene list
  - Document actual unique gene count
  - Note which genes appear in multiple categories
  - Output: Cleaned gene list with category mapping

## Phase 2: Directory Structure Creation

- [x] **T2.1**: Create main directory `hidden/important-genes-2/`
  - Verify directory doesn't exist
  - Create with proper permissions

- [x] **T2.2**: Create category subdirectories
  - Create 12 category folders based on T1.2 output
  - Verify all folders created successfully
  - Output: Directory structure listing

## Phase 3: Gene File Creation

**Note**: File naming uses descriptive format: `<gene-symbol>-<full-name>-<short-
description>-<rsid>.yaml`

### Phase 3a: Top Priority Genes (5 genes)

- [x] **T3.1**: Create `mthfr-methylenetetrahydrofolate-reductase-c677t-rs1801133.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.2**: Create `apoe-apolipoprotein-e-e4-rs429358.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.3**: Create `fto-fat-mass-and-obesity-associated-rs9939609.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.4**: Create `brca1-breast-cancer-1-rs799917.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.5**: Create `brca2-breast-cancer-2-rs206115.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.6**: Create `comt-catechol-o-methyltransferase-val158met-rs4680.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3b: High-Impact Health Genes (8 genes)

- [x] **T3.7**: Create `cyp2d6-cytochrome-p450-2d6-rs3892097.yaml` in `high-impact-health-genes/`

- [x] **T3.8**: Create `cyp2c19-cytochrome-p450-2c19-rs4244285.yaml` in `high-impact-health-genes/`

**Note**: File naming uses descriptive format: `<gene-symbol>-<full-name>-<short-description>-<rsid>.yaml`

### Phase 3a: Top Priority Genes (5 genes)

- [x] **T3.1**: Create `mthfr-methylenetetrahydrofolate-reductase-c677t-rs1801133.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.2**: Create `apoe-apolipoprotein-e-e4-rs429358.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.3**: Create `fto-fat-mass-and-obesity-associated-rs9939609.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.4**: Create `brca1-breast-cancer-1-rs799917.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.5**: Create `brca2-breast-cancer-2-rs206115.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.6**: Create `comt-catechol-o-methyltransferase-val158met-rs4680.yaml` in `top-priority-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3b: High-Impact Health Genes (8 genes)

- [x] **T3.7**: Create `cyp2d6-cytochrome-p450-2d6-rs3892097.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.8**: Create `cyp2c19-cytochrome-p450-2c19-rs4244285.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.9**: Create `vdr-vitamin-d-receptor-rs1544410.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.10**: Create `ace-angiotensin-converting-enzyme-rs4343.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.11**: Create `nos3-nitric-oxide-synthase-3-rs1799983.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.12**: Create `fut2-fucosyltransferase-2-rs601338.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.13**: Create `sod2-superoxide-dismutase-2-rs4880.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.14**: Create `maoa-monoamine-oxidase-a-rs6323.yaml` in `high-impact-health-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

### Phase 3c: Metabolism & Detoxification Genes (7 genes)

- [x] **T3.15**: Create `cyp1a1-cytochrome-p450-1a1-rs1048943.yaml` in `metabolism-detoxification-genes/`

- [x] **T3.16**: Create `nat2-n-acetyltransferase-2-rs1801280.yaml` in `metabolism-detoxification-genes/`

- [x] **T3.17**: Create `gstp1-glutathione-s-transferase-p1-rs1695.yaml` in `metabolism-detoxification-genes/`

- [x] **T3.18**: Create `aldh2-aldehyde-dehydrogenase-2-rs671.yaml` in `metabolism-detoxification-genes/`

- [x] **T3.19**: Create `pparg-peroxisome-proliferator-activated-receptor-gamma-rs1801282.yaml` in `metabolism-detoxification-genes/`

- [x] **T3.20**: Create `ucp1-uncoupling-protein-1-rs1800592.yaml` in `metabolism-detoxification-genes/`

- [x] **T3.21**: Create `slc2a2-solute-carrier-family-2-member-2-rs5400.yaml` in `metabolism-detoxification-genes/`

### Phase 3d: Cardiovascular & Heart Health Genes (5 genes)

- [x] **T3.22**: Create `apoa1-apolipoprotein-a1-rs670.yaml` in `cardiovascular-heart-health-genes/`

- [x] **T3.23**: Create `apob-apolipoprotein-b-rs693.yaml` in `cardiovascular-heart-health-genes/`

- [x] **T3.24**: Create `cetp-cholesteryl-ester-transfer-protein-rs708272.yaml` in `cardiovascular-heart-health-genes/`

- [x] **T3.25**: Create `lpl-lipoprotein-lipase-rs1800590.yaml` in `cardiovascular-heart-health-genes/`

- [x] **T3.26**: Create `pcsk9-proprotein-convertase-subtilisin-kexin-9-rs505151.yaml` in `cardiovascular-heart-health-genes/`

### Phase 3e: Immune & Inflammation Genes (5 genes)

- [x] **T3.27**: Create `il1b-interleukin-1-beta-rs1143634.yaml` in `immune-inflammation-genes/`

- [x] **T3.28**: Create `il6-interleukin-6-rs1800795.yaml` in `immune-inflammation-genes/`

- [x] **T3.29**: Create `tnf-tumor-necrosis-factor-rs1800629.yaml` in `immune-inflammation-genes/`

- [x] **T3.30**: Create `crp-c-reactive-protein-rs1205.yaml` in `immune-inflammation-genes/`

- [x] **T3.31**: Create `hla-drb1-human-leukocyte-antigen-drb1-rs660895.yaml` in `immune-inflammation-genes/`

### Phase 3f: Brain & Mental Health Genes (5 genes)

- [x] **T3.32**: Create `bdnf-brain-derived-neurotrophic-factor-val66met-rs6265.yaml` in `brain-mental-health-genes/`

- [x] **T3.33**: Create `drd2-dopamine-receptor-d2-rs1800497.yaml` in `brain-mental-health-genes/`

- [x] **T3.34**: Create `slc6a4-serotonin-transporter-5-httlpr-rs25531.yaml` in `brain-mental-health-genes/`

- [x] **T3.35**: Handle COMT and MAOA (already created in T3.6 and T3.14)

### Phase 3g: Sleep & Circadian Rhythm Genes (3 genes)

- [x] **T3.36**: Create `clock-circadian-locomotor-output-cycles-kaput-rs1801260.yaml` in `sleep-circadian-rhythm-genes/`

- [x] **T3.37**: Create `per2-period-circadian-regulator-2-rs2304672.yaml` in `sleep-circadian-rhythm-genes/`

- [x] **T3.38**: Create `mtnr1a-melatonin-receptor-1a-rs2119882.yaml` and `mtnr1b-melatonin-receptor-1b-rs10830963.yaml` in `sleep-circadian-rhythm-genes/`

### Phase 3h: Hormone & Reproductive Health Genes (3 genes)

- [x] **T3.39**: Create `esr1-estrogen-receptor-1-rs2234693.yaml` in `hormone-reproductive-health-genes/`

- [x] **T3.40**: Create `shbg-sex-hormone-binding-globulin-rs6259.yaml` in `hormone-reproductive-health-genes/`

- [x] **T3.41**: Create `cyp19a1-aromatase-rs10046.yaml` in `hormone-reproductive-health-genes/`

### Phase 3i: Nutrient Metabolism Genes (7 genes)

- [x] **T3.42**: Create `mtr-methionine-synthase-rs1805087.yaml` in `nutrient-metabolism-genes/`

- [x] **T3.43**: Create `mtrr-methionine-synthase-reductase-rs1801394.yaml` in `nutrient-metabolism-genes/`

- [x] **T3.44**: Create `cbs-cystathionine-beta-synthase-rs234706.yaml` in `nutrient-metabolism-genes/`

- [x] **T3.45**: Create `bhmt-betaine-homocysteine-s-methyltransferase-rs3733890.yaml` in `nutrient-metabolism-genes/`

- [x] **T3.46**: Create `tcn2-transcobalamin-2-rs1801198.yaml` in `nutrient-metabolism-genes/`

- [x] **T3.47**: Create `slc19a1-solute-carrier-family-19-member-1-rs1051266.yaml` in `nutrient-metabolism-genes/`

- [x] **T3.48**: Create `folh1-folate-hydrolase-1-rs202676.yaml` in `nutrient-metabolism-genes/`

### Phase 3j: Additional Important Genes (12 genes)

- [x] **T3.49**: Create `adrb2-beta-2-adrenergic-receptor-rs1042713.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.50**: Create `adrb3-beta-3-adrenergic-receptor-rs4994.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.51**: Create `lepr-leptin-receptor-rs1137101.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.52**: Create `mc4r-melanocortin-4-receptor-rs17782313.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.53**: Create `adipoq-adiponectin-rs1501299.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.54**: Create `ppargc1a-pparg-coactivator-1-alpha-rs8192678.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.55**: Create `gckr-glucokinase-regulator-rs780094.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.56**: Create `tcf7l2-transcription-factor-7-like-2-rs7903146.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.57**: Create `pnpla3-patatin-like-phospholipase-3-rs738409.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.58**: Create `slc30a8-zinc-transporter-8-rs13266634.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.59**: Create `hfe-hemochromatosis-rs1799945.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.60**: Create `tas2r38-taste-receptor-rs713598.yaml` in `additional-important-genes/`
  - Extract basic info from DNA-GENES.md
  - Research rsids, chromosome, position via browser MCP
  - Validate YAML schema
  - Compact context after completion

- [x] **T3.61**: Create `adrb1-beta-1-adrenergic-receptor-rs1801253.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.62**: Create `adipor1-adiponectin-receptor-1-rs7539542.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.63**: Create `agxt-alanine-glyoxylate-aminotransferase-rs34116584.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.64**: Create `akt1-akt-serine-threonine-kinase-rs1130233.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.65**: Create `alad-aminolevulinate-dehydratase-rs1805312.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.66**: Create `alas2-aminolevulinate-synthase-2-rs16954073.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.67**: Create `amy1a-amylase-1a-rs4248129.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

- [x] **T3.68**: Create `ank3-ankyrin-3-rs10994336.yaml` in `additional-important-genes/`
   - Extract basic info from DNA-GENES.md
   - Research rsids, chromosome, position via browser MCP
   - Validate YAML schema
   - Compact context after completion

### Phase 3k: Additional Important Genes from Source.md (genes 69-386)

<!-- Expanded individual tasks created from `hidden/source.md` unique gene list -->

- [x] **T3.69**: Create `4-1bb-tumor-necrosis-factor-receptor-superfamily-member-9.yaml` in `additional-important-genes/`
- [x] **T3.70**: Create `4-1bbl-tumor-necrosis-factor-ligand-superfamily-member-4.yaml` in `additional-important-genes/`
- [x] **T3.71**: Create `5-httlpr-serotonin-transporter-linked-polymorphic-region.yaml` in `additional-important-genes/`
- [x] **T3.72**: Create `aanat-arylalkylamine-n-acetyltransferase-rs4446909.yaml` in `additional-important-genes/`
- [x] **T3.73**: Create `abcb1-atp-binding-cassette-subfamily-b-member-1-rs1045642.yaml` in `additional-important-genes/`
- [x] **T3.74**: Create `abcc1-atp-binding-cassette-subfamily-c-member-1-rs35592.yaml` in `additional-important-genes/`
- [x] **T3.75**: Create `abcc2-atp-binding-cassette-subfamily-c-member-2-rs717620.yaml` in `additional-important-genes/`
- [x] **T3.76**: Create `abcc8-atp-binding-cassette-subfamily-c-member-8-rs757110.yaml` in `additional-important-genes/`
- [x] **T3.77**: Create `abo-abo-blood-group-rs8176719.yaml` in `additional-important-genes/`
- [x] **T3.78**: Create `acadm-acyl-coa-dehydrogenase-medium-chain-rs779312.yaml` in `additional-important-genes/`
- [x] **T3.79**: Create `acadvl-acyl-coa-dehydrogenase-very-long-chain-rs2119502.yaml` in `additional-important-genes/`
- [x] **T3.80**: Create `ada-adenosine-deaminase-rs73598374.yaml` in `additional-important-genes/`
- [x] **T3.81**: Create `adamts4-adam-metallopeptidase-with-thrombospondin-type-4-rs4233367.yaml` in `additional-important-genes/`
- [x] **T3.82**: Create `adamts5-adam-metallopeptidase-with-thrombospondin-type-5-rs2830585.yaml` in `additional-important-genes/`
- [x] **T3.83**: Create `adh1b-alcohol-dehydrogenase-1b-rs1229984.yaml` in `additional-important-genes/`
- [x] **T3.84**: Create `adh1c-alcohol-dehydrogenase-1c-rs698.yaml` in `additional-important-genes/`
- [x] **T3.85**: Create `adoa2a-adenosine-a2a-receptor-rs5751876.yaml` in `additional-important-genes/`
- [x] **T3.86**: Create `adra1a-adrenergic-receptor-alpha-1a-rs1048101.yaml` in `additional-important-genes/`
- [x] **T3.87**: Create `adra2a-adrenergic-receptor-alpha-2a-rs1800544.yaml` in `additional-important-genes/`
- [x] **T3.88**: Create `ahcy-s-adenosylhomocysteine-hydrolase-rs1128457.yaml` in `additional-important-genes/`
- [x] **T3.89**: Create `aldh1b1-aldehyde-dehydrogenase-1-family-member-b1-rs2073478.yaml` in `additional-important-genes/`
- [x] **T3.90**: Create `aldob-aldolase-b-fructose-bisphosphate-rs174082.yaml` in `additional-important-genes/`

<!-- Explicit tasks for remaining genes from source.md (T3.91 -> T3.393) -->

- [x] **T3.91**: Create `4-1bb-tnfrsf9.yaml` in `additional-important-genes/`
- [x] **T3.92**: Create `4-1bbl-tnfsf9.yaml` in `additional-important-genes/`
- [x] **T3.93**: Create `5-httlpr-serotonin-transporter.yaml` in `additional-important-genes/`
- [x] **T3.94**: Create `adora2a-adenosine-a2a-receptor.yaml` in `additional-important-genes/`
- [x] **T3.95**: Create `apoa5-apolipoprotein-a5.yaml` in `additional-important-genes/`
- [x] **T3.96**: Create `apoc3-apolipoprotein-c3.yaml` in `additional-important-genes/`
- [x] **T3.97**: Create `arntl-aryl-hydrocarbon-receptor-nuclear-translocator-like.yaml` in `additional-important-genes/`
- [x] **T3.98**: Create `asmt-acetylserotonin-o-methyltransferase.yaml` in `additional-important-genes/`
- [x] **T3.99**: Create `atg16l1-autophagy-related-16-like-1.yaml` in `additional-important-genes/`
- [x] **T3.100**: Create `avpr1a-vasopressin-receptor-1a.yaml` in `additional-important-genes/`
- [x] **T3.101**: Create `baffr-tnfrsf13c.yaml` in `additional-important-genes/`
- [x] **T3.102**: Create `bche-butyrylcholinesterase.yaml` in `additional-important-genes/`
- [x] **T3.103**: Create `bhlhe41-basic-helix-loop-helix-family-member-e41.yaml` in `additional-important-genes/`
- [x] **T3.104**: Create `bmal1-brain-and-muscle-arnt-like-1.yaml` in `additional-important-genes/`
- [x] **T3.105**: Create `bmp6-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.106**: Create `cacna1c-calcium-channel.yaml` in `additional-important-genes/`
- [x] **T3.107**: Create `card9-caspase-recruitment-domain-family-member-9.yaml` in `additional-important-genes/`
- [x] **T3.108**: Create `cat-catalase.yaml` in `additional-important-genes/`
- [x] **T3.109**: Create `cd27-cd27-molecule.yaml` in `additional-important-genes/`
- [x] **T3.110**: Create `cd28-cd28-molecule.yaml` in `additional-important-genes/`
- [x] **T3.111**: Create `cd30-tnfrsf8.yaml` in `additional-important-genes/`
- [x] **T3.112**: Create `cd30l-tnfsf8.yaml` in `additional-important-genes/`
- [x] **T3.113**: Create `cd36-fatty-acid-translocase.yaml` in `additional-important-genes/`
- [x] **T3.114**: Create `cd40-cd40-molecule.yaml` in `additional-important-genes/`
- [x] **T3.115**: Create `cd40lg-cd40-ligand.yaml` in `additional-important-genes/`
- [x] **T3.116**: Create `cd70-cd70-molecule.yaml` in `additional-important-genes/`
- [x] **T3.117**: Create `cd80-cd80-molecule.yaml` in `additional-important-genes/`
- [x] **T3.118**: Create `cd86-cd86-molecule.yaml` in `additional-important-genes/`
- [x] **T3.119**: Create `celsr2-cadherin-egf-lag-seven-pass-g-type-receptor-2.yaml` in `additional-important-genes/`
- [x] **T3.120**: Create `chdh-choline-dehydrogenase.yaml` in `additional-important-genes/`
- [x] **T3.121**: Create `chka-choline-kinase-alpha.yaml` in `additional-important-genes/`
- [x] **T3.122**: Create `chkb-choline-kinase-beta.yaml` in `additional-important-genes/`
- [x] **T3.123**: Create `chrna4-nicotinic-acetylcholine-receptor.yaml` in `additional-important-genes/`
- [x] **T3.124**: Create `chrna5-nicotinic-acetylcholine-receptor.yaml` in `additional-important-genes/`
- [x] **T3.125**: Create `cilp2-cartilage-intermediate-layer-protein-2.yaml` in `additional-important-genes/`
- [x] **T3.126**: Create `cnr1-cannabinoid-receptor-1.yaml` in `additional-important-genes/`
- [x] **T3.127**: Create `cnr2-cannabinoid-receptor-2.yaml` in `additional-important-genes/`
- [x] **T3.128**: Create `col10a1-collagen-type-x-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.129**: Create `col11a1-collagen-type-xi-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.130**: Create `col11a2-collagen-type-xi-alpha-2.yaml` in `additional-important-genes/`
- [x] **T3.131**: Create `col12a1-collagen-type-xii-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.132**: Create `col14a1-collagen-type-xiv-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.133**: Create `col1a1-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.134**: Create `col1a2-collagen-type-i-alpha-2.yaml` in `additional-important-genes/`
- [x] **T3.135**: Create `col2a1-collagen-type-ii-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.136**: Create `col3a1-collagen-type-iii-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.137**: Create `col5a1-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.138**: Create `col5a2-collagen-type-v-alpha-2.yaml` in `additional-important-genes/`
- [x] **T3.139**: Create `col6a1-collagen-type-vi-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.140**: Create `col6a2-collagen-type-vi-alpha-2.yaml` in `additional-important-genes/`
- [x] **T3.141**: Create `col6a3-collagen-type-vi-alpha-3.yaml` in `additional-important-genes/`
- [x] **T3.142**: Create `col9a1-collagen-type-ix-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.143**: Create `col9a2-collagen-type-ix-alpha-2.yaml` in `additional-important-genes/`
- [x] **T3.144**: Create `col9a3-collagen-type-ix-alpha-3.yaml` in `additional-important-genes/`
- [x] **T3.145**: Create `cpt1a-carnitine-palmitoyltransferase-1a.yaml` in `additional-important-genes/`
- [x] **T3.146**: Create `cpt2-carnitine-palmitoyltransferase-2.yaml` in `additional-important-genes/`
- [x] **T3.147**: Create `crhr1-corticotropin-releasing-hormone-receptor-1.yaml` in `additional-important-genes/`
- [x] **T3.148**: Create `crhr2-corticotropin-releasing-hormone-receptor-2.yaml` in `additional-important-genes/`
- [x] **T3.149**: Create `cry2-cryptochrome-2.yaml` in `additional-important-genes/`
- [x] **T3.150**: Create `cth-cystathionine-gamma-lyase.yaml` in `additional-important-genes/`
- [x] **T3.151**: Create `ctla4-cytotoxic-t-lymphocyte-associated-protein-4.yaml` in `additional-important-genes/`
- [x] **T3.152**: Create `cubn-cubilin.yaml` in `additional-important-genes/`
- [x] **T3.153**: Create `cyp1a2-cytochrome-p450-family-1-subfamily-a-member-2.yaml` in `additional-important-genes/`
- [x] **T3.154**: Create `cyp1b1-cytochrome-p450-family-1-subfamily-b-member-1.yaml` in `additional-important-genes/`
- [x] **T3.155**: Create `cyp24a1-cytochrome-p450-family-24-subfamily-a-member-1.yaml` in `additional-important-genes/`
- [x] **T3.156**: Create `cyp27b1-cytochrome-p450-family-27-subfamily-b-member-1.yaml` in `additional-important-genes/`
- [x] **T3.157**: Create `cyp2a6-cytochrome-p450-family-2-subfamily-a-member-6.yaml` in `additional-important-genes/`
- [x] **T3.158**: Create `cyp2b6-cytochrome-p450-family-2-subfamily-b-member-6.yaml` in `additional-important-genes/`
- [x] **T3.159**: Create `cyp2c9-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.160**: Create `cyp2e1-cytochrome-p450-family-2-subfamily-e-member-1.yaml` in `additional-important-genes/`
- [x] **T3.161**: Create `cyp2r1-cytochrome-p450-family-2-subfamily-r-member-1.yaml` in `additional-important-genes/`
- [x] **T3.162**: Create `cyp3a4-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.163**: Create `cyp3a5-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.164**: Create `cyp4a11-cytochrome-p450-family-4-subfamily-a-member-11.yaml` in `additional-important-genes/`
- [x] **T3.165**: Create `cyp4f2-cytochrome-p450-family-4-subfamily-f-member-2.yaml` in `additional-important-genes/`
- [x] **T3.166**: Create `cyp4v2-cytochrome-p450-family-4-subfamily-v-member-2.yaml` in `additional-important-genes/`
- [x] **T3.167**: Create `dao-diamine-oxidase.yaml` in `additional-important-genes/`
- [x] **T3.168**: Create `dbp-d-binding-protein.yaml` in `additional-important-genes/`
- [x] **T3.169**: Create `dec1-basic-helix-loop-helix-family-member-e40.yaml` in `additional-important-genes/`
- [x] **T3.170**: Create `dec2-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.171**: Create `dhcr7-7-dehydrocholesterol-reductase.yaml` in `additional-important-genes/`
- [x] **T3.172**: Create `dhfr-dihydrofolate-reductase.yaml` in `additional-important-genes/`
- [x] **T3.173**: Create `disc1-disrupted-in-schizophrenia-1.yaml` in `additional-important-genes/`
- [x] **T3.174**: Create `dpyd-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.175**: Create `dr3-tnfrsf25.yaml` in `additional-important-genes/`
- [x] **T3.176**: Create `dr6-tnfrsf21.yaml` in `additional-important-genes/`
- [x] **T3.177**: Create `drd3-dopamine-receptor-d3.yaml` in `additional-important-genes/`
- [x] **T3.178**: Create `ephx1-epoxide-hydrolase-1.yaml` in `additional-important-genes/`
- [x] **T3.179**: Create `ephx2-epoxide-hydrolase-2.yaml` in `additional-important-genes/`
- [x] **T3.180**: Create `f13a1-coagulation-factor-xiii-a1.yaml` in `additional-important-genes/`
- [x] **T3.181**: Create `f2-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.182**: Create `f5-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.183**: Create `faah-fatty-acid-amide-hydrolase.yaml` in `additional-important-genes/`
- [x] **T3.184**: Create `fabp2-fatty-acid-binding-protein-2.yaml` in `additional-important-genes/`
- [x] **T3.185**: Create `fbn1-fibrillin-1.yaml` in `additional-important-genes/`
- [x] **T3.186**: Create `fbn2-fibrillin-2.yaml` in `additional-important-genes/`
- [x] **T3.187**: Create `fkbp5-fk506-binding-protein-5.yaml` in `additional-important-genes/`
- [x] **T3.188**: Create `foxo1-forkhead-box-o1.yaml` in `additional-important-genes/`
- [x] **T3.189**: Create `foxo3-forkhead-box-o3.yaml` in `additional-important-genes/`
- [x] **T3.190**: Create `fpn1-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.191**: Create `g6pd-glucose-6-phosphate-dehydrogenase.yaml` in `additional-important-genes/`
- [x] **T3.192**: Create `gaba-a-gaba-receptor.yaml` in `additional-important-genes/`
- [x] **T3.193**: Create `gad1-glutamate-decarboxylase-1.yaml` in `additional-important-genes/`
- [x] **T3.194**: Create `gc-vitamin-d-binding-protein.yaml` in `additional-important-genes/`
- [x] **T3.195**: Create `gclc-glutamate-cysteine-ligase.yaml` in `additional-important-genes/`
- [x] **T3.196**: Create `gclm-glutamate-cysteine-ligase.yaml` in `additional-important-genes/`
- [x] **T3.197**: Create `ggcx-gamma-glutamyl-carboxylase.yaml` in `additional-important-genes/`
- [x] **T3.198**: Create `ghr-growth-hormone-receptor.yaml` in `additional-important-genes/`
- [x] **T3.199**: Create `gipr-gastric-inhibitory-polypeptide-receptor.yaml` in `additional-important-genes/`
- [x] **T3.200**: Create `gitrl-tnfsf18.yaml` in `additional-important-genes/`

- [x] **T3.201**: Create `glul-glutamine-synthetase.yaml` in `additional-important-genes/`
- [x] **T3.202**: Create `gnmt-glycine-n-methyltransferase.yaml` in `additional-important-genes/`
- [x] **T3.203**: Create `gp1ba-glycoprotein-ib-alpha.yaml` in `additional-important-genes/`
- [x] **T3.204**: Create `gpc1.yaml` in `additional-important-genes/`
- [x] **T3.205**: Create `gpc2.yaml` in `additional-important-genes/`
- [x] **T3.206**: Create `gpc3-glypican-3.yaml` in `additional-important-genes/`
- [x] **T3.207**: Create `gpc4-glypican-4.yaml` in `additional-important-genes/`
- [x] **T3.208**: Create `gpc5-glypican-5.yaml` in `additional-important-genes/`
- [x] **T3.209**: Create `gpc6-glypican-6.yaml` in `additional-important-genes/`
- [x] **T3.210**: Create `gpx4-glutathione-peroxidase-4.yaml` in `additional-important-genes/`
- [x] **T3.211**: Create `grhpr-glyoxylate-reductase-hydroxypyruvate-reductase.yaml` in `additional-important-genes/`
- [x] **T3.212**: Create `gria3-glutamate-receptor.yaml` in `additional-important-genes/`
- [x] **T3.213**: Create `grin-glutamate-receptor.yaml` in `additional-important-genes/`
- [x] **T3.214**: Create `gsr-glutathione-reductase.yaml` in `additional-important-genes/`
- [x] **T3.215**: Create `gsta1-glutathione-s-transferase-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.216**: Create `gstm1-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.217**: Create `gstm3-glutathione-s-transferase-mu-3.yaml` in `additional-important-genes/`
- [x] **T3.218**: Create `gstt1-glutathione-s-transferase-theta-1.yaml` in `additional-important-genes/`
- [x] **T3.219**: Create `hadha-hydroxyacyl-coa-dehydrogenase.yaml` in `additional-important-genes/`
- [x] **T3.220**: Create `hadhb-hydroxyacyl-coa-dehydrogenase.yaml` in `additional-important-genes/`
- [x] **T3.221**: Create `hamp-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.222**: Create `hba1-hemoglobin-alpha-1.yaml` in `additional-important-genes/`
- [x] **T3.223**: Create `hba2-hemoglobin-alpha-2.yaml` in `additional-important-genes/`
- [x] **T3.224**: Create `hbb-hemoglobin-beta.yaml` in `additional-important-genes/`
- [x] **T3.225**: Create `hdc-histidine-decarboxylase.yaml` in `additional-important-genes/`
- [x] **T3.226**: Create `herc2-hect-and-rld-domain-containing-e3-ubiquitin-protein-ligase-2.yaml` in `additional-important-genes/`
- [x] **T3.227**: Create `hjv-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.228**: Create `hla-a-human-leukocyte-antigen-a.yaml` in `additional-important-genes/`
- [x] **T3.229**: Create `hla-b-human-leukocyte-antigen-b.yaml` in `additional-important-genes/`
- [x] **T3.230**: Create `hla-c-human-leukocyte-antigen-c.yaml` in `additional-important-genes/`
- [x] **T3.231**: Create `hla-dp-human-leukocyte-antigen-dp.yaml` in `additional-important-genes/`
- [x] **T3.232**: Create `hla-dq-human-leukocyte-antigen-dq.yaml` in `additional-important-genes/`
- [x] **T3.233**: Create `hla-dr-human-leukocyte-antigen-dr.yaml` in `additional-important-genes/`
- [x] **T3.234**: Create `hla-drb1-human-leukocyte-antigen-drb1.yaml` in `additional-important-genes/`
- [x] **T3.235**: Create `hmgcr-hmg-coa-reductase.yaml` in `additional-important-genes/`
- [x] **T3.236**: Create `hnf1a-hepatocyte-nuclear-factor-1-alpha.yaml` in `additional-important-genes/`
- [x] **T3.237**: Create `hnf4a-hepatocyte-nuclear-factor-4-alpha.yaml` in `additional-important-genes/`
- [x] **T3.238**: Create `hnmt-histamine-n-methyltransferase.yaml` in `additional-important-genes/`
- [x] **T3.239**: Create `hoga1-4-hydroxy-2-oxoglutarate-aldolase-1.yaml` in `additional-important-genes/`
- [x] **T3.240**: Create `hrh1-histamine-receptor-h1.yaml` in `additional-important-genes/`
- [x] **T3.241**: Create `hrh2-histamine-receptor-h2.yaml` in `additional-important-genes/`
- [x] **T3.242**: Create `hrh4-histamine-receptor-h4.yaml` in `additional-important-genes/`
- [x] **T3.243**: Create `htr1a-serotonin-receptor-1a.yaml` in `additional-important-genes/`
- [x] **T3.244**: Create `htr2a-serotonin-receptor-2a.yaml` in `additional-important-genes/`
- [x] **T3.245**: Create `htr2c-serotonin-receptor-2c.yaml` in `additional-important-genes/`
- [x] **T3.246**: Create `htr3a-serotonin-receptor-3a.yaml` in `additional-important-genes/`
- [x] **T3.247**: Create `ifng-interferon-gamma.yaml` in `additional-important-genes/`
- [x] **T3.248**: Create `igf1-insulin-like-growth-factor-1.yaml` in `additional-important-genes/`
- [x] **T3.249**: Create `igf1r-insulin-like-growth-factor-1-receptor.yaml` in `additional-important-genes/`
- [x] **T3.250**: Create `il10-interleukin-10.yaml` in `additional-important-genes/`
- [x] **T3.251**: Create `il12-interleukin-12.yaml` in `additional-important-genes/`
- [x] **T3.252**: Create `il13-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.253**: Create `il17-interleukin-17.yaml` in `additional-important-genes/`
- [x] **T3.254**: Create `il18-interleukin-18.yaml` in `additional-important-genes/`
- [x] **T3.255**: Create `il1a-interleukin-1-alpha.yaml` in `additional-important-genes/`
- [x] **T3.256**: Create `il1rn-interleukin-1-receptor-antagonist.yaml` in `additional-important-genes/`
- [x] **T3.257**: Create `il2-interleukin-2.yaml` in `additional-important-genes/`
- [x] **T3.258**: Create `il21-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.259**: Create `il23-interleukin-23.yaml` in `additional-important-genes/`
- [x] **T3.260**: Create `il23r-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.261**: Create `il4-interleukin-4.yaml` in `additional-important-genes/`
- [x] **T3.262**: Create `il5-interleukin-5.yaml` in `additional-important-genes/`
- [x] **T3.263**: Create `il8-interleukin-8.yaml` in `additional-important-genes/`
- [x] **T3.264**: Create `insig2-insulin-induced-gene-2.yaml` in `additional-important-genes/`
- [x] **T3.265**: Create `irgm-immunity-related-gtpase-m.yaml` in `additional-important-genes/`
- [x] **T3.266**: Create `irs1-insulin-receptor-substrate-1.yaml` in `additional-important-genes/`
- [x] **T3.267**: Create `itgb3-integrin-beta-3.yaml` in `additional-important-genes/`
- [x] **T3.268**: Create `kcnj11-potassium-channel.yaml` in `additional-important-genes/`
- [x] **T3.269**: Create `lct-lactase.yaml` in `additional-important-genes/`
- [x] **T3.270**: Create `ldlr-ldl-receptor.yaml` in `additional-important-genes/`
- [x] **T3.271**: Create `lipc-hepatic-lipase.yaml` in `additional-important-genes/`
- [x] **T3.272**: Create `lpa-lipoprotein-a.yaml` in `additional-important-genes/`
- [x] **T3.273**: Create `lta-lymphotoxin-alpha.yaml` in `additional-important-genes/`
- [x] **T3.274**: Create `ltb-lymphotoxin-beta.yaml` in `additional-important-genes/`
- [x] **T3.275**: Create `ltbr-lymphotoxin-beta-receptor.yaml` in `additional-important-genes/`
- [x] **T3.276**: Create `maob-monoamine-oxidase-b.yaml` in `additional-important-genes/`
- [x] **T3.277**: Create `mat1a-methionine-adenosyltransferase-1a.yaml` in `additional-important-genes/`
- [x] **T3.278**: Create `matn3-matrilin-3.yaml` in `additional-important-genes/`
- [x] **T3.279**: Create `mc1r-melanocortin-1-receptor.yaml` in `additional-important-genes/`
- [x] **T3.280**: Create `mcm6-minichromosome-maintenance-complex-component-6.yaml` in `additional-important-genes/`
- [x] **T3.281**: Create `mmp1-matrix-metallopeptidase-1.yaml` in `additional-important-genes/`
- [x] **T3.282**: Create `mmp2-matrix-metallopeptidase-2.yaml` in `additional-important-genes/`
- [x] **T3.283**: Create `mmp3-matrix-metallopeptidase-3.yaml` in `additional-important-genes/`
- [x] **T3.284**: Create `mmp9-matrix-metallopeptidase-9.yaml` in `additional-important-genes/`
- [x] **T3.285**: Create `mthfd1-methylenetetrahydrofolate-dehydrogenase.yaml` in `additional-important-genes/`
- [x] **T3.286**: Create `mthfd1l-methylenetetrahydrofolate-dehydrogenase-like.yaml` in `additional-important-genes/`
- [x] **T3.287**: Create `mthfs-methenyltetrahydrofolate-synthetase.yaml` in `additional-important-genes/`
- [x] **T3.288**: Create `muc1-mucin-1.yaml` in `additional-important-genes/`
- [x] **T3.289**: Create `nfkb1-nuclear-factor-kappa-b-subunit-1.yaml` in `additional-important-genes/`
- [x] **T3.290**: Create `nfkbia-nfkb-inhibitor-alpha.yaml` in `additional-important-genes/`
- [x] **T3.291**: Create `nfkbil1-nfkb-inhibitor-like-1.yaml` in `additional-important-genes/`
- [x] **T3.292**: Create `ngfr-nerve-growth-factor-receptor.yaml` in `additional-important-genes/`
- [x] **T3.293**: Create `nlrp3-nlr-family-pyrin-domain-containing-3.yaml` in `additional-important-genes/`
- [x] **T3.294**: Create `nod2-nucleotide-binding-oligomerization-domain-containing-2.yaml` in `additional-important-genes/`
- [x] **T3.295**: Create `npas2-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.296**: Create `nqo1-nad-p.yaml` in `additional-important-genes/`
- [x] **T3.297**: Create `nr1d1-nuclear-receptor-subfamily-1-group-d-member-1.yaml` in `additional-important-genes/`
- [x] **T3.298**: Create `nr1d2-nuclear-receptor-subfamily-1-group-d-member-2.yaml` in `additional-important-genes/`
- [x] **T3.299**: Create `nr3c1-glucocorticoid-receptor.yaml` in `additional-important-genes/`
- [x] **T3.300**: Create `nudt15-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.301**: Create `oca2-oculocutaneous-albinism-ii.yaml` in `additional-important-genes/`
- [x] **T3.302**: Create `or6a2-olfactory-receptor.yaml` in `additional-important-genes/`
- [x] **T3.303**: Create `ox40-tnfrsf4.yaml` in `additional-important-genes/`
- [x] **T3.304**: Create `ox40l-tnfsf4.yaml` in `additional-important-genes/`
- [x] **T3.305**: Create `oxtr-oxytocin-receptor.yaml` in `additional-important-genes/`
- [x] **T3.306**: Create `pdcd1-programmed-cell-death-1.yaml` in `additional-important-genes/`
- [x] **T3.307**: Create `pdxk-pyridoxal-kinase.yaml` in `additional-important-genes/`
- [x] **T3.308**: Create `pemt-phosphatidylethanolamine-n-methyltransferase.yaml` in `additional-important-genes/`
- [x] **T3.309**: Create `per1-period-circadian-regulator-1.yaml` in `additional-important-genes/`
- [x] **T3.310**: Create `per3-period-circadian-regulator-3.yaml` in `additional-important-genes/`
- [x] **T3.311**: Create `pklr-pyruvate-kinase-liver-and-red-blood-cell.yaml` in `additional-important-genes/`
- [x] **T3.312**: Create `plod1-procollagen-lysine-2-oxoglutarate-5-dioxygenase-1.yaml` in `additional-important-genes/`
- [x] **T3.313**: Create `plod2-procollagen-lysine-2-oxoglutarate-5-dioxygenase-2.yaml` in `additional-important-genes/`
- [x] **T3.314**: Create `plod3-procollagen-lysine-2-oxoglutarate-5-dioxygenase-3.yaml` in `additional-important-genes/`
- [x] **T3.315**: Create `polg-dna-polymerase-gamma.yaml` in `additional-important-genes/`
- [x] **T3.316**: Create `pon1-paraoxonase-1.yaml` in `additional-important-genes/`
- [x] **T3.317**: Create `ppara-peroxisome-proliferator-activated-receptor-alpha.yaml` in `additional-important-genes/`
- [x] **T3.318**: Create `ppard-peroxisome-proliferator-activated-receptor-delta.yaml` in `additional-important-genes/`
- [x] **T3.319**: Create `psrc1-proline-and-serine-rich-coiled-coil-1.yaml` in `additional-important-genes/`
- [x] **T3.320**: Create `rora-rar-related-orphan-receptor-a.yaml` in `additional-important-genes/`
- [x] **T3.321**: Create `scd-stearoyl-coa-desaturase.yaml` in `additional-important-genes/`
- [x] **T3.322**: Create `shmt1-serine-hydroxymethyltransferase-1.yaml` in `additional-important-genes/`
- [x] **T3.323**: Create `si-sucrase-isomaltase.yaml` in `additional-important-genes/`
- [x] **T3.324**: Create `sirt1-sirtuin-1.yaml` in `additional-important-genes/`
- [x] **T3.325**: Create `sirt3-sirtuin-3.yaml` in `additional-important-genes/`
- [x] **T3.326**: Create `slc16a1-monocarboxylate-transporter-1.yaml` in `additional-important-genes/`
- [x] **T3.327**: Create `slc18a1-vesicular-monoamine-transporter-1.yaml` in `additional-important-genes/`
- [x] **T3.328**: Create `slc18a2-vesicular-monoamine-transporter-2.yaml` in `additional-important-genes/`
- [x] **T3.329**: Create `slc22a1-organic-cation-transporter-1.yaml` in `additional-important-genes/`
- [x] **T3.330**: Create `slc22a2-organic-cation-transporter-2.yaml` in `additional-important-genes/`
- [x] **T3.331**: Create `slc22a5-carnitine-transporter.yaml` in `additional-important-genes/`
- [x] **T3.332**: Create `slc22a6-organic-anion-transporter.yaml` in `additional-important-genes/`
- [x] **T3.333**: Create `slc23a1-vitamin-c-transporter.yaml` in `additional-important-genes/`
- [x] **T3.334**: Create `slc25a20-carnitine-acylcarnitine-translocase.yaml` in `additional-important-genes/`
- [x] **T3.335**: Create `slc25a38-mitochondrial-carrier-family.yaml` in `additional-important-genes/`
- [x] **T3.336**: Create `slc2a14-glucose-transporter.yaml` in `additional-important-genes/`
- [x] **T3.337**: Create `slc40a1-solute-carrier-family-40-member-1.yaml` in `additional-important-genes/`
- [x] **T3.338**: Create `slc45a2-solute-carrier-family-45-member-2.yaml` in `additional-important-genes/`
- [x] **T3.339**: Create `slc47a1-multidrug-and-toxin-extrusion-protein-1.yaml` in `additional-important-genes/`
- [x] **T3.340**: Create `slc47a2-multidrug-and-toxin-extrusion-protein-2.yaml` in `additional-important-genes/`
- [x] **T3.341**: Create `slc4a5-sodium-bicarbonate-transporter.yaml` in `additional-important-genes/`
- [x] **T3.342**: Create `slc6a15-neutral-amino-acid-transporter.yaml` in `additional-important-genes/`
- [x] **T3.343**: Create `slc6a2-norepinephrine-transporter.yaml` in `additional-important-genes/`
- [x] **T3.344**: Create `slc6a3-dopamine-transporter.yaml` in `additional-important-genes/`
- [x] **T3.345**: Create `slco1b1-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.346**: Create `slco1b3-solute-carrier-organic-anion-transporter.yaml` in `additional-important-genes/`
- [x] **T3.347**: Create `smad2-smad-family-member-2.yaml` in `additional-important-genes/`
- [x] **T3.348**: Create `smad3-smad-family-member-3.yaml` in `additional-important-genes/`
- [x] **T3.349**: Create `smad4-smad-family-member-4.yaml` in `additional-important-genes/`
- [x] **T3.350**: Create `smoc2-sparc-related-modular-calcium-binding-2.yaml` in `additional-important-genes/`
- [x] **T3.351**: Create `smoc3-sparc-related-modular-calcium-binding-3.yaml` in `additional-important-genes/`
- [x] **T3.352**: Create `sod1-superoxide-dismutase-1.yaml` in `additional-important-genes/`
- [x] **T3.353**: Create `sod3-superoxide-dismutase-3.yaml` in `additional-important-genes/`
- [x] **T3.354**: Create `sort1-sortilin-1.yaml` in `additional-important-genes/`
- [x] **T3.355**: Create `spock1-sparc-osteonectin-cwcv-and-kazal-like-domains-proteoglycan-1.yaml` in `additional-important-genes/`
- [x] **T3.356**: Create `spock2-sparc-osteonectin-cwcv-and-kazal-like-domains-proteoglycan-2.yaml` in `additional-important-genes/`
- [x] **T3.357**: Create `spock3-sparc-osteonectin-cwcv-and-kazal-like-domains-proteoglycan-3.yaml` in `additional-important-genes/`
- [x] **T3.358**: Create `suox-sulfite-oxidase.yaml` in `additional-important-genes/`
- [x] **T3.359**: Create `tas2r16-taste-receptor.yaml` in `additional-important-genes/`
- [x] **T3.360**: Create `tcf1-transcription-factor-1.yaml` in `additional-important-genes/`
- [x] **T3.361**: Create `terc-telomerase-rna-component.yaml` in `additional-important-genes/`
- [x] **T3.362**: Create `tert-telomerase-reverse-transcriptase.yaml` in `additional-important-genes/`
- [x] **T3.363**: Create `tf-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.364**: Create `tfam-mitochondrial-transcription-factor-a.yaml` in `additional-important-genes/`
- [x] **T3.365**: Create `tfr2-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.366**: Create `tfrc-transferrin-receptor.yaml` in `additional-important-genes/`
- [x] **T3.367**: Create `tgfbr1-tgf-beta-receptor-1.yaml` in `additional-important-genes/`
- [x] **T3.368**: Create `tgfbr2-tgf-beta-receptor-2.yaml` in `additional-important-genes/`
- [x] **T3.369**: Create `timeless-timeless-circadian-regulator.yaml` in `additional-important-genes/`
- [x] **T3.370**: Create `timp1-timp-metallopeptidase-inhibitor-1.yaml` in `additional-important-genes/`
- [x] **T3.371**: Create `timp2-timp-metallopeptidase-inhibitor-2.yaml` in `additional-important-genes/`
- [x] **T3.372**: Create `timp3-timp-metallopeptidase-inhibitor-3.yaml` in `additional-important-genes/`
- [x] **T3.373**: Create `timp4-timp-metallopeptidase-inhibitor-4.yaml` in `additional-important-genes/`
- [x] **T3.374**: Create `tl1a-tnfsf15.yaml` in `additional-important-genes/`
- [x] **T3.375**: Create `tlr4-toll-like-receptor-4.yaml` in `additional-important-genes/`
- [x] **T3.376**: Create `tlr7-toll-like-receptor-7.yaml` in `additional-important-genes/`
- [x] **T3.377**: Create `tlr9-toll-like-receptor-9.yaml` in `additional-important-genes/`
- [x] **T3.378**: Create `tmprss6-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.379**: Create `tnfa-tumor-necrosis-factor-alpha.yaml` in `additional-important-genes/`
- [x] **T3.380**: Create `tnfb-tumor-necrosis-factor-beta.yaml` in `additional-important-genes/`
- [x] **T3.381**: Create `tnfsf15-tnf-superfamily-member-15.yaml` in `additional-important-genes/`
- [x] **T3.382**: Create `tnfsf9-tnf-superfamily-member-9.yaml` in `additional-important-genes/`
- [x] **T3.383**: Create `tph2-tryptophan-hydroxylase-2.yaml` in `additional-important-genes/`
- [x] **T3.384**: Create `tpmt-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.385**: Create `tyms-thymidylate-synthetase.yaml` in `additional-important-genes/`
- [x] **T3.386**: Create `tyr-tyrosinase.yaml` in `additional-important-genes/`
- [x] **T3.387**: Create `ucp2-uncoupling-protein-2.yaml` in `additional-important-genes/`
- [x] **T3.388**: Create `ucp3-uncoupling-protein-3.yaml` in `additional-important-genes/`
- [x] **T3.389**: Create `ugt1a1-udp-glucuronosyltransferase-1-1.yaml` in `additional-important-genes/`
- [x] **T3.390**: Create `ugt2b15-udp-glucuronosyltransferase-2b15.yaml` in `additional-important-genes/`
- [x] **T3.391**: Create `vkorc1-vitamin-k-epoxide-reductase-complex-subunit-1.yaml` in `additional-important-genes/`
- [x] **T3.392**: Create `vwf-already-listed-above.yaml` in `additional-important-genes/`
- [x] **T3.393**: Create `wfs1-wolfram-syndrome-1.yaml` in `additional-important-genes/`

### Optional: External Gene Sources

- The following phases were previously used to track additional genes from external sources (SelfDecode and miscellaneous research). These external gene lists are NOT automatically included in `hidden/DNA-GENES.md`.
- If you want to incorporate those external lists, add the genes to `hidden/source.md` (or `hidden/DNA-GENES.md`) first, then process them via Phase 3k-style tasks.

  Note: Current source documents include 386 unique genes; additional external lists (SelfDecode, research) must be curated and added explicitly before automated processing.

## Phase 4: Summary Creation

- [x] **T4.1**: Create `hidden/SUMMARY-2.md` with directory structure overview
  - List all 12 categories
  - Show folder structure
  - Include gene count per category

- [x] **T4.2**: Add category breakdown with gene listings
  - For each category, list all genes with links to YAML files
  - Include gene symbols and full names

- [x] **T4.3**: Add YAML format documentation
  - Document the schema used
  - Provide examples
  - Explain field meanings

- [x] **T4.4**: Add usage instructions
  - How to use with AncestryDNA data
  - Example searches
  - Tips for interpretation

- [x] **T4.5**: Add statistics and metadata
  - Total gene count
  - Category breakdown table
  - Last updated date
  - Sources referenced

- [x] **T4.6**: Review and finalize SUMMARY-2.md
  - Verify all links work
  - Check for completeness
  - Ensure consistent formatting

## Validation Tasks

- [x] **T5.1**: Validate directory structure
  - Verify all 12 category folders exist
  - Check folder names are lowercase and hyphenated
  - Verify no naming conflicts

- [x] **T5.2**: Validate YAML files
  - Check all YAML files follow the schema
  - Verify required fields are present
  - Validate YAML syntax using `yamllint` or Python script
  - Verify rsid format (rs followed by digits)
  - Verify chromosome values are valid (1-22, X, Y, MT)
  - Verify position values are positive integers

- [x] **T5.3**: Verify gene completeness
  - Cross-reference with DNA-GENES.md
  - Ensure all genes have corresponding YAML files
  - Handle duplicates appropriately
  - Verify no duplicate gene files across categories

- [x] **T5.4**: Test summary file
  - Verify all links in SUMMARY-2.md work
  - Check statistics are accurate
  - Ensure formatting is consistent

- [x] **T5.5**: Validate proposal using `openspec validate`
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
