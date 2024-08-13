import cv2
import os
from get_key_frame import KeyFrames

def extract_frames(video_path, output_folder, key_frames):

	key_frames = set(key_frames) # Convert list2set to search index with O(1)

	# Open video 
	cap = cv2.VideoCapture(video_path)

	if not cap.isOpened():
		print("Cannot open video!!!")
		return
	idx_frame = 0 # Using counting frame and indexing frame
	while True:
		ret, frame = cap.read()
		if not ret:
			break

		if idx_frame in key_frames: # 
			frame_filename = os.path.join(output_folder, f"frame_{idx_frame:05d}.jpg")
			cv2.imwrite(frame_filename, frame)
		idx_frame += 1
			
	cap.release()


	

		
