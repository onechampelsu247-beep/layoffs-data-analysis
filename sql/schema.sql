PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS layoff_event;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS industry;
DROP TABLE IF EXISTS country;

CREATE TABLE country (
    country_id   INTEGER PRIMARY KEY,
    country_name TEXT NOT NULL UNIQUE
);

CREATE TABLE industry (
    industry_id   INTEGER PRIMARY KEY,
    industry_name TEXT NOT NULL UNIQUE
);

CREATE TABLE company (
    company_id   INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    country_id   INTEGER NOT NULL REFERENCES country(country_id),
    UNIQUE (company_name, country_id)
);

CREATE TABLE layoff_event (
    event_id         TEXT PRIMARY KEY,
    company_id       INTEGER NOT NULL REFERENCES company(company_id),
    industry_id      INTEGER REFERENCES industry(industry_id),
    hq_city          TEXT,
    funding_stage    TEXT,
    layoff_date      TEXT NOT NULL,
    laid_off_count   INTEGER,
    layoff_size_band TEXT,
    is_mass_layoff   INTEGER CHECK (is_mass_layoff IN (0, 1)),
    is_mega_layoff   INTEGER CHECK (is_mega_layoff IN (0, 1)),
    source_url       TEXT,
    data_source      TEXT NOT NULL CHECK (data_source IN ('kaggle', 'news'))
);