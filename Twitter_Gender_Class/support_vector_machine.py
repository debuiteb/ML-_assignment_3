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

def get_plot_feature_scores(data_frame):
    set_sizes = [100, 500, 1000, 5000, 10000, 20050]

    Y = data_frame["gender"]
    print("y shape:", Y.shape)
    X = data_frame[
        ['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet',
         'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour',
         'g_link_colour', 'b_link_colour']]
    print("X shape", X.shape)

    score_averages = list()
    score_averages = [0] * 12
    print(score_averages)
    ind = 0
    for k in range(2,5): ## change back
        X_with_k_features = preprocessing.feature_select_custom(X, Y, k)
        print(X_with_k_features.shape)

        clf = svm.LinearSVC()

        scores = cross_val_score(clf, X_with_k_features, Y, cv=10)
        print(scores)

        sum_scores = sum(scores)
        num_scores = len(scores)
        average = sum_scores / num_scores

        score_averages[ind] = average
        ind = ind + 1

        #for a in range(len(scores)):
        #    score_averages[a] = score_averages + scores[a]

        #for a in range(len(scores)):
        #   score_averages[a] = score_averages/10



        print(("------ ------- ---------"))

    return score_averages



def svm_run(data_frame,k):
    set_sizes = [100,500,1000,5000,10000,22000]

    Y = data_frame["gender"]
    #print("LIST: " , list(data_frame))
    X = data_frame[['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour', 'g_link_colour', 'b_link_colour']]

    X2 = data_frame[['link_in bio', 'hash_in_tweet', 'at_in_tweet']]

    X = preprocessing.feature_select_custom(X,Y,k)
    #print('list: ' ,list(X))

    i=5

    #print("xshape" ,X.shape)
    #print("yshape" , Y.shape)

    clf = svm.LinearSVC()

    print("aaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhh")

    scores = cross_val_score(clf, X, Y, cv=10)

    print("scores:", scores)
    sum_scores = sum(scores)
    num_scores = len(scores)
    print("average:" , sum_scores/num_scores, " -- k:",k)

    print(("------ ------- ---------"))



def svm_run5(data_frame,k):
    from sklearn.metrics import classification_report
    set_sizes = [100,500,1000,5000, 20000]
    Y = data_frame["gender"]
    X = data_frame[['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour', 'g_link_colour', 'b_link_colour']]
    i=4

    X_train = data_frame.head(int(set_sizes[i] * .7))
    y_train = X_train.gender
    X_train = X_train[['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour', 'g_link_colour', 'b_link_colour']]
    X_test = data_frame.tail(int(set_sizes[i] * .3))
    y_test = X_test.gender
    X_test = X_test[['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour', 'g_link_colour', 'b_link_colour']]
    clf = svm.LinearSVC()
    y_true=y_test
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    target_names = ['man', 'woman', 'brand']
    print(classification_report(y_true, y_pred, target_names=target_names))