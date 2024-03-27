from init import db, ma
from marshmallow import fields

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    workout_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False)
    workout_rating = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="workouts")
    social_shares = db.relationship("SocialShare", back_populates="workout")
    exercises = db.relationship("Exercise", back_populates="workout")

class WorkoutSchema(ma.Schema):
    
    user = fields.Nested('UserSchema', only = ['name', 'email'])

    exercises = fields.List(fields.Nested('ExerciseSchema', exclude=['workout']))
    
    class Meta:
        fields = ('id', 'workout_name', 'description', 'date', 'workout_rating', 'user', 'exercises')
        ordered=True

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)




