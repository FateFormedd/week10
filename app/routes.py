from app import app
from flask import request, render_template
from app.models import Divvy



@app.route('/')
def helloworld():
    return render_template('index.html')

@app.route('/average')
def average():
    data = request.args.to_dict()
    starttime = data['start']
    stoptime = data['end']
    averagetime = 0
    totaltime = 0
    divvy = Divvy.query.filter(Divvy.starttime.between(starttime, stoptime)).all()
    length = len(divvy)
    for i in range(length):
        totaltime = totaltime + divvy[i].trip_duration
    averagetime = totaltime / length
    return {'averagetime': averagetime}