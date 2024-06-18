create table Books (
    book_id int PRIMARY KEY,
    title text not null ,
    author_id int not null ,
    genre text , 
    publication_year int,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

create table Authors (
    author_id int primary key ,
    name text not null ,
    nationality text,
    birth_date date,
    death_date date 
);

create table Users (
    user_id int PRIMARY KEY , 
    user_name text not null ,
    contact_number int 
);

create table Borrowings (
    borrowing_id int primary key,
    book_id int not null,
    user_id int not null,
    borrowing_data date not null,
    return_data date,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
)

create table Reservations (
    reservation_id int primary key,
    book_id int not null,
    user_id int not null,
    reservation_data date not null,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
)



