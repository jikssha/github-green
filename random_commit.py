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

if random.random() < skip_prob:
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
    "README.md",
    "notes/daily.md",
    "docs/diary.md",
    "changelog.md",
    "data/log.txt"
]
messages = [
    "chore: daily update",
    "docs: small tweak",
    "fix: minor typo",
    "style: format",
    "ci: refresh",
    "✨ small update",
    "🔧 maintenance"
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
