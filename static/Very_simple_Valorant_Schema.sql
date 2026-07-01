-- ==========================================================
-- TEAMS
-- ==========================================================

CREATE TABLE teams (

    team_id SERIAL PRIMARY KEY,

    team_name VARCHAR(50) NOT NULL UNIQUE,

    strength SMALLINT DEFAULT 50,

    region VARCHAR(20),

    budget BIGINT DEFAULT 0,

    reputation SMALLINT DEFAULT 50,

    academy_rating SMALLINT DEFAULT 50,

    facilities_rating SMALLINT DEFAULT 50,

    fanbase INTEGER DEFAULT 0

);

-- ==========================================================
-- PLAYERS
-- ==========================================================

CREATE TABLE players (

    player_id SERIAL PRIMARY KEY,

    ign VARCHAR(32) UNIQUE NOT NULL,

    first_name VARCHAR(50),

    last_name VARCHAR(50),

    nationality VARCHAR(50),

    birth_date DATE,

    age INTEGER,

    preferred_role VARCHAR(20),

    secondary_role VARCHAR(20),

    handedness VARCHAR(10),

    current_team_id INTEGER,

    current_ability SMALLINT,

    potential_ability SMALLINT,

    market_value BIGINT,

    salary INTEGER,

    contract_end DATE,

    popularity SMALLINT DEFAULT 50,

    fatigue SMALLINT DEFAULT 0,

    morale SMALLINT DEFAULT 50,

    form SMALLINT DEFAULT 50,

    injury_days_remaining INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (current_team_id)
        REFERENCES teams(team_id)

);

-- ==========================================================
-- MATCHES
-- ==========================================================

CREATE TABLE matches (

    match_id SERIAL PRIMARY KEY,

    tournament_id INTEGER,

    team_a INTEGER,

    team_b INTEGER,

    best_of SMALLINT,

    winner INTEGER,

    played_date DATE,


    FOREIGN KEY(team_a)
        REFERENCES teams(team_id),

    FOREIGN KEY(team_b)
        REFERENCES teams(team_id),

    FOREIGN KEY(winner)
        REFERENCES teams(team_id)

);