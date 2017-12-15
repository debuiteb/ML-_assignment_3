import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import KFold, cross_val_score
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
    #TOTRY Neighbours should be n^0.5, where n is the number of samples
    #for i in range(2, 15):
    # print("Neighbour number %i"%(i))
    clf = neighbors.KNeighborsClassifier(n_neighbors=int(n**0.5))
    Y_fold = Y.head(int(set_size))
    kf2 = KFold(n_splits=10)
    kf2.get_n_splits(Y_fold)
    X_fold2 = X.head(int(set_size))
    kf = KFold(n_splits=10)
    kf.get_n_splits(X_fold2)
    scores = cross_val_score(clf, X_fold2, Y_fold, cv=10)
    sum_scores = sum(scores)
    num_scores = len(scores)
    print(scores)
    plt.plot(scores)
    plt.ylabel("score")
    plt.xlabel("fold number")
    plt.show()
    #print("average:", sum_scores / num_scores, " -- k:", k)

