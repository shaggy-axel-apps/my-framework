# Simple WSGI-framework

# Install
```bash
git clone ... && cd ...

# setup environment
python3.9 -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

# Usage
```bash
# run server
gunicorn src.simple_wsgi:application
```
