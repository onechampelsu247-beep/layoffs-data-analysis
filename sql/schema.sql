-- Định nghĩa cấu trúc bảng cho cơ sở dữ liệu layoffs
CREATE TABLE IF NOT EXISTS layoffs_events (
    event_id TEXT,
    company TEXT,
    location TEXT,
    industry TEXT,
    total_laid_off REAL,
    percentage_laid_off REAL,
    date TEXT,
    stage TEXT,
    country TEXT,
    funds_raised_millions REAL
);