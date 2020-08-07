import tracking as track
import numpy as np
import heat as ht
import gif as gf
import pick_coordinates
import mappingTables as mt
import uiTesting as ui
import t 

sport = ui.sports()
filename= t.filepick()
print(filename)
cord_array = pick_coordinates.c
coordinates = pick_coordinates.pick(filename)

print(np.array(coordinates))

x,y,frames , total_distance , max_speed , min_speed ,average_speed = track.run(filename,np.array(coordinates),sport)

print(max_speed)
print("average speed : " + str(average_speed))

#mt.mappingCoordinates(x,y,frames)
ht.heat(x,y,sport)
gf.animation(x,y,sport)


#TODO LIST
#----------
# file picker cancel button
# back sequence
# close sequence
# exceptions and test cases(cannot unpack non-iterable NoneType object, TypeError: argument of type 'NoneType' is not iterable)




