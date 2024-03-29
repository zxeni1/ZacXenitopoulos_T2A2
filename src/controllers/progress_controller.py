from flask import Blueprint, request, jsonify
from init import db
from models.progress import Progress
from models.progress import Progress, progress_schema

progress_bp = Blueprint('progress', __name__, url_prefix='/progress')

@progress_bp.route('/', methods=['POST'])
def add_progress():
    data = request.json
    weight = data.get('weight')
    bmi = data.get('bmi')
    muscle_mass = data.get('muscle_mass')
    waist_measurements = data.get('waist_measurements')
    workout_id = data.get('workout_id')

    if not all([weight, bmi, muscle_mass, waist_measurements, workout_id]):
        return jsonify({"error": "Missing required fields"}), 400

    progress = Progress(weight=weight, bmi=bmi, muscle_mass=muscle_mass, waist_measurements=waist_measurements, workout_id=workout_id)
    db.session.add(progress)
    db.session.commit()

    return progress_schema.jsonify(progress), 201

@progress_bp.route('/<int:workout_id>', methods=['GET'])
def get_progress(workout_id):
    progress = Progress.query.filter_by(workout_id=workout_id).all()
    return progress_schema.jsonify(progress)

