# CODE REVIEW AI
A Code review AI Tool in progress..

## PHASE 1 (IN PROGRESS)
#### 📌 Overview
This project is a **minimal viable AI-powered code review engine** for Java code.
It combines:
* **Static analysis (rule-based)**
* **AI-inspired review (heuristic fallback)**
The goal was to build a **working end-to-end system in 1–2 hours**, focusing on execution speed and practical learning.
---
#### ⚙️ Features
##### ✅ Static Analysis
Detects:
* Long methods
* Too many parameters
* Usage of `System.out.println`
* Large class size
---
##### 🤖 AI Review (Heuristic-based)
Provides suggestions like:
* Improve architecture (service layer separation)
* Replace `System.out.println` with logging
* Use meaningful variable names
* Detect nested loop complexity
---

### 🔁 Fault-Tolerant Design
* Designed to integrate with LLM APIs
* Gracefully falls back to rule-based review if AI fails
---
##### ▶️ How to Run
##### 1. Clone the repository
##### 2. Run the analyzer
#### 📥 Sample Input
#### 📤 Sample Output
=== STATIC ANALYSIS ===
- Too many parameters (6)
- Avoid System.out.println

=== AI REVIEW ===
- Replace System.out.println with a logging framework
- Use meaningful variable names instead of single letters
- High nested loop complexity detected

##### 🚧 Limitations
* Regex-based parsing (not AST-level)
* Heuristic AI instead of real LLM (for MVP)
* No UI or CI/CD integration
---
##### 🔮 Future Improvements
* Integrate real LLM (OpenAI / local models)
* Use Java AST parsing (e.g., JavaParser)
* GitHub PR integration (auto code review bot)
* Scoring system for code quality
* Web UI for uploads and reports
---
