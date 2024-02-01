import sqlite3
from sqlite3 import Error

# Function to create a connection to the SQLite database in memory
def create_connection():
    conn = None
    try:
        # Attempt to connect to an in-memory SQLite database
        conn = sqlite3.connect(":memory:")
        return conn  # Return the connection object if successful
    except Error as e:
        print(e)  # Print any connection errors
    return None  # Return None if the connection was unsuccessful

# Function to create a Dog table in the database
def create_table(conn):
    # SQL statement to create a Dog table
    dogCreate = ('''CREATE TABLE Dog (
                        Id INTEGER PRIMARY KEY NOT NULL,
                        Name TEXT,
                        Breed TEXT,
                        Height REAL,
                        BirthDate TEXT)''')
    try:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(dogCreate)  # Execute the SQL statement to create the table
    except Error as e:
        print(e)  # Print any SQL execution errors

# Function to insert a new row into the Dog table
def insert_dog(conn, data):
    # SQL statement for inserting a new row into the Dog table
    dogQuery = ('''INSERT INTO Dog (Id, Name, Breed, Height, BirthDate)
                     VALUES (?, ?, ?, ?, ?)''')  # Use placeholders for data insertion
    try:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(dogQuery, data)  # Execute the SQL statement with the provided data
        conn.commit()  # Commit the changes to the database
    except Error as e:
        print(e)  # Print any SQL execution errors
    finally:
        cursor.close()  # Close the cursor

# Function to select and print all rows from the Dog table
def select_all_dogs(conn):
    try:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute("SELECT * FROM Dog")  # Execute the SQL statement to select all rows
        rows = cursor.fetchall()  # Fetch all rows from the query result
        for row in rows:
            print(row)  # Print each row
    except Error as e:
        print(e)  # Print any SQL execution errors
    finally:
        cursor.close()  # Close the cursor

# Main section of the script
if __name__ == '__main__':
    conn = create_connection()  # Create a database connection
    if conn:
        create_table(conn)  # Create the Dog table
        dog_data = (1, "Buddy", "Golden Retriever", 23.5, "2017-04-12")  # Define sample dog data
        insert_dog(conn, dog_data)  # Insert the sample dog data into the table
        print("All dogs:")  # Print a header for the output
        select_all_dogs(conn)  # Select and print all rows from the Dog table
        conn.close()  # Close the database connection
    else:
        print("Error! cannot create the database connection.")  # Print an error if the connection failed
