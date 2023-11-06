from models.trade_models import Trade
from dao.dao import connect_database
from parameters import HOST, PORT, USER, PASSWORD, DATABASE

async def create_new_trade(trade: Trade):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_trade = "INSERT INTO trade SET" + \
        ", ".join(f" {field} = '{value}'" for field, value in trade)

    cursor.execute(create_trade)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Trade created successfully'}

async def select_all_trades():
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = 'SELECT * FROM trade'

    cursor.execute(query)
    trade_list = cursor.fetchall()
    cursor.close()
    connection.close()

    return trade_list

async def select_trade_by_id(id_trade: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'SELECT * FROM trade WHERE id = {id_trade}'

    cursor.execute(query)
    query_result = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_result

async def update_trade(id_trade: int, trade: Trade):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in trade):
        update_trade = f"UPDATE trade SET" + \
            ", ".join(f" {field} = '{value}' " for field,
                      value in trade if value is not None) + f"WHERE id = {id_trade}"

        cursor.execute(update_trade)
        connection.commit()

    cursor.close()
    connection.close()

    return {'message': 'Trade uptaded successfully'}

async def delete_trade_by_id(id_trade: int):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'DELETE FROM trade WHERE id={id_trade}'

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'trade deleted successfully'}