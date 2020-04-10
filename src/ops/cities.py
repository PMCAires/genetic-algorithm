from src.models.city import City
from math import sqrt


def distance(city1: City, city2: City) -> float:
    a = (city1.x - city2.x)**2
    b = (city1.y - city2.y)**2
    return sqrt(a+b)
