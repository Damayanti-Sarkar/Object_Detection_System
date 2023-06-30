# -*- coding: utf-8 -*-
"""Object Detection System .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YcVtMbaIR1jsMrLufvlVKAQFXBfi29Gn
"""

# Importing all the required libraries and packages for the object detection
import cv2
from matplotlib import pyplot as plt

# Opening image
img = cv2.imread("/content/test_image.jpg")

# Loading the classifier
classifier_data = cv2.CascadeClassifier('/content/classifier_data.xml')

# We will use Opencv and convert the image as grayscale and RGB
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Next, we use minSize to not mis-detect the object
found = classifier_data.detectMultiScale(img_gray, minSize =(20, 20))

# We get results only if the object is detected or else no result
amount_found = len(found)
if amount_found != 0:

  # We try to detect more than one particular object
  for (x, y, width, height) in found:

    # We draw a green rectangle around every recognized object
	  cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)

# Creates the environment of the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()