from init import db, ma
from marshmallow import fields
from models.exercise import ExerciseSchema
from models.progress import ProgressSchema

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    workout_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False)
    workout_rating = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="workouts", foreign_keys=[user_id])
    exercises = db.relationship("Exercise", back_populates="workout", cascade="all, delete-orphan")
    progress = db.relationship("Progress", back_populates="workout", cascade="all, delete-orphan")


class WorkoutSchema(ma.Schema):
    
    user = fields.Nested('UserSchema', only=['name', 'email'])

    exercises = fields.List(fields.Nested('ExerciseSchema', only=['exercise_name', 'sets', 'reps', 'weight', 'id']))

    progress = fields.List(fields.Nested('ProgressSchema', only=['id', 'weight', 'bmi', 'muscle_mass', 'waist_measurements']))
    
    class Meta:
        fields = ('id', 'user', 'workout_name', 'description', 'date', 'workout_rating', 'exercises', 'progress')  
        ordered = True

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)








