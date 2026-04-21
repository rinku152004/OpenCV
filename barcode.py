



# # this code is for barcode detection using OpenCV. It reads an image, applies edge detection, finds contours, and draws rectangles around detected barcodes based on their aspect ratio.
# import cv2 as cv
# import numpy as np
# import glob

# images = []  # Initialize the images list

# for file in sorted(glob.glob("images/*.jpg")):
#     img = cv.imread(file)

#     if img is None:
#         print("Failed to load:", file)
#         continue

#     # img = cv.resize(img, (800,600))
#     images.append(img)

# print("Number of images loaded:", len(images))

# if len(images) < 2:
#     print("Need at least 2 images")
#     exit()

# # Create stitcher
# stitcher = cv.Stitcher_create(cv.Stitcher_SCANS)

# status, pano = stitcher.stitch(images)

# if status != cv.Stitcher_OK:
#     print("Error stitching images:", status)
#     exit()

# # Remove black borders
# gray = cv.cvtColor(pano, cv.COLOR_BGR2GRAY)
# _, thresh = cv.threshold(gray, 1, 255, cv.THRESH_BINARY)

# contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# c = max(contours, key=cv.contourArea)
# x,y,w,h = cv.boundingRect(c)

# pano = pano[y:y+h, x:x+w]

# cv.imwrite("images/panorama_result.jpg", pano)

# cv.imshow("Panorama", pano)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ======================================================================================================================

import cv2 as cv

img1 = cv.imread("images/open.jpg")
img2 = cv.imread("images/ml.jpg")

images = [img1, img2]

stitcher = cv.Stitcher.create()
status, pano = stitcher.stitch(images)

if status == cv.Stitcher_OK:
    cv.imwrite("images/result.jpg", pano)
    cv.imshow("Panorama", pano)
    cv.waitKey(0)
else:
    print("Image Not Found")

#===========================================================================

import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

# Read image
img = cv.imread("images/barcodee.jpg")

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Compute gradients (barcode has strong vertical lines)
gradX = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=-1)
gradY = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=-1)

gradient = cv.subtract(gradX, gradY)
gradient = cv.convertScaleAbs(gradient)

# Blur and threshold
blurred = cv.blur(gradient, (9,9))
_, thresh = cv.threshold(blurred, 225, 255, cv.THRESH_BINARY)

# Morphological closing
kernel = cv.getStructuringElement(cv.MORPH_RECT, (21,7))
closed = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

# Remove small noise
closed = cv.erode(closed, None, iterations=4)
closed = cv.dilate(closed, None, iterations=4)

# Find contours
contours, _ = cv.findContours(closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

if contours:
    
    # Largest contour = barcode
    c = max(contours, key=cv.contourArea)

    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    box = np.intp(box)

    # Draw rotated rectangle
    cv.drawContours(img, [box], -1, (0,255,0), 3)

    # Warp perspective to straighten barcode
    width = int(rect[1][0])
    height = int(rect[1][1])

    src_pts = box.astype("float32")
    dst_pts = np.array([[0, height-1],
                        [0, 0],
                        [width-1, 0],
                        [width-1, height-1]], dtype="float32")

    M = cv.getPerspectiveTransform(src_pts, dst_pts)
    warp = cv.warpPerspective(gray, M, (width, height))

    # Decode barcode
    barcodes = decode(warp)
    
    # Draw green rectangle
    # cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)


    btype = barcodes[0].type

    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        print("Barcode Type:", barcode.type)
        print("Decoded Barcode:", data)
        text = f"[{btype}] {data}"

        # Draw yellow text
        cv.putText(img, text,
               (box[0][0], box[0][1] - 10),
               cv.FONT_HERSHEY_SIMPLEX,
               0.7,
               (0,255,255), 2)   # Yellow color

        # print(text)
        # cv.putText(img, data, (50,50),
        #            cv.FONT_HERSHEY_SIMPLEX,
        #            1,(0,255,0),2)

# Show results
cv.imshow("Detected Barcode", img)
cv.imshow("Straightened Barcode", warp)

cv.waitKey(0)
cv.destroyAllWindows()


# if __name__ == "__main__":
#     img = cv.imread("images/barcodee.jpg")
#     # gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     gray = cv.GaussianBlur(img,(3,3),0)
#     edged = cv.Canny(gray, 50, 200, 255)
#     contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#     for c in contours:
#         x,y,w,h = cv.boundingRect(c)
#         aspect_ratio = w / float(h)
#         if aspect_ratio > 2.5:
#             cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     cv.imshow('Image', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()