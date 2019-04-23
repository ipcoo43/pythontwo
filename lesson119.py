from bs4 import BeautifulSoup
import urllib.request

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
request = urllib.request.urlopen(url)
xml = request.read()

soup = BeautifulSoup(xml,'html.parser')
seoul =  soup.find_all('location')[2]
print(seoul.city)
print('날짜\t','\t날씨','최저','최고',sep='\t')
for item in seoul.find_all('data'):
	print(item.tmef.string,':',item.find('wf').text,',',item.tmn.string,',',item.tmx.string)