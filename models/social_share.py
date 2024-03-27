from init import db, ma
from marshmallow import fields
from models.workout import WorkoutSchema
from models.exercise import ExerciseSchema

class SocialShare(db.Model):
    __tablename__ = "social_shares"

    id = db.Column(db.Integer, primary_key=True)
    share_date = db.Column(db.Date)
    share_message = db.Column(db.String(150), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    workout = db.relationship("Workout", back_populates="social_shares")
    exercises = db.relationship("Exercise", back_populates="workout", cascade='all, delete')

class SocialShareSchema(ma.Schema):
    workout = fields.Nested(WorkoutSchema)
    exercises = fields.List(fields.Nested(ExerciseSchema))

    class Meta:
        fields = ('id', 'social_share', 'share_message', 'workout', 'exercises')

social_share_schema = SocialShareSchema()
social_shares_schema = SocialShareSchema(many=True)
