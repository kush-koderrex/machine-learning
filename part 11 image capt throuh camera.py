# import cv2
# img=cv2.imread("lena15.jpg")
#
#
#
#
# print(img)
# cv2.imshow("kush",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
import cv2
import mongo
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow("camera",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()