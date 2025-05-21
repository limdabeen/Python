from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('/Users/imdabin/Desktop/wine.csv', header=None)
print(df.head())
X = df.iloc[:,0:12]
y = df.iloc[:,12]