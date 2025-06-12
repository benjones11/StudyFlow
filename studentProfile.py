import json
import os

ProfilePath = "studentProfile.json"

def load_profile():
    if os.path.exists(ProfilePath):
        with open(ProfilePath, 'r') as file:
            return json.load(file)
    else:
        return create_new_profile()

def save_profile(profile): 
    with open(ProfilePath, 'w') as file:
        json.dump(profile, file, indent=2)
    print("profile saved successfully.")

def create_new_profile():
    print("creating a new profile...")
    name = input("Enter your name: ")
    preferred_study_time = input("Preferred study time (Morning/Afternoon/Evening/Night): ")
    # Expand studySchedule later
    average_Session_Minutes = int(input("Average session minutes: "))
    profile = {
        "name": name,
        "preferredStudyTime": preferred_study_time,
        "studySchedule": {},
        "averageSessionMinutes": average_Session_Minutes, 
    }
    return profile
    print("profile created successfully.")