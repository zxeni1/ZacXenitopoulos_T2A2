from init import db, ma
from marshmallow import fields
from models.user import UserSchema
from models.workout import WorkoutSchema

class Exercise(db.Model):
    __tablename__ = "exercises"
    
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.Text)
    sets = db.Column(db.String(20))
    reps = db.Column(db.String(20))
    weight = db.Column(db.String(20))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    user = db.relationship("User", back_populates="exercises")
    workout = db.relationship("Workout", back_populates="exercises")

class ExerciseSchema(ma.Schema):
    user = fields.Nested(UserSchema)
    workout = fields.Nested(WorkoutSchema)

    class Meta:
        fields = ('id', 'exercise_name', 'sets', 'reps', 'weight', 'user', 'workout')

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)





 

