import cv2 as cv
import threading
import queue
import numpy as np

# Video path
# video_path = "Susi.mp4"

# Queues for pipeline
read_queue = queue.Queue(maxsize=10)
filter_queue = queue.Queue(maxsize=10)
crop_queue = queue.Queue(maxsize=10)
diff_queue = queue.Queue(maxsize=10)

# -----------------------------
# Frame Reader Thread
# -----------------------------
def frame_reader():
    cap = cv.VideoCapture('Rinku.mp4')

    while True:
        ret, frame = cap.read()
        if not ret:
            read_queue.put(None)
            break
        read_queue.put(frame)

    cap.release()


# -----------------------------
# Bilateral Filter Thread
# -----------------------------
def bilateral_filter():
    while True:
        frame = read_queue.get()

        if frame is None:
            filter_queue.put(None)
            break

        filtered = cv.bilateralFilter(frame, 9, 75, 75)
        filter_queue.put(filtered)


# -----------------------------
# Frame Crop Thread
# -----------------------------
def crop_frame():
    while True:
        frame = filter_queue.get()

        if frame is None:
            crop_queue.put(None)
            break

        height = frame.shape[0]
        crop_height = int(height * 0.9)

        cropped = frame[:crop_height, :]
        crop_queue.put(cropped)


# -----------------------------
# Frame Difference Thread
# -----------------------------
def frame_difference():
    prev_frame = None

    while True:
        frame = crop_queue.get()

        if frame is None:
            diff_queue.put(None)
            break

        if prev_frame is None:
            prev_frame = frame
            continue

        diff = cv.absdiff(prev_frame, frame)
        diff_queue.put((frame, diff))

        prev_frame = frame


# -----------------------------
# Display Thread
# -----------------------------
def display_frames():
    while True:
        data = diff_queue.get()

        if data is None:
            break

        frame, diff = data

        # combined = cv.hconcat([frame, diff])
        combined=np.hstack([frame,diff])
        combined=cv.resize(combined,(800,400))

        cv.imshow("Video Processing Pipeline", combined)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()


# -----------------------------
# Create Threads
# -----------------------------
threads = [
    threading.Thread(target=frame_reader),
    threading.Thread(target=bilateral_filter),
    threading.Thread(target=crop_frame),
    threading.Thread(target=frame_difference),
    threading.Thread(target=display_frames),
]

# Start Threads
for t in threads:
    t.start()

# Wait for completion
for t in threads:
    t.join()


# ===========================================================finalllll pipeline code=====================

import cv2 as cv
import time
import threading
import queue
import numpy as np

# ================== STEP 1: RECORD VIDEO ==================
def record_video(filename="recorded.mp4", duration=10):
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return False

    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    out = cv.VideoWriter(filename,
                          cv.VideoWriter_fourcc(*'mp4v'),
                          20.0, (w, h))

    start_time = time.time()

    print("Recording started...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        cv.imshow("Recording (10 sec)", frame)

        # stop after 10 seconds
        if time.time() - start_time >= duration:
            print("Recording completed!")
            break

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()
    return True


# ================== STEP 2: PIPELINE ==================
def run_pipeline(path):
# -------- Queues --------
    q1 = queue.Queue(maxsize=10)
    q2 = queue.Queue(maxsize=10)
    q3 = queue.Queue(maxsize=10)
    q4 = queue.Queue(maxsize=10)

    stop_event = threading.Event()   # ✅ ADD THIS


# -------- Thread 1: Reader --------
    def reader():
        cap = cv.VideoCapture(path)

        while not stop_event.is_set():
            ret, frame = cap.read()
            if not ret:
                break
            try:
                q1.put(frame, timeout=0.5)
            except:
                continue

        cap.release()
        q1.put(None)


# -------- Thread 2: Filter --------
    def filter_thread():
        while not stop_event.is_set():
            try:
                frame = q1.get(timeout=0.5)
            except:
                continue

            if frame is None:
                q2.put(None)
                break

            filtered = cv.bilateralFilter(frame, 8, 70, 70)
            q2.put(filtered)


# -------- Thread 3: Crop --------
    def crop_thread():
        while not stop_event.is_set():
            try:
                frame = q2.get(timeout=0.5)
            except:
                continue

            if frame is None:
                q3.put(None)
                break

            h, w, _ = frame.shape
            cropped = frame[:int(h * 0.9), :]
            q3.put(cropped)


# -------- Thread 4: Difference --------
    def diff_thread():
        prev = None

        while not stop_event.is_set():
            try:
                frame = q3.get(timeout=0.5)
            except:
                continue

            if frame is None:
                q4.put(None)
                break

            if prev is None:
                diff = frame
            else:
                diff = cv.absdiff(prev, frame)

            prev = frame
            q4.put((frame, diff))


# -------- Thread 5: Display --------
    def display_thread():
        while not stop_event.is_set():
            try:
                data = q4.get(timeout=0.5)
            except:
                continue

            if data is None:
                break

            frame, diff = data

            combined = np.hstack([frame, diff])
            combined = cv.resize(combined, (800, 400))

            cv.imshow("Output", combined)

            if cv.waitKey(1) == ord('q'):
                stop_event.set()   # 🔥 STOP ALL THREADS
                break

        cv.destroyAllWindows()


# -------- Run Threads --------
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

    print("Pipeline Finished ✅")


# ================== MAIN ==================
if __name__ == "__main__":

    video_file = "recorded.mp4"

    # Step 1: Record
    success = record_video(video_file, duration=10)

    # Step 2: Run Pipeline
    if success:
        run_pipeline(video_file)