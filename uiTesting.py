import ui 
from operator import itemgetter 

def data_entry():
    matchid = ""
    playerid = ""
    match = []
    
    PlayerState = ui.askUser("Is this a new player ? ")
    if (PlayerState):
        player = ui.informationForm("Please Enter Player's Information",["First Name","Last Name","Club","Date of Birth","Nationlity","Position"])
        if (player == 1):
            ##Back
            print("back")
        else :
            FirstName, LastName, Club,BirthDate ,Nationlity , Position =  itemgetter(0,1,2,3,4,5)(player) 


    else:
        playerid = ui.informationForm("Please Enter Player's ID !",["Player ID"])


    MatchState = ui.askUser("Is this a new match ? ")
    if (MatchState):
        match = ui.informationForm("Please Enter Match's Information",["First Team","Second Team" , "Match Date","result","Stadium"])
        if(match == 1):
            ##Back
            print("Back")
        else:
            FirstTeam, SecondTeam , MatchDate ,Result , Stadium =  itemgetter(0,1,2,3,4)(match)
    else :
        matchid = ui.informationForm("Please Enter Match's ID !",["Match ID"])



data_entry()