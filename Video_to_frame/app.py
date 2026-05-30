import os
import cv2
os.chdir(r"D:\Mlops_Training\Video_to_frame")
cap = cv2.VideoCapture(r"D:\Mlops_Training\Video_to_frame\WIN_20260523_09_15_33_Pro.mp4")
framerate = int(cap.get(cv2.CAP_PROP_FPS))
interval = max(1, round(framerate * 0.25))
framecount = 0
count = 0

while True:
    success, frame = cap.read()
    if not success:
        break
    framecount += 1
    if framecount >= interval:
        print(f"Saving frame: {count}")
        frame = cv2.resize(frame,(1280,720))
        cv2.imwrite(f"11_frames{count}.jpg",frame)
        count+=1
        framecount = 0

cap.release()
cv2.destroyAllWindows()
print("completed")