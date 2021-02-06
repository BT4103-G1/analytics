


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm


def preprocess(file, train, test):
    df_train = pd.read_csv(train, sep=" ", header=None)
    df_test = pd.read_csv(test, sep=" ", header=None)
    
    print(f"Train: {df_train.shape}")
    print(f"Test: {df_test.shape}")

    # Combine train and test
    df = df_train.append(df_test)
    print(f"df: {df.shape}")

    # Actual colnames
    columns = ['Engine_ID', 'RUL',
              'ALT', 'Mach', 'TRA',
              'T2', 'T24', 'T30', 'T50',
               'P2', 'P15', 'P30',
               'Nf', 'Nc', 'epr', 'Ps30', 'phi',
               'NRf', 'NRc', 'BPR', 'farB',
               'htBleed', 'Nf_dmd', 'PCNfR_dmd',
               'W31', 'W32', "SD_22", "SD_23"
              ]

    # Rename columns
    df.columns = columns
    df_train.columns = columns
    df_test.columns = columns

    df.describe().transpose()

    # Plot scatterplot
    plt.rcParams.update({'figure.max_open_warning': 0})
    for i in columns[2:]:
        df.plot(x="RUL", y=i, kind="scatter")

    plt.savefig(file+".png")

