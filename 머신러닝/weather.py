import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

if platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='NanumGothic')  # 리눅스나 colab

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 파일 불러오기
file_path = '/Users/imdabin/Desktop/weather.xlsx'
seoul = pd.read_excel(file_path)

# '년도' 추출
seoul['년도'] = pd.to_datetime(seoul['날짜']).dt.year

# 필요한 열만 추출
seoul = seoul[['년도', '최저기온(℃)', '최고기온(℃)', '평균기온(℃)']]

# NaN(결측값) 제거
seoul = seoul.dropna()

# 특성과 타깃 분리
X = seoul[['년도', '최저기온(℃)', '최고기온(℃)']]
Y = seoul['평균기온(℃)']

x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

plt.figure(figsize=(15, 7))
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("실제 평균기온(℃)")
plt.ylabel("예측 평균기온(℃)")
plt.title("60231222_05_01_LDB")
plt.grid(True)
plt.show()