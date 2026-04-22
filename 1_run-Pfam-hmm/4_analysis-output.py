# %%

from pathlib import Path
import pandas as pd

# %%

path_obj = Path('./metadata/hmmsearch_output')
results = []
for hmm_output_path in path_obj.rglob('*.txt'):
    print(hmm_output_path)
    with open(hmm_output_path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            cols = line.split()
            if len(cols) < 10:
                continue
            results.append({
                "species": str(hmm_output_path).split('/')[-1].split('.')[0],
                "hmm_name": str(hmm_output_path).split('/')[-2],
                "protein_id": cols[0],
                "evalue": float(cols[4]),
                "score": float(cols[5])
            })

# %%

df = pd.DataFrame(results).sort_values(by='species')
# df
df.to_csv("./metadata/mito-gene-in-target.csv")

# %%
