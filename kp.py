import cv2
import numpy as np
import matplotlib.pyplot as plt
img = np.zeros((512,512,3))
cv2.line(img,(0,0),(511,511),(255,0,0),100)
for i in range(img.shape[0]):
    for j in range (img.shape[1]):
        print(img[i,j,0])

plt.imshow(img)
plt.show()
