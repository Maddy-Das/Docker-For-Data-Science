from python:3.7-alpine
workdir /code
env FlASK_APP=app.py
env FLASK_RUN_HOST=0.0.0.0
copy . .
run pip install -r requirements.txt
expose 5000
cmd ["flask", "run"]