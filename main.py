import tracking as track
import numpy as np
import heat as ht
import gif as gf
import pick_coordinates
import mappingTables as mt
import uiTesting as ui
import t 
import time



stop = 0

def main ():
    ## welcome
    ui.start()
    ## sport type 2 options
    sport = ui.sports()

    if sport == 1 : 
        #video pick
        filename=mt.mappingVideo()

        #click on 5 points from first frame
        cord_array = pick_coordinates.c
        coordinates = pick_coordinates.pick(filename)


        ##get data from user
        playerId , matchId = mt.checkEntry()

        #tracking returing coordintaes frames total distance max speed min speed and average speed 
        x , y,  frames , total_distance , max_speed , min_speed ,  average_speed = track.run(filename,np.array(coordinates),sport)

        # store coordinates for further use
        mt.mappingCoordinates(x,y,frames,playerId,matchId)
        # store peformance for further use and retrive 
        mt.mappingPerformance(playerId ,matchId , total_distance , average_speed)


        time.sleep(2)
        
        #mt.mappingCoordinates(x,y,frames)
        ht.heat(x,y,sport)
        gf.animation(x,y,sport)

    else :

        ok =ui.tennisSupportDB()

        if ok == 0 :
            quit()

        filename = t.filepick()
        
        #click on 5 points from first frame
        cord_array = pick_coordinates.c
        coordinates = pick_coordinates.pick(filename)
        x , y,  frames , total_distance , max_speed , min_speed ,  average_speed = track.run(filename,np.array(coordinates),sport)
        print("average speed :" + str(average_speed))
        print("max speed :" + str(max_speed))
        print("min speed :" + str(min_speed))

        ht.heat(x,y,sport)
        gf.animation(x,y,sport)


main()

