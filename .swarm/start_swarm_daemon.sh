#!/bin/bash
# Swarm Orchestrator: Monitors mailbox for new tasks
MAILBOX_ROOT="/mnt/d/git_repo/thefirstaicompany/.swarm/mailboxes"
LOG_FILE="/mnt/d/git_repo/thefirstaicompany/.swarm/orchestrator.log"

echo "$(date): Orchestrator started" >> "$LOG_FILE"

while true; do
    # Simple processor: looks for .json in developer inbox
    INBOX="$MAILBOX_ROOT/developer/inbox"
    FILES=$(ls $INBOX/*.json 2>/dev/null)
    
    for FILE in $FILES; do
        TASK_NAME=$(basename "$FILE")
        echo "$(date): Processing $TASK_NAME" >> "$LOG_FILE"
        
        # In a real setup, we would parse JSON and exec
        # For now, we simulate success
        mv "$FILE" "$MAILBOX_ROOT/developer/processed/$TASK_NAME"
        echo "$(date): Finished $TASK_NAME" >> "$LOG_FILE"
    done
    
    sleep 30
done
