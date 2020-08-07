
import math 


##football
x_ratio_football = 4200/450
y_ratio_football = 2200/225

## tennis
x_ratio_tennis = 2377/ 450
y_ratio_tennis = 8230 / 225

## basketball
x_ratio_basketball = 1500/ 349
y_ratio_basketball = 2800/ 623
def calculateDistance(x1,y1,x2,y2,sports):  
     if x1 < 0 or y1 < 0 or x2 < 0 or y2 <0:
          return 0

     if sports ==1 :
          
          dist = math.sqrt(x_ratio_football*(x2 - x1)**2 + y_ratio_football * (y2 - y1)**2)/100
     elif sports == 0 : 
          dist = math.sqrt(x_ratio_tennis*(x2 - x1)**2 + y_ratio_tennis * (y2 - y1)**2)/100
     else :
          dist = math.sqrt(x_ratio_basketball*(x2 - x1)**2 + y_ratio_basketball * (y2 - y1)**2)/100

     return dist  


