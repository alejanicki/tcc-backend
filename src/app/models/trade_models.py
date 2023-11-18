from datetime import date
from pydantic import BaseModel

class Trade(BaseModel):
    date_trade: date
    id_user: int
    id_prize: int
    cost_trade: int
