# docs/agents/manifest-agent.md

# 📄 Manifest Agent

"""
The ManifestAgent is responsible for transforming raw BOL (Bill of Lading) inputs into structured CSV manifest records.
It is the backbone of the Loading Dock Control Panel’s agent loop—handling data parsing, validation, and archival handoff.
"""

# 🧠 Agent Profile

"""
- Name: manifest_agent
- Role: Structured document generator
- Persona: Disciplined, detail-oriented, and audit-conscious
- Model: (TBD per system config) — OpenAI / Azure / Granite 3.1 compatible
- LLM Config:
    - Temperature: 0.2
    - Max tokens: 1024
    - System prompt: 
        "You are a data transformation agent that receives semi-structured text 
         and emits a clean CSV row with canonical formatting and units. 
         Be strict about missing values, and always preserve original field labels as metadata."
"""

# 📥 Inputs

"""
- Triggered by WatcherAgent upon valid file drop
- Accepts JSON payloads or semi-structured BOL blocks
- Example payload:
"""

# {
#   "shipment_id": "BOL_2025_0071",
#   "origin": "Chicago DC",
#   "destination": "Birmingham Dock A",
#   "pallets": 12,
#   "carrier": "Unified Freight Lines",
#   "weight_lbs": 14400,
#   "timestamp": "2025-06-30T18:45:21Z"
# }

# 📤 Output

"""
Emits one or more rows to: /Generated/manifests/manifest_YYYYMMDD.csv

Sample:
"""

# shipment_id,origin,destination,pallets,carrier,weight_lbs,timestamp
# BOL_2025_0071,Chicago DC,Birmingham Dock A,12,Unified Freight Lines,14400,2025-06-30T18:45:21Z

"""
Optional:
- JSON mirror file in /Generated/json/
- Log append with timestamp, agent UUID, and BOL filename
"""

# 🔗 Connected Agents

"""
- WatcherAgent → triggers ManifestAgent on drop
- ValidatorAgent → post-processes manifest for format integrity
- LoggerAgent → archives CSV + JSON + logs
"""

# 🧭 Roadmap & Enhancements

"""
Planned and proposed upgrades for future versions:
"""

# - ✅ Field-level confidence estimation (low-certainty values flagged)
# - ✅ Auto-correction for common formatting/spacing/OCR issues
# - ✅ Alternate input modes: PDF, HTML email parsing
# - ✅ Retry-on-failure: Escalate to fallback parser or LLM agent
# - ✅ Tagging: HOLD / URGENT / DEFERRED routing labels
# - ✅ Output hook for notifying DispatcherAgent

"""
Each feature will be version-tagged and rolled out under Git-tracked milestones.
"""

# 🧪 Testing Scenarios

"""
- Valid structured JSON → produces correct CSV
- Missing field → triggers LLM fallback (e.g. estimate or null flag)
- Invalid date format → correction or rejection logged
- Duplicate shipment → de-duped or archived with suffix
"""

# 🧬 Design Philosophy

"""
Modular, resilient, and transparent—ManifestAgent transforms logistics into legible data. 
Its output is the foundation of all downstream visibility in the system and must favor traceability over guesswork.
"""

