import sys
import pandas as pd
import os

# run python3 csv-combiner.py filename1.csv filename2.csv


def csv_combiner():
    filenames = sys.argv[1:]
    all_dfs = []

    for filename in filenames:
        df = pd.read_csv(filename)

        if (df.empty == True):
            print(filename + " is empty.")

        base_filename = os.path.basename(filename)
        df['filename'] = [base_filename for row in df.index]
        all_dfs.append(df)

    all_dfs = pd.concat(all_dfs)
    all_dfs.to_csv(sys.stdout, index=False)


csv_combiner()
