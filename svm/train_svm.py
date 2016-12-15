# support vector machine
from sklearn import metrics
from sklearn.svm import LinearSVC, SVC
from sklearn.externals import joblib
from sklearn import datasets
import numpy as np
import time

start = time.time()

X = np.load('../data_store/quant_train_prediction.npy')
ys = np.load('../data_store/train_labels.npy')

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
model = SVC(C=0.425, gamma=0.425, decision_function_shape='ovr', class_weight='balanced', random_state=7) # current best C = 0.1 gamma = 0.1
model = model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

joblib.dump(model, 'top_svm.pkl')

stop = time.time()
print "\n\nexecution time: %.2f seconds\n" % (stop - start)
