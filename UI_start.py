from flask import Flask, render_template, request


@app.route("/home", methods=["POST"])
def home():
    Jobs = request.form.get("Jobs")
    Experience = request.form.get("Experiece")
    Education = request.form.get("Education")
    return render_template("home.html")
