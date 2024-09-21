import requests
import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

nutrionix_api_key = os.getenv("nutrionix_api_key")
nutrionix_appliction_ID = os.getenv("nutrionix_appliction_ID")

SHEETY_TOKEN = os.getenv("SHEETy_TOKEN")

nutrionix_endpoint = os.getenv("nutrionix_endpoint")
sheety_endpoint = os.getenv("sheety_endpoint")



# Renamed the variable to avoid shadowing built-in function
user_input = input("What exercise did you do today?")

headers = {
    'x-app-id': nutrionix_appliction_ID,
    'x-app-key': nutrionix_api_key
}

exercise_data = {
    "query": user_input
}

# Make request to Nutritionix API to analyze exercise
response = requests.post(url=nutrionix_endpoint, headers=headers, json=exercise_data)
response.raise_for_status()
exercises = response.json()["exercises"]

def addexercise(exercise):
    # Get the current date and time
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    time = datetime.datetime.now().strftime("%X")

    # Extract relevant data from the exercise info
    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    header = {
        "Authorization": "Bearer AAHJBHEJ!@£"
    }
    # Prepare the body for Sheety API request
    body = {
        "workout": {  # Ensure this matches the column names in your Google Sheet
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": calories
        }
    }

    # Debugging: Print the request body before sending it
    print(f"Sending data to Sheety: {body}")

    # Make request to Sheety API to add exercise data to the sheet
    response = requests.post(url=sheety_endpoint, json=body, headers=header)
    
    # Debugging: Print the Sheety API response in case of error
    if response.status_code != 200:
        print(f"Error: {response.status_code}, {response.text}")
    
    response.raise_for_status()
    print(response.text)

# Add each exercise to the sheet
for exercise in exercises:
    addexercise(exercise)
