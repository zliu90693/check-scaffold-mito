```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/1_which-chrom-mito
data_path=/home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/data
for sp_path in "${data_path}/"*; do
    
    sp_name=$(basename $sp_path)
    mkdir -p "./data/${sp_name}"
    for fna_path in $(find $sp_path -name "*.fna"); do
        fna_name=$(basename $fna_path)
        ln -sf $fna_path "./data/${sp_name}/${fna_name}"
    done
done
```