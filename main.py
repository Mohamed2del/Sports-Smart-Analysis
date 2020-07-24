import tracking as track
import numpy as np
import heat as ht
import gif as gf
import pick_coordinates


cord_array = pick_coordinates.c
coordinates = pick_coordinates.pick("media/2.mp4")

print(np.array(coordinates))

print("[INFO] starting video stream...")

x,y = track.run('media/2.mp4',np.array(coordinates))

ht.heat(x,y)
gf.animation(x,y)



