#READ ME

# Description
# - The function "cities" returns the geographic coordinates of Amsterdam, Auckland, and Montreal as a dictionary
# - The function "print-cities" prints the geocoordinates of cities supplied through a dictionary as returned by the
#   "cities" function into a text file of given name

#Parameters
# - The "cities" function does not take any parameters
# - The "print_cities" function takes two parameter:
#    - file-name: a string containing the name of the file (with suitable extension) that will be created
#    - city-data: a dictionary containing the name of the cities for which geodata will be printed as keys and tuples with geodata as values
#      Each tuple contains the name of a city, a tuple for the latitute (degrees, minutes, direction) and a tuple for the longitute

# Limitations
# - The "cities" function returns data only for the cities defined in the body (Amsterdam, Auckland, Montreal)
# - To the "print-cities" function, the data needs to be supplied in the above described format
# - No error is raised by the "print_cities" function if wrong values for the direction are entered (other that N, S, W, E)

# Structures
# - the "cities" function defines a dictionary without any special structures
# - the "print_cities functions uses a for loop to go through each city in the dictionary, extract the data from the tuple,
#   combine it into a string and print that sting to the data file

# Output
# - The "cities" function returns a dictionary containing the geodata of Amsterdam, Auckland and Montreal
# - The "print_cities" function creates a file into which the geodata is printed, it returns None

import shelve
city_data = shelve.open('city_data')

def cities ():
    city1 = ('Amsterdam', (52, 22, 'N'), (4, 32, 'E'))
    city2 = ('Auckland', (36, 52, 'S'), (174, 45, 'E'))
    city3 = ('Montreal', (45, 30, 'N'), (73, 35, 'W'))
    city_data['Amsterdam'] = city1
    city_data['Aukland'] = city2
    city_data['Montreal'] = city3


def print_cities(file_name, city_data):
    file = open(file_name, 'w')
    for k in city_data:
        name, lat, long = city_data[k]
        latitute = str(lat[0])+chr(176)+str(lat[1])+chr(39)+lat[2]
        longitute = str(long[0])+chr(176)+str(long[1])+chr(39)+long[2]
        file.write('Name: %-20s Latitute: %-10s Longitute: %-10s  \n' % (name, latitute, longitute))
    file.close()

#cities()
print_cities('cities.txt', city_data)

city_data.close()

