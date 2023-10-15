from flask import Blueprint, render_template, request, url_for



import workouts.jumpingJacks2 as jumpingJacks2
#from workouts.jumpingJacks2 import finalScore

views = Blueprint(__name__, "views")

# @views.route("/")
# def home():
#     return render_template("index.html", name="User")


@views.route('/test')
def test():
    return"hello"

@views.route("/register")
def register():
    return render_template("reg.html", name="New User")

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


@views.route("/terminatejumpingJacks", methods=['GET'])
def terminatejumpingJacks():
    finalScore, caloriesBurned = jumpingJacks2.terminate_JJ()
    print("Final score: ", finalScore)
    return render_template("jumpingJacks.html", userScore=finalScore, caloriesCount=caloriesBurned)


@views.route("/restartjumpingJacks")
def restartjumpingJacks():
    jumpingJacks2.restart_JJ()
    return render_template("jumpingJacks.html")

@views.route("/pushups")
def pushups():
    return "none for now"
