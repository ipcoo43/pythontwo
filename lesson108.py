from bs4 import BeautifulSoup
import urllib.request

print('네이버 시장지표 페이지 가져오기')
url = 'https://finance.naver.com/marketindex/'
html = urllib.request.urlopen(url)

soup = BeautifulSoup(html,'html.parser')
# soup.select_one()
results = soup.select('span.value')
print('[ 환전 고시 환율 ]')
print('달러 환율 =',results[0].string,'원')  
print('엔 환율 =',results[1].string,'원')  
print('유로 환율 =',results[2].string,'원')  
print('중국 환율 =',results[3].string,'원')  
print()

for result in results:
	print(result.string)