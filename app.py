from flask import Flask
from flask import render_template, request, url_for
import pymongo

from views import views



app = Flask(__name__)

#database:
client = pymongo.MongoClient('localhost',27017)
db = client.users

from user import routes

@app.route("/")
def home():
    return render_template("index.html", name="User")

app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=3000)