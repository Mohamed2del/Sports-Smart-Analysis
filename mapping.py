import cv2	    # import the OpenCV library						
import numpy as np  # import the numpy library
import Drawing as draw
# provide points from image 1 الحقيقيه
# top left top right -- buttom left  bottom right center 
#pts_src = np.array([[203,174],[536,192],[250,684],[1196,424],[499,245]])

# tennis map 

# corresponding points from image 2 (i.e. (154, 174) matches (212, 80)) التانيه
# football map
pts_dst_football = np.array([[7,25],[249,24],[5,435],[248,434],[127,224]])

#tennis map

pts_dst_tennis = np.array([[53,60],[203,60],[54,392],[206,390],[130,226]])


# corr = object.fuc
# 
# calculate matrix H

def map (point , pts_src ,sport):
	if (sport == 1) :

		h, status = cv2.findHomography(pts_src, pts_dst_football)
	elif sport == 0 :
		h, status = cv2.findHomography(pts_src, pts_dst_tennis)


	# provide a point you wish to map from image 1 to image 2
	a = np.array([point], dtype='float32')
	a = np.array([a])
	 
	# finally, get the mapping
	pointsOut = cv2.perspectiveTransform(a, h)
	#print(pointsOut)
	x = (pointsOut[0][0][0])
	y = pointsOut[0][0][1]
	

	# el real 			  el fake 854 480
	# (246,164) upper left corner (164,64)
	# (664,167) upper right (675,64)
	# (75,429) down left    (164,416)
	# (840,439) down right  (675,415)
	# (454,257) middle      (421,242)
	red = [0,0,255]
	
	
	image = cv2.imread('media/football.jpg')
	# Make one pixel red
	#draw.draw(pts_dst,image)
	# Save
	## debug the function {
	
	## }end 
	# cv2.imshow("result.png",image)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	return x , y



