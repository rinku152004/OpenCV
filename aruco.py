# import cv2
# import numpy as np
# import time

# # ---------------- SETTINGS ----------------
# LINE_Y = 300          # virtual line position
# COOLDOWN = 3          # seconds to prevent duplicate logs

# # ---------------- ARUCO SETUP ----------------
# aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# detector = cv2.aruco.ArucoDetector(aruco_dict)

# # ---------------- TRACKING ----------------
# last_positions = {}
# last_logged_time = {}

# # ---------------- CAMERA ----------------
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# # ---------------- MAIN LOOP ----------------
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     corners, ids, _ = detector.detectMarkers(gray)

#     # draw virtual line
#     cv2.line(frame, (0, LINE_Y), (frame.shape[1], LINE_Y), (0, 0, 255), 2)

#     if ids is not None:
#         ids = ids.flatten()

#         for i, marker_id in enumerate(ids):
#             pts = corners[i][0]
#             center_y = int(np.mean(pts[:, 1]))

#             # draw marker box
#             cv2.polylines(frame, [pts.astype(int)], True, (0, 255, 0), 2)
#             cv2.putText(frame, f"ID:{marker_id}",
#                         (int(pts[0][0]), int(pts[0][1])),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

#             prev_y = last_positions.get(marker_id, center_y)
#             direction = None

#             # -------- IN / OUT LOGIC --------
#             if prev_y < LINE_Y and center_y >= LINE_Y:
#                 direction = "IN"
#             elif prev_y > LINE_Y and center_y <= LINE_Y:
#                 direction = "OUT"

#             last_positions[marker_id] = center_y

#             # -------- COOLDOWN --------
#             current_time = time.time()

#             if direction:
#                 last_time = last_logged_time.get(marker_id, 0)

#                 if current_time - last_time > COOLDOWN:
#                     print(f"ID {marker_id} -> {direction} at {time.strftime('%H:%M:%S')}")
#                     last_logged_time[marker_id] = current_time

#                     # show on screen
#                     cv2.putText(frame, f"{direction}",
#                                 (int(pts[0][0]), int(pts[0][1]) - 20),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.8,
#                                 (0, 0, 255), 2)

#     cv2.imshow("ArUco IN/OUT System", frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# # ---------------- CLEANUP ----------------
# cap.release()
# cv2.destroyAllWindows()

#===================================================================ArUco Detection=======================================
import cv2
import numpy as np
import time
import json
import logging
from pymongo import MongoClient

# ---------------- CONFIG ----------------
with open("settings.json") as f:
    config = json.load(f)

CAM_SOURCE = config["camera_source"]
LINE_Y = config["line_position"]
CAM_ID = config["camera_id"]
COOLDOWN = config["cooldown_seconds"]

# ---------------- LOGGER ----------------
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# ---------------- DATABASE ----------------
try:
    client = MongoClient(config["mongo_uri"])
    db = client[config["db_name"]]
    collection = db[config["collection_name"]]
    logging.info("MongoDB Connected")
except Exception as e:
    logging.error(f"DB Error: {e}")
    exit()

# ---------------- ARUCO SETUP ----------------
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
detector = cv2.aruco.ArucoDetector(aruco_dict)

# ---------------- TRACKING ----------------
last_positions = {}
last_logged_time = {}

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(CAM_SOURCE)

if not cap.isOpened():
    logging.error("Camera not accessible")
    exit()

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        logging.error("Frame read failed")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, _ = detector.detectMarkers(gray)

    # Draw line
    cv2.line(frame, (0, LINE_Y), (frame.shape[1], LINE_Y), (0, 0, 255), 2)

    if ids is not None:
        ids = ids.flatten()

        for i, marker_id in enumerate(ids):
            pts = corners[i][0]
            center_y = int(np.mean(pts[:, 1]))

            # Draw marker
            cv2.polylines(frame, [pts.astype(int)], True, (0, 255, 0), 2)
            cv2.putText(frame, f"ID:{marker_id}", (int(pts[0][0]), int(pts[0][1])),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            prev_y = last_positions.get(marker_id, center_y)

            direction = None

            # -------- Crossing Logic --------
            if prev_y < LINE_Y and center_y >= LINE_Y:
                direction = "IN"
            elif prev_y > LINE_Y and center_y <= LINE_Y:
                direction = "OUT"

            last_positions[marker_id] = center_y

            # -------- Cooldown --------
            current_time = time.time()

            if direction:
                last_time = last_logged_time.get(marker_id, 0)

                if current_time - last_time > COOLDOWN:
                    data = {
                        "aruco_id": int(marker_id),
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "direction": direction,
                        "camera_id": CAM_ID,
                        "status": "valid"
                    }

                    try:
                        collection.insert_one(data)
                        logging.info(f"Logged: {data}")
                        last_logged_time[marker_id] = current_time
                    except Exception as e:
                        logging.error(f"DB Insert Error: {e}")

    cv2.imshow("Aruco Tracking", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
client.close()
logging.info("System stopped")