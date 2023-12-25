from flask import Blueprint, render_template, request, url_for



import workouts.jumpingJacks2 as jumpingJacks2
import workouts.pushup2 as pushUp
import workouts.tennis as tennisF
import workouts.tennisBH as tennisB
#from workouts.jumpingJacks2 import finalScore

views = Blueprint(__name__, "views")

# @views.route("/")
# def home():
#     return render_template("index.html", name="User")



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

# @views.route("/pushups")
# def pushups():
#     return "none for now"

@views.route("/pushUps")
def pushUpsPage():
    return render_template("pushUps.html")

@views.route("/runPushUps")
def runPushUps():
    return pushUp.run_push_ups_counter()


@views.route("/terminatePushUps", methods=['GET'])
def terminatePushUps():
    finalScore, caloriesBurned = pushUp.terminate_PU()
    print("Final score: ", finalScore)
    return render_template("pushUps.html", userScore=finalScore, caloriesCount=caloriesBurned)


@views.route("/restartPushUps")
def restartPushUps():
    pushUp.restart_PU()
    return render_template("pushUps.html")


@views.route("/TennisForehand")
def tennisForeHand():
    return render_template("tennisForehand.html")

@views.route("/runTF")
def runTF():
    return tennisF.run_tennisF_counter()


@views.route("/terminateTF", methods=['GET'])
def terminateTF():
    finalScore, caloriesBurned = tennisF.terminate_TF()
    print("Final score: ", finalScore)
    return render_template("tennisForehand.html", userScore=finalScore, caloriesCount=caloriesBurned)


@views.route("/restartTF")
def restartPF():
    tennisF.restart_TF()
    return render_template("tennisForehand.html")

@views.route("/TennisBH")
def tennisBH():
    return render_template("tennisBH.html")

@views.route("/runTB")
def runTB():
    return tennisB.run_tennisBH_counter()


@views.route("/terminateTB", methods=['GET'])
def terminateBH():
    finalScore, caloriesBurned = tennisB.terminate_TB()
    print("Final score: ", finalScore)
    return render_template("tennisBH.html", userScore=finalScore, caloriesCount=caloriesBurned)


@views.route("/restartTB")
def restartTB():
    tennisB.restart_TB()
    return render_template("tennisBH.html")

