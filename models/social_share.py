from init import db, ma
from marshmallow import fields
from models.workout import WorkoutSchema
from models.user import UserSchema

class SocialShare(db.Model):
    __tablename__ = "social_shares"

    id = db.Column(db.Integer, primary_key=True)
    share_date = db.Column(db.Date)
    share_message = db.Column(db.String(150), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    workout = db.relationship("Workout", back_populates="social_shares")
    user = db.relationship("User", back_populates="social_shares")

class SocialShareSchema(ma.Schema):
    workout = fields.Nested(WorkoutSchema)
    user = fields.Nested(UserSchema)

    class Meta:
        fields = ('id', 'share_date', 'share_message', 'workout', 'user')

social_share_schema = SocialShareSchema()
social_shares_schema = SocialShareSchema(many=True)

