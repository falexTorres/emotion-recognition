# support vector machine
from sklearn import metrics
from sklearn.externals import joblib
from sklearn import datasets
import numpy as np

X = np.load('../data_store/quant_test_prediction.npy')
ys = np.load('../data_store/test_labels.npy')

labels = []

for y in ys:
        label = np.where(max(y)==y)
        labels.append(label[0][0])

samples = []
for x in X:
        sample = np.where(max(x)==x)
        samples.append(sample[0])

y = labels
X = samples
# fit svm model to data
model = joblib.load('top_svm.pkl')
print(model)
# make predictions
expected = y
predicted = model.predict(X)
np.save('svm_predictions', predicted)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
