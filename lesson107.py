from bs4 import BeautifulSoup

html = '''
<html><body>
<div id="meigen">
	<h1>위키북스 도서</h1>
	<ul class="items art it boo">
		<li>유니티 게임 이펙트 입문</li>
		<li>스위프트로 시작한는 아이폰 앱 개발 교과서</li>
		<li>모던 웹사이트 디자인의 정석</li>
	</ul>
</div>
</body></html>
'''
# 태그 선택자 : "ul", 'div', 'li'
# 아이디 선택자 : #id  => 하나 지정
# 클래스 선택자 : .class => 여러개 지정 가능
# 구조 선택자 : 후손 선택자, 자식 선택자
# 후손 선택자 : 태그 아래의 모든 것 <html>아래의 body, h1, ul, li "#meigen li"
# 자식 선택자 : 태그 바로 아래의 자식 <html>아래의 <body> 만 자식 "ul.items > li"

soup = BeautifulSoup(html,'html.parser')
header = soup.select_one('body> div > h1')    # 하나 선택, 요소
list_items = soup.select('ul.items > li')     # 여러개 선택, 요소의 배열

print(header.string)
#header.attrs['title']
print(soup.select_one('ul').attrs)

for li in list_items:
	print(li.string)