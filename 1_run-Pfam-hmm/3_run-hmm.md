```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm
for hmm_model in ./data/Pfam_hmm/* ; do
    hmm_name=$(basename $hmm_model)
    h_name="${hmm_name%.hmm}"
    ./hmm-search.sh $h_name
done
```