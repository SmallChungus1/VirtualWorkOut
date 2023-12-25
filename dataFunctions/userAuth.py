from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from app import mongoAtlas
def loginCheck(username, userpwd):
    print ("Username:", username)
    print("user password: ", userpwd)
    virtualWorkoutDB = mongoAtlas.db.userAuths
    return True
#def userSignUp():
