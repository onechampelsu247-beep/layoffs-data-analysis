import re
import sqlite3
import pandas as pd

# 1. Doc du lieu tho
df = pd.read_csv("data/raw/layoffs_events.csv")
so_dong_goc = len(df)

# 2. Lam sach
df["company"] = df["company"].str.strip().str.replace(r"\s+copy$", "", regex=True, flags=re.I)
df["country"] = df["country"].str.strip()
df["industry"] = df["industry"].str.strip()
df["hq_city"] = df["hq_city"].str.replace(r",\s*Non-U\.S\.$", "", regex=True).str.strip()
df["layoff_date"] = pd.to_datetime(df["layoff_date"]).dt.strftime("%Y-%m-%d")
df["is_mass_layoff"] = df["is_mass_layoff"].astype(int)
df["is_mega_layoff"] = df["is_mega_layoff"].astype(int)
df["data_source"] = "kaggle"
df = df.astype(object).where(df.notna(), None)

# 3. Tao CSDL tu schema.sql
con = sqlite3.connect("data/layoffs.db")
with open("sql/schema.sql", encoding="utf-8") as f:
    con.executescript(f.read())

# 4. Nap cac bang danh muc
for name in sorted(df["country"].dropna().unique()):
    con.execute("INSERT INTO country (country_name) VALUES (?)", (name,))
for name in sorted(df["industry"].dropna().unique()):
    con.execute("INSERT INTO industry (industry_name) VALUES (?)", (name,))

country_id = dict(con.execute("SELECT country_name, country_id FROM country"))
industry_id = dict(con.execute("SELECT industry_name, industry_id FROM industry"))

# 5. Nap bang company (moi cap ten + quoc gia la mot cong ty)
for ten, qg in df[["company", "country"]].drop_duplicates().itertuples(index=False):
    con.execute(
        "INSERT INTO company (company_name, country_id) VALUES (?, ?)",
        (ten, country_id[qg]),
    )
company_id = {
    (ten, cid): i
    for i, ten, cid in con.execute("SELECT company_id, company_name, country_id FROM company")
}

# 6. Nap bang layoff_event
for r in df.itertuples(index=False):
    con.execute(
        """INSERT INTO layoff_event
           (event_id, company_id, industry_id, hq_city, funding_stage, layoff_date,
            laid_off_count, layoff_size_band, is_mass_layoff, is_mega_layoff,
            source_url, data_source)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            r.event_id,
            company_id[(r.company, country_id[r.country])],
            industry_id.get(r.industry),
            r.hq_city,
            r.funding_stage,
            r.layoff_date,
            None if r.laid_off_count is None else int(r.laid_off_count),
            r.layoff_size_band,
            r.is_mass_layoff,
            r.is_mega_layoff,
            r.source_url,
            r.data_source,
        ),
    )
con.commit()

# 7. Kiem tra
print("So dong CSV goc:", so_dong_goc)
for bang in ["country", "industry", "company", "layoff_event"]:
    n = con.execute(f"SELECT COUNT(*) FROM {bang}").fetchone()[0]
    print(f"Bang {bang}: {n} dong")
con.close()