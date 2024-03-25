from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.workout import Workout

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

    print("Tables seeded")
