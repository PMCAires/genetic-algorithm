import matplotlib.pyplot as plt
from src.models.city import City

cities = [
    City('Porto', 13, 19),
    City('Braga', 10, 8),
    City('Guimarães', 1, 2),
    City('Felgueiras', 5,6)
]


def plot_2d(x, y, labels):
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()


def plot_cities(cities):
    xs = [city.x for city in cities]
    ys = [city.y for city in cities]
    ls = [city.name for city in cities]
    plot_2d(xs, ys, ls)

cities = [
    City('Porto', 13, 19),
    City('Braga', 10, 8),
    City('Guimarães', 1, 2),
    City('Felgueiras', 5, 6)
]

plot_cities(cities)