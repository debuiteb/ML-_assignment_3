import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas



def train():
    X_train, X_test, y_train, y_test = model_selection.train_test_split()

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train,y_train)

    accuaracy = clf.score(X_test,y_test)

    print("acc: " , accuaracy)

    return 0



def predict():

    return 0