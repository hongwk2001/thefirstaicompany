const { spawnSync } = require('child_process');
const path = require('path');
const fs = require('fs');

/**
 * Request manual clearance for an action via the triage cockpit.
 * @param {string} actionName Name of the action needing clearance.
 * @param {string} impactSummary Brief summary of the impact.
 * @param {string} [detailsText] Optional detailed ledger/metadata.
 * @returns {boolean} True if approved, false otherwise.
 */
function requestClearance(actionName, impactSummary, detailsText = '') {
  const cockpitPath = path.join(__dirname, 'triage_cockpit.js');
  let detailsFile = null;

  if (detailsText) {
    detailsFile = path.join(__dirname, `temp_ledger_${Date.now()}.txt`);
    fs.writeFileSync(detailsFile, detailsText, 'utf8');
  }

  const args = [cockpitPath, actionName, impactSummary];
  if (detailsFile) {
    args.push(detailsFile);
  }

  // Spawn the cockpit process synchronously, inheriting stdio so the user can type in the console
  const result = spawnSync('node', args, { stdio: 'inherit' });

  if (detailsFile && fs.existsSync(detailsFile)) {
    try {
      fs.unlinkSync(detailsFile);
    } catch (e) {
      // Ignore cleanup error
    }
  }

  return result.status === 0;
}

module.exports = { requestClearance };
