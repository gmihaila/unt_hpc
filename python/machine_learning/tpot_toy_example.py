import numpy as np
import pandas as pd

from tpot import TPOTClassifier, TPOTRegressor

#scikit-learn package (https://pypi.org/project/scikit-learn)
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc, roc_auc_score
from sklearn.model_selection import train_test_split #TAKES NUMPY OR DATA FRAME!!
from sklearn.metrics.scorer import make_scorer
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

import matplotlib.pyplot as plt

import itertools

#Split train and test set.
RANDOM_STATE = 123

# Parse data


path_file = 'pima-indians-diabetes.data.csv'
df = pd.read_csv(path_file, header=None)
x_df = df.drop(df.columns[8],axis=1)
y_df = df[df.columns[8]]
print("Head:")
print(df.head())

X, X_test, y, y_test = train_test_split(x_df, y_df, train_size=0.85, random_state=42)
X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.85, random_state=RANDOM_STATE)


print("\nTrain: ", X_train.shape[0])
print("Validation: ",X_validation.shape[0])
print("Test: ",X_test.shape[0])

tpot = None
del tpot

tpot = TPOTClassifier(
                      verbosity=3,
                      scoring="accuracy",
                      random_state=23,
                      periodic_checkpoint_folder="tpot_mnst1.txt",
                      generations=10,
                      n_jobs=-1,
                      population_size=100
                      )

# with joblib.parallel_backend("dask"):
tpot.fit(X_train, y_train)

tpot.score(X_test, y_test)

# Winning pipelines
print(tpot.fitted_pipeline_)

# copy file
# tpot.export('tpot_mnist_pipeline.py')

# Get predictions
y_predict = tpot.predict(X_test)

# Probability of malignant tissue produced by the model
y_prob = [probs[1] for probs in tpot.predict_proba(X_test)]


#Accuracy on test set
print("Test accuracy: %s\n"%(accuracy_score(y_test, y_predict).round(2)))

# Confusion matrix test set
conf_mat = pd.DataFrame(
    confusion_matrix(y_test, y_predict),
    columns=['Predicted NO', 'Predicted YES'],
    index=['Actual NO', 'Actual YES']
)
print(conf_mat)


# Compute area under the curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)


# only use if you can visualise

#Set default figure size
# plt.rcParams['figure.figsize'] = (8,8)
#
# # Plot ROC curve
# plt.figure()
# lw = 2
# plt.plot(fpr, tpr, color='darkorange',
#          lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
# plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title("Title")
# plt.legend(loc="lower right")
# plt.show()
