

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('images/hello.png')
crop_img = image[50:80, 50:200]
cv.imshow('Cropped Image', crop_img)
flipped = cv.flip(image, 1)
cv.imshow('Flipped Image', flipped)
flipped_vertical = cv.flip(image, 0)
cv.imshow('Flipped Vertical Image', flipped_vertical)
flipped_both = cv.flip(image, -1)
cv.imshow('Flipped Both Image', flipped_both)
# gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
if image is not None:

    resized_image = cv.resize(image, (600, 400))
    cv.imshow('Original Image',image)
    cv.imshow('Resized Image', resized_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    h, w = resized_image.shape[:2]
    c = resized_image.shape[2] if len(resized_image.shape) > 2 else 1
    print('Height: {}, Width: {}, Channels: {}'.format(h, w, c))
else:    
    print('Could not read the image.')

img = cv.imread('images/chessboard.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int8(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()

# ==========================================================================================================================================================
import numpy as np
import cv2 as cv
# it detects corners in an image using the Harris Corner Detection algorithm. It reads an image, 
# converts it to grayscale, and applies the
filename = 'images/chessboard.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv.imshow('dst',img)
cv.waitKey(0)
cv.destroyAllWindows()

# ==========================================================================================================================================================

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/chessboard.jpg', cv.IMREAD_GRAYSCALE)

# Initiate FAST detector
star = cv.xfeatures2d.StarDetector_create()

# Initiate BRIEF extractor
brief = cv.xfeatures2d.BriefDescriptorExtractor_create()

# find the keypoints with STAR
kp = star.detect(img,None)

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print( brief.descriptorSize() )
print( des.shape )
cv.drawKeypoints(img, kp, img, color=(255,0,0))
plt.imshow(img),plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

#==========================================================================================================================================================
# this code snippet demonstrates how to read an image, detect chessboard corners, and display the original and rotated
# images using OpenCV. It also prints the height, width, and center of the image.
# it is known as callibration of camera using chessboard pattern. It is used to find the intrinsic and extrinsic parameters of the camera.
import cv2 as cv

image= cv.imread('images/chessboard.jpg')

if image is None:
    print('Could not read the image.')
else:
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (7,7), None)

    if ret == True:
        cv.drawChessboardCorners(image, (7,7), corners, ret)
        cv.imshow('Chessboard Corners', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print('Chessboard corners not found.')

    

    (h, w) = image.shape[:2]
    print('Height: {}, Width: {}'.format(h, w))
    center= (w // 2, h // 2)
    print('Center: {}'.format(center))
    M= cv.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))
    cv.imshow('Original Image', image)
    cv.imshow('Rotated Image', rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()

# =========================================================================================================================================================
import numpy as np
import cv2 as cv
import glob

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('images/open.jpg')

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
    
    else:
        print('Chessboard corners not found in image: {}'.format(fname))

cv.destroyAllWindows()
# =========================================================================================================================================================


import numpy as np
import cv2 as cv
import glob

# Load previously saved data
with np.load('calibration_data.npz') as data:
    mtx = data['mtx']
    dist = data['dist']

    


def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel().astype("int32"))
    imgpts = imgpts.astype("int32")
    img = cv.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    img = cv.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    img = cv.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img


# def draw(img, corners, imgpts):
#     imgpts = np.int32(imgpts).reshape(-1,2)

#     # draw ground floor in green
#     img = cv.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)

#     # draw pillars in blue color
#     for i,j in zip(range(4),range(4,8)):
#         img = cv.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)

#     # draw top layer in red color
#     img = cv.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

#     return img

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)
# axis_cube= np.float32([[0,0,0], [3,0,0], [3,3,0], [0,3,0],
#                         [0,0,-3], [3,0,-3], [3,3,-3], [0,3,-3]])

for fname in glob.glob('images/chessboard.jpg'):
    img = cv.imread(fname)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (7,6),None)

    if ret == True:
        corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

        # Find the rotation and translation vectors.
        ret,rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)

        # project 3D points to image plane
        imgpts, jac = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)

        img = draw(img,corners2,imgpts)
        cv.imshow('img',img)
        k = cv.waitKey(0) & 0xFF
        if k == ord('s'):
            cv.imwrite('images/' + fname[:6] + '.png', img)

cv.destroyAllWindows()