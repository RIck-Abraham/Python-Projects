import sqlite3
from sqlite3 import Error

# Creates connection to sqlite in-memory database
def create_connection():
    """ 
    Create a connection to in-memory database
    :return: Connection object
    """
   
    # YOUR CODE HERE
    # Use sqlite3.connect(":memory:") to create connection object
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


return conn


# Creates Horse table
def create_table(conn):
    """ 
    Create Horse table
    :param conn: Connection object
    :return: Nothing
    """
    
    # YOUR CODE HERE    
    try:
        CREATE Table Horse (
            Id integer PRIMARY KEY, NOT NULL
            Name text,
            Breed text,
            Height double,
            BirthDate text,
        );
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
   
   
# Inserts row to Horse table given data tuple 
def insert_horse(conn, data):
    """
    Create a new row in Horse table
    :param conn: Connection object
    :param data: tuple of values for new row
    :return: Nothing
    """
    
    # YOUR CODE HERE
    # Use the ? character as placeholder for SQLite query parameters
    sql = INSERT INTO Horse(Id, Name, Breed, Height, BirthDate)
              VALUES(?,?,?,?,?,?)

    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


# Selects and prints all rows of Horse table
def select_all_horses(conn):
    """
    Query all rows in the Horse table
    :param conn: the Connection object
    :return: Nothing
    """
  
    # YOUR CODE HERE
    cur = conn.cursor()
    cur.execute("SELECT * FROM Horse")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

    
# DO NOT MODIFY main
if __name__ == '__main__':

    # Create connection to sqlite in-memroy database
    conn = create_connection()
    if conn is None:
        print("Error! cannot create the database connection.")

    # Create Horse table
    create_table(conn)
    
    # Insert row to Horse table
    horse_data = (1, "Babe", "Quarter Horse", 15.3, "2015-02-10")
    insert_horse(conn, horse_data)

    # Select and print all Horse table rows
    print("All horses:")
    select_all_horses(conn)
