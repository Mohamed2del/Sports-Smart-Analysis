# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import  Drawing as draw
import time
import mapping as map
#import mappingTables as mt
import numpy as np
import distance  as dis
from real_time_stats import real_time

points = []
# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations
OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
#	"kcf": cv2.TrackerKCF_create,
#	"boosting": cv2.TrackerBoosting_create
}

xs = []
ys = []
frames = []
red = [155,0,255]


d = [[246,164],[664,167],[75,429],[840,439]]
# if a video path was not supplied, grab the reference to the web cam
time.sleep(.5)

# otherwise, grab a reference to the video file

# loop over frames from the video stream

def change_res(cap , width, height):
    cap.set(3, width)
    cap.set(4, height)




    
def run (video , pts_src , sport) :
	Player_Marked =False

    
	# otherwise, grab a reference to the video file
	i =0
	FPS_SMOOTHING = 0.9
    
    
	fps = 0.0
	prev = time.time()

	distance = 0
	total_distance = 0
	speed_list = []
	max_speed = 0
	min_speed = 0
	pointer = 0
	t = 3
	frames_count = 0


	# loop over frames from the video stream
	vs = cv2.VideoCapture(video)
	#change_res(vs,854,480)
    
	trackers = cv2.MultiTracker_create() 

	while True:
		frames_count = frames_count + 1
		# grab the current frame, then handle if we are using a
		# VideoStream or VideoCapture object
		frame = vs.read()
		frame = frame[1] 
		now = time.time()
		fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
		prev = now
		fpstext = 'FPS = ' + str(int(fps))  
		
		##real_time_stats_on_screen
		real_time(frame,distance , total_distance , max_speed , min_speed)



        # check to see if we have reached the end of the stream
		if frame is None:
			#print(corr)
			average_speed = sum(speed_list)/len(speed_list)
			

			return xs , ys , frames , total_distance , max_speed , min_speed , average_speed
			break
	 
		# resize the frame (so we can process it faster)
		#frame = imutils.resize(frame, width=1920,height=1080)
		# grab the updated bounding box coordinates (if any) for each
		# object that is being tracked
		(success, boxes) = trackers.update(frame)
	 
		# loop over the bounding boxes and draw then on the frame
		for box in boxes:
		
			(x, y, w, h) = [int(v) for v in box]
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
			
				# print(str(x+int(w/2))+','+str(y+int(h/2)))

			if (i % 90 == 0 ):	
				# xs.append(x+int(w/2))
				# ys.append(y+int(h))	
				x_map,y_map= map.map([x+int(w/2),y+int(h)],pts_src , sport)
				xs.append(x_map)
				ys.append(y_map)
				frames.append(frames_count)

				points.append(x_map)
				points.append(y_map)

				if (len(points) >= 4):
					#(x1,y1,x2,y2)
					#distance = mt.distance(points[pointer-3],points[pointer-2],points[pointer-1],points[pointer])/100
					distance = dis.calculateDistance(points[pointer-3],points[pointer-2],points[pointer-1],points[pointer],sport)
					total_distance = total_distance + distance
					speed = ((distance) / t) * 3.6
					speed_list.append(speed)
					max_speed = max(speed_list)
					min_speed = min(speed_list)

				pointer +=2

			
			cv2.circle(frame, (x+int(w/2),y+int(h)), 5, red, -1)

				
			i+=1
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		
		# if the 's' key is selected, we are going to "select" a bounding
		# box to track
		if(Player_Marked == False):
			
			if key == ord("s"):
				# select the bounding box of the object we want to track (make
				# sure you press ENTER or SPACE after selecting the ROI)
				# mt.mappingMatch()
				# mt.mappingPlayer()


					
				box = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
		
				# create a new object tracker for the bounding box and add it
				# to our multi-object tracker
				tracker = OPENCV_OBJECT_TRACKERS['csrt']()
				trackers.add(tracker, frame, box)
				Player_Marked = True
				
				# if the `q` key was pressed, break from the loop
		if key == ord("q"):	
			break

		if key ==ord("p"):
			cv2.waitKey()

 

	# otherwise, release the file pointer
	else:
		vs.release()
	 
	# close all windows
	cv2.destroyAllWindows()


   
	
	
