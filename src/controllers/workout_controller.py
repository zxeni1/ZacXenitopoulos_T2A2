from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.workout import Workout, workouts_schema, workout_schema
from models.exercise import Exercise, ExerciseSchema, exercise_schema
from models.progress import Progress, ProgressSchema, progress_schema

workouts_bp = Blueprint('workouts', __name__, url_prefix='/workouts')

@workouts_bp.route('/')
def get_all_workouts():
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
        return {"error": f"Workout with id {workout_id} not found"}, 404

@workouts_bp.route('/', methods=["POST"])
@jwt_required()
def create_workout():
    body_data = request.get_json()
    workout = Workout(
        workout_name=body_data.get('workout_name'),
        description=body_data.get('description'),
        date=date.today(),
        workout_rating=body_data.get('workout_rating'),
        user_id=get_jwt_identity()
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

@workouts_bp.route('/<int:workout_id>', methods=["PUT", "PATCH"])
def update_workout(workout_id):
    body_data = request.get_json()
    workout = Workout.query.get_or_404(workout_id)

    if workout:
        workout.workout_name = body_data.get('workout_name', workout.workout_name)
        workout.description = body_data.get('description', workout.description)
        workout.date = body_data.get('date', workout.date)
        workout.workout_rating = body_data.get('workout_rating', workout.workout_rating)

        db.session.commit()
        return workout_schema.dump(workout)
    
    else:
        return {'error': f"Workout with id '{workout_id}' not found"}, 404

@workouts_bp.route("/<int:workout_id>/exercises", methods=["POST"])
@jwt_required()
def create_exercise(workout_id):
    body_data = request.get_json()
    stmt = db.select(Workout).filter_by(id=workout_id)
    workout = db.session.scalar(stmt)
    if workout:
        exercise = Exercise(
            exercise_name=body_data.get('exercise_name'),
            sets=body_data.get('sets'),
            reps=body_data.get('reps'),
            weight=body_data.get('weight'),
            user_id=get_jwt_identity(),
            workout_id=workout.id
        )
        db.session.add(exercise)
        db.session.commit()
        return exercise_schema.dump(exercise), 201
    else:
        return {"error": f"Workout with id '{workout_id}' does not exist"}, 404

@workouts_bp.route('/<int:workout_id>/exercises/<int:exercise_id>', methods=["DELETE"])
@jwt_required()
def delete_exercise(workout_id, exercise_id):
    stmt = db.select(Exercise).filter_by(id=exercise_id)
    exercise = db.session.scalar(stmt)
    if exercise and exercise.workout.id == workout_id:
        db.session.delete(exercise)
        db.session.commit()
        return{"message": f"Exercise with id '{exercise_id}' has been deleted"}
    else:
        return {"error": f"Exercise with id '{exercise_id}' not found in workout with id {workout_id}"}, 404
    
@workouts_bp.route('/<int:workout_id>/exercises/<int:exercise_id>', methods=["PUT", "PATCH"])
@jwt_required()
def edit_exercise(workout_id, exercise_id):
    body_data = request.get_json()
    stmt = db.select(Exercise).filter_by(id=exercise_id, workout_id=workout_id)
    exercise = db.session.scalar(stmt)
    if exercise:
        exercise.exercise_name = body_data.get('exercise_name') or exercise.exercise_name
        exercise.sets = body_data.get('sets') or exercise.sets
        exercise.reps = body_data.get('reps') or exercise.reps
        exercise.weight = body_data.get('weight') or exercise.weight
        db.session.commit()
        return exercise_schema.dump(exercise)
    else: 
        return {"error": f"Exercise with id {exercise_id} not found in workout with id {workout_id}"}
    
@workouts_bp.route('/<int:workout_id>/progress', methods=["GET"])
def get_progress(workout_id):
    stmt = db.select(Progress).filter_by(workout_id=workout_id)
    progress = db.session.scalars(stmt)
    return progress_schema.dump(progress)

@workouts_bp.route('/<int:workout_id>/progress/<int:progress_id>', methods=["GET"])
def get_one_progress(workout_id, progress_id):
    stmt = db.select(Progress).filter_by(id=progress_id, workout_id=workout_id)
    progress = db.session.scalar(stmt)
    if progress:
        return progress_schema.dump(progress)
    else:
        return {"error": f"Progress with id {progress_id} not found in workout with id {workout_id}"}, 404

@workouts_bp.route('/<int:workout_id>/progress', methods=["POST"])
@jwt_required()
def add_progress(workout_id):
    body_data = request.get_json()
    progress = Progress(
        weight=body_data.get('weight'),
        bmi=body_data.get('bmi'),
        muscle_mass=body_data.get('muscle_mass'),
        waist_measurements=body_data.get('waist_measurements'),
        workout_id=workout_id
    )
    db.session.add(progress)
    db.session.commit()
    return progress_schema.dump(progress), 201

@workouts_bp.route('/<int:workout_id>/progress/<int:progress_id>', methods=["DELETE"])
@jwt_required()
def delete_progress(workout_id, progress_id):
    stmt = db.select(Progress).filter_by(id=progress_id, workout_id=workout_id)
    progress = db.session.scalar(stmt)
    if progress:
        db.session.delete(progress)
        db.session.commit()
        return {"message": f"Progress with id {progress_id} has been deleted"}
    else:
        return {"error": f"Progress with id {progress_id} not found in workout with id {workout_id}"}, 404

@workouts_bp.route('/<int:workout_id>/progress/<int:progress_id>', methods=["PUT", "PATCH"])
@jwt_required()
def edit_progress(workout_id, progress_id):
    body_data = request.get_json()
    stmt = db.select(Progress).filter_by(id=progress_id, workout_id=workout_id)
    progress = db.session.scalar(stmt)
    if progress:
        progress.weight = body_data.get('weight', progress.weight)
        progress.bmi = body_data.get('bmi', progress.bmi)
        progress.muscle_mass = body_data.get('muscle_mass', progress.muscle_mass)
        progress.waist_measurements = body_data.get('waist_measurements', progress.waist_measurements)
        db.session.commit()
        return progress_schema.dump(progress)
    else: 
        return {"error": f"Progress with id {progress_id} not found in workout with id {workout_id}"}, 404





    
