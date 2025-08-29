# utils/ai_parser.py

import json
import dateparser
from datetime import datetime, timedelta

def load_manual_tasks(json_text: str):
    """
    Parse manually pasted JSON from ChatGPT.
    Converts 'time' fields into datetime objects when possible.
    """
    try:
        data = json.loads(json_text)
        for t in data.get("tasks", []):
            raw_time = t.get("time")
            if raw_time and raw_time.lower() != "null":
                dt = dateparser.parse(raw_time, settings={"PREFER_DATES_FROM": "future"})
                t["parsed_time"] = dt if dt else raw_time
            else:
                t["parsed_time"] = None
        return data
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON: {e}"}
