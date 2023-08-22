from flask import Flask, request, jsonify
from flask_restful import Api
from models import db, Event 
from resources import EventResource
from datetime import datetime 
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
migrate = Migrate(app, db)
db.init_app(app)

@app.route('/events', methods=['GET'])
def list_events():
    events = Event.query.all()
    events_data = [{"id": event.id, "title": event.title, "date": event.date, "time": event.time.strftime('%H:%M'),
                     "location": event.location, "description": event.description} for event in events]

    return jsonify(events_data), 200


@app.route('/add_event', methods=['POST'])
def add_event():
    data = request.get_json()
    title = data.get('title')
    
    date = datetime.strptime(data.get('date'), '%Y-%m-%d')
    time = datetime.strptime(data.get('time'), '%H:%M').time()
    
    location = data.get('location')
    description = data.get('description')

    event = Event(title=title,
                  date=date,
                  time=time,
                  location=location,
                  description=description)
    db.session.add(event)
    db.session.commit()
    
    return jsonify({"message": "Event added successfully"}), 201
    
@app.route('/edit_event/<int:event_id>', methods=['PUT'])
def edit_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        return jsonify({"message": "Event not found"}), 404
    
    data = request.get_json()
    event.title = data.get('title')
    
    event.date = datetime.strptime(data.get('date'), '%Y-%m-%d')
    event.time = datetime.strptime(data.get('time'), '%H:%M').time()
    
    event.location = data.get('location')
    event.description = data.get('description')
    
    db.session.commit()
    
    return jsonify({"message": "Event updated successfully"}), 200

@app.route('/delete_event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event is None:
        return jsonify({"message": "Event not found"}), 404
    
    db.session.delete(event)
    db.session.commit()
    
    return jsonify({"message": "Event deleted successfully"}), 204

if __name__ == '__main__':
    app.run()
