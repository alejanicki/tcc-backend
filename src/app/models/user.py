from pydantic import BaseModel, Field, EmailStr

#Regex CPF
REGEX_CPF=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$'
REGEX_BDATE=r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$'

class User(BaseModel):
    first_name: str
    last_name: str
    cpf: str = Field(pattern=REGEX_CPF)
    birth_date: str = Field(pattern=REGEX_BDATE)
    email: EmailStr
    credit: float
    password: str
    terms_conds: bool
    share_data: bool