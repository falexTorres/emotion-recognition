import numpy as np
import matplotlib.pyplot as plt

n = 1234

X_fdt = np.load('../fer_X_test_smooth.npy')
#y = np.load('../fer_y_train.npy')
X = np.load('../fer_X_test.npy')
plt.subplot(1,2,1)
plt.imshow(X[n], cmap='gray')
plt.xlabel("without")
plt.subplot(1,2,2)
plt.imshow(X_fdt[n], cmap='gray')
plt.xlabel("with")
plt.imshow(X_fdt[n], cmap='gray')
plt.show()
