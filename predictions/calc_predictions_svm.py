import numpy as np

preds = np.load('../svm/svm_predictions.npy')
labels = np.load('../data_store/test_labels.npy')
total = 0.0
for i in xrange(labels.shape[0]):
        pred = preds[i]
        label = np.where(labels[i]==max(labels[i]))[0][0]
        #v = labels[i][0] == np.where(preds[i]==max(preds[i]))[0][0]
        #pred = np.where(preds[i]==max(preds[i]))[0][0]
        if pred == label:
                total += 1

total = (total / preds.shape[0]) * 100
print "\naccuracy: " + str(total)[0:6] + "%\n\n"
