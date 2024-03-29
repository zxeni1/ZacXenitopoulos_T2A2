# Fitness Tracker API

## Zac Xenitopoulos T2 A2 

### Github: [Click here!](https://github.com/zxeni1/ZacXenitopoulos_T2A2)
### Trello: [Click here!](https://trello.com/b/oWQI3reL/zacxenitopoulost2a2)

### How to run the Fitness Tracker API

1. Create a new PostgreSQL user and give permissions 

2. Create a PostgreSQL database
```
CREATE DATABASE fitnesstracker_db;
```
3. Edit ".env" file so "DATABASE_URI" matches user and database details
```
DATABASE_URI=postgresql://myuser:mypassword@localhost/fitnesstracker_db
```
4. Start Python virtual environment
```
python3 -m venv .venv
```
5. Activate the virtual environment
```
source venv/bin/activate
```
6. Install requirements
```
pip install -r requirements.txt
```
7. Create and seed tables
```
flask db drop  
flask db create 
flask db seed   
```
8. Run the Flask app
```
flask run
```

## Identification of the problem you are trying to solve by building this particular app.

The goal of the fitness tracking API I've created is to satisfy the increasing demand for an all-inclusive and transparent way to efficiently track and organise exercise routines. In the modern world, when people of all ages prioritise their health and wellness, having a trustworthy tool to track and analyse fitness data is essential to reaching fitness objectives and upholding a healthy lifestyle.

The absence of a centralised platform that allows users to easily track their fitness activities across several devices and applications is one of the main issues that this fitness tracking API aims to address. Due to the widespread availability of internet platforms, mobile apps, and fitness trackers, users frequently get an abundance of fragmented data from various sources. This chaos not only makes the the capacity to learn about one's total fitness development, but it also presents difficulties in establishing and monitoring attainable fitness objectives.

Users can now compile their fitness data in one location, simplifying the tracking and analysis process, thanks to a single API that interfaces with various fitness gadgets, apps, and platforms. Steps taken, calories burned, distance travelled, and length of workout are just a few of the fitness parameters that can be recorded and analysed with the API.

Furthermore, users can obtain important insights about their fitness trends, patterns, and performance over time thanks to the API's sophisticated analytics features. Users may track their progress, pinpoint areas for improvement, and make well-informed decisions to maximise their fitness routines by utilising data visualisation tools and customisable reports.

Additionally, the fitness monitoring API places a high priority on user privacy and data security, guaranteeing that private health information is safeguarded and complies with legal requirements like GDPR and HIPAA. Users are able to have confidence that their fitness data is always kept private and safe because strong authentication procedures and data encryption techniques are implemented.

In conclusion, by giving users a centralised platform to measure, evaluate, and maximise their fitness activities, the fitness tracking API offers a complete solution to empower users in their fitness journey. Through tackling the issues of data fragmentation, offering practical insights, and emphasising data privacy and security, the API seeks to transform the way people approach fitness tracking and accomplish their wellness and health objectives.

## Why is it a problem that needs solving?

A complete fitness tracking system is required because of the following major obstacles that people attempting to lead healthy lives must overcome:

Fragmented Data Sources: Users are frequently overloaded with data that is dispersed among numerous devices and applications due to the widespread usage of fitness trackers, smartphone apps, and internet platforms. Due to the fragmentation, consumers find it challenging to have a comprehensive understanding of their fitness development because they have to switch between numerous interfaces in order to access and analyse their data.

Lack of Integration: A lot of the fitness trackers on the market now work in isolated silos and aren't compatible with other platforms or devices. Users' capacity to compile information from various sources is restricted by this lack of integration, making it more difficult for them to keep track of and thoroughly evaluate their overall fitness activities.

Limited Insights: Although some fitness trackers have some basic data tracking features, they frequently lack the ability to provide tailored recommendations and actionable insights. In order to maximise their exercises and meet their fitness objectives, users could find it difficult to understand their fitness statistics and make wise judgements.

Privacy and security: Users are becoming more concerned about the security and privacy of their information due to the sensitive nature of health and fitness data. In the absence of strong privacy safeguards, consumers could be reluctant to provide third-party apps access to their health information, which would limit their usage of the advanced analytics and individualised coaching capabilities.

Complexity and Accessibility: Some user groups, such as older persons or people with little technological ability, may find the current fitness tracking solutions excessively complicated or unusable. For a fitness tracking system to be widely accessible and adopted by a variety of user communities, it must be simple to use.

Given these difficulties, a thorough fitness tracking system that overcomes the shortcomings of current instruments is obviously required. Through its smooth integration with various platforms and devices, actionable insights derived from sophisticated analytics, strong privacy and security protocols, and intuitive user interface, this solution can enable people to take charge of their fitness journey and more successfully accomplish their wellness and health objectives.

## Why have you chosen this database system. What are the drawbacks compared to others?

PostgreSQL was selected as the suitable database solution for the fitness tracking API because of its ability to handle structured data, support for intricate relational models, and extensive feature set. The advantages and disadvantages of utilising PostgreSQL for this application are covered in detail below:

**Advantages:**

Relational Data Model: Fitness tracking data, which frequently includes intricate relationships between entities like users, workouts, and activities, is best organised using PostgreSQL's relational data model. This preserves data integrity while enabling effective data storage and retrieval.

ACID Compliance: PostgreSQL guarantees data integrity and consistency even in high-concurrency contexts by abiding by the ACID principles (Atomicity, Consistency, Isolation, Durability). This is essential to preserving the precision and dependability of fitness tracking data, particularly in situations where several individuals may access and edit their data at once.

advanced features: PostgreSQL comes with a plethora of capabilities, including as support for stored procedures, triggers, user-defined functions, and sophisticated SQL queries. Because of these advantages, application code is not as burdened and performance is enhanced because complicated business logic and data processing chores can be implemented within the database itself.

Scalability: PostgreSQL has options for both horizontal and vertical scaling. While horizontal scaling includes spreading data over several servers via methods like sharding or replication, vertical scaling entails increasing the resources of a single server. As the application expands, this scalability guarantees that the fitness monitoring API can manage growing amounts of data and user traffic.

Community Support and Ecosystem: PostgreSQL has a sizable and vibrant open-source community that offers a wealth of third-party tools, tutorials, and documentation. This ecosystem makes it easier to create, debug, and optimise the database system, which guarantees the fitness tracking API's long-term maintainability and maintenance.

**Disadvantages:**

Complexity: Compared to simpler database options, setting up and installing PostgreSQL may need more knowledge, especially for people with little familiarity with relational databases. The intricacy of PostgreSQL may present difficulties for those who lack familiarity with relational database or SQL concepts. For some use cases, NoSQL databases like MongoDB may be more approachable due to their easier setup and schema flexibility.

Resource Intensity: PostgreSQL may require a lot of resources, especially in settings where workloads are write-heavy and concurrency is high. Achieving ideal performance could necessitate careful tuning and optimisation, which could complicate the deployment procedure. NoSQL databases with fewer resource requirements, such as Redis or Couchbase, may perform better in some use cases, such caching or real-time data processing. 

Scaling Challenges: Compared to NoSQL databases made expressly for distributed systems, PostgreSQL databases provide more possibilities for smooth horizontal scaling, although attaining this can be more difficult. Thorough planning and careful consideration of architecture may be necessary to ensure efficient scaling. Since NoSQL databases, such as Cassandra and DynamoDB, are designed for distributed architectures, scaling them horizontally as an application expands is made easier.

Learning Curve: Compared to more approachable NoSQL options, working with PostgreSQL may require developers with no prior experience with SQL or relational database ideas to go through a more rigorous learning curve. It could take assistance and training to properly onboard team members. Developers who are new to database management may find that NoSQL databases offer more flexible schemas and simpler data modelling, which will shorten their learning curve.

## Identify and discuss the key functionalities and benefits of an ORM

A programming approach called Object-Relational Mapping (ORM) enables developers to use an object-oriented paradigm when working with relational databases. By acting as a link between the object-oriented programming model and the relational database model, object-relational mappings (ORMs) enable developers to communicate with databases using well-known object-oriented ideas like classes, objects, and methods. The following are some essential features and advantages of utilising an ORM:

Abstraction of Database Operations: Rather than requiring developers to concentrate on building application logic, ORMs abstract away the complexity of SQL queries and database interactions. Instead of manually writing SQL queries, developers can carry out CRUD (Create, Read, Update, Delete) actions on database entities using high-level programming structures like classes and methods.

Object-Relational Mapping: Database tables are mapped to object classes and object attributes are mapped to database columns by ORMs. Database interactions become more obvious and natural as a result, enabling developers to deal with database entities as if they were standard objects in their programming language.

Query Generation: SQL queries are automatically generated by ORMs using the object-oriented programming that developers have created. This lowers the possibility of errors and enhances code maintainability by doing away with the requirement for developers to write boilerplate SQL code for routine database operations.

Cross-Platform Compatibility: By abstracting away from the details of the underlying database systems, ORMs make it easier to move applications between various database engines. This reduces the need to rewrite significant amounts of code when switching databases or supporting several databases inside a single application.

Database Agnosticism: Because ORMs offer some degree of database agnosticism, programmers are able to create code that is independent of databases. This makes it easier to transition to alternative databases or support several databases at once since developers may build application logic without being restricted to a particular database system.

Data Validation and Type Safety: To help guarantee that only legitimate data is kept in the database, ORMs frequently include built-in techniques for data validation and type safety. This strengthens data integrity and lowers the possibility of data corruption by imposing restrictions at the application level.

Performance Optimisation: Lazy loading, eager loading, and caching are just a few of the capabilities that many ORMs offer to optimise database performance. By lowering latency and minimising the amount of database queries, these features enhance the application's overall performance

Code Reusability and Maintainability: By encapsulating database access functionality within reusable components, ORMs facilitate code reusability and maintainability. This saves code duplication between various application components and facilitates the writing of modular, maintainable code.

To sum up, developers that work with relational databases can benefit from a robust set of features offered by ORMs. ORMs facilitate faster development, better code maintainability, and higher application quality and performance by abstracting away the complexity of database interactions.

## Document all endpoints for your API


Authentication Endpoints:

1. Register User

URL: /api/register

Method: POST

Description: Registers a new user.

Request Body:
```
{
  "username": "string",
  "password": "string"
}
```
Response:

Success: 201 Created
```
{
  "message": "User registered successfully"
}
```
Error: 400 Bad Request
```
{
  "error": "Invalid request body"
}
```
2. Login User

URL: /api/login

Method: POST

Description: Logs in a user.

Request Body:
```
{
  "name": "string",
  "email": "string",
  "password": "string"
}
```
Response:
Success: 200 OK
```
{
  "token": "JWT_token",
  "message": "Login successful"
}
```
Error: 401 Unauthorized
```
{
  "error": "Invalid email or password"
}
```
Fitness Tracking Endpoints:

3. Get All Workouts

URL: /workouts/

Method: GET

Description: Retrieves all workouts.

Response:

Success: 200 OK
```
[
  {
    "id": "integer",
    "workout_name": "string",
    "description": "string",
    "date": "YYYY-MM-DD",
    "workout_rating": "integer",
    "user_id": "integer"
  },
  ...
]
```
4. Get One Workout

URL: /workouts/<int:workout_id>

Method: GET

Description: Retrieves a specific workout by ID.

Response:

Success: 200 OK
```
{
  "id": "integer",
  "workout_name": "string",
  "description": "string",
  "date": "YYYY-MM-DD",
  "workout_rating": "integer",
  "user_id": "integer"
}

```
Error: 404 Not Found
```
{
  "error": "Workout with id {workout_id} not found"
}
```
Create Workout

URL: /workouts/

Method: POST

Description: Creates a new workout.

Authorization Header: Bearer JWT_token

Request Body:
```
{
  "workout_name": "string",
  "description": "string",
  "workout_rating": "integer"
}
```
Response:
Success: 201 Created
```
{
  "id": "integer",
  "workout_name": "string",
  "description": "string",
  "date": "YYYY-MM-DD",
  "workout_rating": "integer",
  "user_id": "integer"
}
```
6. Delete Workout

URL: /workouts/<int:workout_id>

Method: DELETE

Description: Deletes a specific workout by ID.

Response:

Success: 200 OK
```
{
  "message": "Workout '{workout_name}' deleted successfully"
}
```
Error: 404 Not Found
```
{
  "error": "Workout with id {workout_id} not found"
}
```
7. Update Workout

URL: /workouts/<int:workout_id>

Method: PUT or PATCH

Description: Updates a specific workout by ID.

Request Body:
```
{
  "workout_name": "string",
  "description": "string",
  "workout_rating": "integer"
}
```
Response:
Success: 200 OK
```
{
  "id": "integer",
  "workout_name": "string",
  "description": "string",
  "date": "YYYY-MM-DD",
  "workout_rating": "integer",
  "user_id": "integer"
}
```
Error: 404 Not Found
```
{
  "error": "Workout with id {workout_id} not found"
}
```
8. Create Exercise

URL: /workouts/<int:workout_id>/exercises

Method: POST

Description: Adds a new exercise to a workout.

Authorization Header: Bearer JWT_token

Request Body:
```
{
  "exercise_name": "string",
  "sets": "integer",
  "reps": "integer",
  "weight": "float"
}
```
Response:
Success: 201 Created
```
{
  "id": "integer",
  "exercise_name": "string",
  "sets": "integer",
  "reps": "integer",
  "weight": "float",
  "workout_id": "integer",
  "user_id": "integer"
}
```
9. Delete Exercise

URL: /workouts/<int:workout_id>/exercises/<int:exercise_id>

Method: DELETE

Description: Deletes a specific exercise from a workout.

Authorization Header: Bearer JWT_token

Response:

Success: 200 OK
```
{
  "message": "Exercise with id {exercise_id} has been deleted"
}
```
Error: 404 Not Found
```
{
  "error": "Exercise with id {exercise_id} not found in workout with id {workout_id}"
}
```
10. Edit Exercise

URL: /workouts/<int:workout_id>/exercises/<int:exercise_id>

Method: PUT or PATCH

Description: Edits a specific exercise from a workout.

Authorization Header: Bearer JWT_token

Request Body:
```
{
  "exercise_name": "string",
  "sets": "integer",
  "reps": "integer",
  "weight": "float"
}
```
Response:

Success: 200 OK
```
{
  "id": "integer",
  "exercise_name": "string",
  "sets": "integer",
  "reps": "integer",
  "weight": "float",
  "workout_id": "integer",
  "user_id": "integer"
}
```
Error: 404 Not Found
```
{
  "error": "Exercise with id
}
```
Get Progress

URL: /workouts/<int:workout_id>/progress

Method: GET

Description: Retrieves progress for a specific workout.

Response:

Success: 200 OK
```
  {
    "id": "integer",
    "weight": "float",
    "bmi": "float",
    "muscle_mass": "float",
    "waist_measurements": "float",
    "workout_id": "integer"
  }
```
Get One Progress

URL: /workouts/<int:workout_id>/progress/<int:progress_id>

Method: GET

Description: Retrieves a specific progress entry for a workout.

Response:

Success: 200 OK
```
{
  "id": "integer",
  "weight": "float",
  "bmi": "float",
  "muscle_mass": "float",
  "waist_measurements": "float",
  "workout_id": "integer"
}
```
Error: 404 Not Found
```
{
  "error": "Progress with id {progress_id} not found in workout with id {workout_id}"
}
```
13. Add Progress

URL: /workouts/<int:workout_id>/progress

Method: POST

Description: Adds progress to a specific workout.

Authorization Header: Bearer JWT_token

Request Body:
```
{
  "weight": "float",
  "bmi": "float",
  "muscle_mass": "float",
  "waist_measurements": "float"
}
```
Response:

Success: 201 Created
```
{
  "id": "integer",
  "weight": "float",
  "bmi": "float",
  "muscle_mass": "float",
  "waist_measurements": "float",
  "workout_id": "integer"
}
```
14. Delete Progress

URL: /workouts/<int:workout_id>/progress/<int:progress_id>

Method: DELETE

Description: Deletes a specific progress entry for a workout.

Authorization Header: Bearer JWT_token

Response:

Success: 200 OK
```
{
  "message": "Progress with id {progress_id} has been deleted"
}
```
Error: 404 Not Found
```
{
  "error": "Progress with id {progress_id} not found in workout with id {workout_id}"
}
```
15. Edit Progress

URL: /workouts/<int:workout_id>/progress/<int:progress_id>

Method: PUT or PATCH

Description: Edits a specific progress entry for a workout.

Authorization Header: Bearer JWT_token

Request Body:
```
{
  "weight": "float",
  "bmi": "float",
  "muscle_mass": "float",
  "waist_measurements": "float"
}
```
Response:

Success: 200 OK
```
{
  "id": "integer",
  "weight": "float",
  "bmi": "float",
  "muscle_mass": "float",
  "waist_measurements": "float",
  "workout_id": "integer"
}
```
Error: 404 Not Found
```
{
  "error": "Progress with id {progress_id} not found in workout with id {workout_id}"
}
```

## An ERD for your app

![ERD](docs/fitnesstracker.drawio.png)

## Detail any third party services that your app will use
 
| Third Party Services | Description                                                                                    |
|----------------------|-------------------------------------------------------------------------------------------------
| Flask                | Micro web framework for Python, used for building web applications.                            |
| PostgreSQL           | Open-source relational database management system.                                             |
| SQLAlchemy           | SQL toolkit and Object-Relational Mapping (ORM) library for Python.                            |
| Marshmellow          | Library for object serialization and deserialization, often used for API schema definitions.   |
| Flask-Bcrypt         | Flask extension for bcrypt hashing utilities, used for secure password hashing.                |
| Flask-JWT-Extended   | Flask extension for JSON Web Tokens (JWT), facilitating user authentication and authorization. |
| Psycopg2             | PostgreSQL adapter for Python, enabling communication between Python apps and PostgreSQL DBs.  |
| dotenv               | Python module for managing configuration settings using .env files.                            |

## Describe your projects models in terms of the relationships they have with each other

**User Model:**
Relationships:
One-to-Many with Workout model: Each user can have multiple workouts.

One-to-Many with Exercise model: Each user can have multiple exercises.

Description: The User model represents users of the application. Users can create workouts and exercises, and their data is associated with these workouts and exercises through foreign keys.

**Workout Model:**
Relationships:
Many-to-One with User model: Many workouts can belong to one user.

One-to-Many with Exercise model: Each workout can have multiple exercises.

One-to-Many with Progress model: Each workout can have multiple progress entries.

Description: The Workout model represents individual workout sessions. Each workout belongs to a single user and can consist of multiple exercises. Progress data can be tracked and associated with each workout.

**Exercise Model:**

Relationships:
Many-to-One with User model: Many exercises can belong to one user.

Many-to-One with Workout model: Many exercises can belong to one workout.

Description: The Exercise model represents individual exercises performed during workout sessions. Exercises are associated with both users and workouts, allowing for tracking and organization of exercise data.

**Progress Model:**

Relationships:
Many-to-One with Workout model: Many progress entries can belong to one workout.

Description: The Progress model represents progress data tracked during workout sessions. Each progress entry is associated with a specific workout, allowing users to monitor their progress over time.

These relationships enable users to organize and track their workouts, exercises, and progress effectively within the application.

## Discuss the database relations to be implemented in your application

**User-Workout Relationship:**

Type: One-to-Many (1:N)
Description: Each user can have multiple workouts, but each workout belongs to only one user. This relationship allows users to create and manage their own workouts independently.

**User-Exercise Relationship:**

Type: One-to-Many (1:N)
Description: Similar to the user-workout relationship, each user can have multiple exercises associated with them. However, each exercise belongs to only one user. This relationship allows users to track their exercises and manage them within their account.

**Workout-Exercise Relationship:**

Type: One-to-Many (1:N)
Description: Each workout can consist of multiple exercises, but each exercise is associated with only one workout. This relationship allows users to organize and structure their workouts by adding multiple exercises to each workout session.

**Workout-Progress Relationship:**

Type: One-to-Many (1:N)
Description: Each workout can have multiple progress entries associated with it, but each progress entry is linked to only one workout. This relationship enables users to track their progress over time for each workout session.

These database relationships ensure data integrity and enable efficient querying and manipulation of data within the application. By establishing these relationships, users can manage their workouts, exercises, and progress seamlessly, leading to a better user experience overall.

## Describe the way tasks are allocated and tracked in your project

In the project, tasks are allocated and tracked using Trello, an online project management tool. The project board in Trello is organized into three main categories: "To Do," "In Development," and "Completed."

**To Do:**
This category contains tasks that have been identified but are yet to be started. These tasks are awaiting allocation and prioritization.

**In Development:**
Tasks move to this category once they are assigned to a team member (in this case, yourself) and work has begun on them. This category serves as a work-in-progress section where tasks are actively being worked on.

**Completed:**
Once a task is finished, it is moved to the "Completed" category. This category serves as a record of all tasks that have been successfully completed.
Each task in Trello, represented by a card, contains the following information:

**Assigned Person:**
Each task is assigned to a specific team member responsible for its completion. In this case, tasks are assigned to yourself, indicating that you are responsible for completing them.

**Due Dates:**
A due date is set for each task, indicating the deadline by which it should be completed. This helps in prioritizing tasks and ensuring timely delivery.

**Description:**
A description of the task is provided on the card, detailing what needs to be done and any specific requirements or instructions.

**Checklists:**
Checklists are often used to break down tasks into smaller sub-tasks or steps. These checklists provide a clear roadmap for completing the task and help in tracking progress.

By utilising Trello in this way, you can effectively allocate, track, and manage tasks throughout the project lifecycle. This approach promotes transparency, collaboration, and accountability among team members, ultimately contributing to the successful completion of the project.

![](/docs/A2B41D29-84DC-42CB-BF98-E63F10AEF971.jpeg)
![](/docs/C2A7A758-52B8-4470-B086-47D96D68323C.jpeg)

