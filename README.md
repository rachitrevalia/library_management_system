# Library Management System

This project is a terminal-based library management system built with Python and SQLite. It allows users to borrow, return, and reserve books, while also providing information about books and authors. The system is designed to handle books, authors, users, borrowings, and reservations, and stores the data in an SQLite database.

## Features

- **View Book Details**: View a list of books along with their details such as title, author, genre, and publication year.
- **Borrow Books**: Borrow a book by providing your user ID, book ID, name, and contact information.
- **Return Books**: Return a borrowed book by providing your user ID, book ID, name, and contact information.
- **Reserve Books**: Reserve a book for a specific date by providing your user ID and book ID.
- **View Author Details**: View details of all authors including their ID, name, nationality, birth date, and death date.

## Database Schema

The project uses an SQLite database with the following tables:

- **Books**: Contains details about books, including `book_id`, `title`, `author_id`, `genre`, and `publication_year`.
- **Authors**: Stores author information such as `author_id`, `name`, `nationality`, `birth_date`, and `death_date`.
- **Users**: Contains information about library users, such as `user_id`, `user_name`, and `contact_number`.
- **Borrowings**: Tracks book borrowings by users, with columns for `borrowing_id`, `book_id`, `user_id`, `borrowing_date`, and `return_date`.
- **Reservations**: Stores book reservations, including `reservation_id`, `book_id`, `user_id`, and `reservation_date`.

## Requirements

- Python 3.x
- SQLite (SQLite3 module is included in Python by default)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   ```

2.	Navigate to the project directory:
    ```bash
    cd library-management-system
    ```

## Usage
1.	Make sure your SQLite database (library_database.db) is set up with the required schema. You can use the provided setuptable.sql and insertdata.sql files to create and populate the database.

2.	Run the program:
    ```bash
    python ./src/main.py
    ```

3.	The terminal interface will appear with the following options  

    •	Type 1 to view books and their details.  
	•	Type 2 to borrow a book.  
	•	Type 3 to return a book.  
	•	Type 4 to reserve a book.  
	•	Type 5 to view authors.  
	•	Type 6 to exit the program.

## Code Structure

    • main.py: The main Python script that handles user interactions and database operations.

	• setuptable.sql: SQL script to create the necessary tables in the SQLite database.

	•insertdata.sql: SQL script to insert sample data into the database.


#### Feel free to edit it according to your needs and project specifics.