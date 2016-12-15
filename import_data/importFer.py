import numpy as np
import matplotlib.pyplot as plt
import time

## 48x48 pixel grayscale images ##

## 3 columns in csv- emotion (label), pixels, and usage (training or test) ##

# 0 = angry
# 1 = disgust
# 2 = fear
# 3 = happy
# 4 = sad
# 5 = surprise
# 6 = neutral

start_time = time.time()

p = 0 # pixel counter
l = 0 # line counter or image counter
t = 0 # test line counter or image counter
y_train = np.array([[]])
X_train = np.zeros((28709, 48, 48))
y_test = np.array([[]])
X_test = np.zeros((3589, 48, 48))

with open('fer2013.csv') as f:
  next(f)
  for line in f:
    csv_columns = line.split(',')
    pixels = csv_columns[1].split(' ')
    data_type = csv_columns[2].strip()
    label = csv_columns[0]
    #label = np.zeros((1, 7))

    #if csv_columns[0] == 0:
      #label[0][0] = 1
    #elif csv_columns[0] == 1:
      #label[0][1] = 1
    #elif csv_columns[0] == 2:
      #label[0][2] = 1
    #elif csv_columns[0] == 3:
      #label[0][3] = 1
    #elif csv_columns[0] == 4:
      #label[0][4] = 1
    #elif csv_columns[0] == 5:
      #label[0][5] = 1
    #else:
      #label[0][6] = 1

    if data_type == "Training":     
      y_train = np.append(y_train, int(label))
      for i in range(48):
        for j in range(48):
          X_train[l][i][j] = pixels[p]
          p += 1
      p = 0
      l += 1
 #   elif "Test" in data_type:
    elif "PrivateTest" == data_type:
      y_test = np.append(y_test, int(label))
      for i in range(48):
        for j in range(48):         
          X_test[t][i][j] = pixels[p]
          p += 1
      p = 0
      t += 1

## reshape labels ##
#y_train = y_train.reshape(28709, 7)
#y_test = y_test.reshape(3589, 7)
y_train = y_train.reshape(28709, 1)
y_test = y_test.reshape(3589, 1)

## persist data on disk ##
np.save("../fer_X_train", X_train)
np.save("../fer_y_train", y_train)
np.save("../fer_X_test", X_test)
np.save("../fer_y_test", y_test)

print "--- %s seconds ---" % (time.time() - start_time)
#plt.xlabel(int(labels[0]))
plt.imshow(X_test[380], cmap='gray')
plt.show()
