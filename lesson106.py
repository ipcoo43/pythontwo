import urllib.request
import urllib.parse

api = 'https://search.naver.com/search.naver'
values={
	'sm':'tab_sug.top',
	'where':'kin',
	'query':'초콜릿' # %EC%B4%88%EC%BD%9C%EB%A6%BF
}

params = urllib.parse.urlencode(values) # 요청 매개 변수
url = api + '?' + params
print('ape =',api)
print('params =',params)
print('url =', url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')  # euc-kr
print(text)