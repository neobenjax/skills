# Personal Knowledge Agent Skill

## About
This project implements an Antigravity Agent Skill that allows an AI assistant to answer personal questions about the user by querying a local knowledge base. It uses the Open Knowledge Format (OKF) to store personal details, educational history, and professional experience in a structured, agent-readable format. When queried, the agent retrieves this information and performs a web search to supplement the response (e.g., finding a matching LinkedIn profile).

## Purpose
The primary purpose of this skill is to provide a privacy-first, locally-managed way for AI agents to have context about "who you are." Instead of relying on a distant, opaque database, the agent reads human-editable markdown files stored right in your workspace. This ensures you have full control over what the agent knows about you and how it represents you.

## Resources & Documentation
- **Open Knowledge Format (OKF):** [OKF Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)
- **AgentSkills Documentation:** [AgentSkills Home](https://agentskills.io/home)
- **Antigravity Skills:** Customized Antigravity Agent framework for running workspace-specific skills.
- **Reference Article:** [How OKF Can Improve Data Sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)

## Structure
- `knowledge-catalog/`: Contains the OKF markdown files (e.g., `personal_info.md`, `education.md`, `experience.md`).
- `.agents/skills/personal-knowledge/`: Contains the `SKILL.md` file which defines the agent's behavior and triggers.

---
*Maintained by [@neobenjax](https://github.com/neobenjax).*

