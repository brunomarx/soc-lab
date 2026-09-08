# Triage assistant

Analysts can run alert triage through any MCP-capable assistant. The repo ships a
project-level `.mcp.json` that points at the lab's `cloud-auth-broker` server, which
hands out short-lived cloud sessions for the lab accounts so the assistant can pull
CloudTrail context while you work an alert.

## Usage

1. Open the repo in your assistant. It picks up `.mcp.json` automatically.
2. Ask it to pull context for an alert ID, for example the last 24h of CloudTrail
   activity for a principal.
3. Review what it returns before acting on it.

The broker is read-only. If you need write access, use your own SSO profile.
