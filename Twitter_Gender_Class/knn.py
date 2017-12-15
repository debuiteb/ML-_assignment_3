import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, cross_val_score, cross_val_predict
import pandas
import preprocessing
import matplotlib.pyplot as plt


def knn_run(data_frame, k):
    set_size = 20000
    Y = data_frame["gender"]
    X = data_frame[
        ['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet',
         'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour',
         'g_link_colour', 'b_link_colour']]
    X = preprocessing.feature_select_custom(X, Y, k)
    [n,m] = X.shape
    print(Y.shape)

    clf = neighbors.KNeighborsClassifier(n_neighbors=int(n**0.5))
    scores = cross_val_score(clf, X, Y, cv=10)
    pred = cross_val_predict(clf, X, Y, cv=10)
    acc = accuracy_score(Y, pred)
    print(acc)

    sum_scores = sum(scores)
    num_scores = len(scores)
    print(scores)
    plt.plot(scores)
    plt.ylabel("score")
    plt.xlabel("fold number")
    plt.show()
    #print("average:", sum_scores / num_scores, " -- k:", k)

