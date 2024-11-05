import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://news.naver.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

articles = []

news_section = soup.find_all('div', {'class': 'newsnow_tx_inner'})

for news in news_section:
    title = news.find('a').get_text(strip=True)  
    link = news.find('a')['href']  
    
    articles.append({
        'Title': title,
        'Link': link
    })

df = pd.DataFrame(articles)

print(df.head())

df.to_csv('naver_news.csv', index=False)

print("크롤링한 데이터를 'naver_news.csv' 파일로 저장했습니다.")
