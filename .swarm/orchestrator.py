import os
import json
import time

MAILBOX_DIR = "/mnt/d/git_repo/thefirstaicompany/.swarm/mailboxes"
DEV_INBOX = os.path.join(MAILBOX_DIR, "developer", "inbox")

def create_task(agent, description, command):
    task = {
        "description": description,
        "command": command,
        "timestamp": time.time()
    }
    filename = f"task_{int(time.time())}.json"
    filepath = os.path.join(MAILBOX_DIR, agent, "inbox", filename)
    with open(filepath, "w") as f:
        json.dump(task, f)
    print(f"✅ Task created in {agent} mailbox: {filename}")

# Create an initial task to check the setup
create_task("developer", "Verify swarm infrastructure", "echo 'Swarm infrastructure verified' > /tmp/swarm_verified")
