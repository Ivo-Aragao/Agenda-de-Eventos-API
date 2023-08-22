from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Event, EventSchema 
from datetime import datetime

class EventResource(Resource):
    def get(self, event_id=None):
        if event_id is None:
            events = Event.query.all()
            events_data = [{"id": event.id, "title": event.title, "date": event.date, "time": event.time,
                            "location": event.location, "description": event.description} for event in events]
            return jsonify(events_data), 200
        
        event = Event.query.get(event_id)
        if event:
            event_data = {
                "id": event.id,
                "title": event.title,
                "date": event.date,
                "time": event.time.strftime('%H:%M'),
                "location": event.location,
                "description": event.description
            }
            return jsonify(event_data), 200
        else:
            return {'message': 'Event not found'}, 404
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('date', type=str, required=True)
        parser.add_argument('time', type=str, required=True)
        parser.add_argument('location', type=str)
        parser.add_argument('description', type=str)
        
        args = parser.parse_args()
        title = args['title']
        date = datetime.strptime(args['date'], '%Y-%m-%d')
        time = datetime.strptime(args['time'], '%H:%M').time()
        location = args['location']
        description = args['description']

        event = Event(title=title,
                      date=date,
                      time=time,
                      location=location,
                      description=description)
        db.session.add(event)
        db.session.commit()
        
        event_data = {
            "id": event.id,
            "title": event.title,
            "date": event.date,
            "time": event.time.strftime('%H:%M'),
            "location": event.location,
            "description": event.description
        }
        return jsonify(event_data), 201
    
    def put(self, event_id):
        event = Event.query.get(event_id)
        if event:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('date', type=str)
            parser.add_argument('time', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('description', type=str)
            
            args = parser.parse_args()
            
            if args['title']:
                event.title = args['title']
            if args['date']:
                event.date = datetime.strptime(args['date'], '%Y-%m-%d')
            if args['time']:
                event.time = datetime.strptime(args['time'], '%H:%M').time()
            if args['location']:
                event.location = args['location']
            if args['description']:
                event.description = args['description']
            
            db.session.commit()
            
            event_data = {
                "id": event.id,
                "title": event.title,
                "date": event.date,
                "time": event.time.strftime('%H:%M'),
                "location": event.location,
                "description": event.description
            }
            return jsonify(event_data), 200
        else:
            return {'message': 'Event not found'}, 404

    def delete(self, event_id):
        event = Event.query.get(event_id)
        if event:
            db.session.delete(event)
            db.session.commit()
            return {'message': 'Event deleted'}, 204
        else:
            return {'message': 'Event not found'}, 404
