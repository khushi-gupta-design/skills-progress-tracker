# skills-progress-tracker
my skills progress tracker 
Skills Progress Tracker

A simple command-line tool built in Python to track my learning progress across Python, SQL, and Power BI — part of my ongoing journey toward becoming a data analyst.

Features

Track multiple skills, each with its own set of sub-topics and completion percentages
Visual progress bars for each skill (e.g. [$$$$$$$###] 70.0%)
Persistent storage — progress is saved to and loaded from a JSON file, so nothing is lost between runs
Auto-generated summary text, ready to copy-paste into a LinkedIn post

Tech / Concepts Used

Python (Object-Oriented Programming — classes, methods)
Dictionaries and loops
File handling with JSON (json.dump / json.load)
f-strings for formatted output

How It Works

The project has two main classes:

Skill — represents a single skill (e.g. Python), holding a dictionary of sub-topics and their completion percentages. Includes methods to add topics, calculate average progress, and generate a text-based progress bar.
SkillTracker — manages multiple Skill objects. Includes methods to add skills, display all progress, save/load data to a JSON file, and generate a LinkedIn-ready summary.

Sample Output

Python: [$$$$$$$###] 70.0%
SQL: [$$$$$$$$###] 75.0%
Power BI: [$$$#######] 30.0%

How to Run

python project.py

Progress is automatically saved to progress.json in the same folder, and reloaded the next time the script runs.

What's Next

Converting this into a web app (likely with Streamlit) for a more visual, shareable version
Adding an update_topic method to edit existing progress



