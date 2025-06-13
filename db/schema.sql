-- jobs table (normalized job listings)
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- id (primary key)
    title TEXT NOT NULL, -- title
    company TEXT, -- company name
    location TEXT, -- location
    description TEXT, -- description
    url TEXT UNIQUE, -- url
    source TEXT, -- source
    fetched_at TEXT, -- fetch_at time
    is_duplicate BOOLEAN DEFAULT 0 -- is duplicate?
)