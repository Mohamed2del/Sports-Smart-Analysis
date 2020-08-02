import mysql.connector
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import itertools
import dataEntry as data
import easygui
import math
from PIL import Image
import uiTesting as ui





   
mydb = mysql.connector.connect(host="localhost", user="playertrack", password="123123", database="playertrack")
mycursor = mydb.cursor()

def mappingCoordinates(x,y,frames):
   
    zipped=zip(x,y,frames)
    type(zipped)

    print("\n")
    for i, j, f in zipped:
        
        coordinates = "INSERT INTO coordinates_player (x_coordinate, y_coordinate, current_frame) VALUES (%s,%s,%s)"
        value=(int(i), int(j), int(f))
        mycursor.execute(coordinates, value)
        

    mydb.commit()
    print(mycursor.rowcount, "Player Record is Inserted.")

    #Called in main function

        

def mappingVideo():
#    try:
    ext=".mp4"
    print("Please select a video ...")

    while(True):
        filename = easygui.fileopenbox()
        # show an "Open" dialog box and return the path to the selected file


        if(ext not in filename):
            print(filename+"\n"+"Please Select a file that has \".mp4\" in the end\n")
            continue

        break
        # loop to check if ext is not ".mp4" once it's found --- break the loop


        
    

    video = "INSERT INTO video (video_name) VALUES (%s)"
    value = filename
    mycursor.execute(video, (value,))    
    mydb.commit()
    print(mycursor.rowcount, "Video is selected and it's name stored in the database.\n")
    return filename


    #Called in main function

#    except mys
        


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)



# def mappingMatch():

#     while(True):
#         try:
#             print ("\n---------------------------------------------------------\n")
#             matchState = int(input("Enter 0 if the match is new Or 1 if he is allready existing in the database : "))
#             print(matchState)

        
#             if (matchState == 0): 
#                 match = "INSERT INTO match_played (first_team, second_team, match_date, stadium, result) VALUES (%s,%s,%s,%s,%s)"
#                 firstTeam, secondTeam, matchDate, stadium, result = data.matchData()
# ##############################################################
#                 while (hasNumbers(firstTeam) or hasNumbers(secondTeam) or hasNumbers(stadium)):
#                     print("\nFirst team, second team or stadium can't be integers please re enter as strings\n")
#                     firstTeam, secondTeam, matchDate, stadium, result = data.matchData()

            
#                 value = (firstTeam,secondTeam,matchDate,stadium,result)
#                 mycursor.execute(match, value)
#                 mydb.commit()
#                 print(mycursor.rowcount, "Match data is recorded.")
#                 break

#             elif (matchState == 1):
#                 while(True):
#                     #if():
#                     print("\n---------------------------------------------------------\nEnter Match ID: ")
#                     playerId = (input("Match ID: "))
#                     print("")
#                 break

#             else:
#                 print("\nPlease enter a valid input\n")
                
                


#         except mysql.connector.Error as err:
#             print("please follow the represented format in entering data\n---------------------------------------------------------\n")
#             print("First Team: NAME\nSecond Team: NAME\nMatch Date: YYYY-MM-DD\nStadium: NAME\nResult: NUMBER-NUMBER\n")
#         mappingMatch()






def mappingMatch():
   
        fields=[]
        fields=ui.matchDataEntry()
        #to return two options if the match is new or not
        #return new match 5 index firstTeam, secondTeam, ....
        if(len(fields)>1):

           
            match = "INSERT INTO match_played (first_team, second_team, match_date, stadium, result) VALUES (%s,%s,%s,%s,%s)"
            firstTeam, secondTeam, matchDate, stadium, result = fields
            
            
            value = (firstTeam, secondTeam, matchDate, stadium, result)
            mycursor.execute(match, value)
            mydb.commit()
            print(mycursor.rowcount, "Player profile is Created.")

        else:
            #return match ID   
            mycursor.execute("SELECT match_id FROM match_played WHERE match_id=%s", (fields[0],))
            search = mycursor.fetchall()
            print(search)




# def mappingPlayer():
#     while(True):
#         try:

#             print ("\n --------------------------------------------------------------------\n")
#             playerState = int(input("Enter 0 if the player is new Or 1 if he is allready existing in the database : "))
#             print(playerState)



#             if (playerState == 0): 
#                 player = "INSERT INTO player (player_first_name, player_last_name, birth_date, nationality, club_name, number_player, position) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#                 firstName,lastName,birthDate,nationality,clubName,number,position = data.playerData()
# ##############################################################
#                 while (hasNumbers(firstName) or hasNumbers(lastName) or hasNumbers(nationality) or hasNumbers(clubName) or hasNumbers(position)):
#                     print("First Name, Nast Name, Nationality, Club Name or Position can't be integers please re enter as strings")
#                     firstName,lastName,birthDate,nationality,clubName,number,position = data.playerData()
            
            
#                 value = (firstName,lastName,birthDate,nationality,clubName,number,position)
#                 mycursor.execute(player, value)
#                 mydb.commit()
#                 print(mycursor.rowcount, "Player profile is Created.")
#                 break

#             elif (playerState == 1):
#                 while(True):
#                     print("\n---------------------------------------------------------\nEnter Player ID: ")
#                     playerId = (input("Player ID: "))

#                     mycursor.execute("SELECT player_id FROM player WHERE id=?", playerId)
#                     search = mycursor.fetchall()

#                     if search is None:
#                         print("No matching found")
#                     else:
#                         for row in search:
#                             print (row[0]+"\n") 

#                 break

#             else:
#                     print("\nPlease enter a valid input\n")
                    

#         except mysql.connector.Error as err:
#             print("please follow the represented format in entering data\n---------------------------------------------------------\n")
#             print("First Name: NAME\nLast Name: NAME\nBirth Date: YYYY-MM-DD\nNationality: NAME\nClub Name: NAME\nPlayer Number: NN\nPosition: NAME OR APPREVEIATION\n")
            

def mappingPlayer():

        fields=[]
        fields=ui.playerDataEntry()
        print(fields)
        if(len(fields)>1):
        #to return two options if the player is new or not
            

            #return new player 7 index firstName, lastName, ....
            player = "INSERT INTO player (player_first_name, player_last_name, birth_date, nationality, club_name, number_player, position) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            firstName,lastName,birthDate,nationality,clubName,number,position = fields
            ##############################################################
            
            
            value = (firstName,lastName,birthDate,nationality,clubName,number,position)
            mycursor.execute(player, value)
            mydb.commit()
            print(mycursor.rowcount, "Player profile is Created.")

        else:
            #return player ID       
            mycursor.execute("SELECT player_id FROM player WHERE player_id=%s", (fields[0],))
            search = mycursor.fetchall()
            print(search)




def distance(x1,y1,x2,y2):

    x_ratio = 4200/450
    y_ratio = 2200/225

    dist = math.sqrt(x_ratio*(x2 - x1)**2 + y_ratio * (y2 - y1)**2)  
    return dist


def mappingPerformance():

    performance = "INSERT INTO performance_player (distance_covered, avg_speed) VALUES (%s,%s)"

    value=(7.8,20.4)
    mycursor.execute(performance, value)
        
    mydb.commit()
    print(mycursor.rowcount, "Performance of the requested player is recorded.")







