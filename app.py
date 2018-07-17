from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres1234@localhost/height_collector'
# create SQLAlchemy object for flask app
db = SQLAlchemy(app)


# go to Python Console,
# from app import db to create table without running flask
class Data(db.Model):
    # create the table in DB, define all attributes
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]

        # finding if email already existed in db
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            # calculate mean of height by applying func.avg, and extract scalar value
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 2)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            print(average_height)
            return render_template("success.html")
    return render_template('index.html', text="That email has already existed")


@app.route("/upload", methods=['POST'])
def upload():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        # save uploaded file as new file
        file.save(secure_filename("uploaded_"+file.filename))  # new file name will be "uploaded_filename"
        # open the new file and append some contents
        with open("uploaded_"+file.filename, "a") as f:
            f.write("This is an appended content")
        print(file)
        # after uploading, upload.html is rendered together with download button of download.html
        return render_template("upload.html", btn="download.html")


@app.route("/download")
def download():
    # send new file to users, and allow user to download it instead of opening it on browser
    return send_file("uploaded_"+file.filename, attachment_filename="your_new_file.csv", as_attachment=True)


# if the script is being executed, not being imported
if __name__ == "__main__":
    app.debug = True
    app.run(port=4999)


