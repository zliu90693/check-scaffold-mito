# %%

from pyfaidx import Fasta
from gtfparse import read_gtf
import polars as pl

# %%

def get_mito_pep(sp_name, gtf_path, prefix, faa_path):
    gtf_df = read_gtf(gtf_path)
    gtf_df_mito = gtf_df.filter(
        gtf_df["seqname"] == prefix, gtf_df["protein_id"] != "", gtf_df["feature"] == "CDS"
    )
    gtf_df_mito_pepid = gtf_df_mito["protein_id"].to_list()

    ffaa = Fasta(faa_path)
    intersection_len = len(set(gtf_df_mito_pepid) & set(ffaa.keys()))
    print(intersection_len)

    if intersection_len == 13:
        with open(f"./metadata/{sp_name}.faa", 'w') as f:
            for sid in gtf_df_mito_pepid:
                record = ffaa[sid]
                header = record.long_name
                sequence = record[:].seq
                f.write(f">{header}\n{sequence}\n")
        if "gene" in gtf_df_mito.columns: # 这里考虑了ensembl和RefSeq提供的gtf的格式不同, RefSeq可能有protein_id无gene_id, 有gene无gene_name
            gtf_df_mito_csv = gtf_df_mito.select( # Refseq
                pl.col("gene"),
                pl.col("protein_id")
            )
        else:
            gtf_df_mito_csv = gtf_df_mito.select( # ensembl
                pl.col("gene_name"),
                pl.col("protein_id")
            )
        gtf_df_mito_csv.write_csv(f"./metadata/{sp_name}.csv")

# %%

get_mito_pep(
    sp_name="Apis_cerana_mito",
    gtf_path="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_genomic.gtf",
    prefix="NC_014295.1",
    faa_path="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_protein.faa"
)
# %%

get_mito_pep(
    sp_name="Apis_mellifera_mito",
    gtf_path="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.62.gtf",
    prefix="CM009947.2",
    faa_path="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.pep.all.faa"
)

# %%

get_mito_pep(
    sp_name="Drosophila_melanogaster_mito",
    gtf_path="./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.62.gtf",
    prefix="mitochondrion_genome",
    faa_path="./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.pep.all.faa"
)
# %%

# def get_mito_info(sp_name, gtf_path, prefix, faa_path):
#     gtf_df = read_gtf(gtf_path)
#     gtf_df_mito = gtf_df.filter(
#         gtf_df["seqname"] == prefix, gtf_df["protein_id"] != "", gtf_df["feature"] == "CDS"
#     )
#     gtf_df_mito_pepid = gtf_df_mito["protein_id"].to_list()

#     ffaa = Fasta(faa_path)

#     intersection_len = len(set(gtf_df_mito_pepid) & set(ffaa.keys))
#     print(intersection_len)

#     if intersection_len == 13:
#         if "gene" in gtf_df_mito.columns: # 这里考虑了ensembl和RefSeq提供的gtf的格式不同, RefSeq可能有protein_id无gene_id, 有gene无gene_name
#             gtf_df_mito_csv = gtf_df_mito.select( # Refseq
#                 pl.col("gene"),
#                 pl.col("protein_id")
#             )
#         else:
#             gtf_df_mito_csv = gtf_df_mito.select( # ensembl
#                 pl.col("gene_name"),
#                 pl.col("protein_id")
#             )
#         gtf_df_mito_csv.write_csv(f"./metadata/{sp_name}.csv")

# # %%

# get_mito_info(
#     sp_name="Apis_cerana",
#     gtf_path="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_genomic.gtf",
#     prefix="NC_014295.1",
#     faa_path="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_protein.faa"
# )

# # %%

# get_mito_info(
#     sp_name="Apis_mellifera",
#     gtf_path="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.62.gtf",
#     prefix="CM009947.2",
#     faa_path="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.pep.all.faa"
# )

# # %%

# get_mito_info(
#     sp_name="Drosophila_melanogaster",
#     gtf_path="./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.62.gtf",
#     prefix="mitochondrion_genome",
#     faa_path="./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.pep.all.faa"
# )
