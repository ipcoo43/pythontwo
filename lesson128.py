import openpyxl

workbook = openpyxl.Workbook() 
sheet = workbook.active

# 데이터 쓰기
sheet['A1'] = '테스트 파일'
sheet['B2'] = '안녕하세요'
sheet.merge_cells('A1:C1')
sheet['A1'].font = openpyxl.styles.Font(size=20,color='FF0000')

workbook.save('newFile.xlsx')