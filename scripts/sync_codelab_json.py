import gspread
import pandas as pd
import json
from datetime import datetime
import os

# ✅ Authenticate using your service account
gc = gspread.service_account(filename="service_account.json")

# ✅ Open the Google Sheet by URL
spreadsheet_url = "https://docs.google.com/spreadsheets/d/179xSRFDvYraYWAMpbPxLWViuwOHEyrM43DnrWPNpQeU/edit"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet("Form Responses 1")

# ✅ Get all rows as a list of dicts
records = worksheet.get_all_records()

# ✅ Load existing JSON if it exists
json_file = "journal-data.json"
if os.path.exists(json_file):
    with open(json_file, "r") as f:
        current_data = json.load(f)
else:
    current_data = []

# ✅ Track existing dates to prevent duplicates
existing_dates = {entry["date"] for entry in current_data}

# ✅ Add only NEW rows
new_rows = 0
for row in records:
    date_str = row["Date"]

    if not date_str.strip():
        print(f"⚠️ Skipping row with empty date: {row}")
        continue

    try:
        # Handle possible time part
        if " " in date_str:
            date_obj = datetime.strptime(date_str.strip(), "%m/%d/%Y %H:%M:%S")
        else:
            date_obj = datetime.strptime(date_str.strip(), "%m/%d/%Y")
    except ValueError as e:
        print(f"⚠️ Invalid date format in row: {row} -> {e}")
        continue

    date_iso = date_obj.strftime("%Y-%m-%d")
    day_name = date_obj.strftime("%A")

    if date_iso in existing_dates:
        continue

    new_entry = {
        "date": date_iso,
        "day": day_name,
        "problemName": row["Problem Name"],
        "problemStatement": row["Problem Statement"],
        "codeLink": row["Code Link"],
        "keywords": [kw.strip() for kw in row["Keywords (Comma Separated)"].split(",")],
        "difficulty": row["Difficulty Level"].lower()
    }

    current_data.append(new_entry)
    new_rows += 1

# ✅ Write updated JSON if there’s new data
with open(json_file, "w") as f:
    json.dump(current_data, f, indent=2)

print(f"✅ Synced {len(current_data)} total entries to {json_file} (+{new_rows} new rows)")