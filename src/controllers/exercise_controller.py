from flask import Blueprint, request, jsonify
from init import db
from models.exercise import Exercise
from models.exercise import Exercise, exercise_schema

exercise_bp = Blueprint('exercises', __name__, url_prefix='/exercises')

@exercise_bp.route('/', methods=['POST'])
def add_exercise():
    data = request.json
    name = data.get('name')
    weight = data.get('weight')
    reps = data.get('reps')
    sets = data.get('sets')
    workout_id = data.get('workout_id')

    if not all([name, weight, reps, sets, workout_id]):
        return jsonify({"error": "Missing required fields"}), 400

    exercise = Exercise(name=name, weight=weight, reps=reps, sets=sets, workout_id=workout_id)
    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.jsonify(exercise), 201

@exercise_bp.route('/<int:workout_id>', methods=['GET'])
def get_exercises(workout_id):
    exercises = Exercise.query.filter_by(workout_id=workout_id).all()
    return exercise_schema.jsonify(exercises)
