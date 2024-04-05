
from Group_work_1_complete import haversine, radians, distance
from Class_2_1_slice_better import slice_better

#lat_1 = input('give the latitude of city 1 as sign (1 for east, -1 for west) degrees minutes seperated by spaces: ')
#long_1 = input('give the longitude of city 1 as sign (1 for north, -1 for south) degrees minutes seperated by spaces: ')
#lat_2 = input('give the latitude of city 2 as sign (1 for east, -1 for west) degrees minutes seperated by spaces: ')
#long_2 = input('give the longitude of city 2 as sign (1 for north, -1 for south) degrees minutes seperated by spaces: ')

lat_1 = '1 1 1'
long_1 = '1 1 1'
lat_2 = '1 1 1'
long_2 = '1 1 1'

lat1_sing, lat1_deg, lat1_min = slice_better(lat_1)
long1_sing, long1_deg, long1_min = slice_better(long_1)
lat2_sing, lat2_deg, lat2_min = slice_better(lat_2)
long2_sing, long2_deg, long2_min = slice_better(long_2)

print(distance(int(lat1_sing), int(lat1_deg),int(lat1_min),int(long1_sing), int(long1_deg),int(long1_min), int(lat2_sing),int(lat2_deg), int(lat2_min),int(long2_sing),int(long2_deg),int(long2_min)))
