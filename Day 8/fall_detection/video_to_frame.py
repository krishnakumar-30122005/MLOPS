import cv2
import os 
os.chdir(r'D:\fall_detection\frames')

video_path = r'D:\fall_detection\video\video (2).avi'
cap = cv2.VideoCapture(video_path)

count = 142
frame_count = 0
while True:
    success, frame = cap.read()
    if not success:
        break
    frame_count+=1
    if frame_count%2==0:
        print(f"frame {count}.jpg being read..")
        cv2.imwrite(f'frames{count}.jpg',frame)
        count+=1
cap.release()
cv2.destroyAllWindows()
print("Completed")
