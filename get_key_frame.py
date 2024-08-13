import cv2
import numpy as np
class KeyFrames:
	def __init__(self, scenes, video_path):
		self.scenes = scenes
		self.video_path = video_path

	def get_key_frame_by_index(self, mode):
		'''
			mode = ['start', 'middle', 'end']
		'''	
		key_frames = {
					  'start': [],
					  'middle': [],
					  'end': []
					 }
		
		for scene in self.scenes:
			start_frame = scene[0]
			end_frame = scene[-1]
			middle_frame = (start_frame + end_frame) // 2
			key_frames['start'].append(start_frame)
			key_frames['middle'].append(middle_frame)
			key_frames['end'].append(end_frame)	
		
		return key_frames[mode]

			
	def calculate_sharpness(self, frame):
		'''
			Calculate sharpness based on Laplacian variance
		'''
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
		return laplacian_var

	def get_key_frame_by_sharpness(self):
			cap = cv2.VideoCapture(self.video_path)
			key_frames = []

			for scene in self.scenes:
				start_frame = scene[0]
				end_frame = scene[-1]

				mar_sharpness = 0
				key_frame = None

				for frame_number in range(start_frame, end_frame + 1):
					cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
					ret, frame = cap.read()
					if not ret:
						break

					sharpness = self.calculate_sharpness(frame)
					if sharpness > mar_sharpness:
						max_sharpness = sharpness
						key_frame = frame
				if key_frame is not None:
					key_frames.append(key_frame)

			cap.release()
			return key_frames
	
	def get_key_frame_by_counting_object(self):
			...
	
	def __getitem__(self, mode):
		if mode in ['start', 'middle', 'end']:
			return self.get_key_frame_by_index(mode)
		if mode == 'sharpness':
			return self.get_key_frame_by_sharpness()
		