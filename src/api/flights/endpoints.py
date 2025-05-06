from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends, Header

from .query_params import FlightSearchParams

flights_router = APIRouter(
    prefix="/flights",
    tags=["flights"]
)

@flights_router.get("/")
def get_flights(params: FlightSearchParams = Depends(), header = Header()) -> JSONResponse:
    try:
        print("Here Header ->", header)
        print(params.from_city)
        print(params.to_city)
    except Exception as e:
        print(e)
        raise
