const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

// Target directory for developer mailbox inbox
const INBOX_DIR = path.resolve(__dirname, 'mailboxes', 'developer', 'inbox');

// Parse command to execute from CLI arguments
const args = process.argv.slice(2);
if (args.length === 0) {
  console.error("Usage: node test_runner.js <command> [args...]");
  process.exit(1);
}

const command = args[0];
const cmdArgs = args.slice(1);

console.log(`🚀 Swarm QA Test Runner: Executing \`${command} ${cmdArgs.join(' ')}\`...`);

const startTime = new Date();
const child = spawn(command, cmdArgs, { shell: false });

let stdoutData = '';
let stderrData = '';

child.stdout.on('data', (data) => {
  stdoutData += data.toString();
  process.stdout.write(data);
});

child.stderr.on('data', (data) => {
  stderrData += data.toString();
  process.stderr.write(data);
});

child.on('close', (code) => {
  const endTime = new Date();
  const durationMs = endTime - startTime;

  if (code !== 0) {
    console.error(`\n❌ Execution failed with exit code ${code}`);
    
    // Create the typed failure object
    const failureObject = {
      type: "EXECUTION_FAILURE",
      timestamp: endTime.toISOString(),
      durationMs,
      command: `${command} ${cmdArgs.join(' ')}`,
      exitCode: code,
      summary: stderrData.trim().split('\n')[0] || "Unknown error occurred",
      stdout: stdoutData,
      stderr: stderrData
    };

    // Make sure inbox directory exists
    if (!fs.existsSync(INBOX_DIR)) {
      fs.mkdirSync(INBOX_DIR, { recursive: true });
    }

    // Write failures back to developer inbox as typed objects
    const filename = `error_${startTime.getTime()}.json`;
    const filepath = path.join(INBOX_DIR, filename);
    
    fs.writeFileSync(filepath, JSON.stringify(failureObject, null, 2), 'utf8');
    console.log(`\n📬 Failure report piped back to developer mailbox:\n   ${filepath}`);
    process.exit(code);
  } else {
    console.log(`\n✅ Execution completed successfully in ${durationMs}ms.`);
  }
});
