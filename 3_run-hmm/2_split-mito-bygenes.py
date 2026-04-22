# %%

from pyfaidx import Fasta
import pandas as pd
from functools import reduce
import os

# %%

new_cols = ['gene', 'protein_id_Acer']
Acer_info = pd.read_csv("./data/mito_info/Apis_cerana_mito.csv", header=0, names=new_cols)
new_cols = ['gene', 'protein_id_Amel']
Amel_info = pd.read_csv("./data/mito_info/Apis_mellifera_mito.csv", header=0, names=new_cols)
new_cols = ['gene', 'protein_id_Dmel']
Dmel_info = pd.read_csv("./data/mito_info/Drosophila_melanogaster_mito.csv", header=0, names=new_cols)

#     gene protein_id_Acer
# 0    ND2  YP_003735169.1
# 1   COX1  YP_003735170.2
# 2   COX2  YP_003735171.1
# 3   ATP8  YP_003735172.1
# 4   ATP6  YP_003735173.1
# 5   COX3  YP_003735174.1
# 6    ND3  YP_003735175.1
# 7    ND5  YP_003735176.1
# 8    ND4  YP_003735177.1
# 9   ND4L  YP_003735178.1
# 10   ND6  YP_003735179.1
# 11  CYTB  YP_003735180.1
# 12   ND1  YP_003735181.1

#     gene protein_id_Amel
# 0   COX1       NP_008083
# 1   ATP6       NP_008086
# 2   ATP8       NP_008085
# 3   COX2       NP_008084
# 4   COX3       NP_008087
# 5    ND4       NP_008090
# 6   CYTB       NP_008093
# 7    ND1       NP_008094
# 8    ND5       NP_008089
# 9    ND2       NP_008082
# 10   ND3       NP_008088
# 11   ND6       NP_008092
# 12  ND4L       NP_008091

#     gene protein_id_Dmel
# 0   COX2     FBpp0100177
# 1   ATP8     FBpp0100178
# 2   CYTB     FBpp0390634
# 3   COX1     FBpp0100176
# 4    ND1     FBpp0390631
# 5   ND4L     FBpp0100184
# 6    ND4     FBpp0390632
# 7   ATP6     FBpp0390630
# 8   COX3     FBpp0100180
# 9    ND5     FBpp0390633
# 10   ND6     FBpp0100185
# 11   ND2     FBpp0100175
# 12   ND3     FBpp0100181

# %%

if (set(Dmel_info.iloc[:,0].to_list()) == set(Amel_info.iloc[:,0].to_list())) & \
    (set(Dmel_info.iloc[:,0].to_list()) == set(Acer_info.iloc[:,0].to_list())):
    dfs = [Acer_info, Amel_info, Dmel_info]
    final_df = reduce(lambda left, right: pd.merge(left, right, on='gene'), dfs)

#     gene protein_id_Acer protein_id_Amel protein_id_Dmel
# 0    ND2  YP_003735169.1       NP_008082     FBpp0100175
# 1   COX1  YP_003735170.2       NP_008083     FBpp0100176
# 2   COX2  YP_003735171.1       NP_008084     FBpp0100177
# 3   ATP8  YP_003735172.1       NP_008085     FBpp0100178
# 4   ATP6  YP_003735173.1       NP_008086     FBpp0390630
# 5   COX3  YP_003735174.1       NP_008087     FBpp0100180
# 6    ND3  YP_003735175.1       NP_008088     FBpp0100181
# 7    ND5  YP_003735176.1       NP_008089     FBpp0390633
# 8    ND4  YP_003735177.1       NP_008090     FBpp0390632
# 9   ND4L  YP_003735178.1       NP_008091     FBpp0100184
# 10   ND6  YP_003735179.1       NP_008092     FBpp0100185
# 11  CYTB  YP_003735180.1       NP_008093     FBpp0390634
# 12   ND1  YP_003735181.1       NP_008094     FBpp0390631

# %%

Acer_mito = Fasta("./data/mito_genes/Apis_cerana_mito.faa")
Amel_mito = Fasta("./data/mito_genes/Apis_mellifera_mito.faa")
Dmel_mito = Fasta("./data/mito_genes/Drosophila_melanogaster_mito.faa")

# %%

mito_sources = {
    'protein_id_Acer': Acer_mito,
    'protein_id_Amel': Amel_mito,
    'protein_id_Dmel': Dmel_mito
}

# Traversing the dataset row by row
for index, row in final_df.iterrows():
    gene_name = row['gene']
    output_path = os.path.join("./data/mito_genes_splitbygenes", f"{gene_name}.faa")
    
    with open(output_path, 'w') as f:
        for col_name, fasta_obj in mito_sources.items():
            target_id = row[col_name]
            
            if target_id in fasta_obj:
                record = fasta_obj[target_id]
                
                f.write(f">{record.long_name}\n")
                f.write(f"{record[:].seq}\n")
            else:
                print(f"Warning: No {target_id} in {col_name}")

# %%
