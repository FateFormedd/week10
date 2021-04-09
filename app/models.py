import os
from app import db
from datetime import DateTime


class Divvy(self):
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer)
    starttime = db.Column(db.DateTime())
    stoptime = db.Column(db.DateTime())
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String(50))
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String(50))
    usertype = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    birthday = db.Column(db.DateTime)
    trip_duration = db.Column(db.Integer)

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
