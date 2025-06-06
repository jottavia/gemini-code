# Project Roadmap for Jules (AI Assistant)

**Preamble:** This document is the Project Roadmap for Jules, the AI assistant. Its contents should be referenced by Jules at the start of new tasks and updated with all significant progress, changes to future goals, and completed milestones.

---

## 1. Project Overview

*   **Project Name**: Gemini Code
*   **Current Version**: 0.1.106 (as of 2025-06-06)
*   **Core Functionality**: AI assistant with a dual role:
    *   **AI System Administrator**: For managing and administering Linux/FreeBSD systems. Capabilities include shell command execution (with `sudo` for root privileges via `BashTool`), file system management, and configuration assistance.
    *   **AI Coding Assistant**: For software development tasks, including code generation, explanation, debugging, and refactoring.
*   **Key Technologies**: Google Gemini models, Python, Click, Rich.

## 2. Recent Milestones (Since Dual Role Definition)

*   **Enhanced `BashTool`**: Added `use_sudo` capability for root-level command execution. (Completed: feat/ai-sysadmin-sudo branch, then merged to main)
*   **Updated System Prompt**: `GeminiModel` system prompt revised to reflect the AI's dual role and provide guidance on `sudo` usage. (Completed: feat/ai-sysadmin-sudo branch, then merged to main)
*   **Documentation Overhaul**: `README.md`, `INSTALL.MD`, `brainstorm.md` updated to describe the dual System Administrator and Coding Assistant roles. (Completed: docs/ai-sysadmin-role updates, then merged to main)
*   **Fork Synchronization**: Addressed user concerns about fork updates, culminating in all recent changes being visible on `main`. (Completed: sync-fork-test and consolidated-session-updates branches, then merged to main)
*   **Project Roadmap Creation**: This `PROJECT_ROADMAP.md` file established. (Current task)

## 3. Current Development Focus / Short-Term Goals

*   **Establish and Test `PROJECT_ROADMAP.md`**: Ensure this file is correctly created, submitted, and integrated into the workflow.
*   **Practical `sudo` Task**: Execute a simple but practical system administration task that requires `sudo` (e.g., "list contents of a root-owned directory" or "check status of a system service like cron/sshd") to verify the `BashTool`'s `use_sudo` functionality and LLM planning for it.
*   **Refine LLM Prompts for SysAdmin Tasks**: Based on initial tests, refine the system prompt or provide more specific examples to the LLM on how to plan and execute common sysadmin operations safely and effectively.
*   **Basic Monitoring Example**: Attempt a basic system monitoring task (e.g., "Show me current disk usage" or "List top 5 CPU consuming processes").

## 4. Long-Term Vision & Future Goals

*   **Comprehensive AI System Administrator**:
    *   Robust package management (install, update, remove across different Linux distros and FreeBSD).
    *   Advanced service management (enable, disable, detailed status checks).
    *   System monitoring and alerting (proactive, not just reactive).
    *   Network configuration and troubleshooting assistance.
    *   User account management (with extreme caution and confirmations).
    *   Automated execution of routine maintenance tasks based on user approval.
    *   Enhanced parsing and understanding of complex command outputs.
*   **Advanced Coding Assistance**:
    *   Deeper codebase understanding and context retention.
    *   More sophisticated refactoring capabilities.
    *   Integration with build systems and CI/CD pipelines.
*   **Seamless Dual Role Integration**:
    *   Ability to use coding skills to create sysadmin scripts or tools on the fly.
    *   Contextual awareness to switch between coding and sysadmin tasks smoothly.
*   **Safety and Reliability**:
    *   Further development of safety protocols for privileged operations.
    *   Improved error handling and recovery.
    *   "Read-only" or "dry-run" modes for sensitive sysadmin tasks.
*   **(Refer to `brainstorm.md` for more granular ideas and older concepts).**

## 5. Instructions for Jules (AI Assistant)

*   **Reference this Document**: Review this `PROJECT_ROADMAP.md` at the beginning of new tasks or when planning significant changes.
*   **Update Milestones**: After completing a major feature, resolving a key issue, or submitting a significant set of changes, add an entry to "Recent Milestones". Include the date/commit/branch if helpful.
*   **Update Current Focus**: As short-term goals are met or priorities shift, update the "Current Development Focus" section.
*   **Evolve Future Goals**: Periodically review and update the "Long-Term Vision & Future Goals" section based on user feedback and project evolution.
*   **Log Changes Systematically**: When this file is updated, the commit message should clearly indicate that the Project Roadmap has been modified.

---
*This document was last updated by Jules on: <placeholder_for_dynamic_date_if_possible_otherwise_manual_date_here_or_remove_this_line>*
