from sklearn import svm, metrics
import pandas
from sklearn.model_selection import train_test_split

csv = pandas.read_csv('iris.csv')
data = csv[['SepalLength','SepalWidth','PetalLength','PetalWidth']]
label = csv['Name']

train_date, test_data, train_label, test_label = train_test_split(data, label)

clf = svm.SVC()
clf.fit(train_date,train_label)
results = clf.predict(test_data)

score = metrics.accuracy_score(results,test_label)
print('정답률 :',score)