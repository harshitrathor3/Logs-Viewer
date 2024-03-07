# app/models.py
from app import db
from app import mongo
# import logging

# logging.basicConfig(level=logging.DEBUG)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(20))
    message = db.Column(db.Text)
    resourceId = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
    traceId = db.Column(db.String(50))
    spanId = db.Column(db.String(50))
    commit = db.Column(db.String(40))
    parentResourceId = db.Column(db.String(50))


class LogMongo:
    @staticmethod
    def insert_log(log_data):
        mongo.db.logs.insert_one(log_data)

    @staticmethod
    def search_logs(search_params):
        try:
            query = {k: v for k, v in search_params.items() if v is not None and v != ''}
            result = list(mongo.db.logs.find(query))
            return result
        except Exception as e:
            print(f"Error searching logs in MongoDB: {e}")