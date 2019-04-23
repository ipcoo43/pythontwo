import csv, codecs

filename = 'test.csv'
file = codecs.open(filename, 'r', 'euc_kr')

reader = csv.reader(file,delimiter=",")
for cells in reader:
	print(cells[0], cells[1],cells[2]) 