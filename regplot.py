import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/imdabin/Desktop/(2010-2020) weather.xlsx'
df = pd.read_excel(file_path)

df.drop('지점', axis=1, inplace=True)
df.columns = ['날짜', '평균기온', '최저기온', '최고기온']
df.dropna(subset=['최고기온'], axis=0, inplace=True)
df['년도'] = df['날짜'].dt.year
conditions = (df['날짜'].dt.month == 8) & (df['날짜'].dt.day == 15)
seoul0815 = df[conditions]
fig = plt.figure(figsize=(15, 7))
sns.regplot(x='년도', y='평균기온', data=seoul0815)
plt.grid()
plt.show()