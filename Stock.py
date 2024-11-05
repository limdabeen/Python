import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 삼성전자와 애플의 주가 데이터를 yfinance로 불러오기
samsung = yf.download('005930.KS', start='2013-01-01', end='2023-01-01')  # '005930.KS'는 삼성전자 종목 코드
apple = yf.download('AAPL', start='2013-01-01', end='2023-01-01')  # 애플 종목 코드

# 상위 5개 데이터 출력
print("삼성전자 주가 데이터:")
print(samsung.head())

print("\n애플 주가 데이터:")
print(apple.head())

# CSV 파일로 저장
samsung.to_csv('samsung_stock.csv')
apple.to_csv('apple_stock.csv')

# 삼성전자 주가 그래프
plt.figure(figsize=(10, 5))
plt.plot(samsung.index, samsung['Close'], label='Samsung Electronics')
plt.title('Samsung Electronics Stock Prices (2013-2023)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()

# 애플 주가 그래프
plt.figure(figsize=(10, 5))
plt.plot(apple.index, apple['Close'], label='Apple')
plt.title('Apple Stock Prices (2013-2023)')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()