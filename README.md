# Valorant Season Recap

A Spotify Wrapped-inspired analytics experience for Valorant players.

Valorant Season Recap transforms raw player match history into personalized seasonal insights, statistics, and highlights.

The project is designed to provide gamers with a fun way to reflect on their performance while serving as a production-style data engineering portfolio project.

---

## Project Goals

This project has two primary goals:

### 1. Build a User-Facing Product

Create an engaging recap experience where players can:

- View their seasonal performance summary
- Discover gameplay trends
- Explore agent, map, and weapon performance
- See personalized highlights from their matches

### 2. Build a Production-Quality Data Engineering System

Develop a scalable data pipeline demonstrating:

- API data ingestion
- ETL pipeline design
- Database modeling
- Analytics engineering
- Data transformation
- Software documentation
- Production development practices

---

# Features (TBD)

## Current

- Valorant API integration
- Player match data extraction
- Match parsing and normalization
- PostgreSQL data storage
- Core match and player analytics schema

## Planned

- Seasonal recap generation
- Agent performance analysis
- Map performance insights
- Highlight metrics
- Interactive web interface
- Public deployment

---

# Architecture Overview

The project follows a data pipeline architecture: 

Valorant API --> Data Extraction --> Transformation/Normalization --> Database --> Analytics Aggregations --> Season Recap Application


---

# Technology Stack

## Backend

- Python
- PostgreSQL

## Data Engineering

- ETL pipeline architecture
- Data normalization
- SQL analytics modeling

## APIs

- Unofficial Valorant API[https://github.com/Henrik-3/unofficial-valorant-api]
- HenrikDev Valorant API[https://docs.henrikdev.xyz/valorant/changes/v4.6.0]
    - has a rate limit of 30 calls per second
- API and Schema[https://app.swaggerhub.com/apis-docs/Henrik-3/HenrikDev-API/4.2.1]
- API Wrapper[https://raimannma.github.io/ValorantAPI/_source_files/valo_api.endpoints.html]

## Development

- Git/GitHub
- VS Code

---


Documentation and architecture details can be found in `/docs`.

---

# Getting Started

Documentation for setup and running the pipeline: docs/04-development/local-setup.md (insert link)
 
