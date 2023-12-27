from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from config import Config
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient(Config.MONGO_URI)
workoutDB = client.VirtualWorkout
workoutUsers = workoutDB.usersAuth
def loginCheck(username, userpwd):
    from app import bcrypt #moved inside to avoid circular import errors
    queryResult = workoutUsers.find_one({'username': username})
    if queryResult is not None:
        if (bcrypt.check_password_hash(queryResult['password'], userpwd)):
            return True
    print("login attempt failed!")
    return False    
    

    
def userSignUp(username, userpwd, pwdConfirm):
    if str(userpwd) != str(pwdConfirm):
        return False
    from app import bcrypt
    queryResult = workoutUsers.find_one({'username': username})
    if  queryResult is None: #ensure username not already taken 
        pw_hash = bcrypt.generate_password_hash(userpwd)
        workoutUsers.insert_one({'username':username,'password':pw_hash})
        return True
    return False
