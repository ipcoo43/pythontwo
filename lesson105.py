print('''
[ Request ]
- 요청 방식 : GET, POST, PUT, DELETE, PATCH
- 요청 대상 : media.daum.net  => HostName
- 추가적인 정보 
 > 경로 : /photo-viewer => Path
 > 데이터 : ?cid = 318190 => GET방식
 > 헤시 : #2017060505

[ 분석 ]
- 요청 방식 : GET
- 요청 대상 : search.naver.com/  => HostName
- 추가적인 정보 
 > 경로 : /search.naver => Path
 > 데이터 :?sm=tab_sug.top  => 요청 매개 변수
						&where=kin
						&query=초콜릿(디코딩) # %EC%B4%88%EC%BD%9C%EB%A6%BF(인코딩)
''')