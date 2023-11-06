from models.prize_models import Prize
from dao.dao import connect_database
from parameters import HOST, PORT, USER, PASSWORD, DATABASE

async def create_new_prize(prize: Prize):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_prize = "INSERT INTO prize SET" + \
        ", ".join(f" {field} = '{value}'" for field, value in prize)

    cursor.execute(create_prize)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Prize created successfully'}


async def select_all_prizes():
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = 'SELECT * FROM prize'

    cursor.execute(query)
    prize_list = cursor.fetchall()
    cursor.close()
    connection.close()

    return prize_list

async def select_prize_by_id(id_prize: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'SELECT * FROM prize WHERE id = {id_prize}'

    cursor.execute(query)
    query_result = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_result

async def update_prize(id_prize: int, prize: Prize):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in prize):
        update_prize = f"UPDATE prize SET" + \
            ", ".join(f" {field} = '{value}' " for field,
                      value in prize if value is not None) + f"WHERE id = {id_prize}"

        cursor.execute(update_prize)
        connection.commit()

    cursor.close()
    connection.close()

    return {'message': 'Prize uptaded successfully'}

async def delete_prize_by_id(id_prize: int):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'DELETE FROM prize WHERE id={id_prize}'

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'prize deleted successfully'}