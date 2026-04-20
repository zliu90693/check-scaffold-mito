# %%

from gtfparse import read_gtf

df = read_gtf("./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_genomic.gtf")
df

# %%

mito_df = df.filter(
    df["seqname"] == "NC_014295.1",
    df["gene_biotype"] == "protein_coding"
)

# %%


