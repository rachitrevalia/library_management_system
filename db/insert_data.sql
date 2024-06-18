INSERT INTO Authors ( author_id, name, nationality, birth_date, death_date) 
VALUES
    ('101','Harper Lee', 'American', '1926-04-28', '2016-02-19'),
    ('102','George Orwell', 'British', '1903-06-25', '1950-01-21'),
    ('103','Jane Austen', 'British', '1775-12-16', '1817-07-18'),
    ('104','F. Scott Fitzgerald', 'American', '1896-09-24', '1940-12-21'),
    ('105','J.K. Rowling', 'British', '1965-07-31', NULL),
    ('106','J.D. Salinger', 'American', '1919-01-01', '2010-01-27'),
    ('107','J.R.R. Tolkien', 'British', '1892-01-03', '1973-09-02'),
    ('108','Virginia Woolf', 'British', '1882-01-25', '1941-03-28'),
    ('109','Mark Twain', 'American', '1835-11-30', '1910-04-21'),
    ('110','Gabriel Garcia Marquez', 'Colombian', '1927-03-06', '2014-04-17');

INSERT INTO Books ( book_id ,title, author_id, genre, publication_year) 
VALUES
    (01, 'To Kill a Mockingbird', '101' , 'Fiction', 1960),
    (02,'1984', '102', 'Dystopian', 1949),
    (03,'Pride and Prejudice', '103', 'Romance', 1813),
    (04,'The Great Gatsby', '104', 'Fiction', 1925),
    (05,'Harry Potter and the Sorcerer''s Stone', '105', 'Fantasy', 1997),
    (06,'The Catcher in the Rye', '106', 'Coming-of-age', 1951),
    (07,'Lord of the Rings', '107', 'Fantasy', 1954),
    (08,'To the Lighthouse', '108', 'Modernism', 1927),
    (09,'The Adventures of Huckleberry Finn', '109', 'Adventure', 1884),
    (010,'One Hundred Years of Solitude', '110', 'Magical realism', 1967);

INSERT INTO Users ( user_id , user_name, contact_number)
VALUES 
    (1001 , 'Sophia Martinez' , 9765745353),
    (1002 , 'Benjamin Johnson' , 9287745564),
    (1003 , 'Isabella Thompson' , 8796654363),
    (1004 , 'liam Rodriguez' , 7593519549),
    (1005 , 'Olivia Williams' , 8765903440);

INSERT INTO Borrowings ( borrowing_id ,book_id , user_id , borrowing_date , return_date)
VALUES 
    (77 , 010 , 1001 , '2024-02-23' , NULL),
    (78 , 06 , 1003 , '2024-02-22', NULL),
    (79 , 04 , 1005 , '2024-02-21', NULL),
    (91 , 01 , 1002 , '2024-01-31', NULL),
    (92 , 02 , 1004 , '2024-02-02', NULL);

INSERT INTO Reservations (reservation_id , book_id , user_id , reservation_date)
VALUES 
    (5334 , 03 , 1001 , '2024-02-29'),
    (5443 , 08 , 1004 , '2024-03-03');