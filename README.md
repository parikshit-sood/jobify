# Jobify

Jobify is a modern job aggregator that pulls listings from multiple job boards, removes duplicates using fuzzy matching, and provides  clean, filterable web interface for tracking opportunities.

Designed to help job seekers focus on applying - not copy/pasting duplicate listings.

## Live Demo

[jobify.vercel.app](https://jobify.vercel.app) (Coming soon)

## Architecture Overview

Jobify follows a modular full-stack architecture widely used by startups.

### Tech Stack

| Layer        | Tech Used                          | Purpose                         |
|--------------|-------------------------------------|----------------------------------|
| Frontend     | [Next.js](https://nextjs.org/), Tailwind CSS | Modern React-based UI          |
| Backend API  | [Express](https://expressjs.com/) or [FastAPI](https://fastapi.tiangolo.com/) | RESTful job API                |
| Data Layer   | [PostgreSQL](https://www.postgresql.org/) via Supabase | Cloud-native SQL database      |
| Scraping     | Python scripts (`requests`, `RapidFuzz`) | Scheduled job ingestion        |
| Deployment   | Vercel (frontend), Render/Fly.io (backend), Supabase (DB) | Easy hosting across layers     |

## Features
- Aggregates jobs from RemoteOK, YC Jobs, and more
- Removes near-duplicate listings using fuzzy match algorithms
- Tags jobs by title, company, tech stack, location
- Interactive web interface to search, filter, and save jobs
- Bookmarks persist in PostgreSQL
- Email alerts, Google OAuth, and resume tracking

## Project Structure

```
jobify/
|-- apps/
|---- frontend/
|---- backend/
|-- services/
|---- scraper/
|-- db/
|---- schema.sql
|-- docker-compose.yml
|-- .env.local
|-- README.md
```

## License

This project is licensed under the Apache License 2.0 - see [LICENSE](LICENSE) for details.
