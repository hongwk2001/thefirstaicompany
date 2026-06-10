#!/usr/bin/env bash
# Dev-QA Back-and-Forth Swarm Demo Simulation

echo "===================================================="
echo "🤖 Starting Dev-QA Swarm Loop Simulation"
echo "===================================================="

# Ensure we are on the DEV branch
git checkout dev 2>/dev/null || git checkout -b dev

# 1. Create a buggy calculator file
echo "⚙️  Step 1: Junior developer creates calculator.js with a division bug..."
cat << 'EOF' > calculator.js
function divide(a, b) {
    // BUG: missing check for division by zero!
    return a / b;
}
module.exports = { divide };
EOF

# Create a test script that expects an error when dividing by zero
cat << 'EOF' > test.js
const { divide } = require('./calculator');
const assert = require('assert');

console.log("Running unit tests...");

// Test normal division
assert.strictEqual(divide(6, 2), 3);

// Test division by zero (should throw an error, but returns Infinity instead!)
const val = divide(5, 0);
if (val === Infinity) {
    console.error("FAIL: Division by zero returned Infinity instead of throwing an error!");
    process.exit(1);
}
console.log("All tests passed!");
EOF

sleep 2

# 2. Run the QA Test Runner to intercept the error
echo -e "\n⚙️  Step 2: Running the Swarm QA Test Runner..."
node .swarm/test_runner.js node test.js

sleep 2

# 3. Look at the generated error log
echo -e "\n⚙️  Step 3: Checking developer inbox for typed error logs..."
ls -lt .swarm/mailboxes/developer/inbox/error_*.json | head -n 1

sleep 2

# 4. Simulate the fix being applied by the developer
echo -e "\n⚙️  Step 4: Fixing calculator.js..."
cat << 'EOF' > calculator.js
function divide(a, b) {
    if (b === 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}
module.exports = { divide };
EOF

# Update the test to assert that it throws
cat << 'EOF' > test.js
const { divide } = require('./calculator');
const assert = require('assert');

console.log("Running unit tests...");
assert.strictEqual(divide(6, 2), 3);

assert.throws(() => {
    divide(5, 0);
}, /Division by zero/);

console.log("All tests passed!");
EOF

sleep 2

# 5. Run the QA Test Runner again
echo -e "\n⚙️  Step 5: Re-running the Swarm QA Test Runner (Verification)..."
node .swarm/test_runner.js node test.js

echo -e "\n🎉 Simulation complete! The Dev-QA loop successfully intercepted, logged, and fixed the bug."
# Cleanup test files
rm -f calculator.js test.js
