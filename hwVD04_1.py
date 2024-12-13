from flask import Flask
app = Flask(__name__)
from datetime import datetime


@app.route("/")
def hello_world():
    now = datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    dt = "Дата,время - "+formatted_date_time
    return dt
@app.route("/new/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()