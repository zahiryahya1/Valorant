# API Documentation

## Overview

Valorant Season Recap retrieves player match history using the HenrikDev Valorant API.

The API provides access to player profiles, competitive history, match details, and additional metadata.

Repository

- https://github.com/Henrik-3/unofficial-valorant-api

Documentation

- https://docs.henrikdev.xyz/

---

# Current Usage

The project currently uses the API for:

- Player lookup
- Match history
- Match details
- Episode information
- Act information

---

# Authentication

Authentication is performed using a personal API key.

The API key should never be committed to source control.

Future implementations should load credentials using environment variables.

---

# Rate Limits

Current API limit

- 30 requests per minute

Current status

⚠️ Rate limiting is not yet fully implemented.

Planned improvements

- Automatic throttling
- Retry logic
- Exponential backoff
- Request queue

---

# Error Handling

Future API handling should account for:

- Invalid Riot IDs
- Missing matches
- Private accounts
- Rate limiting
- API outages
- Unexpected response formats

---

# External Dependency

This project depends on an unofficial API.

Potential risks include:

- Endpoint changes
- Rate limit changes
- API downtime
- Version compatibility

The application should be designed to gracefully handle API failures.

---

# Future Improvements

Potential future enhancements include:

- Local response caching
- Incremental synchronization
- Background refresh jobs
- Scheduled data updates