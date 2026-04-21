import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
cv.imwrite('images/drawing.png',img)
cv.imshow('image',img)
cv.waitKey(0)

import cv2 as cv
import numpy as np

# Create a white canvas
img = np.ones((500, 500, 3), dtype="uint8") * 255

# Draw three colored circles (OpenCV colors)
cv.circle(img, (250,150), 80, (0,0,255), -1)    # Red circle
cv.circle(img, (150,350), 80, (0,255,0), -1)    # Green circle
cv.circle(img, (350,350), 80, (255,0,0), -1)    # Blue circle

# Draw inner white circles (to give ring effect)
cv.circle(img, (250,150), 35, (255,255,255), -1)
cv.circle(img, (150,350), 35, (255,255,255), -1)
cv.circle(img, (350,350), 35, (255,255,255), -1)

# Show image
cv.imshow("OpenCV Logo", img)

cv.waitKey(0)
cv.destroyAllWindows()




import cv2 as cv
import numpy as np

# Create white background
img = np.ones((500, 500, 3), dtype="uint8") * 255

# Draw OpenCV style elliptical shapes

# Red part
cv.ellipse(img, (250,150), (100,60), 0, 30, 330, (0,0,255), -1)

# Green part
cv.ellipse(img, (150,330), (100,60), 120, 30, 330, (0,255,0), -1)

# Blue part
cv.ellipse(img, (350,330), (100,60), 240, 30, 330, (255,0,0), -1)

# Inner white circles
cv.circle(img, (250,150), 35, (255,255,255), -1)
cv.circle(img, (150,330), 35, (255,255,255), -1)
cv.circle(img, (350,330), 35, (255,255,255), -1)

# Show image
cv.imshow("OpenCV Logo", img)

cv.waitKey(0)
cv.destroyAllWindows()


import cv2 as cv
import numpy as np

img = np.ones((400,400,3), dtype="uint8") * 255

cv.ellipse(img,(200,100),(70,70),0,40,320,(0,0,255),50)   # Red
cv.ellipse(img,(110,270),(70,70),0,40,320,(0,255,0),50)   # Green
cv.ellipse(img,(290,270),(70,70),0,40,320,(255,0,0),50)   # Blue

cv.imshow("OpenCV Logo", img)
cv.waitKey(0)
cv.destroyAllWindows()