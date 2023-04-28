import os
from flask import Flask, render_template, send_file, url_for


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/download")
def download():
    file = basedir + url_for("static", filename="assets/resume.docx")
    filenme = os.path.basename(file)
    return send_file(
        file,
        mimetype="application/msword",
        download_name=filenme,
        as_attachment=True,
    )


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
