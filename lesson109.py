# 모듈 추출하기
import urllib.request
from bs4 import BeautifulSoup
import time

# 기사 목록을 가져 오기
url = 'https://news.naver.com/main/home.nhn'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')

results = soup.select('.mlist2.no_bg a') #strong

with open('test.txt','w',encoding='utf-8') as fp:
	fp.write('')

for result in results:
	# 기사 가져 오기
	# print(result.attrs['href'])
	url_article = result.attrs['href']
	html = urllib.request.urlopen(url_article)
	soup_article = BeautifulSoup(html,'html.parser')
	content = soup_article.select_one('#articleBodyContents')
	# print(content.contents)
	
	# 가공 하기
	output = ''
	for item in content.contents:
		stripped = str(item).strip()
		if stripped == '':
			continue
		if stripped[0] not in ['<','/']:
			output += str(item).strip()
	wcontent = output.replace('본문 내용TV플레이어','')
	print(wcontent)
	print('-'*70)
	time.sleep(1)
	with open('test.txt','a',encoding='utf-8') as fp:
		fp.write(wcontent)