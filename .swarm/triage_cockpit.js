const readline = require('readline');
const fs = require('fs');
const path = require('path');

// Read args: action name, impact summary, details path
const args = process.argv.slice(2);
if (args.length < 2) {
  console.error("Usage: node triage_cockpit.js <action_name> <impact_summary> [details_file]");
  process.exit(1);
}

const actionName = args[0];
const impactSummary = args[1];
const detailsFile = args[2];

let details = '';
if (detailsFile && fs.existsSync(detailsFile)) {
  details = fs.readFileSync(detailsFile, 'utf8');
}

// Format the ledger summary in clean markdown
const border = "======================================================================";
console.log(`\n${border}`);
console.log("🛑 ASSIGNED ASSISTED TRIAGE COCKPIT - PENDING CLEARANCE");
console.log(border);
console.log(`\n👉 ACTION: ${actionName}`);
console.log(`👉 IMPACT: ${impactSummary}`);

if (details) {
  console.log("\n--- DETAILED TRANSACTION LEDGER ---");
  console.log(details.trim());
  console.log("----------------------------------");
}

console.log(`\n⚠️  CRITICAL: This operation requires explicit manual clearance.`);
console.log(`Any mutation or deployment is frozen until approved.`);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('\n📝 Enter "APPROVE" to clear this action, or "DENY" to reject: ', (answer) => {
  rl.close();
  if (answer.trim().toUpperCase() === 'APPROVE') {
    console.log("\n✅ CLEARANCE GRANTED. Resuming execution...");
    process.exit(0);
  } else {
    console.log("\n❌ CLEARANCE DENIED. Operation aborted.");
    process.exit(1);
  }
});
