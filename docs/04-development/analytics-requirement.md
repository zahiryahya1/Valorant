# Analytics Requirements

## 1. Purpose

The Analytics Requirements document defines how gameplay data is transformed into meaningful player insights for the Valorant Season Recap application.

This document bridges the gap between:

- Product requirements
- Data architecture
- Database design
- Analytics implementation

The goal is to create a scalable analytics system capable of generating Spotify Wrapped-style season summaries while maintaining reliable and maintainable data engineering practices.

---

# 2. Analytics Architecture

The analytics system follows a layered data architecture that transforms gameplay data into user-facing insights.


```mermaid
flowchart LR

A[Raw Layer]

A --> B[Normalized Layer]

B --> C[Analytics Layer]

C --> D[Application Layer]
```

---

## 01 Raw Layer

### Purpose

Stores original gameplay data collected from external APIs before transformation.

### Data Source

- HenrikDev Valorant API

### Characteristics

- Original API response format
- Used for recovery and reprocessing
- No business logic applied

---

## 02 Normalized Layer

### Purpose

Transforms raw API responses into structured relational tables representing gameplay facts.

### Responsibilities

- Parse and clean API responses
- Standardize data formats
- Remove duplicates
- Establish relationships between entities

### Characteristics

The normalized layer contains the source-of-truth gameplay data used for analytics calculations.

### Primary Sources

- `players`
- `matches`
- `player_match_stats`
- `rounds`
- `kill_events`
- `damage_events`

---

## 03 Analytics Layer

### Purpose

Transforms normalized gameplay data into aggregated metrics optimized for application usage.

### Responsibilities

- Calculate player statistics
- Aggregate metrics by time period
- Generate analytical summaries
- Store reusable insights

### Characteristics

Analytics tables should contain precomputed metrics to avoid expensive calculations during user requests.

### Primary Outputs

- `player_period_stats`
- `player_agent_period_stats`
- `player_map_period_stats`
- `player_weapon_period_stats`
- `player_side_period_stats`
- `player_highlight_period_stats`

---

## 04 Application Layer

### Purpose

Transforms analytical outputs into user-facing experiences.

### Responsibilities

- Deliver recap data to users
- Format metrics for presentation
- Support frontend visualization

---

## Analytics Flow

The complete data flow is:

```mermaid
flowchart LR

A[External API]

A --> B[Raw gameplay response]

B --> C[Normalized gameplay tables]

C --> D[Aggregated player analytics]

D --> E[Season recap experience]
```

# 3. Analytics Development Principles

The analytics system follows these principles to ensure metrics are reliable, scalable, and maintainable.

---

## Principle 1: Precompute Analytics Metrics

Analytics metrics should be calculated before user requests and stored in the Analytics Layer.

The application should retrieve prepared metrics rather than performing complex calculations during runtime.

Preferred flow:

```mermaid
flowchart LR

A[Normalized Data]

A --> B[Analytics Pipeline]

B --> C[Analytics Tables]

C --> D[Application]
```

Avoid:

```mermaid
flowchart LR

A[Application Request]

A --> B[Run Complex Calculations]

B --> C[Return Results]
```

---

## Principle 2: Separate Gameplay Facts From Insights

The system should separate raw gameplay measurements from derived interpretations.

### Facts

Directly measured gameplay data:

- Kills
- Deaths
- Damage
- Wins
- Matches Played

### Insights

Metrics derived from multiple facts:

- Performance Score
- Carry Games
- Player Personality
- Achievement Badges

---

## Principle 3: Maintain Reusable Analytics

Analytics calculations should support multiple product experiences.

Metrics should be reusable for:

- Season Recap
- Player Profile
- Future social features
- Historical analysis

---

## Principle 4: Define Metric Logic Before Implementation

Each metric should have a documented definition before implementation.

Each metric requirement should define:

- Data source
- Calculation logic
- Destination table
- Validation approach

---

## Principle 5: Prioritize Accuracy Over Complexity

Metrics should only be implemented when they can be calculated reliably from available data.

If data availability or calculation logic is uncertain, the metric should be deferred until requirements are better defined.


# 4. Metric Requirement Template

Each analytics metric should be documented using the following structure.

---

## [Metric ID] [Metric Name]

### Definition

Describe what the metric represents and why it is valuable to the user experience.

### Source Layer

The layer where the required data originates:

- 01 Raw Layer
- 02 Normalized Layer
- 03 Analytics Layer
- 04 Application Layer

### Source Table

List the database tables required to calculate the metric.

Example: 
- matches
- rounds

### Destination

The location where the calculated metric is stored. 

Example

- Table: player_period_stats
- Column: win_rate

### Calculation Logic

Describe the calculation or transformation required.

Example:

- wins / mathces_played

### Release

Target release:

- Release 1
- Future

### Acceptance Criteria

Describe how the metric will be verified. 

Example:

- Compare aggregate results against raw match-level calculations
- Validate against known player statistics

# 5. Analytics Metric Requirements

This section defines the analytical metrics required for the Valorant Season Recap application.

Each metric defines the required data source, calculation logic, destination, and validation approach.

---

# 5.1 Act Summary Metrics

Season Summary metrics provide an overview of a player's activity and performance during a selected period.

These metrics form the foundation of the season recap experience.

---

## AS-001 Matches Played

### Definition

Total number of matches played by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Table

- player_match_stats
- matches

### Destination

- Table: player_period_stats
- Column: matches_played

### Calculation Logic

Count the number of unique matches associated with the player.

### Release

Release 1

### Acceptance Criteria

- none

---

## AS-002 Wins

### Definition

Total number of matches won by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Table

- player_match_stats

### Destination

- Table: layer_period_stats
- Column: wins

### Calculation Logic

Count matches where the player won is true.

### Release

Release 1

### Acceptance Criteria

- Wins + losses = matches played

---

## AS-003 Losses

### Definition

Total number of matches lost by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Table

- player_match_stats

### Destination

- Table: player_period_stats
- Column: losses

### Calculation Logic

Count matches where the player won is false.

### Release

Release 1

### Acceptance Criteria

- Wins + losses = matches played

---

## SUM-004 Win Rate

### Definition

Percentage of matches won by a player during the selected period.

### Source Layer

03 Analytics Layer

### Source Table

- player_period_stats

### Destination

- Table: player_period_stats
- column: win_rate

### calculated Logic

- wins / matches_played ( should be a calculated field within the database table)

### Release

Release 1

### Acceptance Criteria

- none

---

## AS-005 Total Hours Played

### Definition

Total gameplay time during the selected period.

### Source Layer

02 Normalized Layer

### Source Table

- matches

### Destination

- Table: player_period_stats
- Column: total_hours


### Calculation Logic

For each match, add game length. Convert seconds to hours.

### Release

Release 1

### Acceptance Criteria

- none

---

## SUM-006 Total Rounds Played

### Definition

Total number of rounds played during the selected period.

### Source Layer

02 Normalized Layer

### Source Table

- matches

### Destination

- Table: player_period_stats
- Column: total_rounds

### Calculation Logic

For each match within a period, sum rounds played.

### Release

Release 1

### Acceptance Criteria

- none

---

## SUM-007 Average Match Length

### Definition

Average duration of matches played during the selected period ion hours.

### Source Layer

02 Normalized Layer

### Source Table
- player_match_stats
- matches

### Destination

- Table: player_period_stats
- Column: avg_match_length

### Calculation Logic

Divide total_hours by matches_played (calculated field within the table)

### Complexity

Low

### Release

Release 1

### Status

Planned

### Validation

Compare against individual match durations.


# 5.2 Competitive Progression Metrics

Competitive Progression metrics summarize a player's ranked performance throughout a season. These metrics capture where a player started, where they peaked, where they finished, and how their rank evolved over time.

---

## COMP-001 Starting Rank

### Definition

The player's competitive rank at the beginning of the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_period_stats`
- **Column:** `initial_rank`

### Calculation Logic

Identify the player's first competitive match within the selected period and record the corresponding rank.

### Release

Release 1

### Acceptance Criteria

The value matches the player's rank from their earliest competitive match within the selected period.

---

## COMP-002 Peak Rank

### Definition

The highest competitive rank achieved during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods
- dim_ranks

### Destination

- **Table:** `player_period_stats`
- **Column:** `peak_rank`

### Calculation Logic

Determine the highest ranked tier achieved during the selected period using the numeric rank mapping.

### Release

Release 1

### Acceptance Criteria

The recorded rank equals the highest competitive rank observed during the selected period.

---

## COMP-003 Ending Rank

### Definition

The player's competitive rank at the end of the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_period_stats`
- **Column:** `end_rank`

### Calculation Logic

Identify the player's final competitive match within the selected period and record the corresponding rank.

### Release

Release 1

### Acceptance Criteria

The value matches the player's rank from their final competitive match within the selected period.

---

## COMP-004 Median Rank

### Definition

The competitive rank occupied for the greatest portion of the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods
- dim_ranks

### Destination

- **Table:** `player_period_stats`
- **Column:** `median_rank`

### Calculation Logic

Determine the most frequently occurring competitive rank during the selected period.

If multiple ranks have the same frequency, select the highest rank achieved.

### Release

Release 1

### Acceptance Criteria

The recorded rank represents the player's most frequently observed competitive rank during the selected period.

---

## COMP-005 Rank Progression

### Definition

A chronological representation of the player's competitive rank progression throughout the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods
- dim_ranks

### Destination

Not stored.

### Calculation Logic

Sort competitive matches by match date and associate each match with the player's recorded rank to produce a progression timeline.

### Release

Release 1

### Acceptance Criteria

The generated timeline accurately reflects the player's rank progression across the selected period.



# 5.3 Combat Performance Metrics

Combat Performance metrics summarize a player's mechanical performance during the selected period.

These metrics measure individual combat contribution through kills, deaths, assists, damage output, and accuracy.

---

## CP-001 Total Kills

### Definition

Total number of kills achieved by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `total_kills`

### Calculation Logic

Sum all kills recorded for the player.

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level kills for the player during the selected period.

---

## CP-002 Total Deaths

### Definition

Total number of deaths experienced by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `total_deaths`

### Calculation Logic

Sum all deaths recorded for the player.

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level deaths for the player during the selected period.

---

## CP-003 Total Assists

### Definition

Total number of assists earned by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `total_assists`

### Calculation Logic

Sum all assists recorded for the player.

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level assists for the player during the selected period.

---

## CP-004 K/D Ratio

### Definition

The ratio of kills compared to deaths during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_period_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `kd_ratio`

### Calculation Logic

If deaths equal zero, then total kills. 

else, total_kills / total_deaths (calculated field)

### Release

Release 1

### Acceptance Criteria

The calculated value matches the ratio of total kills divided by total deaths.

---

## CP-005 Total Damage

### Definition

Total damage dealt by a player during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `total_damage`

### Calculation Logic

Sum all damage. (calcualted field)

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level damage values.

---

## CP-006 Average Kills Per Match

### Definition

Average number of kills achieved per match during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_period_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `avg_kills_per_match`

### Calculation Logic

total_kills / matches_played (calcualted field)

### Release

Release 1

### Acceptance Criteria

The calculated value equals total kills divided by total matches played.

---

## CP-007 Average Damage Per Match

### Definition

Average damage dealt per match during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_period_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `avg_damage_per_match`

### Calculation Logic

total_damage / matches_played (calculated field)

### Release

Release 1

### Acceptance Criteria

The calculated value equals total damage divided by total matches played.

---

## CP-008 Total Headshots

### Definition

Total number of headshots achieved during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `headshots`

### Calculation Logic

Sum all headshots.

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level headshots.

---

## CP-009 Headshot Percentage

### Definition

Percentage of shots that resulted in headshots during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_period_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `headshot_percent`

### Calculation Logic

Accuracy is calculated based on recorded hit locations. 

headshots / (headshots + bodyshots + legshots)

### Release

Release 1

### Acceptance Criteria

The calculated percentage matches the headshot count divided by total recorded hit locations.

---

## CP-010 Bodyshots

### Definition

Total number of body shots recorded during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `bodyshots`

### Calculation Logic

sum of bodyshots. 

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level body shots.

---

## CP-011 Legshots

### Definition

Total number of leg shots recorded during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_period_stats`
- **Column:** `legshots`

### Calculation Logic

sum of legshots

### Release

Release 1

### Acceptance Criteria

The calculated total matches the sum of match-level leg shots.

---

# 5.4 Agent Analytics

Agent Analytics measure a player's performance across each agent played during the selected period. These metrics provide insight into agent preferences, effectiveness, and playstyle.

All metrics in this section are stored in the `player_agent_period_stats` table.

---

## AG-001 Matches Played by Agent

### Definition

The total number of matches played with each agent during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `matches_played`

### Calculation Logic

Count the number of matches grouped by player and agent.

### Release

Release 1

### Acceptance Criteria

The total equals the number of matches played on each agent during the selected period.

---

## AG-002 Wins by Agent

### Definition

The total number of wins achieved while playing each agent.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `wins`

### Calculation Logic

Count matches where `won = TRUE`.

### Release

Release 1

### Acceptance Criteria

The win total matches the number of wins recorded for the agent.

---

## AG-003 Losses by Agent

### Definition

The total number of losses while playing each agent.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `losses`

### Calculation Logic

Count matches where `won = FALSE`.

### Release

Release 1

### Acceptance Criteria

Wins + Losses equals Matches Played for every agent.

---

## AG-004 Win Rate by Agent

### Definition

The percentage of matches won while playing each agent.

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `win_rate`

### Calculation Logic

wins / matches_played (calculated field)

### Release

Release 1

### Acceptance Criteria

The calculated value equals wins divided by matches played.

---

## AG-005 Total Kills by Agent

### Definition

The total number of kills achieved with each agent.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `kills`

### Calculation Logic

Sum of kills with matches played by the agent

### Release

Release 1

### Acceptance Criteria

The total equals the sum of kills recorded for that agent.

---

## AG-006 Total Deaths by Agent

### Definition

The total number of deaths while playing each agent.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `deaths`

### Calculation Logic

Sum of deaths with matches played by the agent


### Release

Release 1

### Acceptance Criteria

The total equals the sum of deaths recorded for that agent.

---

## AG-007 Total Assists by Agent

### Definition

The total number of assists while playing each agent.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `assists`

### Calculation Logic

Sum of assists with matches played by the agent

### Release

Release 1

### Acceptance Criteria

The total equals the sum of assists recorded for that agent.

---

## AG-008 K/D Ratio by Agent

### Definition

The ratio of kills to deaths for each agent.

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `kd_ratio`

### Calculation Logic

total kills / total deaths (calcualted field)

If deaths equal zero, return total kills.

### Release

Release 1

### Acceptance Criteria

The value equals total kills divided by total deaths.

---

## AG-009 Total Damage by Agent

### Definition

The total damage dealt per match while playing each agent.

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `total_damage`

### Calculation Logic

sum damage by agent for all games within period. 

### Release

Release 1

### Acceptance Criteria

The value equals total damage by matches played.

---

## AG-010 Average Damage by Agent

### Definition

The average damage dealt per match while playing each agent.

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats

### Destination

- **Table:** `player_agent_period_stats`
- **Column:** `avg_damage`

### Calculation Logic

average damage by agent within period. 

### Release

Release 1

### Acceptance Criteria

The value equals average damage by matches played.

---

## AG-011 Most Played Agent

### Definition

The agent with the greatest number of matches played during the selected period.

### Source Layer

04 Application Layer

### Source Tables

- player_agent_period_stats

### Destination

Not stored.

### Calculation Logic

Select the agent with the highest `matches_played`.

### Release

Release 1

### Acceptance Criteria

The returned agent has the highest match count for the selected period.

---

## AG-012 Best Win Rate Agent

### Definition

The agent with the highest win rate during the selected period.

### Source Layer

04 Application Layer

### Source Tables

- player_agent_period_stats

### Destination

Not stored.

### Calculation Logic

Rank agents by `win_rate`.

Minimum match threshold may be introduced in a future release.

### Release

Release 1

### Acceptance Criteria

The returned agent has the highest valid win rate.

---

## AG-013 Worst Win Rate Agent

### Definition

The agent with the lowest win rate during the selected period.

### Source Layer

04 Application Layer

### Source Tables

- player_agent_period_stats

### Destination

Not stored.

### Calculation Logic

Rank agents by ascending `win_rate`.

Minimum match threshold may be introduced in a future release.

### Release

Release 1

### Acceptance Criteria

The returned agent has the lowest valid win rate.

---

## AG-014 Most Improved Agent

### Definition

The agent showing the greatest improvement in player performance compared to a previous period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats

### Destination

Not stored.

### Calculation Logic

Compare selected performance metrics (for example, win rate, K/D ratio, or Performance Score) between two periods for each agent.

The agent with the greatest positive improvement is returned.

### Release

Future

### Acceptance Criteria

The identified agent demonstrates the largest positive improvement according to the selected comparison metric.

---

## AG-015 Role Preference

### Definition

The distribution of matches played across Valorant agent roles (Duelist, Controller, Initiator, Sentinel).

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats
- dim_agents (Future)

### Destination

Not stored.

### Calculation Logic

Aggregate matches played by agent role and calculate the percentage of total matches played for each role.

### Release

Future

### Acceptance Criteria

The calculated distribution accurately represents the percentage of matches played for each agent role.

---

## AG-016 Flexibility Score

### Definition

A measure of how diverse a player's agent pool is during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_agent_period_stats

### Destination

Not stored.

### Calculation Logic

Compute a diversity score using the number of unique agents played and the distribution of matches across those agents.

The exact scoring algorithm will be defined during implementation.

### Release

Future

### Acceptance Criteria

Players using a wider variety of agents receive a higher Flexibility Score than players who primarily play a single agent.


# 5.5 Map Analytics

Map Analytics summarize a player's performance across each map played during the selected period. These metrics provide insight into map preferences and identify environments where the player performs best.

All metrics in this section are stored in the `player_map_period_stats` table unless otherwise specified.

---

## MAP-001 Best Map

### Definition

The map on which the player achieved the strongest overall performance during the selected period.

### Source Layer

04 Application Layer

### Source Tables

- player_map_period_stats

### Destination

Not stored.

Calculated when generating the season recap.

### Calculation Logic

Rank maps using a selected performance metric (for Release 1, Win Rate).

Future versions may use a composite Performance Score.

### Release

Release 1

### Acceptance Criteria

The returned map has the highest qualifying performance for the selected period.

---

## MAP-002 Worst Map

### Definition

The map on which the player performed the weakest during the selected period.

### Source Layer

04 Application Layer

### Source Tables

- player_map_period_stats

### Destination

Not stored.

Calculated when generating the season recap.

### Calculation Logic

Rank maps by lowest Win Rate.

Future versions may use a composite Performance Score.

### Release

Release 1

### Acceptance Criteria

The returned map has the lowest qualifying performance for the selected period.

---

## MAP-003 Wins by Map

### Definition

The number of wins achived per map.

### Source Layer

03 Analytical Layer

### Source Tables

- player_match_stats

### Destination

- player_map_period_stats

### Calculation Logic

Count number of wins
### Release

Release 1

### Acceptance Criteria

The number of wins matches the count of total wins for the map. 

---

## MAP-004 Matches for Map

### Definition

The number of matches per map.

### Source Layer

03 Analytical Layer

### Source Tables

- player_match_stats

### Destination

- **Table:** `player_map_period_stats`
- **Column:** `matches_played`

### Calculation Logic

Count number of matches

### Release

Release 1

### Acceptance Criteria

The number of matches equal the number of mathces played on the map.

---

## MAP-005 Win Rate by Map

### Definition

The percentage of matches won on each map during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_map_period_stats

### Destination

- **Table:** `player_map_period_stats`
- **Column:** `win_rate`

### Calculation Logic

wins / matches_played

### Release

Release 1

### Acceptance Criteria

The calculated value equals wins divided by matches played for each map.

---

## MAP-008 K/D Ratio by Map

### Definition

The ratio of kills to deaths on each map during the selected period.

### Source Layer

03 Analytics Layer

### Source Tables

- player_map_period_stats

### Destination

**Table:** `player_map_period_stats`

**Column:** `kd_ratio`

### Calculation Logic

```text
kills / deaths
```

If deaths equal zero, return total kills.

### Release

Release 1

### Acceptance Criteria

The calculated value equals total kills divided by total deaths for each map.

---

## MAP-005 Damage by Map

### Definition

The total damage dealt on each map during the selected period.

### Source Layer

02 Normalized Layer

### Source Tables

- player_match_stats
- matches
- dim_periods

### Destination

**Table:** `player_map_period_stats`

**Column:** `damage`

### Calculation Logic

```sql
SUM(damage)
```

Group by player and map.

### Release

Release 1

### Acceptance Criteria

The calculated value equals the total damage dealt on each map during the selected period.

---

## MAP-006 Attack vs Defense by Map

### Definition

Comparison of player performance on the attacking and defending sides for each map.

### Source Layer

03 Analytics Layer

### Source Tables

- player_side_period_stats
- player_map_period_stats

### Destination

Not stored.

Generated for map-specific analytics.

### Calculation Logic

Compare side-specific metrics (Win Rate, K/D, Damage) for each map.

### Release

Future

### Acceptance Criteria

The generated comparison accurately summarizes player performance by side for every map.

---

## MAP-007 Overtime Frequency

### Definition

The number and percentage of matches reaching overtime for each map.

### Source Layer

02 Normalized Layer

### Source Tables

- matches
- dim_periods

### Destination

Not stored.

Calculated when requested.

### Calculation Logic

Identify matches whose total rounds exceed the regulation match length and group by map.

### Release

Future

### Acceptance Criteria

The calculated frequency equals the number of overtime matches divided by total matches played on each map.

---

## MAP-008 Dodge Rate

### Definition

The percentage of queues dodged before a match begins for each map.

### Source Layer

01 Raw Layer

### Source Tables

API response (Future)

### Destination

Not stored.

### Calculation Logic

Dependent on future API support.

### Release

Future

### Acceptance Criteria

Implemented only if the Valorant API exposes reliable dodge information.






## Related Documentation

- Metric Catalog
- Database Schema
- Architecture
- Season Recap Feature

