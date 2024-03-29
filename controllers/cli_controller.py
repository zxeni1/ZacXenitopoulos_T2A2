from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.workout import Workout
from models.exercise import Exercise
from models.progress import Progress  

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
    # Drop all existing tables
    db.drop_all()
    print("Tables dropped")

    # Create all tables
    db.create_all()
    print("Tables created")

    # Seed initial data
    # Create users
    admin_user = User(
        email="admin@email.com",
        password=bcrypt.generate_password_hash('123456').decode('utf-8'),
        is_admin=True
    )
    regular_user = User(
        name="User 1",
        email="user1@email.com",
        password=bcrypt.generate_password_hash('123456').decode('utf-8')
    )
    db.session.add_all([admin_user, regular_user])
    db.session.commit()

    # Create workouts
    workouts = [
        Workout(
            workout_name="Chest Day",
            description="chest and triceps",
            date=date.today(),
            workout_rating="4/5",
            user=admin_user
        ),
        Workout(
            workout_name="Leg Day",
            description="Legs and cardio weight session",
            date=date.today(),
            workout_rating="5/5",
            user=admin_user
        ),
        Workout(
            workout_name="Back and Biceps",
            description="back and biceps weight session",
            date=date.today(),
            workout_rating="2/5",
            user=regular_user
        ),
        Workout(
            workout_name="Cardio Session",
            description="Bike and treadmill cardio session",
            date=date.today(),
            workout_rating="3/5",
            user=regular_user
        )
    ]
    db.session.add_all(workouts)
    db.session.commit()

    # Create exercises
    exercises = [
        Exercise(
            exercise_name="Bench Press",
            sets="3",
            reps="12",
            weight="80kg",
            user=admin_user,
            workout=workouts[0]
        ),
        Exercise(
            exercise_name="Deadlifts",
            sets="5",
            reps="5",
            weight="100kg",
            user=regular_user,
            workout=workouts[2]
        ),
        Exercise(
            exercise_name="Treadmill",
            sets="5",
            reps="5 minutes",
            weight="0kg",
            user=regular_user,
            workout=workouts[3]
        ),
        Exercise(
            exercise_name="Squats",
            sets="3",
            reps="15",
            weight="60kg",
            user=admin_user,
            workout=workouts[1]
        )
    ]
    db.session.add_all(exercises)
    db.session.commit()

    # Seed progress data
    progress_data = [
        Progress(
            weight=80.5,
            bmi=22.1,
            muscle_mass=65.3,
            waist_measurements=30.5,
            workout=workouts[0]
        ),
        Progress(
            weight=75.8,
            bmi=20.3,
            muscle_mass=63.8,
            waist_measurements=29.2,
            workout=workouts[1]
        )
    ]
    db.session.add_all(progress_data)
    db.session.commit()

    print("Tables seeded")

