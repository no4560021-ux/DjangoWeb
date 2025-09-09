# DjangoWeb

一個教學用的 Django 專案。

## 環境
- Python 3.10+
- Django（版本見 `requirements.txt`）

## 快速啟動
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows（macOS/Linux: source .venv/bin/activate）
python -m pip install -r requirements.txt
python manage.py migrate
# 若有資料備份：
# python manage.py loaddata data.json
python manage.py runserver
