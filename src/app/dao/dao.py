import mysql.connector


def connect_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
    )
    cursor = connection.cursor(dictionary=True)

    return connection, cursor
