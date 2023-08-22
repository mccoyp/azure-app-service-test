import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
   print("Request for index page received")
   return "hiiii :3"


if __name__ == "__main__":
   app.run()
