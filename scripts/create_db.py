import sqlite3
import pandas as pd

# Kết nối đến database
con = sqlite3.connect("layoffs.db")
cursor = con.cursor()

# 1. Đọc và thực thi file schema.sql để tạo cấu trúc bảng
with open("sql/schema.sql", "r", encoding="utf-8") as f:
    schema_script = f.read()

cursor.executescript(schema_script)
con.commit()

# 2. Nạp dữ liệu từ file CSV vào database bằng pandas
df_events = pd.read_csv("data/raw/layoffs_events.csv")
df_events.to_sql("layoffs_events", con, if_exists="replace", index=False)

con.close()
print("Đã tạo database và nạp dữ liệu thành công!")