# import cv2
# import numpy as np
# import pandas
#
# img=np.zeros((512,512),np.uint8)
# img2=255+(np.zeros((512,512),np.uint8))
# img3=(np.ones((512,512),np.uint8))
#
# cv2.imshow("black",img)
# cv2.imshow("white",img2)
# cv2.imshow("white",img3)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#############################################################################



import cv2
import numpy as np
window="Win"
img=np.zeros((512,512),np.uint8)



#
# # cv2.line(img,(0,0),(511,511),(155,170,55),50)
# cv2.rectangle(img,(100,100),(350,250),(155,170,55),5)
# cv2.circle(img,(300,300),(100),(255),-5)
# cv2.putText(img,"kush",org=(55,290),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=2,color=(100,170,50),thickness=4)
cv2.namedWindow(window)

def draw(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)



cv2.setMouseCallback(window,onMouse=draw)
while True:
    cv2.imshow(window,img)
    if cv2.waitKey(20)==27:
        break


# cv2.imshow("line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()