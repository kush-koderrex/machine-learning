# import cv2
# import numpy as np
# img=cv2.imread("lena15.jpg")
# print(img.shape)
# cv2.imshow("RGB",img)
#
#
# print("Height",int(img.shape[0]))
# print("Width",int(img.shape[1]))
# print("Depth",int(img.shape[2]))
# print("Dtype",str(img.dtype))
#
# cv2.waitKey(0)
#
# cv2.imwrite("output.jpg",img)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# img=cv2.imread("lena15.jpg")
#
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,img_bw=cv2.threshold(gray,126,255,cv2.THRESH_BINARY)
# print(gray.shape)
# cv2.imshow("Gray",gray)
# print(img.shape)
# cv2.imshow("binary",img_bw)
# cv2.imshow("RGB",img)
# print(img_bw.shape)
# print(ret)
#
#
# cv2.waitKey(0)
#
# cv2.imwrite("output.jpg",img)
# cv2.destroyAllWindows()


import cv2
import numpy as np
img=cv2.imread("lena15.jpg")
print(img.shape)
B,G,R=cv2.split(img)
cv2.imshow("RGB",img)
cv2.waitKey(0)
cv2.imshow("RED",R)
cv2.waitKey(0)
cv2.imshow("green",G)
cv2.waitKey(0)
cv2.imshow("Blue",B)
merge=cv2.merge([B,G,R])
cv2.imshow("Merge",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()





