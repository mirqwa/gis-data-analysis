import os

import pandas as pd


if __name__ == "__main__":
    data_dir = "data"
    dfs = []
    for root, _, files in os.walk(data_dir):
        for file in files:
            df = pd.read_csv(f"{root}/{file}")
            dfs.append(df)
    
    df_main = pd.concat(dfs, ignore_index=True)

