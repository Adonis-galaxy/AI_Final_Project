from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB  
from sklearn.naive_bayes import BernoulliNB  
from sklearn.naive_bayes import ComplementNB  
X, y = load_iris(return_X_y=True)
from base import baseline
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

gnb = ComplementNB(alpha=1.1)
# y_pred = gnb.fit(X_train, y_train).predict(X_test)
# print("Number of mislabeled points out of a total %d points : %d"% (X_test.shape[0], (y_test != y_pred).sum()))
baseline(gnb)
# print(type(gnb))
