import urllib.request

url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test1.png'

mem = urllib.request.urlopen(url).read()

with open(savename,'wb') as fp:
	fp.write(mem)
	print('저장되었습니다.')