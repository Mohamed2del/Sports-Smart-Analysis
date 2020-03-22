import tracking as track
import numpy as np
import heat as ht
import gif as gf


x,y = track.run('media/2.mp4')

ht.heat(x,y)
gf.animation(x,y)



