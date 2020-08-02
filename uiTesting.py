import ui 
from operator import itemgetter 




def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def playerDataEntry():
    playerid = ""
    
    PlayerState = ui.askUser("Is this a new player ? ")
    if (PlayerState):
            player = ui.informationForm("Please Enter Player's Information",["First Name","Last Name","Birth Date","Nationlity","Club Name","Player Number","Position of Playing"])
            if (player == 1):
                ##Back
                print("back")
            else :

                FirstName, LastName, BirthDate, Nationlity, Club, PlayerNumber, Position =  itemgetter(0,1,2,3,4,5,6)(player) 
                return FirstName, LastName, BirthDate, Nationlity, Club, PlayerNumber, Position



    else:
            playerid = ui.informationForm("Please Enter Player's ID !",["Player ID"])
            return playerid

def matchDataEntry():

    matchid = ""
    match = []


    MatchState = ui.askUser("Is this a new match ? ")
    if (MatchState):
        match = ui.informationForm("Please Enter Match's Information",["First Team","Second Team" , "Match Date","result","Stadium"])
        if(match == 1):
            ##Back
            print("Back")
        else:
            FirstTeam, SecondTeam, MatchDate, Stadium, Result =  itemgetter(0,1,2,3,4)(match)
            return FirstTeam, SecondTeam, MatchDate, Stadium, Result
    else :
        matchId = ui.informationForm("Please Enter Match's ID !",["Match ID"])
        return matchId
