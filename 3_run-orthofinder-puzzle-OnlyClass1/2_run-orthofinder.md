```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder-puzzle-OnlyClass1
# which primary_transcript.py
# /home/liuzhiyu/Software/miniconda3/envs/check-mito/bin/primary_transcript.py
for f in data/* ; do python /home/liuzhiyu/Software/miniconda3/envs/check-mito/bin/primary_transcript.py $f ; done
```

```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder-puzzle-OnlyClass1
orthofinder -f "data/primary_transcripts"
```