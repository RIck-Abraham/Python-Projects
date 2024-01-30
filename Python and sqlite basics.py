import sqlite3
from sqlite3 import Error

# NOTE: Do not modify
# Creates a sqlite3 database connection (in memory)
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        return conn
    except Error as e:
        print(e)

    return conn

# Creates a table
def create_table(conn, create_table_sql):
    # FIXME: Type your code here
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    #cursor.commit()
    
# Inserts horse data as a row in the database
def insert_horse(conn, data):
    # FIXME: Type your code here
    cursor = conn.cursor()
    cursor.execute(data)
    #cursor.commit()

# Prints all rows of data fromthe horses table
def select_all_horses(conn):
    # FIXME: Type your code here
    cursor = conn.cursor()
    fetch_SQL = ('SELECT * FROM Horses ')
    cursor.execute(fetch_SQL)
    
    print('All Horses:')
    for row in cursor.fetchall():
       print(row)

    
    fetch_sql = ('SELECT * FROM Horses')
    cursor = conn.cursor()
    cursor.execute(fetch_sql)
    #cursor.commit()
    cursor.close()


if __name__ == '__main__':
    database = r"HorseStable.db"

    # FIXME 1: Call the create_connection function to connect to the database HorseStable.db
    connect = create_connection(database)
    
    # FIXME 2: Create the sql statement string to create a table
    sql = ("CREATE TABLE Horses ("
        "id INTEGER PRIMARY KEY NOT NULL," 
        "Name TEXT," 
        "Breed TEXT,"
        "Height REAL,"
        "Birthday TEXT)")
    

    # FIXME 3: Call the create_table function passing the sql statement string
    create_table(connect, sql)

    # FIXME 4: Insert the horse data into the database
    insert_sql = ("INSERT INTO HORSES"
               "(id, name, breed, height, birthday)"
               "VALUES (1, 'Babe', 'Quarter Horse', 15.3, '2015-02-10')")
    insert_horse(connect, insert_sql)

    # FIXME 5: Print out all hourses by calling the select_all_horses function
    select_all_horses(connect)
