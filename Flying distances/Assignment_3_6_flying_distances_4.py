def cities ():
    city1 = ('Amsterdam', (52, 22, 'N'), (4, 32, 'E'))
    city2 = ('Auckland', (36, 52, 'S'), (174, 45, 'E'))
    city3 = ('Montreal', (45, 30, 'N'), (73, 35, 'W'))
    cities = {city1[0]: city1, city2[0]: city2, city3[0]: city3}
    return cities
print(cities())
