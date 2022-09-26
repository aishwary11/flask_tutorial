from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    print(datetime.utcnow().date())
    return "Hello!! World"


if __name__ == "__main__":
    app.run(debug=True)
