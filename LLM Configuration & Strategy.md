# 🧠 Language Model (LLM) Configuration & Strategy

This section outlines the LLM architecture, persona injection patterns, and prompt strategies used (or planned) to drive agent intelligence in the Loading Dock Control Panel system.

---

## 📦 Model Selection

The system is designed to be model-flexible. Primary targets for deployment:

- **OpenAI GPT-4-turbo**
- **Azure OpenAI variants**
- **Granite 3.1 (IBM)** — Currently under evaluation
- **Anthropic Claude (future compatibility)**

LLM configuration is loaded via `llm_config` blocks in agent templates or `config.json`.

---

## 🔧 LLM Config Schema (example)

```json
{
  "model": "gpt-4",
  "temperature": 0.2,
  "max_tokens": 1024,
  "stream": false,
  "system_message": "You are a structured document parser focused on high accuracy and auditability."
}
