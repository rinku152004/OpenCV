# import cv2

# # Create ArUco dictionary
# dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# # Generate marker (ID = 23, size = 200x200)
# marker_image = cv2.aruco.generateImageMarker(dictionary, 23, 200)

# # Save marker image
# cv2.imwrite("images/marker23.png", marker_image)

# print("Marker saved as marker23.png")


# ===================================================================================================================


# import cv2
# import argparse

# # ---------------- Argument Parser ----------------
# parser = argparse.ArgumentParser(description="ArUco Marker Generator")

# parser.add_argument("outfile", nargs='?', default="images/res.png",
#                     help="Output image file")

# parser.add_argument("-d", type=int, default=0,
#                     help="Dictionary ID")

# parser.add_argument("-cd", type=str, default=None,
#                     help="Custom dictionary file")

# parser.add_argument("-id", type=int, default=0,
#                     help="Marker ID")

# parser.add_argument("-ms", type=int, default=200,
#                     help="Marker size (pixels)")

# parser.add_argument("-bb", type=int, default=1,
#                     help="Border bits")

# parser.add_argument("-si", action='store_true',
#                     help="Show generated image")

# args = parser.parse_args()


# # ---------------- Dictionary Mapping ----------------
# ARUCO_DICT = {
#     0: cv2.aruco.DICT_4X4_50,
#     1: cv2.aruco.DICT_4X4_100,
#     2: cv2.aruco.DICT_4X4_250,
#     3: cv2.aruco.DICT_4X4_1000,
#     4: cv2.aruco.DICT_5X5_50,
#     5: cv2.aruco.DICT_5X5_100,
#     6: cv2.aruco.DICT_5X5_250,
#     7: cv2.aruco.DICT_5X5_1000,
#     8: cv2.aruco.DICT_6X6_50,
#     9: cv2.aruco.DICT_6X6_100,
#     10: cv2.aruco.DICT_6X6_250,
#     11: cv2.aruco.DICT_6X6_1000,
#     12: cv2.aruco.DICT_7X7_50,
#     13: cv2.aruco.DICT_7X7_100,
#     14: cv2.aruco.DICT_7X7_250,
#     15: cv2.aruco.DICT_7X7_1000,
#     16: cv2.aruco.DICT_ARUCO_ORIGINAL
# }


# # ---------------- Load Dictionary ----------------
# if args.cd:
#     print("Custom dictionary loading not implemented in Python easily")
#     exit()

# if args.d not in ARUCO_DICT:
#     print("Invalid dictionary ID")
#     exit()

# dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[args.d])


# # ---------------- Generate Marker ----------------
# try:
#     marker = cv2.aruco.generateImageMarker(
#         dictionary,
#         args.id,
#         args.ms,
#         borderBits=args.bb
#     )
# except:
#     marker = cv2.aruco.drawMarker(
#         dictionary,
#         args.id,
#         args.ms,
#         borderBits=args.bb
#     )


# # ---------------- Save ----------------
# cv2.imwrite(args.outfile, marker)
# print(f"Saved: {args.outfile}")


# # ---------------- Show Image ----------------
# if args.si:
#     cv2.imshow("Marker", marker)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import cv2

import argparse

# ---------------- Argument Parser ----------------
parser = argparse.ArgumentParser(description="Generate ArUco Marker")


parser.add_argument("outfile", nargs='?', default="images/res.png",
                    help="Output image file")

parser.add_argument("-d", type=int, default=0,
                    help="Dictionary ID")

parser.add_argument("-cd", type=str, default=None,
                    help="Custom dictionary file")

parser.add_argument("-id", type=int, default=0,
                    help="Marker ID")

parser.add_argument("-ms", type=int, default=200,
                    help="Marker size (pixels)")

parser.add_argument("-bb", type=int, default=1,
                    help="Border bits")

parser.add_argument("-si", action='store_true',
                    help="Show generated image")


args = parser.parse_args()

# ---------------- Dictionary Mapping ----------------
ARUCO_DICT = {
    0: cv2.aruco.DICT_4X4_50,
    1: cv2.aruco.DICT_4X4_100,
    2: cv2.aruco.DICT_4X4_250,
    3: cv2.aruco.DICT_4X4_1000,
    4: cv2.aruco.DICT_5X5_50,
    5: cv2.aruco.DICT_5X5_100,
    6: cv2.aruco.DICT_5X5_250,
    7: cv2.aruco.DICT_5X5_1000,
    8: cv2.aruco.DICT_6X6_50,
    9: cv2.aruco.DICT_6X6_100,
    10: cv2.aruco.DICT_6X6_250,
    11: cv2.aruco.DICT_6X6_1000,
    12: cv2.aruco.DICT_7X7_50,
    13: cv2.aruco.DICT_7X7_100,
    14: cv2.aruco.DICT_7X7_250,
    15: cv2.aruco.DICT_7X7_1000,
    16: cv2.aruco.DICT_ARUCO_ORIGINAL
}

# ---------------- Validate Dictionary ----------------
# # ---------------- Load Dictionary ----------------
if args.cd:
    print("Custom dictionary loading not implemented in Python easily")
    exit()

if args.d not in ARUCO_DICT:
    print("Invalid dictionary ID")
    exit()

dictionary = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[args.d])

# ---------------- Generate Marker ----------------
try:
    marker = cv2.aruco.generateImageMarker(
        dictionary,
        args.id,
        args.ms,
        borderBits=args.bb
    )
except:
    marker = cv2.aruco.drawMarker(
        dictionary,
        args.id,
        args.ms,
        borderBits=args.bb
    )
# marker_image = cv2.aruco.generateImageMarker(dictionary, args.id, 200)

# ---------------- Save ----------------
cv2.imwrite(args.outfile, marker)

print(f"Marker saved: {args.outfile}")

# # ---------------- Show Image ----------------
if args.si:
    cv2.imshow("Marker", marker)
    cv2.waitKey(0)
    cv2.destroyAllWindows()