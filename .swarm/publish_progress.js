const fs = require('fs');
const path = require('path');
const { requestClearance } = require('./approve_gate');

const PROGRESS_PATH = path.join(__dirname, 'progress.md');
const README_PATH = path.join(__dirname, '..', 'README.md');
const PROMOTER_INBOX = path.join(__dirname, 'mailboxes', 'promoter', 'inbox');

function parseMilestones(progressContent) {
  const lines = progressContent.split('\n');
  let inMilestones = false;
  const milestones = [];

  for (const line of lines) {
    if (line.includes('## 🏁 Completed Milestones')) {
      inMilestones = true;
      continue;
    }
    if (inMilestones && line.startsWith('---')) {
      inMilestones = false;
      break;
    }
    if (inMilestones && line.trim() !== '') {
      // Parse table row: | Phase | Milestone | Description | Status | Completed Date |
      if (line.includes('|') && !line.includes('Milestone |') && !line.includes(':---')) {
        const parts = line.split('|').map(p => p.trim());
        if (parts.length >= 6) {
          milestones.push({
            phase: parts[1].replace(/\*\*/g, ''),
            milestone: parts[2],
            description: parts[3],
            status: parts[4],
            date: parts[5]
          });
        }
      }
    }
  }
  return milestones;
}

function generateReadmeContent(milestones) {
  let tableRows = milestones.map(m => 
    `| ${m.phase} | ${m.milestone} | ${m.description} | ${m.status} | ${m.date} |`
  ).join('\n');

  return `# 🚀 The First AI Company - TKPROF AI Agent Factory

Welcome to the central repository for the first AI company project, executing agent workflows inside WSL 2 and Docker sandboxes.

## 🏆 Completed Milestones

| Phase | Milestone | Description | Status | Completed Date |
| :--- | :--- | :--- | :--- | :--- |
${tableRows}

---
*This file is automatically updated by the Swarm Build-In-Public Content Pipe.*
`;
}

function generateOutreachDraft(milestones) {
  const latest = milestones[milestones.length - 1];
  return `# 📢 Build-In-Public Outreach Update

**Subject:** Milestone Reached: ${latest.milestone} - ${latest.description}

Hey world! We are building the first AI company completely in public. We've just certified our latest milestone under the TKPROF Swarm System:

- **Milestone:** ${latest.milestone}
- **Description:** ${latest.description}
- **Phase:** ${latest.phase}
- **Status:** ${latest.status} (Completed: ${latest.date})

### Current Progress Ledger:
${milestones.map(m => `- [x] **${m.milestone}**: ${m.description} (${m.phase})`).join('\n')}

Stay tuned for more updates as we activate our assisted triage cockpits and automated publishing gateways!
`;
}

function run() {
  console.log("🔍 Checking progress ledger...");
  if (!fs.existsSync(PROGRESS_PATH)) {
    console.error("Error: progress.md not found.");
    process.exit(1);
  }

  const progressContent = fs.readFileSync(PROGRESS_PATH, 'utf8');
  const milestones = parseMilestones(progressContent);

  if (milestones.length === 0) {
    console.log("⚠️ No completed milestones found to publish.");
    process.exit(0);
  }

  const latest = milestones[milestones.length - 1];
  const impactSummary = `Publish progress update for latest milestone: ${latest.milestone} (${latest.description})`;

  console.log("🔒 Requesting manual clearance for publication...");
  const approved = requestClearance("Publish Progress", impactSummary, JSON.stringify(milestones, null, 2));

  if (!approved) {
    console.log("❌ Action denied by user. Aborting publication.");
    process.exit(1);
  }

  console.log("✅ Clearance granted. Writing outputs...");

  // Update root README.md
  const readmeContent = generateReadmeContent(milestones);
  fs.writeFileSync(README_PATH, readmeContent, 'utf8');
  console.log(`📝 Updated root README.md: ${README_PATH}`);

  // Create outreach draft
  if (!fs.existsSync(PROMOTER_INBOX)) {
    fs.mkdirSync(PROMOTER_INBOX, { recursive: true });
  }
  const outreachPath = path.join(PROMOTER_INBOX, 'outreach_draft.md');
  fs.writeFileSync(outreachPath, generateOutreachDraft(milestones), 'utf8');
  console.log(`📬 Outreach draft saved: ${outreachPath}`);

  console.log("🎉 Build-In-Public Content Pipe completed successfully!");
}

if (require.main === module) {
  run();
}
