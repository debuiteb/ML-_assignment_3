import nltk
from nltk import word_tokenize
import preprocessing as preprocessing


import numpy as np
import pandas
import csv
import itertools
from sklearn.svm import SVR
from datetime import datetime
from dateutil.parser import parse
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.regression import mean_squared_error,r2_score
from sklearn.model_selection import KFold, GridSearchCV,cross_val_score
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics.classification import accuracy_score,precision_score
from sklearn.metrics import recall_score


def seventyThirty():
    file_path = "gender.csv"
	data_frame = preprocessing.read_file(file_path) # pandas dataframe
	set_sizes = [100,500,1000,5000,10000,20000,100000,500000,1000000,5000000,10000000,50000000,100000000]
	data_frame = preprocessing.clean(data_frame) # data now has the correct amount of rows
	#Y=data_frame["gender"]
	#X=data_frame["created","description","fav_number", "link_color", "sidebar_color", "text", "tweet_count", "tweet_created", "hash_in_bio", "at_in_bio", "link_in_bio", "hash_in_bio","at_in_bio", "link_in_bio","hash_in_tweet", "at_in_tweet", "link_in_tweet"]
	#X=data_frame['created', 'description', 'fav_number', 'link_color', 'sidebar_color', 'text', 'tweet_count', 'tweet_created', 'hash_in_bio', 'at_in_bio', 'link_in_bio', 'hash_in_bio', 'at_in_bio', 'link_in_bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet']
	#X=data_frame["created","text"]
	i=5
	data_frame=data_frame.dropna()
	clf = svm.LinearSVC()

	#data_frame.head(100)

	Y = data_frame["gender"]
	X = data_frame[["fav_number", "tweet_count", "hash_in_bio", "at_in_bio", "link_in_bio","hash_in_tweet", "at_in_tweet", "link_in_tweet", "account_age"]]

	X_fold = Y.head(int(set_sizes[i]))
	kf2 = KFold(n_splits=10)
	kf2.get_n_splits(X_fold)
	#Y_fold=X_fold



	X_fold2 = X.head(int(set_sizes[i]))
	kf = KFold(n_splits=10)
	kf.get_n_splits(X_fold2)
	#clf.fit(x_train,y_train)
	#results=clf.predict(x_test)
	#X_train, X_test, y_train, y_test = train_test_split(
	#    iris.data, iris.target, test_size=0.4, random_state=0)

	#X_train.shape, y_train.shape

	#X_test.shape, y_test.shape


	#clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
	#clf.score(X_test, y_test) 
	#X_fold.head(1000)
	#clf.fit(X_fold2,X_fold)



	#predicted = cross_val_predict(clf, X, Y, cv=10)
	#clf = svm.SVC(kernel='linear', C=1)
	scores = cross_val_score(clf, X_fold2, X_fold, cv=10)

	#from sklearn.model_selection import cross_validate
	#scoring = ['created', 'description']
	#clf = svm.SVC(kernel='linear', C=1, random_state=0)
	#scores = cross_val_score(clf, data_frame["created"], Y, scoring=scoring,cv=5)
	#sorted(scores.keys())

	#scores['test_recall_macro']
	print(scores)



