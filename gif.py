import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import cv2
import Drawing as draw
def animation (x,y,sports):
	if sports == 1 : 
		img = cv2.imread("media/football.jpg")
	elif sports ==0 : 
		img = cv2.imread("media/map2.jpg")

	fig, ax = plt.subplots()
    
	ax.imshow(img,origin ='upper')
	plt.ylim(max(plt.ylim()), min(plt.ylim()))
	graph, = plt.plot([], [] , color='red')
	def animate(i):
		graph.set_data(x[:i+1], y[:i+1])
            
		return graph
	ani = FuncAnimation(fig,animate)
	plt.show()
# ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                # repeat_delay=1000)

# ani.save('dynamic_images.mp4')