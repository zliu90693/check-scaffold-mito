#!/bin/bash

declare gene_name="$1"

mkdir -p "./metadata/hmm_interfile/${gene_name}"
mkdir -p "./metadata/hmmsearch_output/${gene_name}"
mafft --auto "./data/mito_genes_splitbygenes/${gene_name}.faa" > "./metadata/hmm_interfile/${gene_name}/${gene_name}_aligned.faa"
hmmbuild "./metadata/hmm_interfile/${gene_name}/${gene_name}.hmm" "./metadata/hmm_interfile/${gene_name}/${gene_name}_aligned.faa"
for target_faa in ./data/target_sp_allpep/* ; do
    faa_name=$(basename $target_faa)
    f_name="${faa_name%.faa}"
    hmmsearch --tblout "./metadata/hmmsearch_output/${gene_name}/${f_name}.txt" \
           -E 1e-5 \
           "./metadata/hmm_interfile/${gene_name}/${gene_name}.hmm" \
           $target_faa
done