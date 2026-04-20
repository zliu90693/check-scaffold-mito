```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/2_find-mito-gene
data_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/data

mito_sp=("Apis_cerana" "Apis_mellifera" "Drosophila_melanogaster")

for sp_name in "${mito_sp[@]}"; do

    sp_path="${data_path}/${sp_name}"
    mkdir -p "./data/${sp_name}"

    find "$sp_path" -type f \( -name "*.faa" -o -name "*.gtf" \) | while read -r f_path; do
        f_name=$(basename "$f_path")
        # 使用 -f 参数确保如果软链已存在可以覆盖/更新，防止重复运行报错
        ln -sf "$f_path" "./data/${sp_name}/${f_name}"
    done
done
```