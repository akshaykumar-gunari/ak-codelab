import gspread
import json
from datetime import datetime
import os

# 1️⃣ Authenticate
gc = gspread.service_account(filename="service_account.json")

# 2️⃣ Open Google Sheet
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1Iksef33n4A8M6AE87CFzsIso22SFCs_OwL3IzLku3Us/edit"
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.worksheet("Form Responses 1")

# 3️⃣ Get all rows
records = worksheet.get_all_records()
print(f"✅ Fetched {len(records)} rows from the sheet")

# 4️⃣ Load existing JSON, fallback if empty
json_file = "daily-challenge/daily-challenge-data.json"
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

    # Split to handle potential timestamps
    date_part = date_str.split()[0]

    # Try multiple date formats
    date_obj = None
    date_formats = [
        "%Y/%m/%d",     # 2025/08/06 (YYYY/MM/DD) - your current format
        "%Y-%m-%d",     # 2025-08-06 (YYYY-MM-DD)
        "%m/%d/%Y",     # 8/6/2025 (MM/DD/YYYY)
        "%d/%m/%Y",     # 6/8/2025 (DD/MM/YYYY)
    ]

    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(date_part, fmt)
            print(f"✅ Parsed date {date_part} using format {fmt}")
            break
        except ValueError:
            continue

    if date_obj is None:
        print(f"❌ Could not parse date: {date_part}")
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
        "problemStatementLink": row["Problem Statement Link"],
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
