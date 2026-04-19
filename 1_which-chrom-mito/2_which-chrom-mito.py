# Depends on conda environment: check-mito (see .env/check-mito.yml)

# %%

# from pyfaidx import Fasta

# ffna = Fasta("./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_genomic.fna")
# for name in ffna.keys():
#     print(name)

# # %%

# for name in ffna.keys():
#     if name.startswith("NC"):
#         print(f"{name}: {len(ffna[name])}")

# %%

from pyfaidx import Fasta

def check_chrom_length(ffna_file, prefix=""):
    ffna = Fasta(ffna_file)
    if prefix:
        for name in ffna.keys():
            if name.startswith(prefix):
                print(f"{name}: {len(ffna[name])}")

    else:
        for name in ffna.keys():
            print(name)


# %%
Acer_fna="./data/Apis_cerana/GCF_029169275.1_AcerK_1.0_genomic.fna"
check_chrom_length(Acer_fna)
# %%
check_chrom_length(Acer_fna, "NC")
# NC_083852.1: 27131825
# NC_083853.1: 15875455
# NC_083854.1: 13386827
# NC_083855.1: 13159592
# NC_083856.1: 13471485
# NC_083857.1: 17285085
# NC_083858.1: 13645534
# NC_083859.1: 12170773
# NC_083860.1: 11954044
# NC_083861.1: 12434583
# NC_083862.1: 15832348
# NC_083863.1: 11302906
# NC_083864.1: 11000381
# NC_083865.1: 11731789
# NC_083866.1: 9491825
# NC_083867.1: 7109830
# NC_014295.1: 15895 <---


# %%
Amel_fna="./data/Apis_mellifera/Apis_mellifera.Amel_HAv3.1.dna.toplevel.fna"
check_chrom_length(Amel_fna)
# %%
check_chrom_length(Amel_fna, "CM")
# CM009931.2: 27754200
# CM009932.2: 16089512
# CM009933.2: 13619445
# CM009934.2: 13404451
# CM009935.2: 13896941
# CM009936.2: 17789102
# CM009937.2: 14198698
# CM009938.2: 12717210
# CM009939.2: 12354651
# CM009940.2: 12360052
# CM009941.2: 16352600
# CM009942.2: 11514234
# CM009943.2: 11279722
# CM009944.2: 10670842
# CM009945.2: 9534514
# CM009946.2: 7238532
# CM009947.2: 16343 <---


# %%
Bter_fna="./data/Bombus_terrestris/Bombus_terrestris_gca910591885v2.iyBomTerr1.2.dna.toplevel.fna"
check_chrom_length(Bter_fna)
# %%
for pre in range(1,10):
    check_chrom_length(Bter_fna, f"{pre}")
# 1: 18372659
# 10: 20491647
# 11: 20781255
# 12: 12897853
# 13: 14593050
# 14: 11964351
# 15: 11413514
# 16: 8887048
# 17: 11646943
# 18: 5271557
# 2: 19735706
# 3: 22099476
# 4: 18668021
# 5: 14194883
# 6: 23129593
# 7: 25524254
# 8: 11657431
# 9: 19446242


# %%
Cflo_fna="./data/Camponotus_floridanus/Camponotus_floridanus_gca003227725v1rs.Cflo_v7.5.dna.toplevel.fna"
check_chrom_length(Cflo_fna)
# %%
check_chrom_length(Cflo_fna, "QAN")

# %%
Ccal_fna="./data/Ceratina_calcarata/Ceratina_calcarata_genome_uni1041-mb-hirise-teril_10-15-2020_final_assembly.fna"
check_chrom_length(Ccal_fna)
# %%
check_chrom_length(Ccal_fna, "Sc")


# %%
Dmel_fna = "./data/Drosophila_melanogaster/Drosophila_melanogaster.BDGP6.54.dna.toplevel.fna"
check_chrom_length(Dmel_fna)
# %%
check_chrom_length(Dmel_fna, "mito")
# mitochondrion_genome: 19524 <---


# %%
Hsal_fna = "./data/Harpegnathos_saltator/Harpegnathos_saltator_gca003227715v2rs.Hsal_v8.5.dna.toplevel.fna"
check_chrom_length(Hsal_fna)
# %%
check_chrom_length(Hsal_fna, "QANH")


# %%
Lzep_fna_1 = "./data/Lasioglossum_zephyrus/GCA_028455615.1_LZEP_v2.2.0_genomic.fna"
check_chrom_length(Lzep_fna_1)
# %%
check_chrom_length(Lzep_fna_1, "CM")
# CM052320.1: 14459315
# CM052321.1: 25729413
# CM052322.1: 12391266
# CM052323.1: 14651701
# CM052324.1: 13343356
# CM052325.1: 12155835
# CM052326.1: 23416501
# CM052327.1: 11150181
# CM052328.1: 20394881
# CM052329.1: 23461232
# CM052330.1: 20746387
# CM052331.1: 7716444
# CM052332.1: 19623023
# CM052333.1: 14608330


# %%
Lzep_fna_2 = "./data/Lasioglossum_zephyrus/LZEP_genome_v2.1.1.fna"
check_chrom_length(Lzep_fna_2)
# %%
check_chrom_length(Lzep_fna_2, "LZEP")


# %%
Lalb_fna = "./data/Lasioglossum_albipes/LALB_genome_v2.1.1.fna"
check_chrom_length(Lalb_fna)
# %%
check_chrom_length(Lalb_fna, "LALB")


# %%
Mpha_fna = "./data/Monomorium_pharaonis/Monomorium_pharaonis_gca013373865v2.ASM1337386v2.dna.toplevel.fna"
check_chrom_length(Mpha_fna)
# %%
check_chrom_length(Mpha_fna, "CM")


# # %%
# Mpha_fna = "../data/Monomorium_pharaonis/GCF_013373865.1_ASM1337386v2_genomic.fna"
# check_chrom_length(Mpha_fna)
# # %%
# check_chrom_length(Mpha_fna, "NC")
# # %%
