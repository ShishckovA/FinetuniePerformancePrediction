import os
import pandas as pd
import numpy as np


files = os.listdir("SentEval/data/probing")
files = [file for file in files if file.endswith(".txt")]
print(files)
all_texts = []
for file in files:
    df = pd.read_csv(f"SentEval/data/probing/{file}", sep="\t", header=None)
    all_texts.append(df.loc[:, 2].values)

with open(f"SentEval/data/all_data.txt", "w") as fout:
    for elem in np.concatenate(all_texts)[:15000]:
        print(elem, file=fout)