import pandas as pd
import random
import json
from flask import jsonify

stats = []
events = pd.read_csv("events.csv")
curr_event = None
week = 0
def start():
    global week
    global stats
    global curr_event
    #[health, happiness, money, academics, ecopoints]
    stats = [90, 80, 0, 50, 0]
    #their money is randomized
    stats[2] = random.randint(20, 50)
    week = 1

    #set move-in to curr_event
    curr_event = events.iloc[0].tolist()

    return jsonify(
        {
            "Name": curr_event[0],
            "Description": curr_event[1],
            "Choice1" : curr_event[2],
            "Choice2" : curr_event[4],
        }
    )

def choice_made(choice):
    global stats
    modifiers = None
    if (choice == 1):
        modifiers = curr_event[3]
    else:
        modifiers = curr_event[5]

    modifiers = modifiers.split(",")

    # now update stats
    # health
    stats[0] += int(modifiers[0])
    if stats[0] > 100:
        stats[0] = 100
    elif stats[0] < 0:
        stats[0] = 0

    #happiness
    stats[1] += int(modifiers[1])
    if stats[1] > 100:
        stats[1] = 100
    elif stats[1] < 0:
        stats[1] = 0

    #money
    stats[2] += int(modifiers[2])
    if stats[2] < 0:
        stats[2] = 0

    # academics
    stats[3] += int(modifiers[3])
    if stats[3] > 100:
        stats[3] = 100
    elif stats[3] < 0:
        stats[3] = 0

    # ecopoints
    stats[4] += int(modifiers[4])

    return jsonify(
        {
            "Health": stats[0],
            "Happiness": stats[1],
            "Money": stats[2],
            "Academics": stats[3],
            "EcoPoints": stats[4],
        }
    )

def get_event():
    #check if semester is over
    global week
    global curr_event
    if (week > 16):
        return jsonify(
            {
                "Name": "Summary",
                "Desciption" : summary(),
            }
        )

    week += 1

    #if health is too low
    if (stats[0] < 15):
        curr_event = events.iloc[1].tolist()
    #if happiness is too low
    elif (stats[1] < 30):
        curr_event = events.iloc[2].tolist()
    # if academics too low
    elif (stats[3] < 20):
        curr_event = events.iloc[3].tolist()
    else:
        rand_event_index = random.randint(4, len(events) - 1)
        curr_event = events.iloc[rand_event_index].tolist()

    return jsonify(
        {
            "Name": curr_event[0],
            "Description": curr_event[1],
            "Choice1" : curr_event[2],
            "Choice2" : curr_event[4],
        }
    )


def summary():
    sum = ""


    return sum
