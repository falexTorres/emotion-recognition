import cv2
import numpy as np
from PIL import Image
import sys

SIZE_FACE = 48

images_in = np.load('../fer_X_test.npy')
images_out = []

kernel_sharpen = np.array([[-1,-1,-1,-1,-1],
                           [-1,2,2,2,-1],
                           [-1,2,8,2,-1],
                           [-1,2,2,2,-1],
                           [-1,-1,-1,-1,-1]]) / 8.0

for i in range(0, images_in.shape[0]):
    #img = Image.fromarray(images_in[i]).convert('L')
    #img = np.array(img)[:, :].copy()
    #tmp = format_image(img)
    images_out.append(cv2.filter2D(images_in[i], -1, kernel_sharpen))

print "Total: " + str(len(images_out))
np.save('../fer_X_test_smooth.npy', images_out)
