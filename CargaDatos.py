import pandas as pd
import numpy as np

def carga_dataframe(nombreCSV):
    df = pd.read_csv(nombreCSV)
    return df



