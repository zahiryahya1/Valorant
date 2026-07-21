# Database Schema

## Overview

The database is organized into three logical layers.

1. Core Tables
2. Dimension Tables
3. Analytics Tables

This separation reduces redundancy while supporting efficient analytical queries.

----

# Schema Overview

```mermaid
flowchart TD
    API --> CoreTables[Core Tables]
    CoreTables --> AggregateComputation[Aggregate Computation]
    AggregateComputation --> AnalyticsTables[Analytics Tables]
    AnalyticsTables --> Frontend

---

# Core Tables

These tables store normalized gameplay events.

| Table | Purpose |
|--------|---------|
| players | Unique player information |
| matches | Match metadata |
| player_match_stats | Player statistics for each match |
| rounds | Round-level information |
| kill_events | Individual kill events |
| damage_events | Individual damage events |
| sessions | Gameplay sessions |
| session_matches | Match-to-session relationships |

---

# Dimension Tables

These tables provide descriptive metadata used by analytical queries.

| Table | Purpose |
|--------|---------|
| episodes | Valorant Episodes |
| acts | Valorant Acts |
| dim_periods | Reporting periods |
| dim_ranks | Rank lookup values |

---

# Analytics Tables

These tables contain precomputed statistics for fast reporting.

| Table | Purpose |
|--------|---------|
| player_period_stats | Overall player summaries |
| player_agent_period_stats | Agent performance |
| player_map_period_stats | Map performance |
| player_weapon_period_stats | Weapon performance |
| player_side_period_stats | Attacking / defending performance |
| player_highlight_period_stats | Fun recap metrics |

---

# Data Lifecycle

```mermaid
flowchart TD

API

↓

Core Tables

↓

Aggregate Computation

↓

Analytics Tables

↓

Frontend
```

---

# Design Principles

The schema was designed with the following goals:

- Normalize raw gameplay data
- Preserve historical records
- Support scalable analytics
- Minimize duplicated information
- Optimize reporting queries