#Main should just call the other files

import support_vector_machine as svm
import knn as knn
import preprocessing as preprocessing
import CSV_creator as csv_maker
from pylab import *

print('starting...')

file_path = csv_maker.read()

data_frame = preprocessing.read_file(file_path)
data_frame = preprocessing.clean(data_frame)


score_averages = svm.get_plot_feature_scores(data_frame)

plt.plot(score_averages)
plt.ylabel("score averages")
plt.xlabel("number of features")

plt.show()

score_averages = knn.get_plot_feature_scores(data_frame)

plt.plot(score_averages)
plt.ylabel("score averages")
plt.xlabel("number of features")

plt.show()
