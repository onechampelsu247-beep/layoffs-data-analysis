# Phân tích dữ liệu sa thải nhân sự trong ngành công nghệ toàn cầu

Dự án RBL môn DBI202 (học kỳ Sum 2026), nhóm [2].

## Mục tiêu
Xây dựng một cơ sở dữ liệu SQLite từ dữ liệu sa thải công nghệ (2020 đến 07/2025), làm sạch dữ liệu và phân tích xu hướng theo thời gian, ngành và quốc gia.
Câu hỏi nghiên cứu: 
RQ1: Số lượng và tỷ lệ sa thải trong ngành công nghệ thay đổi như thế nào qua các năm 2022–2026?
RQ2: Ngành công nghệ nào và quốc gia nào chịu ảnh hưởng nặng nề nhất?
RQ3 :Mức độ ảnh hưởng của sa thải công nghệ khác nhau như thế nào giữa các quốc gia và các ngành?

## Nguồn dữ liệu
- Kaggle: Global Tech Layoffs, Analysis Dataset (tác giả blixture), dữ liệu gốc từ Layoffs.fyi. Truy cập ngày [ngày/tháng/năm].
- Nguồn bổ sung (đang thực hiện): tin tức báo chí về sa thải công nghệ.

## Cấu trúc thư mục
```
data/raw/        Dữ liệu thô (CSV tải từ Kaggle)
data/clean/      Dữ liệu đã làm sạch
scripts/         Các script Python
sql/schema.sql   Cấu trúc CSDL (4 bảng)
docs/            Sơ đồ quy trình, ERD, hình minh họa
requirements.txt Danh sách thư viện
```

## Thiết kế CSDL
Gồm 4 bảng: `country`, `industry`, `company`, `layoff_event`. Một quốc gia có nhiều công ty, một công ty có nhiều sự kiện sa thải. Chi tiết xem `sql/schema.sql`.

## Cách chạy
Yêu cầu: Python 3.13.

```
py -3.13 -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\load_db.py
```

Kết quả mong đợi: 2673 dòng CSV gốc nạp vào CSDL `data/layoffs.db` (country 54, industry 30, company 1945, layoff_event 2673). File `.db` không đưa lên GitHub, được tạo lại bằng lệnh trên.

## Các script
- `explore.py`: xem nhanh dữ liệu thô
- `check_company.py`: kiểm tra chất lượng dữ liệu
- `load_db.py`: làm sạch và nạp dữ liệu vào SQLite
- `crawl_test.py`: thử thu thập dữ liệu từ báo chí

## Sử dụng AI
Nhóm có dùng công cụ AI hỗ trợ viết code và khắc phục lỗi. Chi tiết xem trong báo cáo.