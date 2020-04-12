from src.models.city import City
from math import sqrt
from typing import List
import string
import random
from random import randrange


def distance(city1: City, city2: City) -> float:
    a = (city1.x - city2.x)**2
    b = (city1.y - city2.y)**2
    return sqrt(a+b)


def path_distance(cities: List[City]) -> float:
    distances = []
    for i, j in zip(cities, cities[1:]):
        distances.append(distance(i, j))
    total_distance = sum(distances)
    return total_distance


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def generate_cities(n: int) -> List[City]:
    cities = [
        City(random_generator(), randrange(100), randrange(100))
        for i in range(n)
    ]
    return cities





