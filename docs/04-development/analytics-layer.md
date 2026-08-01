# Analytics Layer

## Overview

## Purpose

The Analytics Layer transforms normalized gameplay data into meaningful player insights.

It serves as the bridge between the transactional database and the user-facing Season Recap.

Rather than querying raw match data directly, the application should consume pre-computed analytics that are optimized for reporting and storytelling.

---

# Responsibilities

The Analytics Layer is responsible for:

- Aggregating player performance
- Calculating season statistics
- Computing advanced metrics
- Generating recap-ready datasets
- Supporting future analytical features

The Analytics Layer is **not** responsible for:

- Fetching API data
- Parsing JSON
- Rendering the frontend

---

# Architecture

```
HenrikDev API
        ↓

Data Synchronization

        ↓

Normalized Database

        ↓

Analytics Layer

        ↓

Season Recap

        ↓

Frontend
```

---

# Design Principles

## Source of Truth

Normalized tables remain the authoritative source of gameplay data.

Analytics tables should always be reproducible from normalized data.

---

## Reproducibility

Every metric should be derived from stored data.

Analytics should never require another API request.

---

## Separation of Concerns

The analytics layer should expose business metrics rather than database tables.

Example:

Instead of:

```
player_match_stats
```

The recap consumes:

```
Highest Kill Game

Favorite Agent

Longest Win Streak

Peak Rank
```

---

## Pre-Computed Analytics

Frequently used metrics should be stored in aggregate tables.

Benefits include:

- Faster recap generation
- Simpler frontend queries
- Consistent calculations

---

# Data Flow

```
Raw Match Data

↓

Normalized Tables

↓

Aggregate Calculations

↓

Player Period Statistics

↓

Recap Generator
```

---

# Analytics Categories

The analytics layer organizes calculations into logical categories.

## Season Summary

Examples:

- Matches played
- Wins
- Losses
- Win rate
- Hours played

---

## Competitive Performance

Examples:

- Initial rank
- Peak rank
- Final rank
- Rank progression

---

## Agent Analytics

Examples:

- Favorite agent
- Win rate by agent
- K/D by agent

---

## Map Analytics

Examples:

- Best map
- Worst map
- Most played map

---

## Combat Analytics

Examples:

- Kills
- Deaths
- Assists
- Damage
- Headshot percentage

---

## Highlight Analytics

Examples:

- Highest kill game
- Highest damage game
- Match MVPs
- Longest win streak

---

## Behavioral Analytics

Examples:

- Time of day performance
- Session length
- Play frequency
- Weekend vs weekday

---

# Aggregate Tables

The Analytics Layer stores pre-computed metrics in aggregate tables.

Current aggregates include:

- player_period_stats
- player_agent_period_stats
- player_map_period_stats
- player_weapon_period_stats
- player_side_period_stats
- player_highlight_period_stats

Future aggregate tables may be added as new analytics are introduced.

---

# Recap Generation

The Season Recap should retrieve data exclusively from aggregate tables whenever possible.

Benefits:

- Faster page loads
- Reduced database complexity
- Consistent analytics
- Simpler frontend

---

# Current Status

## Completed

- Aggregate schema designed
- Period dimension created
- Core analytics categories identified

---

## In Progress

- Aggregate computation pipeline
- Metric validation
- Period processing

---

## Future

- Historical comparisons
- Career analytics
- Friend comparisons
- Advanced behavioral insights

---

# Guiding Principle

The Analytics Layer transforms gameplay data into player stories.

Raw data answers:

> "What happened?"

The Analytics Layer answers:

> "What does it mean?"