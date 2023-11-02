from typing import Optional
from pydantic import BaseModel, Field

# Regex CEP e NUMERO
REGEX_ZIP_CODE = r'^[0-9]{5}\-?[0-9]{3}$'
REGEX_ADDRESS_NUMBER = r'^[0-9]{0,14}$'

# Modelo de criação para address


class Address(BaseModel):
    zip_code: str = Field(pattern=REGEX_ZIP_CODE)
    street_name: str
    state_user: str
    city: str
    neighborhood: str
    address_number: str = Field(pattern=REGEX_ADDRESS_NUMBER)
    complement: Optional[str] = Field(None)

# Modelo de update para address


class AddressUpdate(BaseModel):
    zip_code: Optional[str] = Field(None, pattern=REGEX_ZIP_CODE)
    street_name: Optional[str] = Field(None)
    state_user: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    neighborhood: Optional[str] = Field(None)
    address_number: Optional[str] = Field(None, pattern=REGEX_ADDRESS_NUMBER)
    complements: Optional[str] = Field(None)
