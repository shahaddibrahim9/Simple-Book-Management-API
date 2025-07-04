﻿# Simple-Book-Management-API
A simple RESTful API for managing a collection of books built using FastAPI and SQLite.

# Features
- Add new books
- Retrieve all books
- Get details of a specific book
- Update book information
- Delete books
- Basic Authentication (Bonus)
- Pagination support (Bonus)

# Tech Stack
- Backend Framework: FastAPI (Python)
- Database: SQLite (Relational DB)
- Authentication: Basic Auth 
- Documentation: Swagger UI 

#Installation
1- Clone the repository 
- bash git clone https://github.com/shahaddibrahim9/Simple-Book-Management-API.git 
- cd Simple-Book-Management-API

2- Create a virtual environment 
python -m venv venv venv\Scripts\activate

3- Install dependencies 
pip install -r requirements.txt

4- Run the server 
uvicorn app.main:app --reload

5- Access the API docs 
- Swagger UI: http://127.0.0.1:8000/docs 
- ReDoc: http://127.0.0.1:8000/redoc
