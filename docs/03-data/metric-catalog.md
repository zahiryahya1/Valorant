# Metric Catalog

## Purpose

The Metric Catalog serves as the authoritative reference for every analytical metric used throughout the application.

Each metric is categorized by business domain and assigned a priority for implementation. The catalog defines **what** the application measures, while implementation details are documented separately in the Analytics Requirements.

---

# Metric Status

| Status | Description |
|----------|-------------|
| Planned | Metric has been defined but not implemented. |
| In Progress | Metric is currently under development. |
| Implemented | Metric has been implemented. |
| Validated | Metric has been tested and verified. |
| Future | Planned for a future release. |

---

# Priority Definitions

| Priority | Description |
|----------|-------------|
| Must | Required for Release 1 (MVP). |
| Should | Valuable for Release 1 if time permits. |
| Future | Planned for a future release. |

---

# Season Summary

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| SS-001 | Matches Played | Must | Planned | Core recap statistic |
| SS-002 | Wins | Must | Planned | |
| SS-003 | Losses | Must | Planned | |
| SS-004 | Win Rate | Must | Planned | |
| SS-005 | Total Hours Played | Must | Planned | Derived from match duration |
| SS-006 | Total Rounds Played | Must | Planned | |
| SS-007 | Average Match Length | Should | Planned | |

---

# Competitive Progression

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| CP-001 | Starting Rank | Must | Planned | |
| CP-002 | Peak Rank | Must | Planned | |
| CP-003 | Ending Rank | Must | Planned | |
| CP-004 | Median Rank | Must | Planned | Rank with the most time spent |
| CP-005 | Rank Progression | Should | Planned | Animated timeline |

---

# Combat Performance

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| COM-001 | Kills | Must | Planned | |
| COM-002 | Deaths | Must | Planned | |
| COM-003 | Assists | Must | Planned | |
| COM-004 | K/D Ratio | Must | Planned | |
| COM-005 | Damage | Must | Planned | |
| COM-006 | Average Kills per Match | Must | Planned | |
| COM-007 | Average Damage per Match | Must | Planned | |
| COM-008 | Headshots | Must | Planned | |
| COM-009 | Headshot Percentage | Must | Planned | |
| COM-010 | Bodyshots | Must | Planned | |
| COM-011 | Legshots | Must | Planned | |
| COM-012 | Accuracy Percentage | Must | Planned | |

---

# Agent Analytics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| AG-001 | Most Played Agent | Must | Planned | |
| AG-002 | Best Win Rate Agent | Must | Planned | |
| AG-003 | Worst Agent | Must | Planned | |
| AG-004 | Win Rate by Agent | Must | Planned | |
| AG-005 | K/D by Agent | Must | Planned | |
| AG-006 | Matches by Agent | Must | Planned | |
| AG-007 | Most Improved Agent | Future | Future | |
| AG-008 | Role Preference | Future | Future | Preferred role distribution |
| AG-009 | Flexibility Score | Future | Future | Agent diversity |

---

# Map Analytics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| MAP-001 | Best Map | Must | Planned | |
| MAP-002 | Worst Map | Must | Planned | |
| MAP-003 | Win Rate by Map | Must | Planned | |
| MAP-004 | K/D by Map | Must | Planned | |
| MAP-005 | Damage by Map | Should | Planned | |
| MAP-006 | Attack vs Defense by Map | Future | Future | |
| MAP-007 | Overtime Frequency | Future | Future | |
| MAP-008 | Dodge Rate | Future | Future | If API supports |

---

# Weapon Analytics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| WP-001 | Deaths by Weapon | Should | Planned | |
| WP-002 | Kills by Weapon | Must | Planned | |
| WP-003 | Headshot Percentage by Weapon | Must | Planned | |

---

# Side Performance

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| SIDE-001 | Attack Win Rate | Must | Planned | |
| SIDE-002 | Defense Win Rate | Must | Planned | |
| SIDE-003 | K/D by Side | Should | Planned | |
| SIDE-004 | Best Side by Map | Future | Future | |
| SIDE-005 | Round Differential | Future | Future | |

---

# Session Analytics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| SES-001 | Longest Gaming Session | Future | Future | |
| SES-002 | Number of Sessions | Future | Future | |
| SES-003 | Average Session Length | Future | Future | |
| SES-004 | Number of Overtimes | Future | Future | |
| SES-005 | Overtime Win Rate | Future | Future | |
| SES-006 | Latest Night Played | Future | Future | |
| SES-007 | Earliest Morning Played | Future | Future | |
| SES-008 | Longest Ranked Grind | Future | Future | |
| SES-009 | Most Matches in One Day | Future | Future | |

---

# Highlight Metrics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| HL-001 | Highest Kill Game | Must | Planned | |
| HL-002 | Highest Damage Game | Must | Planned | |
| HL-003 | Longest Win Streak | Should | Planned | |
| HL-004 | Longest Loss Streak | Should | Planned | |
| HL-005 | Match MVP Count | Must | Planned | |
| HL-006 | Team MVP Count | Must | Planned | |
| HL-007 | Total Aces | Should | Planned | |
| HL-008 | Best Match | Should | Planned | |
| HL-009 | Most Clutch Match | Future | Future | |
| HL-010 | Times Carried | Future | Future | |
| HL-011 | Largest Comeback | Future | Future | |
| HL-012 | Number of Comebacks | Future | Future | |
| HL-013 | Number of Blunders | Future | Future | Lost after large lead |

---

# Time-Based Analytics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| TIME-001 | Weekend vs Weekday Performance | Should | Planned | |
| TIME-002 | Time of Day Performance | Should | Planned | |
| TIME-003 | Hour-by-Hour Heatmap | Future | Future | |
| TIME-004 | Monthly Trends | Future | Future | |
| TIME-005 | Favorite Play Day | Future | Future | |

---

# Objective Metrics

| ID | Metric | Priority | Status | Notes |
|----|--------|----------|--------|------|
| OBJ-001 | Bombs Planted | Must | Planned | |
| OBJ-002 | Bombs Defused | Must | Planned | |
| OBJ-003 | Spike Plant Success Rate | Future | Future | |
| OBJ-004 | Objective Score | Future | Future | |

---

# Personality Metrics

Derived from multiple analytical metrics.

Release 1 examples:

- Deadly
- Consistent
- Fighter
- Controller Specialist
- Marathon Grinder
- Clutch Performer

Future:

- Player archetypes
- Multiple personality dimensions
- Achievement badges

---

# Social Metrics

Future:

- Friend Comparison
- Percentile Rankings
- Community Comparisons
- Shareable statistics

---

# Historical Metrics

Future:

- Season-over-Season Improvement
- Career K/D
- Career Win Rate
- Rank Progression Across Seasons
- Lifetime Agent Usage
- Long-Term Trends