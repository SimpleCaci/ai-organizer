import json
import datetime

def generate_schedule(tasks_json, mode="normal"):
    """
    mode: "tired", "normal", "focus"
    """
    try:
        tasks = json.loads(tasks_json)
    except:
        return "⚠️ Could not parse tasks."

    schedule = []
    start_time = datetime.datetime.now().replace(hour=9, minute=0)  # Start at 9 AM

    for task in tasks:
        duration = 60  # default 1 hour

        if mode == "tired":
            if task.get("priority") == "high":
                duration = 45
            else:
                continue  # skip non-urgent tasks
        elif mode == "focus":
            duration = 90  # deeper blocks
        else:
            duration = 60

        end_time = start_time + datetime.timedelta(minutes=duration)

        schedule.append({
            "task": task.get("task", "Untitled"),
            "start": start_time.strftime("%I:%M %p"),
            "end": end_time.strftime("%I:%M %p"),
            "priority": task.get("priority", "medium")
        })

        start_time = end_time  # update for next block

    return schedule
