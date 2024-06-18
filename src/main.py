import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('./data/library_database.db')
cursor = con.cursor()

# Function to display book details
def display_books(book):
    """Display Book Details"""
    print("'", book[0], "'", "is the ID for the book")
    print("'", book[1], "'", "is the title of the book having", "'", book[3], "'", "genre.")
    print("'", book[2], "'", "wrote this book in ", "'", book[4], "'")
    print("\n")

# Function to display author details
def display_authors(author):
    """Display Author Details"""
    print(f"Author ID: {author[0]}")
    print(f"Name: {author[1]}")
    print(f"Nationality: {author[2]}")
    print(f"Birth Date: {author[3]}")
    print(f"Death Date: {author[4]}")
    print("\n")

# Function to borrow a book
def borrow_book(user_id, book_id, user_name, contact_number):
    """Borrow a book"""
    try:
        # Insert borrowing details into the Borrowings table
        cursor.execute("""
            INSERT INTO Borrowings (user_id, book_id, borrowing_date)
            VALUES (?, ?, date('now'))
        """, (user_id, book_id))  

        # Insert user details into the Users table
        cursor.execute("""
            INSERT INTO Users (user_id, user_name, contact_number)
            VALUES (?, ?, ?)
        """, (user_id, user_name, contact_number)) 

        # Commit changes to the database
        con.commit()
        print("Thanks for borrowing the book. Don't forget to return it on time!")
    except sqlite3.Error as e:
        # Print error message if an error occurs
        print("Error:", e)

# Function to return a borrowed book
def return_book(user_id, book_id , user_name, contact_number):
    """Return a borrowed Book"""
    try:
        # Delete borrowing record from the Borrowings table
        cursor.execute("""
            DELETE FROM Borrowings
            WHERE user_id = ? AND book_id = ?
        """, (user_id, book_id))
        
        # Delete user record from the Users table
        cursor.execute("""
            DELETE FROM Users
            WHERE user_id = ? AND user_name = ? AND contact_number = ?
        """, (user_id, user_name, contact_number))
        
        # Commit changes to the database
        con.commit()
        print("Thanks for returning the book. Come again!")
    except sqlite3.Error as e:
        # Print error message if an error occurs
        print(e)

# Function to reserve a book
def reserve_book(user_id, book_id):
    """Reserve a Book"""
    try:
        # Insert reservation details into the Reservations table
        cursor.execute("""
            INSERT INTO Reservations (user_id, book_id, reservation_date)
            VALUES (?, ?, date('now'))
        """, (user_id, book_id))
        
        # Commit changes to the database
        con.commit()
        print("Book reserved successfully.")
    except sqlite3.Error as e:
        # Print error message if an error occurs
        print(e)

# Main function to handle user interaction
def main():
    while True:
        print("\n ************ Welcome To The Library ************ \n")
        print("> Type 1 To View Books and It's Details")
        print("> Type 2 to Borrow Books If You Like to Any Of Books You Viewed")
        print("> Have You Read The Book? Now, You can Type 3 to Return It.")
        print("> Type 4 to Reserve a Book for A Specific Date")
        print("> Type 5 To If You Want To know about all the Authors")
        print("> Type 6 TO Exit")

        # Get user choice
        choice = int(input("Enter Your Choice:"))

        if choice == 1:
            # View book details
            cursor.execute("""
                SELECT b.book_id, b.title, a.name, b.genre, b.publication_year
                FROM books b JOIN Authors a ON b.author_id = a.author_id
            """)
            books = cursor.fetchall()
            for book in books:
                display_books(book)
        elif choice == 2:
            # Borrow a book
            user_id = int(input("Enter Your ID:"))
            book_id = int(input("Enter ID of the Book You Want to Borrow:"))
            user_name = input("Enter Your Name:")
            contact_number = input("Enter Your 10 digit Contact Number:")
            borrow_book(user_id, book_id, user_name, contact_number)
        elif choice == 3:
            # Return a book
            user_id = int(input("Enter Your ID:"))
            book_id = int(input("Enter ID of the Book You Want to Return:"))
            user_name = input("Enter Your Name:")
            contact_number = input("Enter Your 10 digit Contact Number:")
            return_book(user_id, book_id, user_name, contact_number)
        elif choice == 4:
            # Reserve a book
            user_id = int(input("Enter Your ID:"))
            book_id = int(input("Enter ID of the Book You Want to Reserve:"))
            reserve_book(user_id, book_id)
        elif choice == 5:
            cursor.execute("SELECT * FROM Authors")
            authors = cursor.fetchall()
            for author in authors:
                display_authors(author)
        elif choice == 6:
            # Exit the program
            print("Thanks for coming! Visit Again!")
            break
        else:
            print("Invalid Choice. Try Again!")
    
    # Close the database connection
    con.close()

if __name__ == "__main__":
    main()
