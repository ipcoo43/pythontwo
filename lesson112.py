import requests
from bs4 import BeautifulSoup

# 세션 만들기
session = requests.session()

# 로그인
url = 'http://www.hanbit.co.kr//member/login_proc.php'
data = {
	'return_url':'http://www.hanbit.co.kr/index.html',
	'm_id':'ipcoo43',
	'm_passwd':'********'
}

response = session.post(url, data=data)
response.raise_for_status()

# 마일리지 가져와 보기
url = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'
response = session.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text,'html.parser')
text = soup.select_one('.mileage_section1 span').get_text()
print('마일리지 :',text)
