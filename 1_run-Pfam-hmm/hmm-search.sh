#!/bin/bash

declare hmm_name="$1"

mkdir -p "./metadata/hmmsearch_output/${hmm_name}"
for target_faa in ./data/target_sp_allpep/* ; do
    faa_name=$(basename $target_faa)
    f_name="${faa_name%.faa}"
    hmmsearch --tblout "./metadata/hmmsearch_output/${hmm_name}/${f_name}.txt" \
           -E 1e-5 \
           "./data/Pfam_hmm/${hmm_name}.hmm" \
           $target_faa
done