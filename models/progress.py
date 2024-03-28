from init import db, ma
from marshmallow import fields

class Progress(db.Model):
    __tablename__ = "progress"

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float)
    muscle_mass = db.Column(db.Float)
    waist_measurement = db.Column(db.Float)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    workout = db.relationship("Workout", back_populates="progress")

class ProgressSchema(ma.Schema):
    class Meta:
        fields = ('id', 'weight', 'bmi', 'muscle_mass', 'waist_measurement', 'workout_id')
        ordered = True

progress_schema = ProgressSchema()
progresses_schema = ProgressSchema(many=True)
