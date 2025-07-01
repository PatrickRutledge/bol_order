# docs/agents/watcher-agent.md

# 🛰 Watcher Agent

"""
The WatcherAgent monitors a target directory (`/Incoming`) for new file events and triggers the appropriate agent chain (e.g. ManifestAgent) upon detection.
Its goal is to provide reliable, low-latency task initiation for asynchronous agent workflows.
"""

# 🧠 Agent Profile

"""
- Name: watcher_agent
- Role: Filesystem event listener and orchestrator
- Persona: Alert, low-latency, and minimal-opinion
- Tech Stack: Python watchdog, threaded callback
- Notification Mode: Event or polling (configurable)
"""

# 🧭 Responsibilities

- Detect file drops or changes in `/Incoming/`
- Debounce duplicate events (e.g., save + metadata updates)
- Confirm filetype matches config whitelist (e.g. `.txt`, `.json`)
- Trigger ManifestAgent via internal system call or AutoGen loop message
- Optionally log each detection event

# ⚙️ Config Options

- `watch_path`: Target folder (e.g. `/Incoming`)
- `valid_extensions`: Allowlist (e.g. `['.txt', '.json']`)
- `debounce_ms`: Time delay for batching updates
- `on_trigger`: Which agent to call when match found

# 🧪 Example Event

```json
{
  "event": "created",
  "file": "BOL_2025_0073.txt",
  "timestamp": "2025-06-30T18:51:00Z",
  "agent": "manifest_agent"
}
