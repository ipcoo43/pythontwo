from sklearn import svm, metrics
import pandas

csv = pandas.read_csv('iris_a.csv')
data = csv[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label = csv['Name']
sample = [[5.1, 3.0, 1.3, 0.2]]

clf = svm.SVC()
clf.fit(data,label)
results = clf.predict(sample)
print(results)

# score = metirics.accuracy_score()
# print('정답률 :',score)