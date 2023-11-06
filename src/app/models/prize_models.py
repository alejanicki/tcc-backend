from pydantic import BaseModel


class Prize(BaseModel):
    name_prize: str
    cost: float
    description_prize: str