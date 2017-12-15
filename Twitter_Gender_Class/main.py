#Main should just call the other files

import support_vector_machine as svm
import knn as knn
import preprocessing as preprocessing
import pandas
import matplotlib.pyplot as plt
import CSV_creator as csv_maker
from pylab import *


print('starting...')

#brian_path = "C:\\Users\\bboyd\\Documents\\college - 4th year\\Machine Learning\\Assignment 3\\twitter-user-gender-classification\\gender.csv"


file_path = csv_maker.read()

data_frame = preprocessing.read_file(file_path) # pandas dataframe

data_frame = preprocessing.clean(data_frame) # data now has the correct amount of rows

data_frame.dropna()

#for i in range(2,16):
    #svm.svm_run(data_frame,i)
    #knn.knn_run(data_frame,i)
#print(data_frame)


'''
score_averages = svm.get_plot_feature_scores(data_frame)

plt.plot(score_averages)
plt.ylabel("score averages")
plt.xlabel("number of features")


plt.show()
'''

score_averages = knn.get_plot_feature_scores(data_frame)

plt.plot(score_averages)
plt.ylabel("score averages")
plt.xlabel("number of features")


plt.show()

#a = svm.do()
#b = cluster.do()

#print("A: " , a)
#print("B: " , b)


