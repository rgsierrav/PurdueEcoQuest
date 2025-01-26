import pandas as pd
import random
from flask import jsonify

# Global Variables
stats = []
events = []
curr_event = []
week = 0

# Load CSV file into Pandas DataFrame
try:
    events = pd.read_csv("/home/rsierrav/mysite/events.csv")
except FileNotFoundError:
    raise Exception("Error: events.csv not found at the specified path.")
except pd.errors.ParserError:
    raise Exception("Error: Unable to parse events.csv. Please check the file format.")

# Helper function to ensure all data is JSON serializable
def make_serializable(data):
    """
    Ensure all elements in a list are JSON-serializable by converting
    non-standard types (e.g., int64, float64, Timestamp) to standard Python types.
    """
    serializable_data = []
    for x in data:
        if isinstance(x, (pd.Timestamp, pd.Timedelta)):
            serializable_data.append(str(x))  # Convert Pandas Timestamps to strings
        elif isinstance(x, (int, float, str)):
            serializable_data.append(x)  # Keep standard types as is
        else:
            try:
                serializable_data.append(x.item())  # Convert NumPy types to native Python types
            except AttributeError:
                serializable_data.append(x)  # Keep as is if no conversion is possible
    return serializable_data

# Start the game
def start():
    global stats, week, curr_event
    stats = [90, 80, 0, 50, 0]  # Initialize stats [health, happiness, money, academics, ecopoints]
    stats[2] = random.randint(20, 50)  # Randomize starting money
    week = 1
    curr_event = events.iloc[0].tolist()
    curr_event = make_serializable(curr_event)  # Ensure JSON serializability

    return jsonify({
        "Name": curr_event[0],
        "Description": curr_event[1],
        "Choice1": curr_event[2],
        "Choice2": curr_event[4],
    })

# Handle player choices
def choice_made(choice):
    global stats, curr_event
    if not curr_event or not stats:
        return jsonify({"error": "Game not started. Please start the game first."}), 400

    # Get modifiers based on the choice made
    modifiers = curr_event[3] if choice == 1 else curr_event[5]
    modifiers = modifiers.split(",")  # Split the modifiers into a list of strings
    modifiers = [int(mod) for mod in modifiers]  # Convert all modifiers to integers

    # Update stats based on modifiers
    stats[0] = max(0, min(100, stats[0] + modifiers[0]))  # Health
    stats[1] = max(0, min(100, stats[1] + modifiers[1]))  # Happiness
    stats[2] = max(0, stats[2] + modifiers[2])            # Money
    stats[3] = max(0, min(100, stats[3] + modifiers[3]))  # Academics
    stats[4] += modifiers[4]                              # EcoPoints

    return jsonify({
        "Health": stats[0],
        "Happiness": stats[1],
        "Money": stats[2],
        "Academics": stats[3],
        "EcoPoints": stats[4],
    })

# Get the next event
def get_event():
    global week, curr_event, stats
    if not stats:
        return jsonify({"error": "Game not started. Please start the game first."}), 400

    if week > 16:  # Check if the semester is over
        return jsonify({
            "Name": "Summary",
            "Description": summary(),
        })

    week += 1

    # Check conditions to select the next event
    if stats[0] < 15:  # Health is too low
        curr_event = events.iloc[1].tolist()
    elif stats[1] < 30:  # Happiness is too low
        curr_event = events.iloc[2].tolist()
    elif stats[3] < 20:  # Academics are too low
        curr_event = events.iloc[3].tolist()
    else:  # Select a random event
        rand_event_index = random.randint(4, len(events) - 1)
        curr_event = events.iloc[rand_event_index].tolist()

    curr_event = make_serializable(curr_event)  # Ensure JSON serializability

    return jsonify({
        "Name": curr_event[0],
        "Description": curr_event[1],
        "Choice1": curr_event[2],
        "Choice2": curr_event[4],
    })

# Summary of the game
def summary():
    return f"Game Over! Final Stats - Health: {stats[0]}, Happiness: {stats[1]}, Money: {stats[2]}, Academics: {stats[3]}, EcoPoints: {stats[4]}"
