import ui
from operator import itemgetter
import mysql.connector
import easygui
import datetime
import sys
import heat as ht
import gif as gf

mydb = mysql.connector.connect(host="localhost", user="playertrack", password="123123", database="playertrack")
mycursor = mydb.cursor()


def tennisSupportDB():
    ok = ui.choicesBox("sports-smart-analysis.png",
                       "Warrning : Tennis Doesnt Support Database features yet ! are u sure You want to continue ?",
                       ["Yes", "Cancel"])
    if ok == "Yes":
        return 1
    else:
        return 0


def sports():
    sport = ui.choicesBox("sports-smart-analysis.png", "Please Choose the Sport ?", ["Football", "Tennis", "Back"])
    if (sport == "Football"):
        return 1

    elif (sport == "Tennis"):
        return 0

    elif (sport == "Back"):
        return -1

    else:
        sys.exit(0)


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def isDate(string):
    try:
        datetime.datetime.strptime(string, "%Y-%m-%d")
    except ValueError:
        easygui.msgbox("Date cannot contain letters", "Warnning Message", "OK")


def playerDataEntry():
    while (True):
        PlayerState = ui.askUser("Is this a new player ? ")

        if (PlayerState):
            while (True):
                player = ui.informationForm("Please Enter Player's Information",
                                            ["First Name", "Last Name", "Birth Date", "Nationlity", "Club Name",
                                             "Player Number", "Position of Playing"])

                if (player == 1):
                    break

                elif (player == 2):
                    sys.exit(0)

                else:

                    playerRec = "INSERT INTO player (player_first_name, player_last_name, birth_date, nationality, club_name, number_player, position) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    FirstName, LastName, BirthDate, Nationlity, Club, PlayerNumber, Position = itemgetter(0, 1, 2, 3, 4,
                                                                                                          5, 6)(player)
                    if (hasNumbers(FirstName) or hasNumbers(LastName) or hasNumbers(Nationlity) or hasNumbers(
                            Club) or hasNumbers(Position)):
                        easygui.msgbox("Player name, nationality, club and Position cannot contain Integers",
                                       "Warnning Message", "OK")
                        continue

                    if (not hasNumbers(PlayerNumber) or len(PlayerNumber) > 2):
                        easygui.msgbox("Player Number must be atmost two digits and cannot contain char",
                                       "Warnning Message", "OK")
                        continue

                    if (isDate(BirthDate)):
                        easygui.msgbox("Date must be like the following format YYYY-MM-DD", "Warnning Message", "OK")
                        continue

                    value = (FirstName, LastName, BirthDate, Nationlity, Club, PlayerNumber, Position)
                    mycursor.execute(playerRec, value)
                    mydb.commit()
                    easygui.msgbox("Player Profile is Created and stored in The Database", "Confirmation Message", "OK")
                    return mycursor.lastrowid




        else:
            playerid = ui.informationForm("Please Enter Player's ID !", ["Player ID"])
            if (playerid == 1):
                continue
            playerid = playerid[0]

            print(playerid)
            return playerid


def matchDataEntry():
    while (True):
        MatchState = ui.askUser("Is this a new match ? ")

        if (MatchState):
            while (True):
                match = ui.informationForm("Please Enter Match's Information",
                                           ["First Team", "Second Team", "Match Date", "result", "Stadium"])

                if (match == 1):
                    break

                elif (match == 2):
                    sys.exit(0)

                else:

                    matchRec = "INSERT INTO matches (first_team, second_team, match_date, stadium, result) VALUES (%s,%s,%s,%s,%s)"

                    FirstTeam, SecondTeam, MatchDate, Stadium, Result = itemgetter(0, 1, 2, 3, 4)(match)

                    value = (FirstTeam, SecondTeam, MatchDate, Stadium, Result)

                    mycursor.execute(matchRec, value)

                    mydb.commit()
                    easygui.msgbox("Match data is stored in Database", "Confirmation Message", "OK")
                    return mycursor.lastrowid

        else:

            matchId = ui.informationForm("Please Enter Match's ID !", ["Match ID"])
            if (matchId == 1):
                continue
            matchId = matchId[0]
            print(matchId)
            return matchId


def welcome():
    reply = easygui.buttonbox(image="GD.png", title="Player Performance", choices=["Get Started !!", "Exit"])

    if (reply == "Get Started !!"):
        print("OK")
    else:
        sys.exit(0)


def start():
    while (True):
        reply = easygui.buttonbox(msg="Choose one of the options", title="Selecting Operation",
                                  choices=["Track player", "Retrive Player Performance", "Back", "Cancel"])

        if (reply == "Track player"):
            break


        elif (reply == "Retrive Player Performance"):
            playerid = ui.informationForm("Please Enter Player's ID !", ["Player ID"])
            if (playerid == 1):
                continue
            elif (playerid == 2):
                sys.exit(0)
            playerid = playerid[0]

            matchId = ui.informationForm("Please Enter Match's ID !", ["Match ID"])
            if (matchId == 1):
                continue
            elif (matchId == 2):
                sys.exit(0)
            matchId = matchId[0]

            ht.retrivedHeat(playerid, matchId)
            gf.retrivedAnimation(playerid, matchId)
            response = easygui.ccbox("Do want to do another operation ?", "Confirmation Message")
            if (response):
                continue
            else:
                break

        elif (reply == "Back"):
            return 1



        else:
            sys.exit(0)


def end():
    response = easygui.ccbox("Do want to do another operation ?", "Confirmation Message")
    if (response):
        return -1
    else:
        sys.exit(0)