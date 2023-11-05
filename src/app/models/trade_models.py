from pydantic import BaseModel

class Trade(BaseModel):
    id: int
    date_trade: str
    id_user: int
    id_prize: int
