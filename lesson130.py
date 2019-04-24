print('''
pip install -U scikit-learn scipy matplotlib scikit-image
pip install pandas
''')

from sklearn import svm

clf = svm.SVC()
# clf.fit(데이터,답[레이블])
clf.fit([
	[0,0],  # 각각의 요소를 벡터
	[1,0],  # 데이터를 어떻게 넣으냐가 기계학습의 중요 포인트
	[0,1],
	[1,1]
],[0, 1, 1,	0 ]
)
# clf.predict() 우리가 원하는 답[레이블]의 형식을 넣음, predict는 예측하다.
results = clf.predict([
	[0,0], # 0
	[1,0]  # 1
])  # [0 1]

print(results)