```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_run-Pfam-hmm
data_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/data

for sp_path in "${data_path}/"*; do
    find "$sp_path" -type f -name "*.faa" | while read -r f_path; do
        sp_name=$(basename "$sp_path")
        ln -sf "$f_path" "./data/target_sp_allpep/${sp_name}.faa"
    done
done
```