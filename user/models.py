from flask import Flask, jsonify, request
import uuid
from passlib.hash import pbkdf2_sha256
from app import db 

class User:
    def signup(self):
        user = {
            "_id":uuid.uuid4().hex,
            "username":request.form.get('username'),
            "password":request.form.get('password')
        }

        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        db.users.create(user)
        return jsonify(user), 200