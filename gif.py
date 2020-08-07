import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import cv2
import Drawing as draw
import mysql.connector
import uiTesting as ut
import ui
import easygui


def animation(x, y, sports):
    if sports == 1:
        img = cv2.imread("media/football.jpg")
    elif sports == 0:
        img = cv2.imread("media/map2.jpg")

    fig, ax = plt.subplots()

    ax.imshow(img, origin='upper')
    plt.ylim(max(plt.ylim()), min(plt.ylim()))
    graph, = plt.plot([], [])

    def animate(i):
        graph.set_data(x[:i + 1], y[:i + 1])

        return graph

    ani = FuncAnimation(fig, animate)
    plt.show()


# ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
# repeat_delay=1000)

# ani.save('dynamic_images.mp4')


def retrivedAnimation(playerid, matchId):
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

    ax.imshow(img, origin='upper')
    plt.ylim(max(plt.ylim()), min(plt.ylim()))
    graph, = plt.plot([], [])

    def animate(i):
        graph.set_data(x[:i + 1], y[:i + 1])

        return graph

    ani = FuncAnimation(fig, animate)
    plt.show()
