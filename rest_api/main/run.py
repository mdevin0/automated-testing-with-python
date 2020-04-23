from rest_api.main.app import app
from rest_api.main.db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
