from models.user_models import UserUpdate
from dao.dao import connect_database
from parameters import HOST, PORT, USER, PASSWORD, DATABASE


def select_all_user():
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


# Adiciona uma nova linha a tabela user
async def create_new_user(first_name: str, last_name: str, email: str, password_user: str, terms_conds: bool, share_data: bool):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    name = f'{first_name}" "{last_name}'

    create_user = f'INSERT INTO user (name_user, email, password_user, terms_conditions, share_data) VALUES ("{
        name}", "{email}", "{password_user}", {terms_conds}, {share_data})'

    cursor.execute(create_user)

    connection.commit()
    cursor.close()
    connection.close()

    return {'message': 'User created successfully'}


def update_user(id_user: int, user: UserUpdate):
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

    query = f"SELECT id_address FROM user WHERE id = {id_user}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result


# Verifica cpf
async def verify_data_overwrite(cpf: str, email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM user WHERE cpf = '{cpf}';"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM user WHERE email= '{email}'"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()

    return bool(result_cpf), bool(result_email)


# Verifica email
async def verify_email(email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT email FROM user WHERE email = '{email}';"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None