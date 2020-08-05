
import math 



x_ratio = 4200/450
y_ratio = 2200/225


def calculateDistance(x1,y1,x2,y2):  
     if x1 < 0 or y1 < 0 or x2 < 0 or y2 <0:
          raise ValueError("Points cant be negative ")
          return -1
    
     dist = math.sqrt(x_ratio*(x2 - x1)**2 + y_ratio * (y2 - y1)**2)  
     return dist  

