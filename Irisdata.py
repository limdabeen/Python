# 1. 데이터셋 선택 및 설명
from sklearn.datasets import load_iris
import pandas as pd

# Iris 데이터셋 불러오기
iris = load_iris()

# DataFrame으로 변환
data = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

# 타겟 데이터를 'species'로 추가
data['species'] = iris['target']

# 데이터 설명 출력
print("Iris 데이터셋 설명:")
print(iris['DESCR'])

# 데이터프레임 상위 5개 출력
data.head()

# 2. 데이터 전처리

# 결측치 확인
print("\n결측치 확인:")
print(data.isnull().sum())

# 중복 데이터 확인
print("\n중복 데이터 확인:")
print(data.duplicated().sum())

# 중복 데이터 제거 (필요시)
data = data.drop_duplicates()

# 3. 기초 통계 분석
print("\n기초 통계 정보:")
print(data.describe())

# 각 변수의 평균, 중앙값, 최소값, 최대값 확인
for col in data.columns:
    print(f"\n{col}에 대한 통계 정보:")
    print(f"평균: {data[col].mean()}")
    print(f"중앙값: {data[col].median()}")
    print(f"최소값: {data[col].min()}")
    print(f"최대값: {data[col].max()}")

