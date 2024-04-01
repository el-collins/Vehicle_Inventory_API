from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints

class Vehicle(BaseModel):
    id: Annotated[int, Field(gt=0)]
    make: Annotated[str, StringConstraints(max_length=30)]
    model: Annotated[str, StringConstraints(max_length=30)]
    price: Annotated[float, Field(gt=0)]