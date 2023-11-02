import requests
from passlib.context import CryptContext

LINK_API = "https://api-paises.pages.dev/paises.json"

crypt = CryptContext(schemes=['bcrypt'])

# Processar dados de usuário


async def user_data_processing(cpf: str, cellphone: str, email: str):
    if cpf is not None:
        cpf = cpf.replace('.', '').replace('-', '')
    if cellphone is not None:
        cellphone = cellphone.replace(
            '-', '').replace('(', '').replace(')', '').replace(' ', '').replace('+', '')
    if email is not None:
        email = email.lower().strip()
    return cpf, cellphone, email


# Formatar date de dicionário para formato YYYY-MM-DD


def format_date(date):
    return f"{date.year}-{date.month}-{date.day}"

# Validação de ddi


def consult_ddi(cellphone: str):
    ddi = cellphone.replace('+', '')[:2]
    list_ddi = []
    response = requests.get(LINK_API)
    for value in response.json().values():
        list_ddi.append(value['ddi'])

    if int(ddi) in list_ddi:
        return True
    else:
        return False


def get_pwd_hash(password):

    return crypt.hash(password)


def check_pwd_hash(password_hash, password):

    return crypt.verify(password, password_hash)
