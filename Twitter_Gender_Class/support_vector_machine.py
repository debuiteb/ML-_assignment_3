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
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def svm_run(data_frame,k):
    set_sizes = [100,500,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000,50000000,100000000]

    Y = data_frame["gender"]
    print("LIST: " , list(data_frame))
    X = data_frame[['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour', 'g_link_colour', 'b_link_colour']]

    X = preprocessing.feature_select_custom(X,Y,k)

    i=4

    #print("xshape" ,X.shape)
    #print("yshape" , Y.shape)

    clf = svm.LinearSVC()
    # new
    Y_fold = Y.head(int(set_sizes[i]))
    kf2 = KFold(n_splits=10)
    kf2.get_n_splits(Y_fold)
    X_fold2 = X.head(int(set_sizes[i]))
    #len(X)
    #X_fold2 = X[int(set_sizes[i]) , 1:len(X)]
    kf = KFold(n_splits=10)
    kf.get_n_splits(X_fold2)
    scores = cross_val_score(clf, X_fold2, Y_fold, cv=10)

    #print(scores)
    sum_scores = sum(scores)
    num_scores = len(scores)
    print("average:" , sum_scores/num_scores, " -- k:",k)

