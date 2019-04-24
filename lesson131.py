print('''
pip install -U scikit-learn scipy matplotlib scikit-image
pip install pandas
''')

from sklearn import svm, metrics

datas = [[0,0],[1,0],[0,1],[1,1]]
labels = [0,1,1,0]
examples = [[0,0],[1,0]]
examples_label = [0,1]

clf = svm.SVC()
clf.fit(datas, labels)
results = clf.predict(examples)
print(results)
# metrics.accuracy_score(답, 예측했던 결과)
score = metrics.accuracy_score(examples_label, results)
print('정답률 :',score)