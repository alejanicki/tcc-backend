from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Regex CPF
REGEX_CPF = r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$'
REGEX_BDATE = r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$'
REGEX_CELLPHONE = r'^\+?[0-9]{2}\s?\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$'

# Modelo de criação para usuários


class User(BaseModel):
    address_user: str
    first_name: str
    last_name: str
    birth_date: str = Field(pattern=REGEX_BDATE)
    cpf: str = Field(pattern=REGEX_CPF)
    cellphone: str = Field(pattern=REGEX_CELLPHONE)
    email: EmailStr
    password_user: str
    credit: float
    terms_conds: bool
    share_data: bool

# Modelo de update para usuários


class UserUpdate(BaseModel):
    address_user: Optional[str] = Field(None)
    birth_date: Optional[str] = Field(None, pattern=REGEX_BDATE)
    cpf: Optional[str] = Field(None, pattern=REGEX_CPF)
    cellphone: Optional[str] = Field(None, pattern=REGEX_CELLPHONE)
    email: Optional[EmailStr] = None
    password_user: Optional[str] = Field(None)
