import mysql.connector
import numpy as np
import itertools
import easygui
import math
import uiTesting as ui
import easygui



mydb = mysql.connector.connect(host="localhost", user="playertrack", password="123123", database="playertrack")
mycursor = mydb.cursor()


def checkEntry():
    playerData = ui.playerDataEntry()
    print(playerData)
    
    print("\nCheck Entry\n")


    
       

    matchData = ui.matchDataEntry()
    print(matchData)

    

    return playerData, matchData


def mappingCoordinates(x,y,frames , playerId,matchId ):

    zipped=zip(x,y,frames)
    type(zipped)

    
    for i, j, f in zipped:
        
        coordinates = "INSERT INTO coordinates_player (id_player, id_match, x_coordinate, y_coordinate, current_frame) VALUES (%s,%s,%s,%s,%s)"
        print(playerId)
        print(matchId)
        value=( playerId, matchId, int(i), int(j), int(f))
        mycursor.execute(coordinates, value)
        

    mydb.commit()
    print(mycursor.rowcount, "Player Record is Inserted.")
    easygui.msgbox("Player Record is Inserted","Report Message", "OK")

    #Called in main function

        

def mappingVideo():
    ext=".mp4"

    while(True):
        try:
            filename = easygui.fileopenbox("Please Select Video")
            # show an "Open" dialog box and return the path to the selected file


            if(ext not in filename):

                easygui.msgbox("Please Select a file that has \".mp4\" extention","Wrong Entry Message","OK")
                continue

            
            # loop to check if ext is not ".mp4" once it's found --- break the loop



            video = "INSERT INTO video (video_name) VALUES (%s)"
            value = filename
            mycursor.execute(video, (value,))    
            mydb.commit()
            print(mycursor.rowcount, "Video is selected and it's name stored in the database.\n")
            return filename

        except mysql.connector.Error as e:
            exception=easygui.ccbox("The video name is already stored in the database would you like to continue?", "Warning Message")

            if (exception):     # show a Continue/Cancel dialog
                return filename  # user chose Continue
            else:  # user chose Cancel
                continue

    #Called in main function
        


# def hasNumbers(inputString):
#     return any(char.isdigit() for char in inputString)



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











# def mappingMatch():
   
#         matchData=ui.matchDataEntry()
#         #to return two options if the match is new or not
#         #return new match 5 index firstTeam, secondTeam, ....
#         if(len(matchData)>1):

           
#             match = "INSERT INTO match_played (first_team, second_team, match_date, stadium, result) VALUES (%s,%s,%s,%s,%s)"
#             firstTeam, secondTeam, matchDate, stadium, result = matchData
            
            
#             value = (firstTeam, secondTeam, matchDate, stadium, result)
#             mycursor.execute(match, value)
#             mydb.commit()
#             print(mycursor.rowcount, "Player profile is Created.")

#         else:
#             #return match ID   
#             mycursor.execute("SELECT match_id FROM match_played WHERE match_id=%s", (matchData[0],))
#             search = mycursor.fetchall()
#             print(search)




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
            

# def mappingPlayer():

#         playerData=ui.playerDataEntry()
#         if(len(playerData)>1):
#         #to return two options if the player is new or not
            

#             #return new player 7 index firstName, lastName, ....
#             player = "INSERT INTO player (player_first_name, player_last_name, birth_date, nationality, club_name, number_player, position) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#             firstName,lastName,birthDate,nationality,clubName,number,position = playerData
#             ##############################################################
            
            
#             value = (firstName,lastName,birthDate,nationality,clubName,number,position)
#             mycursor.execute(player, value)
#             mydb.commit()
#             print(mycursor.rowcount, "Player profile is Created.")

#         else:
#             #return player ID       
#             mycursor.execute("SELECT player_id FROM player WHERE player_id=%s", (playerData[0],))
#             search = mycursor.fetchall()
#             print(search)




def distance(x1,y1,x2,y2):

    x_ratio = 4200/450
    y_ratio = 2200/225

    dist = math.sqrt(x_ratio*(x2 - x1)**2 + y_ratio * (y2 - y1)**2)  
    return dist


def mappingPerformance(playerId,matchId , total_distance , average_speed):

    performance = "INSERT INTO performance_player (id_player, id_match, distance_covered, avg_speed) VALUES (%s,%s,%s,%s)"
    value=(playerId,matchId,total_distance,average_speed)
    mycursor.execute(performance, value)
        
    mydb.commit()

    easygui.msgbox("Player total distance covered: "+str(round(total_distance))+"m\nPlayer Average speed in the match: "+str(round(average_speed))+"Km/h","Report Message", "OK")
    print(mycursor.rowcount, "Performance of the requested player is recorded.")

    







