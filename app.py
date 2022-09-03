# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello world'

# Adding dependecies
import datetime as dt
import numpy as np
import pandas as pd

# Now let's get the dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database. Add the SQLAlchemy dependencies after the other dependencies you already imported in app.py.

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# The create_engine() function allows us to access and query our SQLite database file. Now let's reflect the database into our classes.
Base = automap_base()

#  Python Flask function to reflect the tables: Base.prepare()
Base.prepare(engine, reflect=True)

# We'll create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database with the following code:
session = Session(engine)

# Set Up Flask
app = Flask(__name__)
import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

# We can define the welcome route using the code below:
app = Flask(__name__)
@app.route("/")

# First, create a function welcome() with a return statement. Add this line to your code:
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# To run file on the command line run: flask run

# To create the route, add the following code. Make sure that it's aligned all the way to the left.
@app.route("/api/v1.0/precipitation")

# Next, we will create the precipitation() function.
# def precipitation():
#     return

# First, we want to add the line of code that calculates the date one year ago from the most recent date in the database. Do this now so that your code looks like the following:
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    return

# Next, write a query to get the date and precipitation for the previous year. Add this query to your existing code.
# def precipitation():
#    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#    precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return

# Finally, we'll create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# To run file on the command line run: flask run

# Begin by defining the route and route name. As a reminder, this code should occur outside of the previous route and have no indentation. Add this route to your code:
@app.route("/api/v1.0/stations")

# With our route defined, we'll create a new function called stations(). Go ahead and add the following code:
# def stations():
#     return

# Now we need to create a query that will allow us to get all of the stations in our database. Let's add that functionality to our code:
# def stations():
#     results = session.query(Station.station).all()
#     return

# Next, we will convert our unraveled results into a list. To convert the results to a list, we will need to use the list function, which is list(), and then convert that array into a list. Then we'll jsonify the list and return it as JSON. Let's add that functionality to our code:
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# To run file on the command line run: flask run

# For this route, the goal is to return the temperature observations for the previous year. As with the previous routes, begin by defining the route with this code:
@app.route("/api/v1.0/tobs")

# Next, create a function called temp_monthly() by adding the following code:
# def temp_monthly():
#     return

# Now, calculate the date one year ago from the last date in the database. (This is the same date as the one we calculated previously.) Your code should look like this:
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     return

# The next step is to query the primary station for all the temperature observations from the previous year. Here's what the code should look like with the query statement added:
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()
#     return

# Finally, as before, unravel the results into a one-dimensional array and convert that array into a list. Then jsonify the list and return our results, like this:
# def temp_monthly():
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.tobs).\
#       filter(Measurement.station == 'USC00519281').\
#       filter(Measurement.date >= prev_year).all()
#     temps = list(np.ravel(results))

# As we did earlier, we want to jsonify our temps list, and then return it. Add the return statement to the end of your code so that the route looks like this:
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# To run file on the command line run: flask run

# Just one more route to create! Our last route will be to report on the minimum, average, and maximum temperatures. However, this route is different from the previous ones in that we will have to provide both a starting and ending date. Add the following code to create the routes:
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats() to put our code in.
# def stats():
#      return

# We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None.
# def stats(start=None, end=None):
#      return

# With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. We'll start by just creating a list called sel, with the following code:
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

# Since we need to determine the starting and ending date, add an if-not statement to our code. This will help us accomplish a few things. We'll need to query our database using the list that we just made. Then, we'll unravel the results into a one-dimensional array and convert them to a list. Finally, we will jsonify our results and return them.
# def stats(start=None, end=None):
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps=temps)

# Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. We'll use the sel list, which is simply the data points we need to collect. Let's create our next query, which will get our statistics data.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# Finally, we need to run our code. To do this, navigate to the "surfs_up" folder in the command line, and then enter the following command to run your code: flask run
























