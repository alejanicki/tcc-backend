from models.battery_models import Battery
from dao.dao import connect_database
from parameters import HOST, PORT, USER, PASSWORD, DATABASE


async def create_new_battery(battery: Battery):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_battery = "INSERT INTO battery SET" + \
        ", ".join(f" {field} = '{value}'" for field, value in battery)

    cursor.execute(create_battery)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Battery created successfully'}


async def select_all_batteries():
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = 'SELECT * FROM battery'

    cursor.execute(query)
    battery_list = cursor.fetchall()
    cursor.close()
    connection.close()

    return battery_list


async def select_battery_by_id(id_battery: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'SELECT * FROM battery WHERE id = {id_battery}'

    cursor.execute(query)
    query_result = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_result


async def update_battery(id_battery: int, battery: Battery):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in battery):
        update_battery = f"UPDATE battery SET" + \
            ", ".join(f" {field} = '{value}' " for field,
                      value in battery if value is not None) + f"WHERE id = {id_battery}"

        cursor.execute(update_battery)
        connection.commit()

    cursor.close()
    connection.close()

    return {'message': 'Battery uptaded successfully'}


async def delete_battery_by_id(id_battery: int):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'DELETE FROM battery WHERE id={id_battery}'

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'Battery deleted successfully'}
