import tracking as track
import numpy as np
import heat as ht
import gif as gf
import pick_coordinates
import mappingTables as mt
import uiTesting as ui


filename=mt.mappingVideo()
print(filename)
cord_array = pick_coordinates.c
coordinates = pick_coordinates.pick(filename)

print(np.array(coordinates))

x,y,frames = track.run(filename,np.array(coordinates))


mt.mappingCoordinates(x,y,frames)
ht.heat(x,y)
gf.animation(x,y)


#TODO LIST
#----------
# file picker cancel button
# back sequence
# close sequence
# exceptions and test cases(cannot unpack non-iterable NoneType object, TypeError: argument of type 'NoneType' is not iterable)




