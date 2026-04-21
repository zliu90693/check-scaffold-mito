```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-orthofinder
data_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/data

sp4orthofndr=("Apis_cerana" "Apis_mellifera" "Drosophila_melanogaster" "Camponotus_floridanus" "Ceratina_calcarata" "Harpegnathos_saltator" "Lasioglossum_zephyrus" "Lasioglossum_albipes") # Species of category (1) and category (4), eight in total

for sp_name in "${sp4orthofndr[@]}"; do
    sp_path="${data_path}/${sp_name}"
    find "$sp_path" -type f -name "*.faa" | while read -r f_path; do
        f_name=$(basename "$f_path")
        cp "$f_path" "./data/${f_name}"
    done
done
```