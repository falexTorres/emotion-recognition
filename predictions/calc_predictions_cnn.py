import numpy as np

preds = np.load('../data_store/testPrediction.npy')
labels = np.load('../data_store/test_labels.npy')
total = 0.0
print preds[0:5]
print labels[0:5]
for i in xrange(labels.shape[0]):
        label = np.where(labels[i]==max(labels[i]))[0][0]
        pred = np.where(preds[i]==max(preds[i]))[0][0]
        #v = labels[i][0] == np.where(preds[i]==max(preds[i]))[0][0]
        #pred = np.where(preds[i]==max(preds[i]))[0][0]
        if pred == label:
                total += 1

total = (total / preds.shape[0]) * 100
print "\naccuracy: " + str(total)[0:6] + "%\n\n"
