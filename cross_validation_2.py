#file name: cross_validation_2.py
"""Set up the dataset"""
import pandas as pd
df = pd.read_csv('Tunnel_1_4Linear8Sensors9ClassesCappedRange8Fast_10.txt', sep='\t')
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(df.loc[:,df.columns != "Class"], df.Class, random_state = 0)

"""Use cross-validation on the training set to find out the best value for k (in an arbitrary range of k)."""
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
shuffled = shuffle(pd.concat([train_X, train_y], axis=1))
dict = {k:np.mean(cross_val_score(KNeighborsClassifier(n_neighbors=k), shuffled.loc[:,shuffled.columns != "Class"], shuffled.Class, cv=10)) for k in range(1,7)}
max_k = max(dict, key=dict.get)
print(max_k)
"""
output:
1
"""
#We see that the highest accuracy is reached for k=1 (in the first line).
#Now we test how good 1NN performs on the testing data set.
knn = KNeighborsClassifier(n_neighbors=max_k)
knn.fit(train_X, train_y)
predictions = knn.predict(val_X)
accuracy = sum(predictions == val_y)/len(predictions)
print(accuracy)
"""
0.9524296675191816
"""