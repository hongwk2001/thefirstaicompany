const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const MAILBOX_DIR = path.resolve(__dirname, 'mailboxes', 'developer');
const INBOX_DIR = path.join(MAILBOX_DIR, 'inbox');
const PROCESSED_DIR = path.join(MAILBOX_DIR, 'processed');
const PROGRESS_FILE = path.resolve(__dirname, 'progress.md');

// Ensure directories exist
if (!fs.existsSync(PROCESSED_DIR)) fs.mkdirSync(PROCESSED_DIR, { recursive: true });

// Ensure we are on the DEV branch in Git
function ensureDevBranch() {
  try {
    const currentBranch = execSync('git branch --show-current').toString().trim().toLowerCase();
    if (currentBranch !== 'dev') {
      console.log("Git: Switching to 'dev' branch...");
      // Check if dev branch exists locally (case-insensitive check)
      const branches = execSync('git branch').toString().toLowerCase();
      if (branches.includes('dev')) {
        execSync('git checkout dev');
      } else {
        execSync('git checkout -b dev');
      }
    }
  } catch (err) {
    console.error("Warning: Git branch check failed.", err.message);
  }
}

// Update progress.md with active or completed task status
function updateProgress(taskId, description, status) {
  if (!fs.existsSync(PROGRESS_FILE)) return;
  let content = fs.readFileSync(PROGRESS_FILE, 'utf8');
  
  const today = new Date().toISOString().split('T')[0];
  const newRow = `| **Dev Swarm** | ${taskId} | ${description} | ✅ ${status} | ${today} |`;

  if (content.includes(taskId)) {
    // Replace existing task status row
    const lines = content.split('\n');
    const updatedLines = lines.map(line => {
      if (line.includes(taskId)) {
        return newRow;
      }
      return line;
    });
    fs.writeFileSync(PROGRESS_FILE, updatedLines.join('\n'), 'utf8');
  } else {
    // Append to Completed Milestones table
    const targetHeading = "## 🏁 Completed Milestones";
    const replacement = `${targetHeading}\n${newRow}`;
    content = content.replace(targetHeading, replacement);
    fs.writeFileSync(PROGRESS_FILE, content, 'utf8');
  }
}

// Process a single task
function processTask(file) {
  const filePath = path.join(INBOX_DIR, file);
  console.log(`\n📥 Found new task: ${file}`);
  
  let task;
  try {
    task = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (err) {
    console.error("Failed to parse task JSON", err);
    return;
  }

  const taskId = task.id || `task_${Date.now()}`;
  const description = task.description || "Swarm execution task";
  const command = task.command;

  if (!command) {
    console.error("No command specified in task payload.");
    return;
  }

  console.log(`⚙️  Task ID: ${taskId}`);
  console.log(`⚙️  Description: ${description}`);
  console.log(`⚙️  Command: ${command}`);

  ensureDevBranch();

  // Mark in progress in progress.md
  updateProgress(taskId, description, "Running");

  try {
    console.log("🚀 Executing command...");
    const output = execSync(command, { encoding: 'utf8', stdio: 'pipe' });
    console.log("✅ Command executed successfully.");
    console.log(output);

    // Save success result
    const result = {
      status: "SUCCESS",
      timestamp: new Date().toISOString(),
      output: output
    };
    fs.writeFileSync(path.join(PROCESSED_DIR, `${taskId}_result.json`), JSON.stringify(result, null, 2));
    updateProgress(taskId, description, "Complete");
  } catch (err) {
    console.error("❌ Command execution failed:", err.message);
    const result = {
      status: "FAILURE",
      timestamp: new Date().toISOString(),
      error: err.message,
      stderr: err.stderr
    };
    fs.writeFileSync(path.join(PROCESSED_DIR, `${taskId}_result.json`), JSON.stringify(result, null, 2));
    updateProgress(taskId, description, "Failed");
  }

  // Move processed task file
  fs.renameSync(filePath, path.join(PROCESSED_DIR, file));
  console.log(`📦 Moved task to processed folder.`);
}

// Main Polling Loop
function poll() {
  console.log("🤖 Hermes Agent Daemon active. Polling for tasks...");
  
  const files = fs.readdirSync(INBOX_DIR);
  const taskFiles = files.filter(f => f.startsWith('task_') && f.endsWith('.json'));

  if (taskFiles.length > 0) {
    taskFiles.forEach(processTask);
  } else {
    console.log("No new tasks in inbox.");
  }
}

// Run polling loop every 10 seconds or run once for demonstration
const runContinuous = process.argv.includes('--continuous');
if (runContinuous) {
  setInterval(poll, 10000);
  poll();
} else {
  poll();
}
