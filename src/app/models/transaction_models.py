from pydantic import BaseModel
from datetime import date

class Transaction(BaseModel):
    id: int
    date_transaction: date
    id_user: int
    earn: int
    id_battery: int
    number_of_batteries: int
