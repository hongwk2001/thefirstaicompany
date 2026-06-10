const { spawn } = require('child_process');
const path = require('path');

// Strictly define the allowed sandboxed directories
const allowedDirectories = [
  "D:\\git_repo\\thefirstaicompany"
];

console.log("Starting MCP Filesystem Server with sandboxed directories:", allowedDirectories);

// Locate the server-filesystem entry point
const serverScript = path.resolve(__dirname, 'node_modules', '@modelcontextprotocol', 'server-filesystem', 'dist', 'index.js');

const child = spawn('node', [serverScript, ...allowedDirectories], {
  stdio: 'inherit',
  shell: false
});

child.on('close', (code) => {
  console.log(`MCP Filesystem Server process exited with code ${code}`);
});
