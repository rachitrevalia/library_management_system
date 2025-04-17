import sqlite3

con = sqlite3.connect('./data/library_database.db')
cursor = con.cursor()

def display_books(book):
    print(f"'{book[0]}' is the ID for the book")
    print(f"'{book[1]}' is the title of the book having '{book[2]}' genre.")
    print(f"Authors: {book[3]}")
    print(f"Published in: '{book[4]}'\n")

def display_authors(author):
    print(f"Author ID: {author[0]}")
    print(f"Name: {author[1]}")
    print(f"Nationality: {author[2]}")
    print(f"Birth Date: {author[3]}")
    print(f"Death Date: {author[4]}\n")

def borrow_book(user_id, book_id, user_name, contact_number):
    try:
        # Check if user already exists
        cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO Users (user_id, user_name, contact_number) VALUES (?, ?, ?)",
                           (user_id, user_name, contact_number))
        
        cursor.execute("INSERT INTO Borrowings (user_id, book_id, borrowing_date) VALUES (?, ?, date('now'))",
                       (user_id, book_id))

        con.commit()
        print("Thanks for borrowing the book. Don't forget to return it on time!")
    except sqlite3.Error as e:
        print("Error:", e)

def return_book(user_id, book_id):
    try:
        cursor.execute("DELETE FROM Borrowings WHERE user_id = ? AND book_id = ?", (user_id, book_id))
        con.commit()
        print("Thanks for returning the book. Come again!")
    except sqlite3.Error as e:
        print(e)

def reserve_book(user_id, book_id):
    try:
        cursor.execute("INSERT INTO Reservations (user_id, book_id, reservation_date) VALUES (?, ?, date('now'))",
                       (user_id, book_id))
        con.commit()
        print("Book reserved successfully.")
    except sqlite3.Error as e:
        print(e)

def main():
    while True:
        print("\n ************ Welcome To The Library ************ \n")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Reserve Book")
        print("5. View Authors")
        print("6. Exit")

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            cursor.execute("""
                SELECT b.book_id, b.title, b.genre, GROUP_CONCAT(a.name, ', '), b.publication_year
                FROM Books b
                JOIN BookAuthors ba ON b.book_id = ba.book_id
                JOIN Authors a ON a.author_id = ba.author_id
                GROUP BY b.book_id
            """)
            books = cursor.fetchall()
            for book in books:
                display_books(book)
        elif choice == "2":
            user_id = int(input("Your ID: "))
            book_id = int(input("Book ID: "))
            user_name = input("Your Name: ")
            contact_number = input("Contact Number: ")
            borrow_book(user_id, book_id, user_name, contact_number)
        elif choice == "3":
            user_id = int(input("Your ID: "))
            book_id = int(input("Book ID: "))
            return_book(user_id, book_id)
        elif choice == "4":
            user_id = int(input("Your ID: "))
            book_id = int(input("Book ID: "))
            reserve_book(user_id, book_id)
        elif choice == "5":
            cursor.execute("SELECT * FROM Authors")
            authors = cursor.fetchall()
            for author in authors:
                display_authors(author)
        elif choice == "6":
            print("Thanks for coming! Visit Again!")
            break
        else:
            print("Invalid Choice. Try Again!")

    con.close()

if __name__ == "__main__":
    main()
