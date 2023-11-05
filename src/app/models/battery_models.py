from pydantic import BaseModel


class Battery(BaseModel):
    type_battery: str
