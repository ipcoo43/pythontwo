from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
request = urllib.request.urlopen(url)
xml = request.read()

soup = BeautifulSoup(xml,'html.parser')

for location in soup.findAll('location'):
	print(location.city.string)
	print('-'*20)

	for data in location.findAll('data'):
		print('시간 :',data.tmef.string)
		print('날씨 :',data.wf.string)
		print('최저 :',data.tmn.string)
		print('최고 :',data.tmx.string)
		print('신뢰도 :',data.reliability.string)
		print()