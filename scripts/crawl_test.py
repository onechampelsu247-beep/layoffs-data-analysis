import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
import truststore.inject_into_ssl()

url = "https://vneconomy.vn/techconnect/3-thang-dau-nam-2026-hon-45000-lao-dong-cong-nghe-tren-toan-cau-bi-sa-thai.htm"
headers = {"User-Agent": "Mozilla/5.0 (RBL DBI202 student project)"}

# 1. Kiem tra robots.txt (tai bang requests de tranh loi SSL cua urllib)
p = urlparse(url)
robots_url = f"{p.scheme}://{p.netloc}/robots.txt"
rr = requests.get(robots_url, headers=headers, timeout=20)
print("Ma robots.txt:", rr.status_code)
if rr.status_code == 200:
    rp = RobotFileParser()
    rp.parse(rr.text.splitlines())
    print("robots.txt cho phep:", rp.can_fetch("*", url))
else:
    print("Khong doc duoc robots.txt, hay mo tay tren trinh duyet de kiem tra")

# 2. Tai bai bao
r = requests.get(url, headers=headers, timeout=20)
print("Ma trang:", r.status_code)

# 3. Lay thong tin
soup = BeautifulSoup(r.text, "lxml")
tieu_de = soup.find("meta", property="og:title")
ngay = soup.find("meta", property="article:published_time")
print("Tieu de:", tieu_de["content"] if tieu_de else soup.title.get_text(strip=True))
print("Ngay dang:", ngay["content"] if ngay else None)
print("So doan van:", len(soup.find_all("p")))