# Project Scope

## Version 1 Objective

The first version of Valorant Season Recap will focus on creating a complete pipeline from player input to generated seasonal statistics.

The MVP goal:

> Allow a user to enter their Riot ID and generate a personalized Valorant season overview.

---

# In Scope

## Data Collection

- Retrieve player match history
- Collect match metadata
- Collect player statistics
- Store historical match data

## Data Engineering

- Build ETL pipeline
- Normalize API responses
- Store structured data
- Create analytics tables

## Analytics

Generate statistics including:

- Matches played
- Win rate
- K/D ratio
- Agent performance
- Map performance
- Weapon performance
- Highlight statistics

## User Experience

Future functionality:

- Player search
- Season recap page
- Visual summaries

---

# Out of Scope (Current)

The following features are not planned for initial versions:

- Live match tracking
- Real-time coaching
- Match prediction
- Social features
- Competitive matchmaking analysis
- Mobile application

These may be considered in future versions.

---

# Design Principles

## Data First

The quality of analytics depends on reliable data collection and storage.

## Reproducibility

Raw data and transformations should allow results to be regenerated.

## Scalability

The architecture should support additional players and future features.

## Maintainability

Documentation and organization are treated as first-class parts of the project.