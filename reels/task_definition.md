# Video Creation Task: "No Man Company" Journey
## Description
Automate the production of the "No Man Company" journey video series. The pipeline uses an agent swarm (Developer + QA) to generate, validate, and refine content before final human review.

## Workflow Protocol
1.  **Orchestrator Initiation**: User submits this task file to `/mnt/d/git_repo/thefirstaicompany/.swarm/mailboxes/developer/inbox/`.
2.  **Development Phase (Developer Agent)**:
    *   Generates video content based on project assets.
    *   Applies required filters (burned-in captions, branding).
    *   Writes output to `/mnt/d/git_repo/thefirstaicompany/reels/`.
3.  **QA Phase (QA Agent)**:
    *   Monitors generated output.
    *   Validates video integrity, caption readability, and compliance with project style.
    *   Reports results to the swarm dashboard/logs.
4.  **Looping Mechanism**:
    *   If QA detects failures, the task is returned to the Developer for iteration.
    *   QA/Dev loop repeats until criteria are met.
5.  **Final Review (Hermes Agent)**:
    *   Hermes performs the final verification step.
    *   If Hermes identifies any remaining issues, it initiates a new loop.
6.  **Human Approval**:
    *   Only once Hermes marks the content as "PASSED" does it get promoted to the final review queue for your final approval.
    *   You will see only content that has already cleared the automated and agent-based validation gates.

## Monitoring
*   Progress logs available in: `/mnt/d/git_repo/thefirstaicompany/.swarm/orchestrator.log`
*   Task Status Tracking: via the Swarm Dashboard.

## Current Task Initialization
- **Task ID**: `vid_001_journey`
- **Goal**: Render final `no_man_company_journey_final.mp4` using current project assets.
- **Reviewer**: Hermes Agent
- **Status**: [PENDING_USER_EDIT]
