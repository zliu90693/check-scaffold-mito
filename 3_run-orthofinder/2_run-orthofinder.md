```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder
# which primary_transcript.py
# /home/liuzhiyu/Software/miniconda3/envs/check-mito/bin/primary_transcript.py
for f in data/* ; do python /home/liuzhiyu/Software/miniconda3/envs/check-mito/bin/primary_transcript.py $f ; done
```
### Output: 

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 23470 accessions, 9935 genes, 0 unidentified transcripts<br>
Wrote 9935 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/Apis_mellifera.Amel_HAv3.1.pep.all.faa

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 23971 accessions, 12512 genes, 0 unidentified transcripts<br>
Wrote 12512 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/Camponotus_floridanus_gca003227725v1rs.Cflo_v7.5.pep.all.faa

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 30802 accessions, 13986 genes, 0 unidentified transcripts<br>
Wrote 13986 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/Drosophila_melanogaster.BDGP6.54.pep.all.faa

Identified as NCBI file<br>
Found 29188 accessions, 12625 genes, 0 unidentified transcripts<br>
Wrote 12625 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/GCF_029169275.1_AcerK_1.0_protein.faa

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 26772 accessions, 12642 genes, 0 unidentified transcripts<br>
Wrote 12642 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/Harpegnathos_saltator_gca003227715v2rs.Hsal_v8.5.pep.all.faa

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 12900 accessions, <mark style="background: #FF5582A6;">0 genes</mark>, 12900 unidentified transcripts<br>
Wrote 12900 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/LALB_OGS_v2.1.1_pep.faa

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 14033 accessions, <mark style="background: #FF5582A6;">0 genes</mark>, 14033 unidentified transcripts<br>
Wrote 14033 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/LZEP_OGS_v2.1.1_pep.faa

Looking for "gene=" of "gene:" to identify isoforms of same gene<br>
Found 23833 accessions, <mark style="background: #FF5582A6;">0 genes</mark>, 23833 unidentified transcripts<br>
Wrote 23833 genes<br>
/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder/data/primary_transcripts/PO1409_Ceratina_calcarata.protein.faa

↑ <mark style="background: #FF5582A6;">Warning:</mark> Because the protein names in the faa files of the latter three species do not conform to the format `>XP_011145505.1 ... gene=LOC105186768 ...`, primary_transcript.py cannot determine which transcript is the longest and therefore cannot prune faa file, thus retaining all proteins. Therefore, it is possible that the same gene corresponds to multiple transcripts in the latter three faa files. However, considering that the goal of this project is only to find mitochondrial genes, manual transcript screening will not be performed for the time being.

```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder
orthofinder -f "data/primary_transcripts"
```