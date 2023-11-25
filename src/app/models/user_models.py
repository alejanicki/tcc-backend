from dataclasses import field
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Regex CPF
REGEX_CPF = r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$'
REGEX_BDATE = r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$'
REGEX_CELLPHONE = r'^\+?[0-9]{2}\s?\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$'
REGEX_CEP=r'^[0-9]{5}\-?[0-9]{3}$'

# Modelo de criação para usuários


class User(BaseModel):
    name_user: str
    email: EmailStr
    password_user: str
    credit: float = 0.0
    terms_conditions: bool = False
    share_data: bool = False

# Modelo de update para usuários


class UserUpdate(BaseModel):
    address_user: Optional[str] = Field(None)
    name_user: Optional[str] = Field(None)
    date_birth: Optional[str] = Field(None, pattern=REGEX_BDATE)
    cpf: Optional[str] = Field(None, pattern=REGEX_CPF)
    cellphone: Optional[str] = Field(None, pattern=REGEX_CELLPHONE)
    email: Optional[EmailStr] = None
    password_user: Optional[str] = Field(None)
    cep: str = Field(pattern=REGEX_CEP)

