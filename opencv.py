# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html


# import cv2 as cv
# import sys

# # Read an image from the specified file path
# img = cv.imread(cv.samples.findFile("hetal.png"))

# # Check if the image was loaded successfully
# if img is None:
#     sys.exit("Could not read the image.")

# # Display the image in a window named "Display window"
# cv.imshow("Display window", img)

# # Wait for a keystroke in the window (0 means wait indefinitely)
# k = cv.waitKey(0)

# # If the 's' key is pressed, save the image
# if k == ord("s"):
#     cv.imwrite("hetal.png", img)


# ==============================================================================================================================

import cv2
import vlc  # Make sure you ran: pip install python-vlc

video_path = "Susi.mp4"

# 1. Setup VLC for Audio only
# --no-video prevents a second window from popping up
# --avcodec-hw=none fixes the "depth stencil" error on Intel graphics
vlc_instance = vlc.Instance("--no-video", "--avcodec-hw=none")
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(video_path)
player.set_media(media)

# 2. Open Video for Visuals
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Start the audio
player.play()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video with Sound", frame)

    # 3. Handle Exit and Window Closing
    # Press 'q' to quit OR click the 'X' on the window
    key = cv2.waitKey(32) # 30ms delay matches ~33fps; adjust for your video speed
    if key & 0xFF == ord('q'):
        break
    
    # This specifically fixes the "can't close window" issue
    if cv2.getWindowProperty("Video with Sound", cv2.WND_PROP_VISIBLE) < 1:
        break

# 4. Cleanup everything
player.stop()
cap.release()
cv2.destroyAllWindows()

# ===================================================================================================================================================

# import cv2
# import vlc
# # import time

# video_path = r"C:\Users\Admin\Downloads\Rinku_Internship\01.mp4"

# # 1. Start VLC Instance with flags to disable video output and hardware acceleration
# # --no-video: Disables the VLC popup window entirely
# # --avcodec-hw=none: Disables the buggy hardware decoding (D3D11VA)
# vlc_instance = vlc.Instance("--no-video", "--avcodec-hw=none")
# player = vlc_instance.media_player_new()
# media = vlc_instance.media_new(video_path)
# player.set_media(media)

# player.play()
# # video_path = r"C:\Users\Admin\Downloads\Rinku_Internship\01.mp4"

# # 1. Start Audio with VLC
# # player = vlc.MediaPlayer("01.mp4")
# # player.play()

# # 2. Start Video with OpenCV
# cap = cv2.VideoCapture("01.mp4")

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow('Video with Sound', frame)

#     # Sync: waitKey value should roughly match your video FPS (e.g., 25ms for 30fps)
#     if cv2.waitKey(28) & 0xFF == ord('q'):
#         break

# # Cleanup
# player.stop()
# cap.release()
# cv2.destroyAllWindows()


import cv2 as cv
import numpy as np

print("OpenCV:", cv.__version__)
img = np.zeros((120, 400, 3), dtype=np.uint8)
cv.putText(img, "OpenCV OK", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
# If you installed a non-headless build, you can display a window:
# cv.imshow("hello", img); cv.waitKey(0)
# Always safe (headless or not): save to file
cv.imwrite("hello.png", img)
cv.imshow("hello.png", img)
cv.waitKey(0)