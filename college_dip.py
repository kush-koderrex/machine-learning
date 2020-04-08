import cv2
import numpy as np
from matplotlibimport pyplot as plt
img=cv2.imread("lena15.jpg")
ret,image=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
plt.imshow(image)
print(plt.show())


ret,image=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)

cv2.imshow("kush",image)

cv2.waitKey(0)
cv2.destroyAllWindows()