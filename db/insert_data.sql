-- Insert authors
INSERT INTO Authors (author_id, name, nationality, birth_date, death_date) 
VALUES
    (101, 'Harper Lee', 'American', '1926-04-28', '2016-02-19'),
    (102, 'George Orwell', 'British', '1903-06-25', '1950-01-21'),
    (103, 'Jane Austen', 'British', '1775-12-16', '1817-07-18'),
    (104, 'F. Scott Fitzgerald', 'American', '1896-09-24', '1940-12-21'),
    (105, 'J.K. Rowling', 'British', '1965-07-31', NULL),
    (106, 'J.D. Salinger', 'American', '1919-01-01', '2010-01-27'),
    (107, 'J.R.R. Tolkien', 'British', '1892-01-03', '1973-09-02'),
    (108, 'Virginia Woolf', 'British', '1882-01-25', '1941-03-28'),
    (109, 'Mark Twain', 'American', '1835-11-30', '1910-04-21'),
    (110, 'Gabriel Garcia Marquez', 'Colombian', '1927-03-06', '2014-04-17');

-- Insert books (author_id removed)
INSERT INTO Books (book_id, title, genre, publication_year) 
VALUES
    (1, 'To Kill a Mockingbird', 'Fiction', 1960),
    (2, '1984', 'Dystopian', 1949),
    (3, 'Pride and Prejudice', 'Romance', 1813),
    (4, 'The Great Gatsby', 'Fiction', 1925),
    (5, 'Harry Potter and the Sorcerer''s Stone', 'Fantasy', 1997),
    (6, 'The Catcher in the Rye', 'Coming-of-age', 1951),
    (7, 'Lord of the Rings', 'Fantasy', 1954),
    (8, 'To the Lighthouse', 'Modernism', 1927),
    (9, 'The Adventures of Huckleberry Finn', 'Adventure', 1884),
    (10, 'One Hundred Years of Solitude', 'Magical realism', 1967);

-- Insert book-author relationships (for BookAuthors table)
INSERT INTO BookAuthors (book_id, author_id)
VALUES
    (1, 101),
    (2, 102),
    (3, 103),
    (4, 104),
    (5, 105),
    (6, 106),
    (7, 107),
    (8, 108),
    (9, 109),
    (10, 110);

-- Insert users
INSERT INTO Users (user_id, user_name, contact_number)
VALUES 
    (1001, 'Sophia Martinez', '9765745353'),
    (1002, 'Benjamin Johnson', '9287745564'),
    (1003, 'Isabella Thompson', '8796654363'),
    (1004, 'Liam Rodriguez', '7593519549'),
    (1005, 'Olivia Williams', '8765903440');

-- Insert borrowings
INSERT INTO Borrowings (borrowing_id, book_id, user_id, borrowing_date, return_date)
VALUES 
    (77, 10, 1001, '2024-02-23', NULL),
    (78, 6, 1003, '2024-02-22', NULL),
    (79, 4, 1005, '2024-02-21', NULL),
    (91, 1, 1002, '2024-01-31', NULL),
    (92, 2, 1004, '2024-02-02', NULL);

-- Insert reservations
INSERT INTO Reservations (reservation_id, book_id, user_id, reservation_date)
VALUES 
    (5334, 3, 1001, '2024-02-29'),
    (5443, 8, 1004, '2024-03-03');