import psycopg2
from psycopg2 import Error
def first():
    try:
        connection = psycopg2.connect(database = "flask_todo")
        cursor = connection.cursor()

        create_table_query = '''CREATE TABLE list
            (created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            item           TEXT    NOT NULL,
            done         BOOLEAN NOT NULL); '''
            cursor.execute(create_table_query)
            connection.commit()
            print("Table created successfully in PostgreSQL ")
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)
        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
