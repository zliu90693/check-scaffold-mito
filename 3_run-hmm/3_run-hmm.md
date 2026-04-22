Run hmmbuild to build model, and use the model to find proteins from the target species.
```bash
cd /home/liuzhiyu/Projects/neo_caste/check-scaffold-mito/3_run-hmm
for gene_faa in ./data/mito_genes_splitbygenes/* ; do
    faa_name=$(basename $gene_faa)
    g_name="${faa_name%.faa}"
    ./hmm-build-search.sh $g_name
done
```