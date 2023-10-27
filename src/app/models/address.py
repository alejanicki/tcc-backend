from typing import Optional
from pydantic import BaseModel, Field

#Regex CEP e NUMERO
REGEX_ZIP_CODE=r'^[0-9]{5}\-?[0-9]{3}$'
REGEX_ADDRESS_NUMBER=r'^[0-9]{0,14}$'

class Address(BaseModel):
    zip_code: str = Field(pattern=REGEX_ZIP_CODE)
    street_name: str
    state_user: str
    city: str
    neighborhood: str
    address_number: str = Field(pattern=REGEX_ADDRESS_NUMBER)
    complement: Optional[str] = Field(None)