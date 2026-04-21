```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder-puzzle-OnlyClass1
data_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/data

Class1sp4orthofndr=("Apis_cerana" "Apis_mellifera" "Drosophila_melanogaster")
for sp_name in "${Class1sp4orthofndr[@]}"; do
    sp_path="${data_path}/${sp_name}"
    find "$sp_path" -type f -name "*.faa" | while read -r f_path; do
        f_name=$(basename "$f_path")
        cp "$f_path" "./data/${f_name}"
    done
done
```