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

def seventyThirty():
    file_path = ".//gender.csv"
    data_frame = preprocessing.read_file(file_path) # pandas dataframe
    set_sizes = [100,500,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000,50000000,100000000]

    data_frame = preprocessing.clean(data_frame) # data now has the correct amount of rows
    Y=data_frame["gender"]
    X=data_frame["created","description","fav_number", "link_color", "sidebar_color", "text", "tweet_count", "tweet_created", "hash_in_bio", "at_in_bio", "link_in_bio", "hash_in_bio","at_in_bio", "link_in_bio","hash_in_tweet", "at_in_tweet", "link_in_tweet"]
    i=4
    x_train = X.head(int(set_sizes[i]*0.7))
    x_test = X.tail(int(set_sizes[i]*0.3))

    y_train = Y.head(int(set_sizes[i]*0.7))
    y_test = Y.tail(int(set_sizes[i]*0.3))

    clf = svm.SVC()
    clf.fit(x_train,y_train)
    results=clf.predict(x_test)

