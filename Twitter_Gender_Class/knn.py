from sklearn import preprocessing, neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, cross_val_score, cross_val_predict
import preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report



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


def get_plot_feature_scores(data_frame):
    set_sizes = [100, 500, 1000, 5000, 10000, 20050]

    Y = data_frame["gender"]
    print("y shape:", Y.shape)
    X = data_frame[
        ['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet',
         'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour', 'r_link_colour',
         'g_link_colour', 'b_link_colour']]
    print("X shape", X.shape)

    score_averages = [0] * 12
    print(score_averages)
    ind = 0
    for k in range(2,14): ## change back
        X_with_k_features = preprocessing.feature_select_custom(X, Y, k)
        print(X_with_k_features.shape)

        clf = neighbors.KNeighborsClassifier(n_neighbors=int(X_with_k_features.shape[0] ** 0.5))

        scores = cross_val_score(clf, X_with_k_features, Y, cv=10)
        print(scores)

        sum_scores = sum(scores)
        num_scores = len(scores)
        average = sum_scores / num_scores

        score_averages[ind] = average
        ind = ind + 1

        print(("------ ------- ---------"))

    return score_averages


def knn_report(data_frame):
    set_sizes = [100, 500, 1000, 5000, 20000]
    Y = data_frame["gender"]
    X = data_frame[
        ['fav_number', 'tweet_count', 'hash_in bio', 'at_in bio', 'link_in bio', 'hash_in_tweet', 'at_in_tweet',
         'link_in_tweet', 'account_age', 'r_sidebar_colour', 'g_sidebar_colour', 'b_sidebar_colour',
         'r_link_colour', 'g_link_colour', 'b_link_colour']]
    i = 4

    clf = neighbors.KNeighborsClassifier(n_neighbors=int(X.shape[0] ** 0.5))
    y_true = Y

    y_pred = cross_val_predict(clf, X, Y, cv=10)
    target_names = ['man', 'woman', 'brand']
    print(classification_report(y_true, y_pred, target_names=target_names))
