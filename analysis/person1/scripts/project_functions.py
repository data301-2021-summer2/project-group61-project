import numpy as np;
import pandas as pd;
import matplotlib.pylab as plt;
import seaborn as sns;

# Method chaining begins
def load_and_process(url):
    df = (
        pd.read_csv(url)
        .drop(columns=['Positive affect', 'Negative affect'])
        .loc[lambda x: x['year']>2015]
        .sort_values("Life Ladder", ascending=False)
        .dropna(axis='rows', thresh =8).reset_index(drop=True)
        .reset_index(drop=True)
    
    )

    return df;

