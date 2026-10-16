import pandas as pd
import os

# 1. Đọc file thô từ thư mục data/raw
raw_path = "data/raw/layoffs_events.csv"
clean_dir = "data/clean"
clean_path = os.path.join(clean_dir, "layoffs_cleaned.csv")

# Đảm bảo thư mục clean tồn tại
os.makedirs(clean_dir, exist_ok=True)

try:
    df = pd.read_csv(raw_path)
    print(f"Số dòng ban đầu: {len(df)}")

    # Xóa dòng trùng lặp
    df = df.drop_duplicates()

    # Tách hq_city thành city và region nếu có
    if "hq_city" in df.columns:
        df[['hq_city_clean', 'hq_region']] = df['hq_city'].str.split(',', expand=True, n=1)
        df['hq_city_clean'] = df['hq_city_clean'].str.strip()
        df['hq_region'] = df['hq_region'].str.strip()

    # Lưu file đã sạch vào thư mục data/clean/
    df.to_csv(clean_path, index=False)
    print(f"Đã làm sạch và lưu file thành công tại: {clean_path}")
    print(f"Số dòng sau khi làm sạch: {len(df)}")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")