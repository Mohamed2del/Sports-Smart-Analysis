import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
import mysql.connector
import uiTesting as ut
import ui
import easygui


def heat(x, y, sports):
	if (sports == 1):
		img = cv2.imread("media/football.jpg")
	elif sports == 0:
		img = cv2.imread("media/map2.jpg")

	fig, ax = plt.subplots()

	ax.imshow(img, aspect='equal', origin='upper')

	plt.ylim(max(plt.ylim()), min(plt.ylim()))

	# Tidy Axes
	plt.axis('off')

	sns.kdeplot(x, y, legend=True)

	plt.show(block=False)


def retrivedHeat(playerid, matchId):
	mydb = mysql.connector.connect(host="localhost", user="playertrack", password="123123", database="playertrack")
	mycursor = mydb.cursor()

	x = []
	y = []

	heatMap = "SELECT x_coordinate, y_coordinate FROM coordinates_player WHERE id_player=%s AND id_match=%s"
	values = (playerid, matchId)

	mycursor.execute(heatMap, values)
	myresult = mycursor.fetchall()

	for i, j in myresult:
		x.append(i)
		y.append(j)

	img = cv2.imread("media/football.jpg")
	fig, ax = plt.subplots()

	ax.imshow(img, aspect='equal', origin='upper')

	plt.ylim(max(plt.ylim()), min(plt.ylim()))

	# Tidy Axes

	plt.axis('off')
	sns.kdeplot(x, y, legend=True)

	plt.show(block=False)


