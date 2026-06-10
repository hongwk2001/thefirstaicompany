const fs = require('fs');
const path = require('path');

// Paths
const PROGRESS_FILE = path.resolve(__dirname, 'progress.md');
const DRAFT_DIR = path.resolve(__dirname, 'promotional_drafts');

// Helper to parse progress.md for completed milestones
function getCompletedMilestones() {
  if (!fs.existsSync(PROGRESS_FILE)) {
    console.error("Progress ledger not found.");
    return [];
  }

  const content = fs.readFileSync(PROGRESS_FILE, 'utf8');
  const lines = content.split('\n');
  const completed = [];

  // Parse lines matching completed milestones: e.g., | Phase 1 | Milestone 1.1 | ... | ✅ Complete | ... |
  const milestoneRegex = /\|\s*\*\*([^*]+)\*\*\s*\|\s*(Milestone\s*[\d.]+)\s*\|\s*([^|]+)\s*\|\s*✅\s*Complete\s*\|\s*([^|]+)\s*\|/;

  for (const line of lines) {
    const match = line.match(milestoneRegex);
    if (match) {
      completed.push({
        phase: match[1].trim(),
        milestone: match[2].trim(),
        description: match[3].trim(),
        date: match[4].trim()
      });
    }
  }

  return completed;
}

// Format the promotional drafts
function generatePromotionalMaterial(completed) {
  if (completed.length === 0) {
    console.log("No completed achievements found in progress ledger.");
    return null;
  }

  const milestoneListMarkdown = completed
    .map(m => `- **[${m.phase}] ${m.milestone}**: ${m.description} (Completed: ${m.date})`)
    .join('\n');

  const updateTitle = `TKPROF AI Agent Factory Update - ${new Date().toISOString().split('T')[0]}`;

  const mediumDraft = `
# ${updateTitle}

We are excited to share the latest progress from the **TKPROF AI Agent Factory** workspace! 
Our automated swarm processes are running successfully in a Windows 11 / WSL 2 hybrid sandbox environment.

## 🚀 Certified Swarm Achievements
${milestoneListMarkdown}

## 🛠️ Architecture Scope & Safety
- **Surgical Diffs**: Configured via CLAUDE.md to strictly block speculative re-writes.
- **Assisted Triage Cockpit**: Manual approval gateways are active, keeping mutations sandboxed and safe.

---
*Generated automatically by Swarm Promoter Agents.*
  `.trim();

  const dokuWikiDraft = `
====== ${updateTitle} ======

The TKPROF AI Agent Factory has certified the following milestones:

${completed.map(m => `  * **${m.phase}** - ${m.milestone}: ${m.description}`).join('\n')}

===== Operational Constraints =====
  * WSL 2 & Docker integrations are fully healthy.
  * Manual clearance cockpit blocks unsanctioned modifications.
  `.trim();

  return { mediumDraft, dokuWikiDraft };
}

// Main execution
console.log("📢 Swarm Promoter Pipeline initiating...");
const completedMilestones = getCompletedMilestones();
console.log(`🔍 Found ${completedMilestones.length} completed achievements.`);

const drafts = generatePromotionalMaterial(completedMilestones);
if (drafts) {
  if (!fs.existsSync(DRAFT_DIR)) {
    fs.mkdirSync(DRAFT_DIR, { recursive: true });
  }

  fs.writeFileSync(path.join(DRAFT_DIR, 'medium_draft.md'), drafts.mediumDraft, 'utf8');
  fs.writeFileSync(path.join(DRAFT_DIR, 'dokuwiki_draft.txt'), drafts.dokuWikiDraft, 'utf8');

  console.log("\n✅ Promotional drafts generated successfully:");
  console.log(`   - Medium Draft: ${path.join(DRAFT_DIR, 'medium_draft.md')}`);
  console.log(`   - DokuWiki: ${path.join(DRAFT_DIR, 'dokuwiki_draft.txt')}`);
  console.log("\n🚀 Ready for programmatic distribution via `app-promoter`.");
}
