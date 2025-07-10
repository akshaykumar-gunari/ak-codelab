import gspread
import json
from datetime import datetime
import os

# 1️⃣ Authenticate
gc = gspread.service_account(filename="service_account.json")

# 2️⃣ Open Google Sheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/179xSRFDvYraYWAMpbPxLWViuwOHEyrM43DnrWPNpQeU/edit"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet("Form Responses 1")

# 3️⃣ Get all rows
records = worksheet.get_all_records()
print(f"✅ Fetched {len(records)} rows from the sheet")

# 4️⃣ Load existing JSON, fallback if empty
json_file = "journal-data.json"
current_data = []
if os.path.exists(json_file):
    with open(json_file, "r") as f:
        try:
            current_data = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ {json_file} is empty or invalid, starting fresh.")
            current_data = []

print(f"✅ Loaded {len(current_data)} entries from JSON")

# 5️⃣ Build unique keys
existing_keys = {(entry["date"], entry["problemName"]) for entry in current_data}
print(f"✅ Existing keys: {existing_keys}")

new_entries = []

# 6️⃣ Process rows
for row in records:
    print(f"🔍 Checking row: {row}")

    date_str = row["Date"].strip()
    if not date_str:
        print(f"⚠️ Skipping row with empty date: {row}")
        continue

    date_part = date_str.split()[0]
    try:
        date_obj = datetime.strptime(date_part, "%d/%m/%Y")
    except ValueError:
        try:
            date_obj = datetime.strptime(date_part, "%m/%d/%Y")
        except ValueError:
            print(f"❌ Invalid date: {date_part}")
            continue

    date_iso = date_obj.strftime("%Y-%m-%d")
    day_name = date_obj.strftime("%A")

    row_key = (date_iso, row["Problem Name"])
    if row_key in existing_keys:
        print(f"⏭️ Already exists: {row_key}")
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

    new_entries.append(new_entry)
    current_data.append(new_entry)
    print(f"✅ Added: {row_key}")

# 7️⃣ Write only if new
if new_entries:
    with open(json_file, "w") as f:
        json.dump(current_data, f, indent=2)
    print(f"✅ Wrote {len(new_entries)} new rows to {json_file} — total: {len(current_data)}")
else:
    print("⚠️ No new rows. JSON unchanged.")