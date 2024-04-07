# a function similar to the phonebook that allows te reader to ender cities
# to 'cities.txt', to delete them, to calculate the distance between two cities
# and to quit the program

from coordinate_conversion import clean_numbers, convert_coordinates
from calculation import haversine, radians, distance
from write_city_file import print_cities
from read_city_file import controller, delegate

import shelve
city_data = shelve.open('city_data')

def enter_city():
    city = input('What is the name of the city?\n')
    lat_deg = input('Degrees latitute:\n')
    lat_min = input('Minutes latitute: \n')
    lat_sign = input('South (S) or north (N)?\n')
    long_deg = input('Degrees longitute:\n')
    long_min = input('Minutes longitute: \n')
    long_sign = input('East (E) or west (W)?\n')
    lat_tup = (int(clean_numbers(lat_deg)), int(clean_numbers(lat_min)), lat_sign)
    long_tup = (int(clean_numbers(long_deg)), int(clean_numbers(long_min)), long_sign)
    tup = (city, lat_tup, long_tup)
    city_data[city] = tup
    print('Location'+city+'has been added to the memory')

def delete_city():
    city = input('Which city do want to delete?\n')
    if city in city_data:
        del city_data[city]
        print('Location '+city+' has been deleted from the memory')
    else:
        print('This city is not in the list')

def calculate_distance():
    loc1 = input('Provide the name of the first location:\n')
    loc2 = input('Provide the name of the second location:\n')
    if loc1 in city_data and loc2 in city_data:
        dic = convert_coordinates(city_data[loc1][1], city_data[loc1][2], city_data[loc2][1], city_data[loc2][2])
        dist = distance(dic['lat1_sign'], dic['lat1_deg'], dic['lat1_min'], dic['long1_sign'], dic['long1_deg'], dic['long1_min'], dic['lat2_sign'], dic['lat2_deg'], dic['lat2_min'], dic['long2_sign'], dic['long2_deg'], dic['long2_min'])
        print('The distance between '+loc1+' and '+loc2+' is '+str(round(dist, 2))+' km')
    else:
        print('At least one location is not in the memory')

def manage_coordinates():
    global city_data
    print('Welcome, this program is made to store coordinate data and calculate distances between locations')
    print('Please enter one of the action words:\nenter (to enter a new location)\ndelete(to delete a location)\ncalculate (to calculate the distance between two locations)\nprint (to print all cities to a text file)\nread (to read data from a text file in the same format)\nhelp (to see the list of action words again)\nexit(to quit the program)')
    action = input('please enter a valid action word\n')
    while action != 'exit':
        if action == 'help':
            print('Please enter one of the action words:\nenter (to enter a new location)\ndelete(to delete a location)\ncalculate (to calculate the distance between two locations)\nprint (to print all cities to a text file\nread (to read data from a text file in the same format)\nhelp (to see the list of action words again)\nexit(to quit the program)')
        elif action == 'enter':
            enter_city()
        elif action == 'delete':
            delete_city()
        elif action == 'calculate':
            calculate_distance()
        elif action == 'print':
            file = input('Enter a file name with valid extension\n')
            print_cities(file, city_data)
            print('The file '+ file + ' containig all cities in the memory was stored in your current directory')
        elif action == 'read':
            file = input('What name of the file you want to read from? \n')
            try:
                new = controller(file)
                city_data.update(new)
                print ('The data is in the memory, old data was overwritten')
            except:
                print ('The file is not readable. Are you sure its in the right directory and in the correct format (the same as files printed by this progamm)?')
        action = input('please enter a valid action word\n')
    print('Coordinate manager closed')

manage_coordinates()

city_data.close()