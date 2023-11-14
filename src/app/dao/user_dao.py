from typing import Optional, Dict
from models.user_models import User, UserUpdate
from dao.dao import connect_database
from parameters import HOST, PORT, USER, PASSWORD, DATABASE

# Adiciona uma nova linha a tabela user


async def create_new_user(user: User):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_user = "INSERT INTO user SET" + \
        ", ".join(f" {field} = '{1 if value is True else 0 if value is False else f'{value}'}'" for field, value in user)

    cursor.execute(create_user)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'User created successfully'}


# Seleciona todos os usuarios


async def select_all_user():
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = 'SELECT * FROM user'

    cursor.execute(query)
    user_list = cursor.fetchall()
    cursor.close()
    connection.close()

    return user_list


# Seleciona usuario pelo id


async def select_user_by_id(user_id: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'SELECT * FROM user WHERE id = {user_id}'

    cursor.execute(query)
    query_result = cursor.fetchall()
    cursor.close()
    connection.close()

    return query_result


# Atualiza o usuario referenciado


async def update_user(id_user: int, user: UserUpdate):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in user):
        update_user = f"UPDATE user SET" + \
            ", ".join(f" {field} = '{value}' " for field,
                      value in user if value is not None) + f"WHERE id = {id_user}"

        cursor.execute(update_user)
        connection.commit()

    cursor.close()
    connection.close()

    return {'message': 'User uptaded successfully'}


# deletando usuario pelo id
async def delete_user_by_id(user_id: int):
    connection, cursor = connect_database(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f'DELETE FROM user WHERE id={user_id}'

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'User deleted successfully'}

# Verifica cpf


async def verify_data_cpf(cpf: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM user WHERE cpf = '{cpf}'"

    cursor.execute(query_cpf)
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    return result is not None


# Verifica email


async def verify_email(email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT email FROM user WHERE email = '{email}'"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None


# Verifica cpf execeto do usuário que terá o update


async def verify_data_users(id_user: int, cpf: str, email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM user WHERE cpf = '{cpf}' AND id <> {id_user}"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM user WHERE email = '{email}' AND id <> {id_user}"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()

    return bool(result_cpf), bool(result_email)


def verify_user_exists(email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT id AS id_user, password_user FROM user WHERE email = '{email}'"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    
    return result
