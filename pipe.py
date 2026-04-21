# =======================same as second one============================= 
import cv2 as cv
import numpy as np
import threading
import queue

# -------- Queues --------
q1 = queue.Queue(maxsize=10)
q2 = queue.Queue(maxsize=10)
q3 = queue.Queue(maxsize=10)
q4 = queue.Queue(maxsize=10)

stop_event = threading.Event()   # ✅ ADD THIS
def reader():
    
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        q1.put(frame)

    q1.put(None)
    cap.release()


#Thread 2- bilateral filter 
def filter_thread():
    while True:
        frame = q1.get()
        if frame is None:
            q2.put(None)
            break

        filtered = cv.bilateralFilter(frame, 8, 70,70)
        q2.put(filtered)


#Thread 3- crop 
def crop_thread():
    while True:
        frame = q2.get()
        if frame is None:
            q3.put(None)
            break

        h, w, _ = frame.shape
        cropped = frame[:int(h * 0.9), :]
        q3.put(cropped)


#Thread 4- difference
def diff_thread():
    prev = None

    while True:
        frame = q3.get()
        if frame is None:
            q4.put(None)
            break

        if prev is None:
            diff = frame
        else:
            diff = cv.absdiff(prev, frame)

        prev = frame
        q4.put((frame, diff))


#Thread 5- display 
def display_thread():
    while True:
        data = q4.get()
        if data is None:
            break

        frame, diff = data

        combined = np.hstack([frame, diff])
        #combined = cv.hconcat([frame, diff])
        combined = cv.resize(combined, (800, 400))  

        cv.imshow("Output", combined)

        if cv.waitKey(1) == ord('q'):
            stop_event.set()
            break

    cv.destroyAllWindows()


# Run Threads
t1 = threading.Thread(target=reader)
t2 = threading.Thread(target=filter_thread)
t3 = threading.Thread(target=crop_thread)
t4 = threading.Thread(target=diff_thread)
t5 = threading.Thread(target=display_thread)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

cv.destroyAllWindows()

# # =========================Direct show output frames side by side with live video capturing=========================

# import cv2 as cv
# import numpy as np
# import threading
# import queue

# # -------- Queues --------
# q1 = queue.Queue(maxsize=10)
# q2 = queue.Queue(maxsize=10)
# q3 = queue.Queue(maxsize=10)
# q4 = queue.Queue(maxsize=10)

# stop_event = threading.Event()   # ✅ ADD THIS


# # -------- Thread 1: Reader --------
# def reader():
#     cap = cv.VideoCapture(0)

#     while not stop_event.is_set():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         try:
#             q1.put(frame, timeout=0.5)
#         except:
#             continue

#     cap.release()
#     q1.put(None)


# # -------- Thread 2: Filter --------
# def filter_thread():
#     while not stop_event.is_set():
#         try:
#             frame = q1.get(timeout=0.5)
#         except:
#             continue

#         if frame is None:
#             q2.put(None)
#             break

#         filtered = cv.bilateralFilter(frame, 8, 70, 70)
#         q2.put(filtered)


# # -------- Thread 3: Crop --------
# def crop_thread():
#     while not stop_event.is_set():
#         try:
#             frame = q2.get(timeout=0.5)
#         except:
#             continue

#         if frame is None:
#             q3.put(None)
#             break

#         h, w, _ = frame.shape
#         cropped = frame[:int(h * 0.9), :]
#         q3.put(cropped)


# # -------- Thread 4: Difference --------
# def diff_thread():
#     prev = None

#     while not stop_event.is_set():
#         try:
#             frame = q3.get(timeout=0.5)
#         except:
#             continue

#         if frame is None:
#             q4.put(None)
#             break

#         if prev is None:
#             diff = frame
#         else:
#             diff = cv.absdiff(prev, frame)

#         prev = frame
#         q4.put((frame, diff))


# # -------- Thread 5: Display --------
# def display_thread():
#     while not stop_event.is_set():
#         try:
#             data = q4.get(timeout=0.5)
#         except:
#             continue

#         if data is None:
#             break

#         frame, diff = data

#         combined = np.hstack([frame, diff])
#         combined = cv.resize(combined, (800, 400))

#         cv.imshow("Output", combined)

#         if cv.waitKey(1) == ord('q'):
#             stop_event.set()   # 🔥 STOP ALL THREADS
#             break

#     cv.destroyAllWindows()


# # -------- Run Threads --------
# t1 = threading.Thread(target=reader)
# t2 = threading.Thread(target=filter_thread)
# t3 = threading.Thread(target=crop_thread)
# t4 = threading.Thread(target=diff_thread)
# t5 = threading.Thread(target=display_thread)

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

# print("Exited cleanly ✅")


# # ================================Completely work code =====================================
# import cv2
# import time
# import threading
# import queue
# import numpy as np

# # ================== STEP 1: RECORD VIDEO ==================
# def record_video(filename="recorded.mp4", duration=10):
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Cannot open camera")
#         return False

#     w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     out = cv2.VideoWriter(filename,
#                           cv2.VideoWriter_fourcc(*'mp4v'),
#                           20.0, (w, h))

#     start_time = time.time()

#     print("Recording started...")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         out.write(frame)
#         cv2.imshow("Recording (10 sec)", frame)

#         # stop after 10 seconds
#         if time.time() - start_time >= duration:
#             print("Recording completed!")
#             break

#         if cv2.waitKey(1) == ord('q'):
#             break

#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     return True


# # ================== STEP 2: PIPELINE ==================
# def run_pipeline(path):

#     q1 = queue.Queue(maxsize=10)
#     q2 = queue.Queue(maxsize=10)
#     q3 = queue.Queue(maxsize=10)
#     q4 = queue.Queue(maxsize=10)
#     # path="rinku.mp4"
#     stop_event = threading.Event()

#     # -------- Reader --------
#     def reader():
#         cap = cv2.VideoCapture(path)

#         while not stop_event.is_set():
#             ret, frame = cap.read()
#             if not ret:
#                 break
#             q1.put(frame)

#         q1.put(None)
#         cap.release()

#     # -------- Filter --------
#     def filter_stage():
#         while True:
#             frame = q1.get()
#             if frame is None:
#                 q2.put(None)
#                 break

#             filtered = cv2.bilateralFilter(frame, 9, 75, 75)
#             q2.put(filtered)

#     # -------- Crop --------
#     def crop_stage():
#         while True:
#             frame = q2.get()
#             if frame is None:
#                 q3.put(None)
#                 break

#             h = frame.shape[0]
#             cropped = frame[:int(h * 0.9), :]
#             q3.put(cropped)

#     # -------- Difference --------
#     def diff_stage():
#         prev = None

#         while True:
#             frame = q3.get()
#             if frame is None:
#                 q4.put(None)
#                 break

#             if prev is None:
#                 prev = frame
#                 continue

#             diff = cv2.absdiff(prev, frame)
#             q4.put((frame, diff))
#             prev = frame

#     # -------- Display --------
#     def display():

#         cv2.namedWindow("Pipeline Output", cv2.WINDOW_NORMAL)
#         cv2.setWindowProperty("Pipeline Output", cv2.WND_PROP_TOPMOST, 1)

#         while True:
#             data = q4.get()
#             if data is None:
#                 break

#             frame, diff = data

#             combined = np.hstack([frame, diff])
#             combined = cv2.resize(combined, (800, 400))

#             cv2.imshow("Pipeline Output", combined)
#             time.sleep(0.03)

#             if cv2.waitKey(1) == ord('q'):
#                 print("exittingg...")
#                 break
                                
            

#         cv2.destroyAllWindows()

#     # -------- Threads --------
#     threads = [
#         threading.Thread(target=reader, daemon=True),
#         threading.Thread(target=filter_stage, daemon=True),
#         threading.Thread(target=crop_stage, daemon=True),
#         threading.Thread(target=diff_stage, daemon=True),
#         threading.Thread(target=display)
#     ]

#     for t in threads:
#         t.start()

#     threads[-1].join()

#     print("Pipeline Finished ✅")


# # ================== MAIN ==================
# if __name__ == "__main__":

#     video_file = "recorded.mp4"

#     # Step 1: Record
#     success = record_video(video_file, duration=10)

#     # Step 2: Run Pipeline
#     if success:
#         run_pipeline(video_file)