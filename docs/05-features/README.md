# Feature Catalog

## Overview

This document contains the complete catalog of potential features for Valorant Season Recap.

Features are organized by product capability rather than technical implementation.

The purpose of this document is to:

- Capture product ideas
- Define potential user experiences
- Prioritize future development
- Provide the foundation for feature specifications and GitHub issues

This document intentionally does not define implementation details.

---

# Product Goal

Valorant Season Recap transforms player match history into a Spotify Wrapped-style seasonal experience.

The product focuses on:

- Personalized storytelling
- Interesting analytics
- Memorable insights
- Social sharing

A successful feature should help answer:

> "What story does my Valorant season tell?"

---

# Feature Prioritization

## Must Have

Required for the initial product experience.

## Should Have

Strongly improves the experience but not required for the first release.

## Could Have

Interesting enhancements that add value.

## Future Exploration

Ideas that may expand the product in the future.

---

# 1. Player Experience

## Player Search

Priority:
**Must Have**

### Description

Allow users to enter their Riot ID and retrieve their Valorant history.

### User Value

Provides the entry point into the recap experience.

---

## Season Selection

Priority:
**Should Have**

### Description

Allow users to select which season they want to review.

Examples:

- Current season
- Previous season
- Career summary

### User Value

Allows players to explore their history over time.

---

## Season Recap

Priority:
**Must Have**

### Description

Generate a personalized Spotify Wrapped-style summary of a player's season.

Examples:

- Season overview
- Performance highlights
- Personal records
- Favorite play styles

### User Value

The core product experience.

---

# 2. Core Analytics

## Overall Season Statistics

Priority:
**Must Have**

### Description

Provide a high-level summary of the player's season.

Examples:

- Matches played
- Win rate
- Total kills
- Total hours played
- Average performance

---

## Rank Progression

Priority:
**Should Have**

### Description

Visualize how the player's rank changed throughout the season.

Examples:

- Starting rank
- Peak rank
- Ending rank
- Rank climb/fall animation

### User Value

Shows the player's journey, not just the final result.

---

## Agent Performance

Priority:
**Must Have**

### Description

Analyze performance across agents.

Examples:

- Most played agent
- Highest win rate agent
- Best performing agent
- Agent improvement

---

## Map Performance

Priority:
**Must Have**

### Description

Analyze performance across maps.

Examples:

- Best map
- Worst map
- Most played map
- Highest win percentage
- lowest win percentage

---

## Weapon Performance

Priority:
**Should Have**

### Description

Analyze weapon usage and performance.

Examples:

- Favorite weapon
- Most kills
- Headshot percentage
- Weapon accuracy

---

# 3. Advanced Insights

## Time-Based Performance

Priority:
**Could Have**

### Description

Analyze when the player performs best.

Examples:

- Morning vs night performance
- Weekday vs weekend performance
- Best gaming hours

### User Value

Creates unexpected insights players normally do not see.

---

## Win Streak Analysis

Priority:
**Could Have**

### Description

Highlight streak-based achievements.

Examples:

- Longest win streak
- Best climbing streak
- Largest comeback streak

---

## Carry Performance

Priority:
**Should Have**

### Description

Identify games where the player had exceptional impact.

Examples:

- Highest kill game
- Highest damage game
- Match MVP count
- Team carry percentage

---

## Unluckiest Game

Priority:
**Could Have**

### Description

Identify games where performance was strong despite losing.

Examples:

- High kills in a loss
- High damage loss
- Close overtime losses

---

## Personal Records

Priority:
**Should Have**

### Description

Highlight unique achievements.

Examples:

- Most kills
- Highest damage
- Longest game
- Most assists

---

# 4. Social Features

## Shareable Recap Cards

Priority:
**Should Have**

### Description

Allow users to share individual recap moments.

Examples:

- Favorite agent card
- Season summary card
- Best game card
- Rank progression card

### User Value

Supports organic sharing and discovery.

---

## Compare With Friends

Priority:
**Could Have**

### Description

Allow players to compare season summaries.

Examples:

- Total hours
- Favorite agents
- Win rate
- Highest performance

---

## Position in Community Rankings

Priority:
**Future Exploration**

### Description

Compare statistics across a broader player population. Ex. top xx%

---

# 5. Engagement Features

## Career History

Priority:
**Could Have**

### Description

Allow users to explore performance across multiple seasons.

Examples:

- Season comparisons
- Long-term improvement
- Career milestones

---

## Seasonal Trends

Priority:
**Could Have**

### Description

Show how player behavior changes over time.

Examples:

- Improving win rate
- Changing agent preferences
- Increasing playtime

---

# 6. Fun / Entertainment Features

## Gaming Personality

Priority:
**Could Have**

### Description

Create a personality-style summary.

Examples:

- The Strategist
- The Duelist
- The Grinder
- The Carry

---

## Favorite Teammate

Priority:
**Could Have**

### Description

Identify players frequently played with.

---

## Nemesis Player

Priority:
**Future Exploration**

### Description

Identify opponents frequently encountered or lost against.

---

## Longest Gaming Session

Priority:
**Could Have**

### Description

Highlight player commitment.

Example:

> "Your longest Valorant session lasted 6 hours."

---

# 7. Platform Features

## Multiple Game Support

Priority:
**Future Exploration**

### Description

Expand the platform beyond Valorant.

Potential future games:

- Overwatch

---

# MVP Feature Set

The first public version should focus on creating a complete and shareable recap experience.

MVP features:

1. Player Search
2. Season Overview
3. Agent Performance
4. Map Performance
5. Rank Progression
6. Personal Highlights
7. Shareable Recap Experience

---

# Feature Development Process

Every major feature should eventually receive a dedicated specification document.

Example:

```
Feature Idea

↓

Feature Specification

↓

GitHub Epic

↓

GitHub Issues

↓

Implementation

↓

Documentation Update
```

---

# Feature Evaluation Criteria

Before adding a feature, evaluate:

## Does it create insight?

Does the player learn something new?

## Does it create emotion?

Does it make the player excited, surprised, or proud?

## Is it shareable?

Would a player show this to a friend?

## Is it worth the complexity?

Does the value justify the engineering effort?

---

# Guiding Principle

The goal is not to display every statistic available.

The goal is to discover the most interesting story hidden inside the data.