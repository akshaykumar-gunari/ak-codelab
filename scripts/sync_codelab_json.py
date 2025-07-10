import gspread
import json
from datetime import datetime
import os

# ✅ Authenticate using your service account JSON
gc = gspread.service_account(filename="service_account.json")

# ✅ Open your Google Sheet by URL
spreadsheet_url = "https://docs.google.com/spreadsheets/d/179xSRFDvYraYWAMpbPxLWViuwOHEyrM43DnrWPNpQeU/edit"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet("Form Responses 1")

# ✅ Get all rows as dictionaries
records = worksheet.get_all_records()

# ✅ Load existing JSON if it exists
json_file = "daily-challenge/daily-challenge-data.json"
if os.path.exists(json_file):
    with open(json_file, "r") as f:
        current_data = json.load(f)
else:
    current_data = []

# ✅ Gather (date, problemName) to check duplicates properly
existing_keys = {(entry["date"], entry["problemName"]) for entry in current_data}

new_entries = []

for row in records:
    date_str = row["Date"].strip()

    if not date_str:
        print(f"⚠️ Skipping row with empty date: {row}")
        continue

    # If date includes time (like: '10/07/2025 11:23:01'), split to get just the date part
    date_part = date_str.split()[0]

    try:
        # Use correct format: DD/MM/YYYY (your format)
        date_obj = datetime.strptime(date_part, "%d/%m/%Y")
    except ValueError:
        print(f"⚠️ Invalid date format, skipping row: {row}")
        continue

    date_iso = date_obj.strftime("%Y-%m-%d")
    day_name = date_obj.strftime("%A")

    row_key = (date_iso, row["Problem Name"])
    if row_key in existing_keys:
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
    new_entries.append(new_entry)

# ✅ Write updated JSON if new rows were added
if new_entries:
    with open(json_file, "w") as f:
        json.dump(current_data, f, indent=2)
    print(f"✅ Synced {len(new_entries)} new rows to {json_file} (Total: {len(current_data)})")
else:
    print(f"✅ No new rows found. JSON is up to date! (Total: {len(current_data)})")