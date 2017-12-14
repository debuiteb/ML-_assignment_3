#Main should just call the other files

import support_vector_machine as svm
import knn as knn
import preprocessing as preprocessing
import pandas

print('starting...')

#brian_path = "C:\\Users\\bboyd\\Documents\\college - 4th year\\Machine Learning\\Assignment 3\\twitter-user-gender-classification\\gender.csv"


file_path = ".//gender.csv"
data_frame = preprocessing.read_file(file_path) # pandas dataframe

data_frame = preprocessing.clean(data_frame) # data now has the correct amount of rows

data_frame.dropna()

for i in range(2,16):
    #    svm.svm_run(data_frame,i)
    knn.knn_run(data_frame,i)
#print(data_frame)


#a = svm.do()
#b = cluster.do()

#print("A: " , a)
#print("B: " , b)


