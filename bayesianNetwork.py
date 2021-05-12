from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pandas as pd

msg = pd.read_csv('naivetext.csv', names=['message', 'label'])
print('The dimensions of the dataset', msg.shape)
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})

X = msg.message
y = msg.labelnum

print(X)
print(y)

xtrain, xtest, ytrain, ytest = train_test_split(X, y)

print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)

count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)
clf = MultinomialNB().fit(xtrain_dtm, ytrain)
predicted = clf.predict(xtest_dtm)

print('Accuracy metrics')
print('Accuracy of the classifer is', metrics.accuracy_score(ytest, predicted))
print('Confusion matrix')
print(metrics.confusion_matrix(ytest, predicted))
print('Recall and Precison ')
print(metrics.recall_score(ytest, predicted))
print(metrics.precision_score(ytest, predicted))
