#!/usr/bin/env python3
import os, random, subprocess, time, datetime, sys

repo = os.environ.get("REPO")
actor_name = os.environ.get("ACTOR_NAME") or "vaghr"
actor_email = os.environ.get("ACTOR_EMAIL") or f"{actor_name}@users.noreply.github.com"
gha_token = os.environ.get("GITHUB_TOKEN")
push_token = os.environ.get("PUSH_TOKEN")

skip_prob = float(os.environ.get("SKIP_PROB") or 0.08)
max_commits = int(os.environ.get("MAX_COMMITS") or 3)
min_sleep = int(os.environ.get("MIN_SLEEP") or 15)
max_sleep = int(os.environ.get("MAX_SLEEP") or 120)
max_start_delay_min = int(os.environ.get("MAX_START_DELAY_MINUTES") or 60)

if max_commits < 0: max_commits = 0
if min_sleep < 1: min_sleep = 1
if max_sleep < min_sleep: max_sleep = min_sleep + 10

start_delay = random.randint(0, max_start_delay_min * 60)
if start_delay > 0:
    print(f"Initial randomized delay: {start_delay} seconds (~{start_delay//60} minutes)")
    time.sleep(start_delay)

# 周末休息模式：周六日跳过概率翻倍
weekday = datetime.datetime.utcnow().weekday()
effective_skip_prob = skip_prob * 2 if weekday >= 5 else skip_prob
if weekday >= 5:
    print(f"Weekend detected (day={weekday}), skip probability doubled to {effective_skip_prob:.2f}")

if random.random() < effective_skip_prob:
    print("Simulated rest day: skipping commits for today.")
    sys.exit(0)

choices = [0,1,2,3]
weights = [10,40,30,20]
commits_to_make = random.choices(choices, weights)[0]
commits_to_make = min(commits_to_make, max_commits)
print(f"Will make {commits_to_make} commit(s) this run.")

subprocess.check_call(["git", "config", "user.name", actor_name])
subprocess.check_call(["git", "config", "user.email", actor_email])

effective_token = push_token or gha_token
if effective_token:
    remote = f"https://x-access-token:{effective_token}@github.com/{repo}.git"
    subprocess.check_call(["git", "remote", "set-url", "origin", remote])
else:
    print("Warning: no token found. Push may fail.")

files = [
    "data/activity_log.txt",
    "data/status.log",
    "docs/diary.md",
    "changelog.md",
    "data/log.txt"
]

# 扩展的 Commit Message 词库（25+ 条）
messages = [
    # 常规类型
    "chore: update activity log",
    "chore: routine maintenance",
    "chore: sync local changes",
    "docs: update documentation",
    "docs: improve readme",
    "docs: add comments",
    "fix: minor bug fix",
    "fix: correct typo",
    "fix: resolve edge case",
    "style: format code",
    "style: clean up whitespace",
    "style: improve readability",
    "refactor: simplify logic",
    "refactor: extract helper function",
    "refactor: optimize performance",
    "test: add test cases",
    "test: update snapshots",
    "build: update dependencies",
    "build: bump version",
    "ci: update workflow",
    "ci: improve pipeline",
    # 带 emoji 前缀
    "✨ add new feature",
    "🐛 fix minor issue",
    "📝 update notes",
    "🔧 tweak configuration",
    "🚀 improve performance",
    "♻️ refactor code",
    "🎨 improve styling",
    "📦 update packages",
]

for f in files:
    d = "/".join(f.split("/")[:-1])
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

for i in range(commits_to_make):
    f = random.choice(files)
    op = random.choices(["append","replace","touch"], [60,25,15])[0]
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    if op == "append":
        with open(f, "a", encoding="utf-8") as fh:
            fh.write(f"{ts} - auto update\n")
    elif op == "replace":
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(f"# Updated at {ts}\n- note: {random.randint(1000,9999)}\n")
    else:
        open(f, "a", encoding="utf-8").close()

    msg = random.choice(messages)
    if random.random() < 0.35:
        msg += f" ({random.choice(['minor','sync','tidy','daily'])})"
    if random.random() < 0.25:
        msg = f"{random.choice(['🔧','✨','📝'])} {msg}"

    subprocess.call(["git", "add", f])
    try:
        subprocess.check_call(["git", "commit", "-m", msg])
        print(f"Committed: {msg} -> {f}")
    except subprocess.CalledProcessError:
        print("Nothing new to commit for this file.")

    if i < commits_to_make - 1:
        s = random.randint(min_sleep, max_sleep)
        print(f"Sleeping {s}s before next commit...")
        time.sleep(s)

try:
    subprocess.check_call(["git", "push", "origin", "HEAD:main"])
    print("Pushed commits successfully.")
except subprocess.CalledProcessError as e:
    print("Push failed:", e)
    sys.exit(1)
