import os
import requests

# Đường dẫn thư mục lưu file (data/raw)
RAW_DIR = os.path.join("data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

# Link API trỏ tới thư mục chứa dữ liệu của repo layoffs-tracker
# Lưu ý: Nếu file dữ liệu nằm trong thư mục con (ví dụ 'data'), bạn thêm '/data' vào cuối link nhé
API_URL = "https://api.github.com/repos/evgeniimatveev/layoffs-tracker/contents"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def crawl_layoffs_data():
    resp = requests.get(API_URL, headers=HEADERS, timeout=20)
    if resp.status_code != 200:
        print(f"Lỗi truy cập API: {resp.status_code}")
        return

    items = resp.json()
    for item in items:
        # Nếu là file (ưu tiên lấy file .csv, .json, .xlsx), tiến hành tải về data/raw/
        if item["type"] == "file" and item.get("download_url"):
            filename = item["name"]
            download_url = item["download_url"]
            save_path = os.path.join(RAW_DIR, filename)

            print(f"Đang tải file: {filename} ...")
            file_resp = requests.get(download_url, headers=HEADERS, timeout=20)
            if file_resp.status_code == 200:
                with open(save_path, "wb") as f:
                    f.write(file_resp.content)
                print(f" -> Đã lưu thành công: {save_path}")
            else:
                print(f" -> Lỗi {file_resp.status_code} khi tải {filename}")

if __name__ == "__main__":
    crawl_layoffs_data()