# %%

from pyfaidx import Fasta
from gtfparse import read_gtf
import polars as pl

def find_mito(sp_name, gtf_path, prefix, faa_path):
    gtf_df = read_gtf(gtf_path)
    gtf_df_mito = gtf_df.filter(
        gtf_df["seqname"] == prefix, gtf_df["protein_id"] != "", gtf_df["feature"] == "CDS"
    )
    gtf_df_mito_pepid = gtf_df_mito["protein_id"].to_list()

    ffaa = Fasta(faa_path)
    faa_namelist = []
    for name in ffaa.keys():
        faa_namelist.append(name)

    intersection_len = len(set(gtf_df_mito_pepid) & set(faa_namelist))
    print(intersection_len)

    if intersection_len == 13:
        if "gene" in gtf_df_mito.columns:
            gtf_df_mito_csv = gtf_df_mito.select(
                pl.col("gene"),
                pl.col("protein_id")
            )
        else:
            gtf_df_mito_csv = gtf_df_mito.select(
                pl.col("gene_name"),
                pl.col("protein_id")
            )
        gtf_df_mito_csv.write_csv(f"./metadata/{sp_name}.csv")


# %%

find_mito(
    sp_name="Apis_cerana",
    gtf_path="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_genomic.gtf",
    prefix="NC_014295.1",
    faa_path="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_protein.faa"
)
# %%

find_mito(
    sp_name="Apis_mellifera",
    gtf_path="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.62.gtf",
    prefix="CM009947.2",
    faa_path="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.pep.all.faa"
)

# %%

find_mito(
    sp_name="Drosophila_melanogaster",
    gtf_path="./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.62.gtf",
    prefix="mitochondrion_genome",
    faa_path="./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.pep.all.faa"
)