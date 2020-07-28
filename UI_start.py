from flask import Flask, render_template, request


@app.route("/home", methods=["POST"])
def home():
    J = request.form.get("Job")
    return render_template("home.html")
