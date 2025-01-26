import pandas as pd
import random

"""
    PurdueEcoQuest begins the execution of the program
    stats = [health, happiness, money, academics, ecopoints]
    will intialize stats to [95, 80, random, 50, 0]
    
"""

class Game:
    global stats
    global events
    def __init__(self):
        # [health, happiness, money, academics, EcoPoints]
        self.stats = [95, 80, 0, 50, 0]
        # setting money as random
        stats[2] = random.randint(20, 300)

        self.events = pd.read_csv("events.csv")

        #TODO return move-in info


    # Will return string to send to javascript
    def get_event(self):
        #if health is too low
        if (stats[0] < 15):
            ## TODO: trigger sick
        #if happiness is too low
        elif (stats[1] < 30):
            ## TODO: trigger breakdown
        # if academics too low
        elif (stats[3] < 20):
            ## TODO: trigger academic probation warning
        else:
            ##TODO: pick random event

    def update_stats(self, event_num, choice):
        event = events.

#TODO: create start(), get_event(), get_stats(), update_stats() func



def PurdueEcoQuest():
    # [health, happiness, money, academics, EcoPoints]
    stats = [95, 80, 0, 50, 0]
    # setting money as random
    stats[2] = random.randint(20, 300)

    events = pd.read_csv("events.csv")

    # move-in counts as week 0
    # TODO: activate move-in event
    # for sixteen weeks, one event per week
    for week in range(1, 17):
        #if health is too low
        if (stats[0] < 15):
            ## TODO: trigger sick
        #if happiness is too low
        elif (stats[1] < 30):
            ## TODO: trigger breakdown
        # if academics too low
        elif (stats[3] < 20):
            ## TODO: trigger academic probation warning
        else:
            ##TODO: pick random event

    #after 16 weeks, do summary
    summary(stats)

"""
    update_stats will update stats with modifiers and return new list
"""
def update_stats(currstats, modifier):
    #update health
    currstats[0] += modifier[0]
    if (currstats[0] < 0):
        currstats[0] = 0
    elif (currstats[0] > 100):
        currstats[0] = 100

    #update happiness
    currstats[1] += modifier[1]
    if (currstats[1] < 0):
        currstats[1] = 0


    # update money
    # a check to make sure they have enough money should have already been put in place
    currstats[2] -= modifier[2]

    # update academics
    currstats[3] += modifier[3]
    if (currstats[3] < 0):
        currstats[3] = 0

    # update ecopoints
    currstats[4] += modifier[4]

    return currstats

def summary(stats):




PurdueEcoQuest()





