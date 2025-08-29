# app.py

import streamlit as st
from utils.ai_parser import parse_tasks, load_manual_tasks
from datetime import datetime

st.title("AI Task Organizer")

mode = st.radio("Choose input method:", ["Manual (Paste JSON)", "Automatic (Basic Stub)"])

def parse_time_string(t: str):
    """Try to convert time strings like '5pm', 'tomorrow' into real datetime objects."""
    if not t or t.lower() == "null":
        return None
    try:
        return datetime.strptime(t, "%I%p")  # e.g. "5pm"
    except:
        return t  # keep as string if not parseable

if mode == "Automatic (Basic Stub)":
    user_input = st.text_area("Enter your tasks:")
    if st.button("Parse Automatically"):
        if user_input.strip():
            tasks = parse_tasks(user_input)
            st.json(tasks)
        else:
            st.warning("Please enter some tasks first.")

elif mode == "Manual (Paste JSON)":
    manual_input = st.text_area("Paste JSON output from ChatGPT here:")
    if st.button("Load JSON"):
        if manual_input.strip():
            tasks = load_manual_tasks(manual_input)
            if "tasks" in tasks:
                st.success("✅ Schedule created:")
                # sort tasks with times first
                sorted_tasks = sorted(
                    tasks["tasks"], 
                    key=lambda t: t["time"] if t["time"] else "zzz"
                )
                for t in sorted_tasks:
                    task = t["task"]
                    time = t["time"] if t["time"] else "unscheduled"
                    st.write(f"🕒 **{time}** → {task}")
            else:
                st.error(tasks.get("error", "Invalid JSON"))
        else:
            st.warning("Please paste the JSON first.")
