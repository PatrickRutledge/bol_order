# 🧭 Agent Roadmap & Enhancements

This document memorializes ideas, planned improvements, and conceptual upgrades across all defined agents in the Loading Dock Control Panel system. Each entry is scoped for clarity, maintainability, and long-term impact. Agents listed here operate collaboratively under a future AutoGen-compatible framework.

---

## 🔁 Shared System-Wide Enhancements

- **Confidence scoring** per output field for transparency
- **Retry logic** with failover routing to alternate agents
- **Prompt version tracking** across Git versions for auditing
- **Agent persona config** injection via structured system prompts
- **UI signals** linked to backend agent activity (icons, status banners)
- **Configurable middleware** to log every inter-agent message
- **Plugin-based validation** across all agent types
- **Remote deploy hooks** for agents hosted on cloud runtimes

---

## 📄 ManifestAgent — Roadmap

- Field-level **confidence estimation** for each parsed value
- OCR/post-processing rules for **text cleanup** (spacing, casing, units)
- Expanded input support for **PDF**, **email**, and HTML-based manifests
- **Routing flag generation**: HOLD, URGENT, DEFERRED tags
- **Fallback agent ping** if malformed or ambiguous content is detected
- Produce **signature hash** or manifest fingerprint per shipment
- Emit companion **metadata JSON** with origin, agent, and parse status
- Local **prompt override** config to tune persona behavior

---

## 🛰 WatcherAgent — Roadmap

- **Glob pattern** support for subdirectory watching
- **Debounce logic** to reduce double triggers
- Configurable **file extension whitelist** in `.env` or `config.json`
- Trigger downstream retry logic if **target agent fails**
- Identify and **ignore temp files** (`.tmp`, `.crdownload`, etc.)
- Visual **“file received” UI badge** per successful detection
- **Event queueing** if system is offline or ManifestAgent is busy
- Watch multiple folders with mapped dispatch logic

---

## 📚 LoggerAgent — Roadmap

- Support for **daily log bundles** by timestamp or manifest ID
- Option to export human-readable `.log` alongside JSONL
- **Verbosity controls** per environment (e.g. dev, prod, debug)
- **Remote push** capability (e.g. syslog, Elasticsearch, or S3)
- Automatic **log trimming/rotation** after N days
- **Time-delta tags** for agent performance benchmarking

---

## 🧪 ValidatorAgent — Roadmap

- Support for configurable **schema references** or profiles
- Implement **per-field scoring** for quality metrics
- Option to submit rejected rows to **LLM for retry/repair**
- **Highlight conflicts**: duplicate IDs, empty required fields
- Track **warnings vs errors**, route valid subset onward
- Output standardized **rejection report** with rationale and raw data

---

## 🚦 DispatcherAgent — Roadmap (Future)

- Interpret manifest tags (e.g. HOLD, URGENT) into action
- Decide if the shipment is routed internally or escalated
- Integrate with **external APIs** (Slack, Teams, webhook, etc.)
- **Priority load balancing** if system is processing in parallel
- Validate **delivery window compliance** from manifest timestamps

---

> All roadmap items are tracked under source control with milestones. Contributors can grab any unchecked feature and follow the corresponding `agent.md` for intent and structure.
