from init import db, ma
from marshmallow import fields

class Exercise(db.Model):
    __tablename__ = "exercises"
    
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.Text)
    sets = db.Column(db.String(20))
    reps = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeginKey ("users.id"), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    user = db.relationship("User", back_populates="exercises")
    workout = db.relationship("Workout", back_populates="exercises")

    class ExerciseSchema(ma.Schema):

        user = fields.Nested('UserSchema', only=['name', 'email'])

        workout = fields.Nested('WorkoutSchema', exclude=['exercises'])

        class Meta:
            fields = ('id', 'exercise_name', 'user', 'workout')
    
    exercise_schema = ExerciseSchema()
    comments_schema = ExerciseSchema(many=True)



 

