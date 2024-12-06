import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2706",
            database="gallery"
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            
            cursor = connection.cursor()
            cursor.execute("SELECT artist FROM paintings")
            
            for (artist_name,) in cursor:
                print(artist_name)
                
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

connect_to_mysql()