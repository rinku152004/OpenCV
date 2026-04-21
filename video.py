# # ======================================video with sound=================================

# import cv2
# import vlc  # Make sure you ran: pip install python-vlc

# video_path = "images/Susi.mp4"

# # 1. Setup VLC for Audio only
# # --no-video prevents a second window from popping up
# # --avcodec-hw=none fixes the "depth stencil" error on Intel graphics
# vlc_instance = vlc.Instance("--no-video", "--avcodec-hw=none")
# player = vlc_instance.media_player_new()
# media = vlc_instance.media_new(video_path)
# player.set_media(media)

# # 2. Open Video for Visuals
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     print("Error: Could not open video file.")
#     exit()

# # Start the audio
# player.play()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow("Video with Sound", frame)

#     # 3. Handle Exit and Window Closing
#     # Press 'q' to quit OR click the 'X' on the window
#     key = cv2.waitKey(32) # 30ms delay matches ~33fps; adjust for your video speed
#     if key & 0xFF == ord('q'):
#         break
    
#     # This specifically fixes the "can't close window" issue
#     if cv2.getWindowProperty("Video with Sound", cv2.WND_PROP_VISIBLE) < 1:
#         break

# # 4. Cleanup everything
# player.stop()
# cap.release()
# cv2.destroyAllWindows()

# ====================================video capture and save========================================
# import cv2 as cv

# cap = cv.VideoCapture(0)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# out = cv.VideoWriter('images/output.mp4', fourcc, 20.0, (width,height))

# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     out.write(frame)

#     cv.imshow('frame', frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# out.release()
# cv.destroyAllWindows()



# import cv2 as cv

# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
# out = cv.VideoWriter('images/output.mp4', fourcc, 20.0, (width,  height))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Flip the frame vertically
#     # frame = cv.flip(frame, 0)

#     # write the flipped frame
#     out.write(frame)

#     cv.imshow('frame', frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()

# # ======================================Video Capture Only=================================


# import cv2 as cv

# cap = cv.VideoCapture(0)

# fps = cap.get(cv.CAP_PROP_FRAME_WIDTH)
# print("Frames per second using video.get(cv2.CAP_PROP_FRAME_WIDTH): {0}".format(fps))
# fps = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
# print("Frames per second using video.get(cv2.CAP_PROP_FRAME_HEIGHT): {0}".format(fps))

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

# this code captures video from the default camera (usually the webcam), converts each frame to grayscale, and displays it in a window. 
# The video capture continues until the user presses the 'q' key. After the loop, it releases the camera and closes all OpenCV windows.
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(gray, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()


# it is used to capture video from the camera and display it in a window. The code also converts the video frames to grayscale and 
# applies a mask to detect blue colors. The resulting video is displayed in separate windows for the original frame, the mask, and 
# the result of applying the mask. The video capture continues until the user presses the 'Esc' key.

# import cv2 as cv
# import numpy as np

# cap = cv.VideoCapture(0)

# while True:

#     # Capture frame
#     ret, frame = cap.read()

#     # Convert BGR to Gray
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     # Apply threshold to detect bright areas
#     _, mask = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)

#     # Apply mask on original frame
#     res = cv.bitwise_and(frame, frame, mask=mask)

#     # Show results
#     cv.imshow('Original', frame)
#     cv.imshow('Gray', gray)
#     cv.imshow('Mask', mask)
#     cv.imshow('Result', res)

#     if cv.waitKey(5) & 0xFF == 27:
#         break

# cap.release()
# cv.destroyAllWindows()