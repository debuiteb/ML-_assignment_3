#Main should just call the other files

import preprocessing
import support_vector_machine as svm
import cluster as cluster
import preprocessing as preprocessing
import pandas

data = preprocessing.readFile("../gender-classifier-DFE-791531.csv")

'''
filepath = "" #path to csv file
data_frame = preprocessing.readFile() # pandas dataframe

data_frame = preprocessing.clean(data_frame)

a = svm.do()
b = cluster.do()

print("A: " , a)
print("B: " , b)

print('starting...')'''
