import os
from datetime import datetime, timezone

LOG_FILE = "activity_log.md"

def update_activity_log():
    now_utc = datetime.now(timezone.utc)
    timestamp_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    date_str = now_utc.strftime("%Y-%m-%d")
    
    # Ensure log file exists with header
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("# 🚀 Automated Contribution Log\n\n")
            f.write("This file is automatically updated on a schedule to log repository contributions.\n\n")
            f.write("| Date | Timestamp | Activity Status |\n")
            f.write("| :--- | :--- | :--- |\n")
            
    # Append log entry
    log_entry = f"| {date_str} | `{timestamp_str}` | ✅ Auto-commit pulse active |\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
        
    print(f"Log entry added: {timestamp_str}")

if __name__ == "__main__":
    update_activity_log()
