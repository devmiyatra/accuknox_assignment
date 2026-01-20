# AccuKnox AI/ML Trainee – Assignment Submission

## Overview
This repository contains my submission for the AccuKnox AI/ML Trainee assignment.
The assignment focuses on API data retrieval, data processing, SQLite database usage,
CSV import, and basic data visualization using Python.

## Assignment 1 Details

### 1. API Data Retrieval and Storage
- Data is fetched from an external REST API that returns book information in JSON format.
- The data includes book title, author, and publication year.
- The fetched data is stored in a local SQLite database (`books.db`).
- Stored data is retrieved and displayed to verify successful insertion.

File: `books_api_to_db.py`

### 2. Data Processing and Visualization
- Student-related data is fetched from a mock REST API.
- Average test scores are calculated for each student.
- A bar chart is generated to visualize the average scores.

File: `student_scores_visualization.py`

### 3. CSV Data Import to SQLite Database
- User data (name and email) is read from a CSV file.
- The data is inserted into a SQLite database (`students.db`).
- Inserted records are fetched and displayed.

Files:
- `users.csv`
- `csv_to_sqlite.py`

## Assumptions
- No specific REST API was provided, so public mock APIs were used to simulate real-world data.
- Student test scores were assumed for demonstration purposes.
- SQLite was chosen as it is lightweight and does not require additional setup.

## Technologies Used
- Python
- SQLite
- Requests library
- Matplotlib

## How to Run the Project

### Install Dependencies
- python -m pip install requests matplotlib


### Run Scripts
python books_api_to_db.py
python csv_to_sqlite.py
python student_scores_visualization.py


## Output
- Books data stored and displayed from SQLite database
- Users imported from CSV into SQLite database
- Bar chart visualization of average student scores

## Author
Dev Miyatra
