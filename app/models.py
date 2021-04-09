from app import db
from datetime import datetime


class Divvy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, nullable=True)
    starttime = db.Column(db.DateTime(), nullable=True)
    stoptime = db.Column(db.DateTime(), nullable=True)
    bikeid = db.Column(db.Integer, nullable=True)
    from_station_id = db.Column(db.Integer, nullable=True)
    from_station_name = db.Column(db.String(50), nullable=True)
    to_station_id = db.Column(db.Integer, nullable=True)
    to_station_name = db.Column(db.String(50), nullable=True)
    usertype = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    birthday = db.Column(db.String(10), nullable=True)
    trip_duration = db.Column(db.Integer, nullable=True)

    def __init__(self, trip_id, starttime, stoptime, bikeid, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthday, trip_duration):
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration
