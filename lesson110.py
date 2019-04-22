import time
'''
with open('test.txt','r',encoding='utf-8') as fp:
	for i in fp:
		print(i.replace('.','\n'))
		time.sleep(1)

f = open("test.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("test.txt")
try:
   for line in f:
       print(line)
       # 한줄씩 처리하는 코드
finally:
   f.close()
'''
f_name='test.txt'
with open(f_name) as ifp:
	lines = ifp.read().split('.')
	for line in lines:
		print(line)
		time.sleep(3)
