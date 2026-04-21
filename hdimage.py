# from __future__ import print_function
# from __future__ import division
# import cv2 as cv
# import numpy as np
# import argparse
# import os

# def loadExposureSeq(path):
#     images = []
#     times = []
#     with open(os.path.join(path, 'list.txt')) as f:
#         content = f.readlines()
#     for line in content:
#         tokens = line.split()
#         images.append(cv.imread(os.path.join(path, tokens[0])))
#         times.append(1 / float(tokens[1]))

#     return images, np.asarray(times, dtype=np.float32)

# parser = argparse.ArgumentParser(description='Code for High Dynamic Range Imaging tutorial.')
# parser.add_argument('--input', type=str, help='Path to the directory that contains images and exposure times.')
# args = parser.parse_args()

# if not args.input:
#     parser.print_help()
#     exit(0)

# images, times = loadExposureSeq(args.input)

# calibrate = cv.createCalibrateDebevec()
# response = calibrate.process(images, times)

# merge_debevec = cv.createMergeDebevec()
# hdr = merge_debevec.process(images, times, response)

# tonemap = cv.createTonemapDrago(2.2)
# ldr = tonemap.process(hdr)

# merge_mertens = cv.createMergeMertens()
# fusion = merge_mertens.process(images)

# cv.imwrite('images/fusion.png', fusion * 255)
# cv.imwrite('images/ldr.png', ldr * 255)
# cv.imwrite('images/hdr.hdr', hdr)

import cv2 as cv
import numpy as np

cv.utils.logging.setLogLevel(cv.utils.logging.LOG_LEVEL_ERROR)

# Load images
img1 = cv.imread("images/open.jpg")
img2 = cv.imread("images/gray.jpg")

# Check if images loaded
if img1 is None or img2 is None:
    print("Error: Images not found")
    exit()

# Convert images into list
images = [img1, img2]
# align = cv.createAlignMTB()
# align.process(images, images)
# Exposure times (example values)
times = np.array([1/30.0, 1/5.0], dtype=np.float32)

# Step 1: Camera response calibration
calibrate = cv.createCalibrateDebevec()
response = calibrate.process(images, times)

# Step 2: Merge images to HDR
merge_debevec = cv.createMergeDebevec()
hdr = merge_debevec.process(images, times, response)

# Step 3: Tone mapping
tonemap = cv.createTonemapDrago(2.2)
ldr = tonemap.process(hdr)

# Step 4: Exposure Fusion
merge_mertens = cv.createMergeMertens()
fusion = merge_mertens.process(images)

# Clean HDR outputs
ldr = np.nan_to_num(ldr)
fusion = np.nan_to_num(fusion)

# Convert to 8bit images
ldr_8bit = np.clip(ldr * 255, 0, 255).astype(np.uint8)
fusion_8bit = np.clip(fusion * 255, 0, 255).astype(np.uint8)

# Save results
cv.imwrite("images/fusion.png", fusion_8bit)
cv.imwrite("images/ldr.png", ldr_8bit)
cv.imwrite("images/hdr.hdr", hdr)

# Show results
# cv.imshow("Image 1", img1)
# cv.imshow("Image 2", img2)
cv.imshow("Fusion", fusion)
cv.imshow("Tone Mapped HDR", ldr)
cv.imshow("HDR", hdr / np.max(hdr))  # Normalize for display

cv.waitKey(0)
cv.destroyAllWindows()