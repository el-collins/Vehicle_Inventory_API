from fastapi import FastAPI, HTTPException, Query
from typing import Annotated, List
from model import Vehicle

app = FastAPI()


inventory = [
    Vehicle(id=1, make="Toyota", model="Corolla", price=15000.00),
    Vehicle(id=2, make="Honda", model="Civic", price=17000.00),
    Vehicle(id=3, make="Ford", model="Fusion", price=20000.00),
]


@app.get("/vehicle/{vehicle_id}")
async def get_vehicle_by_id(vehicle_id: int):
    for vehicle in inventory:
        if vehicle.id == vehicle_id:
            return vehicle
    raise HTTPException(status_code=404, detail="Vehicle not found")


@app.get("/vehicles/", response_model=List[Vehicle], tags=["Vehicle"])
async def get_vehicles(
    make: Annotated[str | None, Query(max_length=30)] = None,
    model: Annotated[str | None, Query(max_length=30)] = None,
    min_price: Annotated[float | None, Query()] = None,
    max_price: Annotated[float | None, Query()] = None,
):
    result = inventory
    if make:
        result = [vehicle for vehicle in result if vehicle.make == make]
    if model:
        result = [vehicle for vehicle in result if vehicle.model == model]
    if min_price is not None:
        result = [vehicle for vehicle in result if vehicle.price >= min_price]
    if max_price is not None:
        result = [vehicle for vehicle in result if vehicle.price <= max_price]
    return result
