import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = '/Users/imdabin/Desktop/(2010-2020) weather.xlsx'
df = pd.read_excel(file_path)
print(df.head())