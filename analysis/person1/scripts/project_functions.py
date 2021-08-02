import pandas as pd
import numpy as np

# Method chaining begins
def load_and_process(url):
    df = (
        data
        .drop(columns=['Positive affect', 'Negative affect'])
        .loc[lambda x: x['year']>2015]
        .sort_values("Life Ladder", ascending=False)
        .dropna(axis='rows', thresh =8).reset_index(drop=True)
        .reset_index(drop=True)
    
    )

    return df

