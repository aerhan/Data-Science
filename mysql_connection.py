def connect_to_mysql(host, user, password, database):
    """
    Establishes a connection to a MySQL database.

    Parameters:
        host (str): The hostname where the MySQL server is running.
        user (str): The MySQL user to authenticate as.
        password (str): The password for the MySQL user.
        database (str): The name of the MySQL database to use.

    Returns:
        mysql.connector.connection.MySQLConnection: A MySQLConnection object representing the connection to the database.

    Example:
        connection = connect_to_mysql("localhost", "your_user_name", "your_password", "example_database")
        if connection:
            # Perform database operations using the connection
            connection.close()
    """
    import mysql.connector
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4"
        )
        if connection:
            print('Server Connection Successful')
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def query_this(connection, query):
    """
    Executes a SQL query on the provided MySQL connection and returns the result set.

    Parameters:
        connection (mysql.connector.connection.MySQLConnection): The MySQLConnection object representing the database connection.
        query (str): The SQL query to be executed.

    Returns:
        list: A list containing the rows of the result set. Each row is represented as a tuple.

    Example:
        connection = connect_to_mysql("localhost", "root", "your_password", "example_database")
        if connection:
            query_result = query_this(connection, "SELECT * FROM your_table")
            if query_result:
                print("Query Result:")
                for row in query_result:
                    print(row)

            # Don't forget to close the connection when done
            connection.close()
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
    except mysql.connector.Error as err:
        print(f"Error: {err}")
