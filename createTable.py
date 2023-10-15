from app import app, db

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print("An error occurred while creating database tables:")
        print(e)