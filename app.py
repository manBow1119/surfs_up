#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



# #set up the engine
engine = create_engine("sqlite:///hawaii.sqlite")

# #reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

#create variables for the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# #create a session link to database
session = Session(engine)

# # #Create new instance of flask app 'name' is a magic method
app = Flask(__name__)
@app.route("/")
#welcome route
def welcome():
    return(
    """
    Welcome to the Climate Analysis API!\n
    Available Routes:\n
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/temp/start/end\n
    """)

#precipitation routes
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Get precip and date date from last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
      #Get precip for each day 
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#stations route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#temps route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Get temp results for primary station
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)

#multiple routes for start and end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#get temp stats min max avg, start/end route
def stats(start=None, end=None):
    #create variable to store the stats
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    #if-not to determine start and end dates
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    #Calc stats based on start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)