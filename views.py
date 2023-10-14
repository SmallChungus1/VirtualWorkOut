from flask import Blueprint, render_template, request

import jumpingJacks2

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="User")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)

@views.route("/jumpingJacksPage")
def jumpingJacks():
    return render_template("jumpingJacks.html")

@views.route("/runJumpingJacks")
def runJumpingJacks():
    return jumpingJacks2.run_jumping_jacks_counter()

# @views.route("/video_feed")
# def jumpingJacksRun():
#     return jumpingJacks2.run_jumping_jacks_counter()

@views.route("/terminatejumpingJacks")
def terminatejumpingJacks():
    jumpingJacks2.terminate_JJ()
    return render_template("profile.html")

@views.route("/restartjumpingJacks")
def restartjumpingJacks():
    jumpingJacks2.restart_JJ()
    return render_template("jumpingJacks.html")

@views.route("/pushups")
def pushups():
    return "none for now"
