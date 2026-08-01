import streamlit as st

import json

class Skill:
    def __init__(self, name):
        self.name = name
        self.topics = {}

    def add_topic(self, topic_name, percentage):
        self.topics[topic_name] = percentage

    def get_average_progress(self):
        if len(self.topics) == 0:
            return 0
        return sum(self.topics.values()) / len(self.topics.values())

    def get_progress_bar(self):
        avg = self.get_average_progress()
        filled = int(avg / 10)
        empty = 10 - filled
        bar = "$" * filled + "#" * empty
        return bar


class SkillTracker:
    def __init__(self):
        self.skills = {}

    def add_skill(self, skill_name):
        self.skills[skill_name] = Skill(skill_name)

    def show_all(self):
        for skill_name, skill_obj in self.skills.items():
            bar = skill_obj.get_progress_bar()
            avg = skill_obj.get_average_progress()
            print(f"{skill_name}: [{bar}] {avg}%")

    def save_to_file(self, filename="progress.json"):
        data = {}
        for skill_name, skill_obj in self.skills.items():
            data[skill_name] = skill_obj.topics

        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename="progress.json"):
        with open(filename, "r") as f:
            data = json.load(f)

        for skill_name, topics in data.items():
            self.add_skill(skill_name)
            for topic_name, percentage in topics.items():
                self.skills[skill_name].add_topic(topic_name, percentage)

    def generate_linkedin_summary(self):
        summary = "My Skill Progress Update\n\n"
        for skill_name, skill_obj in self.skills.items():
           avg = skill_obj.get_average_progress()
           summary = summary + f"{skill_name}: {avg}%\n"
        summary = summary + "\n#DataAnalyst #LearningInPublic"
        return summary


st.title("My Skills Progress Tracker")
st.write("Tracking my journey in Python, SQL, and Power BI")

password = st.text_input("ENTER PASSWORD", type="password")
edit_mode = (password == "200630")

tracker = SkillTracker()

tracker.add_skill("Python")

if edit_mode:
    basics_done = st.checkbox("Python - Basics", value=True)
    pandas_done = st.checkbox("Python - Pandas", value=False)
else:
    basics_done = True
    pandas_done = False
    basics_value = 100 if basics_done else 0
pandas_value = 100 if pandas_done else 0
tracker.skills["Python"].add_topic("Basics", basics_value)
tracker.skills["Python"].add_topic("Pandas", pandas_value)
  

if edit_mode:
    SQL_BASICS = st.checkbox("SQL - Basics", value=True)
    SQL_ADVANCED = st.checkbox("SQL - Advanced", value=True)
else:
    SQL_BASICS = True
    SQL_ADVANCED = False
Basics_value = 100 if  SQL_BASICS else 0
Advanced_value = 100 if SQL_ADVANCED else 0
tracker.skills["SQL"].add_topic("Basics", Basics_value)
tracker.skills["SQL"].add_topic("Advanced", Advanced_value)
   

if edit_mode:
   POWER_BI = st.checkbox("POWERBI", value=True)
else:
    POWERBI = True
POWERBI_value = 100 if POWER_BI else 0
tracker.skills["Power BI"].add_topic("Dashboards", dashboards_value)


if edit_mode:
    AI_BASICS = st.checkbox("AIAUTOMATION - Basics", value=True)
    AI_ADVANCED = st.checkbox("AIAUTOMATION - Advanced", value=False)
else:
    AI_BASICS = False
    AI_ADVANCED = False
Basics_value = 100 if AI_BASICS else 0
Advanced_value = 100 if AI_ADVANCED else 0
tracker.skills["AIAUTOMATION"].add_topic("Basics", value=False)
tracker.skills["AIAUTOMATION"].add_topic("Advanced",value=False)
    

for skill_name, skill_obj in tracker.skills.items():
    avg = skill_obj.get_average_progress()
    st.subheader(skill_name)
    st.progress(int(avg))
    st.write(f"{avg}%")
