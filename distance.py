
import math 



x_ratio = 4200/450
y_ratio = 2200/225


def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt(x_ratio*(x2 - x1)**2 + y_ratio * (y2 - y1)**2)  
     return dist  

