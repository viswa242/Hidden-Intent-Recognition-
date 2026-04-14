# Hidden-Intent-Recognition-
AI-powered system that detects hidden intent and analyzes conversational risk in real-time. Built with FastAPI, Whisper STT, and transformer-based NLP — supports both single-sentence and multi-turn session-based analysis with confidence scoring and risk alerting.

AI · Risk Analysis · NLP · FastAPI · Whisper STT · Python


Hidden Intent Detection & Conversational Risk Analysis System

An industrial-grade AI pipeline that uncovers hidden intent and 
measures conversational risk in real-time — across both single 
utterances and extended multi-turn dialogues.

What It Does

Most NLP systems detect **what** someone says.
This system detects **what they actually mean**.

By combining transformer-based intent classification with session-aware 
context memory, it identifies subtle risk patterns, escalating behavioral 
signals, and concealed intent that surface only across the arc of a 
conversation — not in any single message.

Core Capabilities

**Dual-mode processing** — stateless single-sentence analysis or 
  full session-based conversational tracking
**Hidden intent classification** — multi-label NLU model that goes 
  beyond surface meaning
**Confidence scoring** — calibrated probability output per prediction
**Context memory** — sliding-window turn history with entity retention
**Risk escalation engine** — LOW / MEDIUM / HIGH / CRITICAL alert levels
**Speech input support** — real-time transcription via OpenAI Whisper
**Session lifecycle management** — create, track, and close conversation 
  sessions with full audit history

Architecture

| Layer | Components |
|---|---|
| User Interaction | CLI · Web · Mobile · Speech Input |
| Input Processing | Whisper STT · Text Normalization |
| API & Control | FastAPI · Mode Router · Session Controller |
| AI / ML | Intent Classifier · Confidence Engine · Pattern Analyzer |
| Conversation Engine | State Manager · Context Memory · Score Accumulator |
| Data & Storage | Session Store (Redis) · Conversation History (SQLite) |
| Output & Analytics | Real-time Predictions · Summary Generator · Alert Engine |

Tech Stack

- **Backend** — FastAPI (Python)
- **Speech-to-Text** — OpenAI Whisper
- **NLP / ML** — Transformers (HuggingFace), scikit-learn
- **Session Store** — Redis / In-memory
- **History Store** — SQLite / JSON
- **Deployment** — Docker-ready

Use Cases

- Conversational AI safety monitoring
- Customer support risk flagging
- Automated interview / interrogation analysis
- Chatbot abuse and manipulation detection
- Research into deceptive language patterns
