# import cv2 as cv
# import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )

# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img,(x,y),100,(255,0,0),-1)

# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)

# while(1):
#     cv.imshow('image',img)
#     if cv.waitKey(20) == ord('q'): 
#         break
# cv.destroyAllWindows()


# ===========================================================================================
# import numpy as np
# import cv2 as cv

# drawing = False # true if mouse is pressed
# mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# ix,iy = -1,-1

# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode

#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y

#     elif event == cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
#                 cv.circle(img,(x,y),2,(0,0,255),-1)

#     elif event == cv.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#         else:
#             cv.circle(img,(x,y),2,(0,0,255),-1)

# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)

# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == ord('q'):
#         break

# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )

# # mouse callback function
# def draw_rectangle(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.rectangle(img,(x,y),(x+100,y+100),(255,0,0),1)

# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_rectangle)

# while(1):
#     cv.imshow('image',img)
#     if cv.waitKey(20) == ord('q'): 
#         break
# cv.destroyAllWindows()


# Trackbars are created using the createTrackbar() function. The parameters of this function are the trackbar name, 
# the window name, the default value, the maximum value and the callback function that is called every time the 
# trackbar value changes. The callback function should have the following form:

import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)

cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)

# 0xFF is used to mask the higher bits of the return value of waitKey() and get only the last 8 bits, which represent 
# the ASCII value of the key pressed. This is necessary because waitKey() can return a value that includes additional 
# information about the key event, such as modifier keys (Shift, Ctrl, Alt) or special keys (function keys, arrow keys).
# By applying the bitwise AND operation with 0xFF, we ensure that we only get the relevant key code for comparison. 
# For example, if the user presses the 'q' key, waitKey() might return a value like 0x00000071, and by masking it 
# with 0xFF, we get 0x71, which corresponds to the ASCII value of 'q'. This allows us to check if the 'q' key was 
# pressed without being affected by any additional information in the return value.

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF # Wait for 1 ms and check if 'q' key is pressed
    if k == 27: # Esc key to exit
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()