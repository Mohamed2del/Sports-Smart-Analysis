import cv2

# Blue color in BGR 
color = (255,0,0) 
#colors_circle = [[255,0,0],[0,255,0],[255,255,255],[100,200,250]]
# Line thickness of 2 px 
thickness = 1
font = cv2.FONT_HERSHEY_SIMPLEX 
# fontScale 
fontScale = 1
def draw(data,img):
	
	for i,u in enumerate(data) :
			pointsx = data[i][0]
			pointsy= data[i][1]
			cord = '('+str(pointsx)+','+str(pointsy)+')'
			cv2.circle(img, (pointsx,pointsy), 5, colors_circle[i], -1)
			cv2.putText(img, str(cord), (pointsx,pointsy), font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
def drawText(img,st,points):
	cv2.putText(img, st, points, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
