import  Drawing as draw

def real_time(frame ,distance , total_distance , max_speed , min_speed):

	draw.drawText(frame,str("Real Time Distance : "+"%.2f" % round(distance, 2)+" m") , (40,80))
	draw.drawText(frame,str("Total Distance : "+"%.2f" % round(total_distance, 2)+" m") , (40,120))
	draw.drawText(frame,str("Current Speed  : " + "%.2f" % round(((distance*3.6)/3) , 2)+" km/h") , (40,160))
	draw.drawText(frame,str("Max Speed  :" + "%.2f" % round(max_speed,2) + "km/h"), (40,200))
	draw.drawText(frame,str("Min Speed  :" + "%.2f" % round(min_speed,2) + "km/h"), (40,240))