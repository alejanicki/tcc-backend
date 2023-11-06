from pydantic import BaseModel
from datetime import date

class Deposit(BaseModel):
    date_deposit: date
    id_user: int
    earned_credit: float
    id_battery: int
    number_of_batteries: int
