import itertools
from typing import List
from src.models.city import City
from src.ops.cities import path_distance, generate_cities
from typing import Tuple
from src.utils.plot import plot_cities


def travelling_salesman (cities:List[City]) -> Tuple[List[City], float]:
    paths = list(itertools.permutations(cities))
    path_distances = []
    for i in paths:
        path_distances.append(path_distance(i))

    optimal = path_distances.index(min(path_distances))

    return (paths[optimal], path_distances[optimal])

cities = [
    City('Porto', 13, 19),
    City('Braga', 10, 8),
    City('Guimarães', 1, 2),
    City('Felgueiras', 5,6),
    City('Caralhinho', 23, 23),
    City('Brasil', -4, -17)
]

cities = generate_cities(6)

result = travelling_salesman(cities)
print(result[0])
print(result[1])

plot_cities(cities)
