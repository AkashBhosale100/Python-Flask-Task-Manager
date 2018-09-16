from app import app, db
from flask import jsonify
from flask import json
from flask import url_for
from flask import request
from app.models import Tasks
from os import sys
from flask import abort
from flask_cors import cross_origin
from datetime import datetime,timezone
import dateutil.parser
from calendar import monthrange

from flask import render_template

tasks = []

def make_public_task(task):
    new_task = [
        {
            'uri': url_for('getTask', task_id=task.id, _external=True),
            'title': str(task.title),
            'description': task.description,
            'timestamp': task.timestamp,
            'scheduledDateTime':task.scheduledDateTime,
            'done': task.done,
            'reminder': task.reminder,
            'completionDateTime':task.completionDateTime,
            'comments':task.comments
        }
    ]
    return new_task

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/todo/tasks', methods=['GET'])
@cross_origin()
def getTasks():
    tasks = Tasks.query.all()
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
@cross_origin()
def getTask(task_id):
   return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/task', methods=['POST'])
@cross_origin()
def createTask():
    if not request.json:
        abort(400)
    task = Tasks(title=request.json['title'],
                 description=request.json.get('description', ""),
                 scheduledDateTime=dateutil.parser.parse(request.json.get('scheduledDateTime', ""))
                 )
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': [make_public_task(task)]}), 201


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
@cross_origin()
def get_task(task_id):
   return jsonify({'tasks': [make_public_task(task) for task in tasks]})


@app.route('/todo/tasks/<int:task_id>', methods=['PUT'])
@cross_origin()
def update_task(task_id):
    task = Tasks.query.get(task_id)
    title = request.json.get('title')
    description = request.json.get('description')
    done = request.json.get('done'),
    scheduledDateTime =request.json.get('scheduledDateTime'),
    completionDateTime=request.json.get('completionDateTime'),
    comments=request.json.get('comments')

    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if done is not None:
        task.done = done[0]
    if scheduledDateTime[0] is not None:
        task.scheduledDateTime=dateutil.parser.parse(scheduledDateTime[0])
    if completionDateTime[0] is not None:
        task.completionDateTime=dateutil.parser.parse(completionDateTime[0])
    else:
        task.completionDateTime=None
    if comments is not None:
        task.comments=comments
    else:
        task.comments=""
    if done is False:
        task.comments=""
    db.session.commit()
    return jsonify({'task': [make_public_task(task)]})


@app.route('/todo/tasks/<int:task_id>', methods=['DELETE'])
@cross_origin()
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if task is None:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})


@app.route('/todo/tasks/reminders', methods=['GET'])
@cross_origin()
def get_reminders():
    tasks = Tasks.query.all()
    reminders = []
    for task in tasks:
        scheduledDateTime = task.scheduledDateTime
        if task.done == False:
            currentTime=datetime.utcnow()
            if currentTime>=scheduledDateTime:
                task.reminder=True
                reminders.append(task)
    return jsonify({'tasks': [make_public_task(task) for task in reminders]})


@app.route('/todo/tasks/done', methods=['GET'])
@cross_origin()
def getDoneTasks():
    tasks = Tasks.query.all()
    doneTasks = []
    for task in tasks:
        if task.done == True:
            doneTasks.append(task)
    return jsonify({'tasks': [make_public_task(task) for task in doneTasks]})


@app.route('/todo/tasks/pending', methods=['GET'])
@cross_origin()
def getPendingTasks():
    tasks = Tasks.query.all()
    pendingTasks = []
    for task in tasks:
        if task.done == False:
            pendingTasks.append(task)
    return jsonify({'tasks': [make_public_task(task) for task in pendingTasks]})


@app.route('/todo/tasks/deleteAll', methods=['GET'])
@cross_origin()
def deleteAllTasks():
    tasks = Tasks.query.all()
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    tasks = Tasks.query.all()
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})
