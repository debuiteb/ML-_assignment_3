#Main should just call the other files

import support_vector_machine as svm
import cluster as cluster
import preprocessing as preprocessing
import pandas

print('starting...')

#brian_path = "C:\\Users\\bboyd\\Documents\\college - 4th year\\Machine Learning\\Assignment 3\\twitter-user-gender-classification\\gender.csv"


file_path = ".//gender.csv"
data_frame = preprocessing.read_file(file_path) # pandas dataframe

data_frame = preprocessing.clean(data_frame)

print(data_frame)

#a = svm.do()
#b = cluster.do()

#print("A: " , a)
#print("B: " , b)


