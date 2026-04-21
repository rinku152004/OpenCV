# import numpy as np
# import cv2 as cv

# img = cv.imread('images/boy1.jpg')
# mask = cv.imread('images/boy2.jpg', cv.IMREAD_GRAYSCALE)

# dst = cv.inpaint(img,mask,3,cv.INPAINT_TELEA)

# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('images/roi.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

# ====================================================================================================================
# OpenCV provides four variations of this technique.
# cv.fastNlMeansDenoising() - works with a single grayscale images
# cv.fastNlMeansDenoisingColored() - works with a color image.
# cv.fastNlMeansDenoisingMulti() - works with image sequence captured in short period of time (grayscale images)
# cv.fastNlMeansDenoisingColoredMulti() - same as above, but for color images.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/roi.jpg')

dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()

# ======================================================================================================================
cap = cv.VideoCapture(0)

# create a list of first 5 frames
img = [cap.read()[1] for i in range(5)]

# convert all to grayscale
gray = [cv.cvtColor(i, cv.COLOR_BGR2RGB) for i in img]

# convert all to float64
gray = [np.float64(i) for i in gray]

# create a noise of variance 25
noise = np.random.randn(*gray[1].shape)*10

# Add this noise to images
noisy = [i+noise for i in gray]

# Convert back to uint8
noisy = [np.uint8(np.clip(i,0,255)) for i in noisy]

# Denoise 3rd frame considering all the 5 frames
dst = cv.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)

image=cv.imwrite("images/rinkuu.jpg",dst)
print("image saved successfully....")

plt.subplot(131),plt.imshow(gray[2],'gray')
plt.subplot(132),plt.imshow(noisy[2],'gray')
plt.subplot(133),plt.imshow(dst,'gray')
plt.show()
cv.waitKey(0)

ima=cv.imread("images/rinkuu.jpg",cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges=cv.Canny(ima,100,200)
plt.subplot(121),plt.imshow(ima,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
# ===========================================================================================================================

import cv2 as cv
import sys
import numpy as np

img = cv.imread("images/ml.jpg")
mblur = cv.medianBlur(img,3)
cv.imshow("Original Image", img)
cv.imshow("Median Blurred Image", mblur)
cv.waitKey(0)

# Define a simple sharpening kernel
kernel = np.array([[0,-1,0],
                   [-1, 5,-1],
                   [0,-1,0]])

sharp = cv.filter2D(img, -1, kernel)
cv.imshow("Original Image", img)
cv.imshow("Sharpened Image", sharp)
cv.waitKey(0)

blur = cv.GaussianBlur(img,(5,5),3)
cv.imshow("Original Image", img)
cv.imshow("Blurred Image", blur)
cv.waitKey(0)

if img is None:
    sys.exit("Could not read the image.")


cv.namedWindow("Display window", cv.WINDOW_NORMAL)
cv.resizeWindow("Display window", 800, 600)  # Set the window size to 800x600
# img = cv.resize(img, (800, 600))

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("images/gray.png", img)
    print("Image saved as gray.png")



# # ==========================================================================================================================================================
# import numpy as np
# import cv2 as cv

# # this code demonstrates how to use the Harris Corner Detection algorithm to identify corners in an 
# # image. It reads an image, converts it to grayscale, and applies the cornerHarris function to detect
# # corners based on the intensity changes in the image. The detected corners are then dilated for 
# # better visibility, and a threshold is applied to mark the corners on the original image. Finally,
# #  the result is displayed using OpenCV.

# img = cv.imread('images/hello.png')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# gray = np.float32(gray)
# dst = cv.cornerHarris(gray,2,3,0.04)

# #result is dilated for marking the corners, not important
# dst = cv.dilate(dst,None)

# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.01*dst.max()]=[0,0,255]

# cv.imshow('dst',img)
# if cv.waitKey(0) & 0xff == 27:
#     cv.destroyAllWindows()

# # ==========================================================================================================================================================
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# # this code demonstrates how to use the GrabCut algorithm for image segmentation. It reads an image, 
# # initializes a mask and background/foreground models, and defines a rectangular region of interest 
# # (ROI) for the algorithm. The GrabCut function is then called to segment the image based on the 
# # defined ROI. Finally, the segmented image is displayed using Matplotlib. The algorithm iteratively
# #  refines the segmentation by classifying pixels as foreground or background based on color and 
# # texture information.
# img = cv.imread('images/roi.jpg')
# assert img is not None, "file could not be read, check with os.path.exists()"
# mask = np.zeros(img.shape[:2],np.uint8)

# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)

# rect = (50,50,450,290)
# cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# img = img*mask2[:,:,np.newaxis]

# plt.imshow(img),plt.colorbar(),plt.show()
# # ==========================================================================================================================================================

# import numpy as np
# import cv2 as cv
# # this code demonstrates how to use the Hough Circle Transform to detect circles in an image. It reads 
# # an image in grayscale, applies a median blur to reduce noise, and then uses the cv.HoughCircles 
# # function to detect circles based on the specified parameters. The detected circles are then drawn 
# # on a color version of the image, and the result is displayed using OpenCV. Each detected circle is
# # represented by its center coordinates and radius, which are used to draw the circles on the image.
# img = cv.imread('images/hello.png', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# img = cv.medianBlur(img,5)
# cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)

# circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
#                             param1=50,param2=30,minRadius=0,maxRadius=0)

# circles = np.uint16(np.around(circles))
# for i in circles[0,:]:
#     # draw the outer circle
#     cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

# cv.imshow('detected circles',cimg)
# cv.waitKey(0)
# cv.destroyAllWindows()



# #=================================================================================================================================
# # import numpy as np
# # import cv2 as cv
# # # accessing and modifying pixels values
# # img= cv.imread('images/starry_night.jpg')
# # assert img is not None, "file could not be read, check with os.path.exists()"
# # px=img[100,100]
# # print(px)
# # # [103 101 100]
# # blue=img[100,100,0]
# # print(blue)
# # # 103
# # img[100,100]=[255,255,255]
# # print(img[100,100]) 
# # # [255 255 255]

# # # accessing image properties: shape, size and datatype
# # print(img.shape)
# # # (3072, 3072, 3)
# # print(img.size) 
# # # 28311552
# # print(img.dtype)
# # # uint8
# # # # splitting and merging image channels
# # b,g,r=cv.split(img)
# # img=cv.merge((b,g,r))
# # # cv.imshow('image',img)


# # ============================================================================================================================================
# # import cv2 as cv
# # import numpy as np
# # from matplotlib import pyplot as plt

# # BLUE = [255,0,0]

# # img1 = cv.imread('images/border.jpg')
# # assert img1 is not None, "file could not be read, check with os.path.exists()"

# # replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
# # reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
# # reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
# # wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
# # constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

# # plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# # plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# # plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# # plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# # plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# # plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

# # plt.show()

# # =========================================================================================================================================


# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt

# img = cv.imread('images/ml.jpg', cv.IMREAD_GRAYSCALE)
# if img is None:
#     print("Could not read the image.")

# # cv.resizeWindow("Display window", 800, 600)  # Set the window size to 800x600
# img = cv.resize(img, (800, 600))
# # assert img is not None, "file could not be read, check with os.path.exists()"
# rows,cols = img.shape


# # it transforms the perspective of the image. The transformation is defined by four points in the input image (pts1) and their 
# # corresponding points in the output image (pts2). The function cv.getPerspectiveTransform calculates the transformation matrix M based on
# # these points, and cv.warpPerspective applies this transformation to the input image, resulting in the output image dst. 
# # The output image will have a size of 300x300 pixels.
# pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
 
# M = cv.getPerspectiveTransform(pts1,pts2)
 
# dst = cv.warpPerspective(img,M,(300,300))
 
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()


# # The transformation is defined by three points in the input image (pts1) and their corresponding points in the 
# # output image (pts2). The function cv.getAffineTransform calculates the transformation matrix M based on these points,
# # and cv.warpAffine applies this transformation to the input image, resulting in the output image dst.

# # pts1 = np.float32([[50,50],[200,50],[50,200]])
# # pts2 = np.float32([[10,100],[200,50],[100,250]])
 
# # M = cv.getAffineTransform(pts1,pts2)
 
# # dst = cv.warpAffine(img,M,(cols,rows))
 
# # plt.subplot(121),plt.imshow(img),plt.title('Input')
# # plt.subplot(122),plt.imshow(dst),plt.title('Output')
# # plt.show()

# # it shifts the image 100 pixels to the right and 50 pixels down. The transformation matrix M is defined as follows:
# # M = np.float32([[1,0,100],[0,1,50]])
# # dst = cv.warpAffine(img,M,(cols,rows))

# # cols-1 and rows-1 are the coordinate limits.
# # it rotates the image 90 degrees around its center. The transformation matrix M is defined as follows:
# # M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
# # dst = cv.warpAffine(img,M,(cols,rows))
# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # ============================================================================================================================================
# # # image blending is the process of combining two images together using a weighted sum. The formula for image blending is:
# # import cv2 as cv
# # img1 = cv.imread('images/ml.jpg')
# # img2 = cv.imread('images/open.jpg')
# # assert img1 is not None, "file could not be read, check with os.path.exists()"
# # assert img2 is not None, "file could not be read, check with os.path.exists()"

# # dst = cv.addWeighted(img1,0.7,img2,0.3,0)

# # cv.imshow('dst',dst)
# # cv.imwrite('images/dst.jpg', dst)
# # cv.waitKey(0)
# # cv.destroyAllWindows()

# # # img=cv.imread('images/open.jpg', cv.IMREAD_COLOR)
# # # cv.imshow('image',img)
# # # cv.imwrite('images/gray_image.jpg', img)
# # # cv.waitKey(0)


# # # Load two images
# img1 = cv.imread('images/roi.jpg')
# img2 = cv.imread('images/fusion.png')
# assert img1 is not None, "file could not be read, check with os.path.exists()"
# assert img2 is not None, "file could not be read, check with os.path.exists()"

# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols]

# # Now create a mask of logo and create its inverse mask also
# img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
# mask_inv = cv.bitwise_not(mask)

# # Now black-out the area of logo in ROI
# img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# # Take only region of logo from logo image.
# img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# # Put logo in ROI and modify the main image
# dst = cv.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst

# cv.imshow('res',img1)
# cv.imwrite('images/res.jpg', img1)
# cv.waitKey(0)
# cv.destroyAllWindows()


# # ============================================================================================================================================
# # img1 = cv.imread('images/overlay.jpg')
# # assert img1 is not None, "file could not be read, check with os.path.exists()"
# # cv.useOptimized()
# # e1 = cv.getTickCount()
# # print( e1 )
# # for i in range(5,49,2):
# #     img1 = cv.medianBlur(img1,i)
# # e2 = cv.getTickCount()
# # print( e2 )
# # f=cv.getTickFrequency()
# # print( f )
# # t = (e2 - e1)/f
# # print( t )


# # # Result I got is 0.521107655 seconds
# # ================================================================================================================================================

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# #the code below applies different types of thresholding to an image. It reads an image in grayscale, applies five different thresholding
# #techniques (BINARY, BINARY_INV, TRUNC, TOZERO, TOZERO_INV), and then displays the original and thresholded images using Matplotlib.Each
# #thresholding technique produces a different binaryimage basedon the specified threshold value (127 in thiscase) and the maximum value(255).
# img = cv.imread('images/starry_night.jpg', cv.IMREAD_COLOR_RGB)
# assert img is not None, "file could not be read, check with os.path.exists()"
# ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

# # ===================================================================================================================================================
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# # this code applies global and adaptive thresholding techniques to an image. It reads an image in grayscale, applies a median blur to 
# # reduce noise, and then applies global thresholding (with a fixed threshold value) and two types of adaptive thresholding (mean and 
# # Gaussian). Finally, it displays the original and thresholded images using Matplotlib. Each thresholding technique produces a different
# #  binary image based on the specified parameters.
# img = cv.imread('images/starry_night.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# img = cv.medianBlur(img,5)

# ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#             cv.THRESH_BINARY,11,2)
# th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv.THRESH_BINARY,11,2)

# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]

# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# # ==========================================================================================================================================================
# # this code shows how to use Otsu's thresholding method to automatically determine the optimal threshold value for an image. It reads a 
# # noisy image in grayscale, applies global thresholding, Otsu's thresholding, and Otsu's thresholding after applying a Gaussian blur to 
# # reduce noise. Finally, it displays the original image, its histogram, and the results of the different thresholding techniques using 
# # Matplotlib.
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('images/roi.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"

# # global thresholding
# ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# # Otsu's thresholding
# ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# # Otsu's thresholding after Gaussian filtering
# blur = cv.GaussianBlur(img,(5,5),0)
# ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# # plot all the images and their histograms
# images = [img, 0, th1,
#           img, 0, th2,
#           blur, 0, th3]
# titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
#           'Original Noisy Image','Histogram',"Otsu's Thresholding",
#           'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

# for i in range(3):
#     plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
#     plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
#     plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
#     plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
# plt.show()


# # ==========================================================================================================================================================

# # this code demonstrates how to use Otsu's thresholding method to automatically determine the optimal threshold value for an image. It 
# # reads an image in grayscale, applies a Gaussian blur to reduce noise, and then calculates the histogram of the blurred image. The code 
# # iterates through all possible threshold values (from 1 to 255) and calculates the within-class variance for each threshold. The 
# # threshold that minimizes this variance is selected as the optimal threshold. Finally, it compares the calculated optimal threshold with 
# # the one obtained using OpenCV's built-in Otsu's thresholding function and prints both values.
# img = cv.imread('images/roi.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# blur = cv.GaussianBlur(img,(5,5),0)

# # find normalized_histogram, and its cumulative distribution function
# hist = cv.calcHist([blur],[0],None,[256],[0,256])
# hist_norm = hist.ravel()/hist.sum()
# Q = hist_norm.cumsum()

# bins = np.arange(256)

# fn_min = np.inf
# thresh = -1

# for i in range(1,256):
#     p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
#     q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
#     if q1 < 1.e-6 or q2 < 1.e-6:
#         continue
#     b1,b2 = np.hsplit(bins,[i]) # weights

#     # finding means and variances
#     m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
#     v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

#     # calculates the minimization function
#     fn = v1*q1 + v2*q2
#     if fn < fn_min:
#         fn_min = fn
#         thresh = i

# # find otsu's threshold value with OpenCV function
# ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# print( "{} {}".format(thresh,ret) )