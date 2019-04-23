print('''
[ CSV/TSV ]
- CSV : Comma-Seperated Value => 쉼표로 구분된 값
 > 1000,비누,300    => 쉼표로 구분     (CSV)
 > 1002 마스크 230 => 띄어 쓰기로 구분 (SSV)
 > 1001	 장갑	 150 => 탭으로 구분      (TSV)
- 한 줄에 데이터는 하나
- 한 줄에는 쉼표로 속성을 구분
- 첫 번째 줄은 헤더로 사용 가능
''')
print('''
[ xml, json, csv 데이터 비교 ]
1. xml 데이터 
	<product>
		<product id="1000">
			<name>비누</name>
			<price>300</price>
		</product>
		<product id="1001">
			<name>장갑</name>
			<price>400</price>
		</product>
		<product id="1002">
			<name>마스크</name>
			<price>500</price>
		</product>
	</product>

2. json 데이터
	[{
		ID:1000,
		이름:"비누",
		가격:300
	},{
		ID:1001,
		이름:"장갑",
		가격:400
	},{
		ID:1002,
		이름:"마스크",
		가격:500
	}]

3. csv 데이터
	ID,이름,가격
	1000,비누,300
	1001,장갑,400
	1002,마스크,5000

4. 데이터 용량 비교 : csv > json > xml
5. 표현력 비교 : xml > json > csv
6. 가독성 비교 : xml > json > csv
7. 최근 동향 : json(현재 많이 사용), csv(데이터 큰 용량의 장점)를 많이 사용
''')