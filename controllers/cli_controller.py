from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.workout import Workout
from models.exercise import Exercise

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    workouts = [
        Workout(
            workout_name="Chest Day",
            description="chest and triceps",
            date=date.today(),
            workout_rating="4/5",
            user_id=users[0].id
        ),
        Workout(
            workout_name="Leg Day",
            description="Legs and cardio weight session",
            date=date.today(),
            workout_rating="5/5",
            user_id=users[0].id
        ),
        Workout(
            workout_name="Back and Biceps",
            description="back and biceps weight session",
            date=date.today(),
            workout_rating="2/5",
            user_id=users[1].id
        ),
        Workout(
            workout_name="Cardio Session",
            description="Bike and treadmill cardio session",
            date=date.today(),
            workout_rating="3/5",
            user_id=users[1].id
        )    
    ]

    db.session.add_all(workouts)
    db.session.commit()

    exercises = [
        Exercise(
            exercise_name="Bench Press",
            sets="3",
            reps="12",
            weight="80kg",
            user=users[0],
            workout=workouts[0]  # Adjusted index to match the available workouts
        ),
        Exercise(
            exercise_name="Deadlifts",
            sets="5",
            reps="5",
            weight="100kg",
            user=users[1],
            workout=workouts[2]  # Adjusted index to match the available workouts
        ),
        Exercise(
            exercise_name="Treadmill",
            sets="5",
            reps="5 minutes",
            weight="0kg",
            user=users[1],
            workout=workouts[3]  # Adjusted index to match the available workouts
        ),
        Exercise(
            exercise_name="Squats",
            sets="3",
            reps="15",
            weight="60kg",
            user=users[0],
            workout=workouts[1]  # Adjusted index to match the available workouts
        )
    ]

    db.session.add_all(exercises)
    db.session.commit()

    print("Tables seeded")