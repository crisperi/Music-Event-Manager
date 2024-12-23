# Music Event Manager

A database-driven application for managing music events, bands, and venues.

## Overview

This project is a Python-based application that utilizes SQLAlchemy for database operations and Alembic for database migrations. It provides a structured way to store and manage information about music bands, venues, and concerts.

## Features

- Database schema for bands, venues, and concerts
- Ability to add, query, and manage music event data
- Relationships between bands, venues, and concerts
- Custom queries for retrieving specific information (e.g., bands with the most performances)

## Project Structure

Music-Event-Manager/
├── app/
│   ├── models.py
│   ├── runfile.py
│   └── migrations/
│       └── versions/
│           └── <migration_files>.py
├── concerts.db
├── Pipfile
├── Pipfile.lock
└── README.md

## Setup

1. Clone the repository:
git clone https://github.com/your-username/Music-Event-Manager.git


2. Navigate to the project directory:
cd Music-Event-Manager


3. Install dependencies:
pipenv install


4. Activate the virtual environment:
pipenv shell


## Usage

1. Run the application to create the database and add initial data:
python app/runfile.py


2. The application will create the necessary tables and populate them with sample data.

## Database Schema

The database consists of three main tables:

- `bands`: Stores information about music bands
- `venues`: Stores information about concert venues
- `concerts`: Stores information about specific concerts, linking bands and venues

## Custom Queries

The application includes custom queries for retrieving specific information:

- `Band.most_performances()`: Returns the band with the most performances
- `Concert.introduction()`: Generates an introduction for a concert

## Contributing

Contributions are welcome! If you have any ideas for new features or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
