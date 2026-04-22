Gene name and PF number correspondence information (obtained manually):
| gene  | PF ID                     |
| ---- | ------------------------- |
| ATP6 | PF00119                   |
| ATP8 | PF00895                   |
| COX1 | PF00115                   |
| COX2 | PF00116,PF02790           |
| COX3 | PF00510                   |
| CYTB | PF00032, PF00033          |
| ND1  | PF00146                   |
| ND2  | PF06444, PF00361          |
| ND3  | PF00507                   |
| ND4  | PF01059, PF00361          |
| ND4L | PF00420                   |
| ND5  | PF06455, PF00361, PF00662 |
| ND6  | PF00499                   |

```bash
gene_id=ATP6
pfam_id=PF00119
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ATP8
pfam_id=PF00895
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=COX1
pfam_id=PF00115
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=COX2
pfam_id=PF00116
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"

pfam_id=PF02790
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=COX3
pfam_id=PF00510
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=CYTB
pfam_id=PF00032
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"

pfam_id=PF00033
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND1
pfam_id=PF00146
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND2
pfam_id=PF06444
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"

pfam_id=PF00361
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND3
pfam_id=PF00507
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND4
pfam_id=PF01059
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"

pfam_id=PF00361
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND4L
pfam_id=PF00420
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND5
pfam_id=PF06455
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"

pfam_id=PF00361
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"

pfam_id=PF00662
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```
```bash
gene_id=ND6
pfam_id=PF00499
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm/data/Pfam_hmm
wget "https://www.ebi.ac.uk/interpro/wwwapi//entry/pfam/${pfam_id}?annotation=hmm" -O "${pfam_id}.gz"
gunzip -c "${pfam_id}.gz" > "${gene_id}_${pfam_id}.hmm"
```