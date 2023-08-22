API Events Schedule(Agenda de Eventos API)

This repository contains a simple Event Management System API built using Flask. It allows users to perform CRUD operations (Create, Read, Update, Delete) on events.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x is installed.
Virtual environment is recommended for isolating dependencies.

Installation

Clone the repository:
git clone https://github.com/Ivo-Aragao/Agenda-de-Eventos-API

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install the required packages:
pip install -r requirements.txt

Create the database and apply migrations:
flask db init
flask db migrate
flask db upgrade

Usage
1.Start the Flask development server:
python app.py

2.The API endpoints are accessible at http://127.0.0.1:5000.

Endpoints
GET /events: Retrieve a list of all events.

POST /add_event: Add a new event. Requires JSON data in the request body with attributes title, date, time, location, and description.

PUT /edit_event/int:event_id: Edit an existing event. Requires JSON data in the request body with attributes to be updated.

DELETE /delete_event/int:event_id: Delete an event.


Example Usage
You can use tools like curl, httpie, or Postman to interact with the API. Here's an example using httpie:

Retrieve a list of events:
http GET http://127.0.0.1:5000/events

Add a new event:
http POST http://127.0.0.1:5000/add_event 
title="New Event" 
date="2023-09-01" 
time="14:00" 
location="Room School" 
description="A new event description."

Edit an existing event:
http PUT http://127.0.0.1:5000/edit_event/1 
title="Updated Event" 
date="2023-09-02" 
time="15:30" 
location="Laboratory School" 
description="Updated event description."

Delete an event:
http DELETE http://127.0.0.1:5000/delete_event/1

Contributors
Ivo Aragão
Igor Ramalho
Geraldo Werbety

