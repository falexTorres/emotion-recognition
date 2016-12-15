import numpy as np
import matplotlib.pyplot as plt

n = 4000

X_fdt = np.load('../fer_X_train_fdt.npy')
y = np.load('../fer_y_train.npy')
X = np.load('../fer_X_train.npy')
plt.xlabel("without")
plt.imshow(X[n], cmap='gray')
plt.show()
plt.xlabel("with")
plt.imshow(X_fdt[n], cmap='gray')
plt.show()
