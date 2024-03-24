from init import db, ma
from marshmallow import fields

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    workout_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    workout_rating = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='workouts')

class WorkoutSchema(ma.Schema):
    user = fields.Nested('UserSchema', only = ['name', 'email'])
    class Meta:
        fields = ('id', 'workout_name', 'description', 'date', 'workout_rating', 'user')

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)




