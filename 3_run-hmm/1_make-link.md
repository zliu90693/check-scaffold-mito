```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-hmm
mito_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/2_find-mito-gene/metadata

find "$mito_path" -type f -name "*.faa" | while read -r f_path; do
    f_name=$(basename "$f_path")
    ln -sf "$f_path" "./data/mito_genes/${f_name}"
done
```

```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-hmm
data_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/data

target_sp=("Bombus_terrestris" "Camponotus_floridanus" "Ceratina_calcarata" "Harpegnathos_saltator" "Lasioglossum_albipes" "Lasioglossum_zephyrus" "Monomorium_pharaonis")
for sp_name in "${target_sp[@]}"; do
    ln -sf "${data_path}/${sp_name}/"*.faa "./data/target_sp_allpep/${sp_name}.faa"
done
```