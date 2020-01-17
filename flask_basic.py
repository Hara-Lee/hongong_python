from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

# Powershell에서 다음과 같은 방법으로 실행
# set FLASK_APP=파일이름.py
# flask run