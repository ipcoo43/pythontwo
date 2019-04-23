import json

json_str = """[
	{"name":"사과","price":1000},
	{"name":"바나나","price":2000},
	{"name":"배","price":3000},
	{"name":"귤","price":4000},
	{"name":"자두","price":5000}
]"""

print('# 문자열 => 파이썬 자료형')
output = json.loads(json_str)
print(output)
print(type(output))
print()

print('# 파이썬 자료형 => JSON 문자열')
text = json.dumps(output)
print(text)
print(type(text))