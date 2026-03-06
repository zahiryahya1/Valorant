-- Core tables indexes
CREATE INDEX idx_matches_start
ON matches(game_start);

CREATE INDEX idx_kill_match
ON kill_events(match_id);

CREATE INDEX idx_kill_killer
ON kill_events(killer_puuid);

CREATE INDEX idx_damage_match
ON damage_events(match_id);

CREATE INDEX idx_match_players_agent
ON match_players(agent);



-- Aggregate tables indexes
CREATE INDEX idx_period_stats_player
ON player_period_stats(player_puuid);

CREATE INDEX idx_agent_period
ON player_agent_period_stats(player_puuid);

CREATE INDEX idx_map_period
ON player_map_period_stats(player_puuid);

CREATE INDEX idx_weapon_period
ON player_weapon_period_stats(player_puuid);