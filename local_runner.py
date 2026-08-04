import time
import subprocess
from datetime import datetime

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def commit_and_push():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Running auto-commit...")
    
    # 1. Update activity log
    out, err, code = run_cmd("python auto_commit.py")
    if code != 0:
        print(f"Error updating log: {err}")
        return

    # 2. Stage changes
    run_cmd("git add activity_log.md")
    
    # 3. Check for diff
    _, _, code = run_cmd("git diff --staged --quiet")
    if code == 0:
        print("No changes detected.")
        return

    # 4. Commit & Push
    out, err, code = run_cmd('git commit -m "chore: automated contribution update"')
    if code != 0:
        print(f"Commit error: {err}")
        return
        
    out, err, code = run_cmd("git push")
    if code == 0:
        print("Successfully committed and pushed to GitHub!")
    else:
        print(f"Push error: {err}")

if __name__ == "__main__":
    import sys
    interval_sec = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    print(f"🚀 Local Auto-Commit Runner Active! (Interval: {interval_sec} seconds)")
    print("Press Ctrl+C to stop.\n")
    
    while True:
        try:
            commit_and_push()
            time.sleep(interval_sec)
        except KeyboardInterrupt:
            print("\nStopped local runner.")
            break
