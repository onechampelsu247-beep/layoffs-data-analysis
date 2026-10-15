import pandas as pd

df = pd.read_csv("data/raw/layoffs_events.csv")
g = df.groupby("company")

for c in ["industry", "country", "hq_city", "funding_stage"]:
    print(c, "- so cong ty co hon 1 gia tri:", (g[c].nunique() > 1).sum())

print()
print(df[df["company"].str.endswith(" copy")][["event_id", "company", "layoff_date", "laid_off_count"]])