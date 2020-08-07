
import pandas as pd
import cv2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns

def heat (x,y, sports) : 
	if (sports == 1) : 
		img = cv2.imread("media/football.jpg")
	elif sports == 0 :
		img = cv2.imread("media/map2.jpg")
	
	
	fig, ax = plt.subplots()

	ax.imshow(img,aspect ='equal',origin ='upper')

	plt.ylim(max(plt.ylim()), min(plt.ylim()))

	#Tidy Axes
	plt.axis('off')
	
	sns.kdeplot(x,y, legend=True , n_level = 50 )
	
	plt.show(block = False)
