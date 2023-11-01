from pydantic import BaseModel

class Battery(BaseModel):
    id: int
    type_battery: str
