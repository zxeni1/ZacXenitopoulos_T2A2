from flask import Blueprint
from init import db
from models.workout import Workout, workouts_schema

workouts_bp = Blueprint('workouts', __name__, url_prefix='/workouts')

@workouts_bp.route('/')
def get_all_cards():
    stmt = db.select(Workout).order_by(Workout.date.desc())
    workouts = db.session.scalars(stmt)
    return workouts_schema.dump(workouts)