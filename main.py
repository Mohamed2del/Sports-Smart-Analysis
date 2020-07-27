import tracking as track
import numpy as np
import heat as ht
import gif as gf
import pick_coordinates
import t

filename = t.filepick()
#coordinates = pick_coordinates.pick(r'''C:\Users\moham\Desktop\football\SportsSmartAnalysis\media\1.mp4''')
coordinates = pick_coordinates.pick(filename)


print("[INFO] starting video stream...")

x,y = track.run('media/2.mp4',np.array(coordinates))

ht.heat(x,y)
gf.animation(x,y)



