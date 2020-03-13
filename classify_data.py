
import sklearn.model_selection
import sklearn.metrics
import numpy as np
data_train = np.loadtxt('min_arabic_data_for_ml.csv', delimiter=' ')

X=data_train[:,0:300]
y=data_train[:,300]

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=1)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=(100,100), max_iter=500, alpha=0.0001,solver='sgd', verbose=10,  random_state=21,tol=0.000000001)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('MLPClassifier')
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('SVC')
from sklearn.svm import SVC # "Support Vector Classifier" 
clf = SVC(kernel='linear') 
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('DecisionTreeClassifier')
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('KNeighborsClassifier')
from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

#print('GaussianProcessClassifier')
#from sklearn.gaussian_process import GaussianProcessClassifier
#from sklearn.gaussian_process.kernels import RBF
#clf= GaussianProcessClassifier(1.0 * RBF(1.0))
#clf.fit(X_train, y_train)
#y_pred = clf.predict(X_test)
#print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('RandomForestClassifier')
from sklearn.ensemble import RandomForestClassifier 
clf= RandomForestClassifier(max_depth=6, n_estimators=12, max_features=5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('AdaBoostClassifier')
from sklearn.ensemble import AdaBoostClassifier
clf= AdaBoostClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('QuadraticDiscriminantAnalysis')
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
clf= QuadraticDiscriminantAnalysis()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))

print('GaussianNB')
from sklearn.naive_bayes import GaussianNB
clf= GaussianNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_pred))