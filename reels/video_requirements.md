# No Man Company Journey Video Requirements

## Project Goal
Create a "Build-In-Public" journey video pipeline for "No Man Company" / "TKPROF AI Agent Factory" in a 9:16 aspect ratio (Instagram Reel/TikTok).


## Contents
should come from https://jigsawpuzzlehelper.com/doku.php?id=5.noman_company:2.noman_company_day3
shoud show images from  https://jigsawpuzzlehelper.com/doku.php?id=5.noman_company:2.noman_company_day3
also already uploaded
xxxx\thefirstaicompany\reels\images\scene_dashboard.png
xxxx\thefirstaicompany\reels\images\scene_evidence.png
https://jigsawpuzzlehelper.com/nomancompany/retro_setup_summary.html

video should show closed caption


## Pipeline Workflow
1. **Orchestrator Initiation**: User provides initial task via the Triage Cockpit.
2. **Developer Agent**: Creates/edits video assets, captions, and content.
3. **QA Agent**: Validates output against requirements.
4. **Dev-QA Loop**: Automated back-and-forth iteration until QA passes.
5. **Human Approval**: You (the user) will review and approve via the dashboard; I will perform a final validation before delivering the final passed artifact.

## Core Technical Specifications
- **Aspect Ratio**: 9:16 (vertical).
- **Captioning**: "Burned-in" captions using `drawtext` (for Windows Media Player/universal compatibility).
- **Swarm Infrastructure**: Mailbox-based (JSON) task dispatching in `/.swarm/` directory.
- **Environment**: WSL (Windows Subsystem for Linux) / Git repo at `/mnt/d/git_repo/thefirstaicompany/`.
- **Validation**:
    - **Dev**: Produces MP4.
    - **QA**: Validates format, captions, and coherence.
    - **Final**: Approval required from you via dashboard, then final check by me.

## Task Inbox
- `developer/inbox/`: Drop task JSON files here for the daemon.
- `developer/processed/`: Daemon-moved tasks.
- `orchestrator.log`: Audit trail for all swarm activities.

## Known Limitations / Notes
- NVIDIA drivers on WSL need update (v570+) for full hardware-accelerated inference.
- CPU inference is the current fallback for large models.
