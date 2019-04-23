print('''
[ xls 사용 ]
- 자료 다운로드 : http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1041
- 받은 자료 최근 통합자료로 새이름 저장
- pip install openpyxl
''')

import openpyxl

book = openpyxl.load_workbook('stats_104102.xlsx')

# 첫 번째 방법 
print(book.get_sheet_names())
print(book.get_sheet_by_name('stats_104102'))

# 두 번째 방법
sheet = book.worksheets[0]
for row in sheet.rows:
	for data in row:
		print(data.value, end=" ")
	print("",end="\n")