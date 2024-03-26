from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.workout import Workout, workouts_schema, workout_schema


workouts_bp = Blueprint('workouts', __name__, url_prefix='/workouts')

@workouts_bp.route('/')
def get_all_cards():
    stmt = db.select(Workout).order_by(Workout.date.desc())
    workouts = db.session.scalars(stmt)
    return workouts_schema.dump(workouts)

@workouts_bp.route('/<int:workout_id>')
def get_one_workout(workout_id):
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)
    if workout:
        return workout_schema.dump(workout)
    else:
        return{"error": f"Workout with id {workout_id} not found"}, 404
    
@workouts_bp.route('/', methods=["POST"])
@jwt_required()
def create_workout():
    body_data = request.get_json()
    workout = Workout(
        workout_name = body_data.get('workout_name'),
        description = body_data.get('description'),
        date = date.today(),
        workout_rating = body_data.get('workout_rating'),
        user_id = get_jwt_identity()
    )

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201

@workouts_bp.route('/<int:workout_id>', methods=["DELETE"])
def delete_workout(workout_id):
    stmt = db.select(Workout).where(Workout.id == workout_id)
    workout = db.session.scalar(stmt)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return {'message': f"Workout '{workout.workout_name}' deleted successfully"}
    else:
        return {'error': f"Workout with id {workout_id} not found"}, 404





