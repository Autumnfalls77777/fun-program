# 🤖 GitHub Auto Commit System

An automated, hands-free GitHub repository maintainer that updates an activity log on a scheduled timer (default: every 12 hours) using Python and GitHub Actions.

---

## ⚙️ How to Change the Auto-Commit Interval / Cooldown

You can easily adjust how often auto-commits happen by editing **[`.github/workflows/auto_commit.yml`](.github/workflows/auto_commit.yml)** on line 14:

```yaml
  schedule:
    # Change the cron string below to adjust the interval:
    - cron: '0 */12 * * *'  # Runs every 12 hours
```

### Quick Cron Examples:
- **Every 12 Hours (Default):** `'0 */12 * * *'`
- **Every 6 Hours:** `'0 */6 * * *'`
- **Every 1 Hour:** `'0 * * * *'`
- **Once Daily (at midnight):** `'0 0 * * *'`

---

## 🚀 One-Time Setup Instructions

Follow these quick steps to launch the system on GitHub:

### Step 1: Initialize Git & Push to GitHub

Open terminal in this project directory and run:

```bash
git init
git add .
git commit -m "feat: initial commit for auto commit system"
git branch -M main
git remote add origin https://github.com/Autumnfalls77777/fun-program.git
git push -u origin main
```


---

### Step 2: Grant Write Permissions to GitHub Actions (CRITICAL)

To allow GitHub Actions to commit and push changes back to your repository automatically:

1. Open your repository on **GitHub.com**.
2. Click **Settings** (top menu of the repository).
3. In the left sidebar, expand **Actions** → click **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Click **Save**.

---

## 🎯 Verification & Manual Runs

- **Automatic:** GitHub Actions will now trigger automatically every 12 hours without any manual action!
- **Manual Trigger:** If you want to test it immediately, go to your GitHub repository's **Actions** tab → click **Auto Commit Workflow** on the left → click **Run workflow**.

---

## 📁 File Structure

- `auto_commit.py` — Python script that appends timestamped entries to `activity_log.md`.
- `activity_log.md` — Markdown file storing execution history.
- `.github/workflows/auto_commit.yml` — GitHub Actions automated workflow configuration.
