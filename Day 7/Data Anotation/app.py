import cv2
import os 

output_folder = "frames1"
video_path = r"d:\Mlops_Training\Data Anotation\videos\data.mp4"

cap = cv2.VideoCapture(video_path)
os.makedirs(output_folder, exist_ok=True)

frame_count = 0
count = 0
while True:
    success, frame = cap.read()
    if not success:
        break
    if frame_count%5 ==0:
        file = os.path.join(
            output_folder,
            f"frame_{count}.jpg"
        )
        cv2.imwrite(file,frame)

        count+=1
    frame_count+=1
cap.release()
print("Frames extracted")
