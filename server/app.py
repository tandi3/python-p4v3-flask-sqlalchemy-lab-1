# server/app.py
#!/usr/bin/env python3

# server/app.py
#!/usr/bin/env python3

# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# Task #3: Get earthquake by ID
@app.route('/earthquakes/<int:id>')
def earthquake_by_id(id):
    quake = Earthquake.query.get(id)
    if quake:
        response = {
            "id": quake.id,
            "location": quake.location,
            "magnitude": quake.magnitude,
            "year": quake.year,
        }
        return make_response(response, 200)
    else:
        return make_response({"message": f"Earthquake {id} not found."}, 404)


# Task #4: Get earthquakes by minimum magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    response = {
        "count": len(quakes),
        "quakes": [
            {
                "id": quake.id,
                "location": quake.location,
                "magnitude": quake.magnitude,
                "year": quake.year,
            }
            for quake in quakes
        ],
    }

    return make_response(response, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
