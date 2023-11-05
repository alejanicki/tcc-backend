from pydantic import BaseModel


class Prizes(BaseModel):
    prize_name: str
    cost: float
    description: str