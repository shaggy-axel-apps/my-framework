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
# run simple wsgi
gunicorn src.simple_wsgi:application

# run wsgi framework
cd src
gunicorn manage:application
```

see urlpatterns in `src.blog_project.urls`
