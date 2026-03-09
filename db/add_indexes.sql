-- ==========================================
-- CORE TABLE INDEXES
-- ==========================================

CREATE INDEX idx_matches_start_time
ON matches(game_start);

CREATE INDEX idx_matches_act
ON matches(act_id);

CREATE INDEX idx_match_players_player
ON match_players(player_puuid);

CREATE INDEX idx_match_players_agent
ON match_players(agent);

CREATE INDEX idx_kill_events_match
ON kill_events(match_id);

CREATE INDEX idx_kill_events_killer
ON kill_events(killer_puuid);

CREATE INDEX idx_kill_events_victim
ON kill_events(victim_puuid);

CREATE INDEX idx_damage_events_match
ON damage_events(match_id);



-- ==========================================
-- AGGREGATE TABLE INDEXES
-- ==========================================

CREATE INDEX idx_player_period_player
ON player_period_stats(player_puuid);

CREATE INDEX idx_player_period_lookup
ON player_period_stats(period_type, period_id);



CREATE INDEX idx_agent_period_player
ON player_agent_period_stats(player_puuid);

CREATE INDEX idx_map_period_player
ON player_map_period_stats(player_puuid);

CREATE INDEX idx_weapon_period_player
ON player_weapon_period_stats(player_puuid);


CREATE INDEX idx_highlight_period_player
ON player_highlight_period_stats(player_puuid);