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

    create_user = "INSERT INTO deposit SET" + \
        ", ".join(f" {field} = '{1 if value is True else 0 if value is False else f'{
                  value}'}'" for field, value in deposit)

    cursor.execute(create_user)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Deposit created successfully'}