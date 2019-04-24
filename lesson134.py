from sklearn import model_selection, svm, metrics

clf = svm.SVC()                   # 기계학습 알고리즘 선택 
clf.fit                           # 학습 하기
predict = clf.predict()           # 예측 하기
score = metrics.accuracy_score()  # 정답률 구하기
print('정답률 :',score)