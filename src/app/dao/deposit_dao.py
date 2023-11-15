from models.deposit_models import Deposit
from dao.dao import connect_database
from parameters import HOST, PORT, USER, PASSWORD, DATABASE


async def create_new_deposit(deposit: Deposit):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_deposit = "INSERT INTO deposit SET" + \
        ", ".join(f" {field} = '{1 if value is True else 0 if value is False else f'{value}'}'" for field, value in deposit)

    cursor.execute(create_deposit)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Deposit created successfully'}

async def select_all_deposit():
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = 'SELECT * FROM deposit'

    cursor.execute(query)
    deposit_list = cursor.fetchall()
    cursor.close()
    connection.close()

    return deposit_list

async def select_deposit_by_id(id_deposit: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'SELECT * FROM deposit WHERE id = {id_deposit}'

    cursor.execute(query)
    query_result = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_result

async def update_deposit(id_deposit: int, deposit: Deposit):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in deposit):
        update_deposit = f"UPDATE deposit SET" + \
            ", ".join(f" {field} = '{value}' " for field,
                      value in deposit if value is not None) + f"WHERE id = {id_deposit}"

        cursor.execute(update_deposit)
        connection.commit()

    cursor.close()
    connection.close()

    return {'message': 'Deposit uptaded successfully'}

async def delete_deposit_by_id(id_deposit: int):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'DELETE FROM user WHERE id={id_deposit}'

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Deposit deleted successfully'}