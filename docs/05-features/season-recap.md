# Season Recap

## Overview

## Description

Season Recap is the core user experience of Valorant Season Recap.

The feature transforms a player's Valorant match history into a Spotify Wrapped-style story highlighting interesting statistics, memorable moments, and unique aspects of their season.

The goal is not to display every available statistic, but to identify the insights that best describe a player's journey.

---

# Product Goal

The Season Recap should make players feel:

- "These stats are surprisingly insightful."
- "That was a fun experience."
- "I want to share this with my friends."

The recap should answer:

> What story does my Valorant season tell?

---

# User Flow

Release 1:

```
Landing Page

↓

User enters Riot ID

↓

Search existing player data

↓

Player data exists?

YES:
Generate recap from database

NO:
Fetch API data
Store player history
Generate recap

↓

Display Season Recap
```

---

# Release 1 Scope

## Included

### Player Lookup

Users enter their Riot ID to generate their recap.

---

### Previous Season Recap

Release 1 automatically generates the previous completed season.

Future versions may allow users to select seasons.

---

### Competitive Focus

The primary recap experience focuses on Competitive gameplay.

Competitive statistics are the main storyline.

Unrated data may be stored and analyzed, but is not the primary experience in Release 1.

---

### Season Story

The recap should contain approximately:

- 10-15 sections/cards
- A beginning, middle, and conclusion
- A shareable summary

The exact sections will evolve as analytics capabilities are developed.

---

# Recap Content

Potential recap sections:

## Season Overview

Examples:

- Matches played
- Hours played
- Wins/losses
- Overall performance


## Competitive Journey

Examples:

- Starting rank
- Peak rank
- Ending rank
- Rank progression


## Agent Performance

Examples:

- Most played agent
- Best performing agent
- Agent preferences


## Map Performance

Examples:

- Best map
- Worst map
- Most played map


## Combat Performance

Examples:

- K/D ratio
- Damage
- Headshot percentage
- Combat highlights


## Personal Highlights

Examples:

- Highest kill game
- Highest damage game
- Longest win streak
- Best individual performance


## Player Personality

The recap should use statistics to create a fun but meaningful description.

Example:

Instead of:

"Your KD was 1.55"

Use:

"You were deadly this season, consistently winning your fights."

Personality should be generated using rule-based logic, not AI.

---

# Design Principles

The recap should follow these principles:

## Story Over Dashboard

The experience should feel like a journey, not a statistics page.

---

## Insight Over Information

Prioritize surprising or interesting statistics over common metrics.

---

## Shareability

The recap should create moments players want to share.

---

## Personalization

Every recap should feel unique to the player.

---

# Data Requirements

The recap requires:

## Player Data

- Riot ID
- Player identifier


## Match Data

- Match history
- Date played
- Map
- Game mode
- Outcome


## Player Statistics

- Kills
- Deaths
- Assists
- Agent
- Rank
- Damage
- Headshots


## Historical Data

The system should maintain permanent player history.

Future capabilities:

- Season comparisons
- Career trends
- Friend comparisons

---

# Generation Strategy

The recap uses a hybrid generation approach.

## Existing Player Data

If player data exists:

```
Database
    ↓
Analytics
    ↓
Generate Recap
```

---

## New Player Data

If player data does not exist:

```
API Request
    ↓
ETL Pipeline
    ↓
Database
    ↓
Analytics
    ↓
Generate Recap
```

---

# Out of Scope (Release 1)

Not included:

- AI-generated summaries
- Friend comparisons
- Public profiles
- Season comparisons
- User accounts
- Multiple recap personalities
- Cross-game support

---

# Future Enhancements

Potential future features:

- Compare seasons
- Compare friends
- Competitive vs casual recap
- AI-assisted storytelling
- Player archetypes
- Public sharing profiles

---

# Acceptance Criteria

The feature is complete when:

- User can enter Riot ID
- System can generate a season recap
- Existing player data is reused
- Missing player data triggers synchronization
- Statistics are accurate
- Recap provides meaningful insights
- Output can be shared