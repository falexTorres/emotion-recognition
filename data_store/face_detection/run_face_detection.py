import cv2
import numpy as np
from PIL import Image
import sys

cascade_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
SIZE_FACE = 48
BORDER_SIZE = 55
scale_factor = 1.01
min_neighbors = 3

def format_image(image):
  tmp = image  
  if len(image.shape) > 2 and image.shape[2] == 3:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
    image = cv2.imdecode(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)
  gray_border = np.zeros((BORDER_SIZE, BORDER_SIZE), np.uint8)
  gray_border[:,:] = 200
  gray_border[((BORDER_SIZE / 2) - (SIZE_FACE/2)):((BORDER_SIZE/2)+(SIZE_FACE/2)), ((BORDER_SIZE/2)-(SIZE_FACE/2)):((BORDER_SIZE/2)+(SIZE_FACE/2))] = image
  image = gray_border
  
  faces = cascade_classifier.detectMultiScale(
    image,
    scaleFactor = scale_factor,
    minNeighbors = min_neighbors
  )
  
  # None is we don't found an image
  if not len(faces) > 0:
    print "No face found"
    #sys.exit()
    return tmp
  max_area_face = faces[0]
  for face in faces:
    if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
      max_area_face = face
  # Chop image to face
  face = max_area_face
  image = image[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]
  # Resize image to network size
  try:
    image = cv2.resize(image, (SIZE_FACE, SIZE_FACE), interpolation = cv2.INTER_CUBIC) / 255.
  except Exception:
    print("[+] Problem during resize")
    return None
  print image.shape
  return image

images_in = np.load('../fer_X_train_smooth.npy')
images_out = []
missed = []

for i in range(0, images_in.shape[0]):
    tmp = images_in[i]
    img = Image.fromarray(images_in[i]).convert('RGB')
    img = np.array(img)[:, :, ::-1].copy()
    tmp1 = format_image(img)
    if np.array_equal(tmp1, img):
      images_out.append(tmp)
      missed.append(tmp)
    else:
      images_out.append(tmp1)

print "Total: " + str(len(images_out))
print "Missed: " + str(len(missed))
np.save('../fer_X_train_smooth_fdt.npy', images_out)
np.save('../fer_X_train_smooth_fdt_missed.npy', missed)

f = open("fdt_results.txt", "a")
write_this = "scale factor = " + str(scale_factor) + "\nmin neighbors = " + str(min_neighbors) + "\nborder size = " + str(BORDER_SIZE) + "\nmissed = " + str(len(missed)) + "\n\n"
f.write(write_this)
f.close()
