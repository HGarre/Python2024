from Group_work_1_complete import haversine, radians, distance
from Class_2_1_slice_better import slice_better

#lat_1 = input('give the latitude of city 1 as sign (1 for east, -1 for west) degrees minutes seperated by spaces: ')
#long_1 = input('give the longitude of city 1 as sign (1 for north, -1 for south) degrees minutes seperated by spaces: ')
#lat_2 = input('give the latitude of city 2 as sign (1 for east, -1 for west) degrees minutes seperated by spaces: ')
#long_2 = input('give the longitude of city 2 as sign (1 for north, -1 for south) degrees minutes seperated by spaces: ')

lat_1 = '1 E'
long_1 = '1 N'
lat_2 = '1 0 E'
long_2 = '1° N'

def clean_numbers (str):
    out = ''
    for i in str:
        if i.isdigit():
            out += i
    return out

lat_1_list = slice_better(lat_1)
if len(lat_1_list) == 2:
    lat1_deg = clean_numbers(lat_1_list[0])
    lat1_min = 0
    if lat_1_list[1] == 'N' or lat_1_list[1] == 'E':
        lat1_sign = 1
    elif lat_1_list[1] == 'S' or lat_1_list[1] == 'W':
        lat1_sign = -1
    else:
        print('invalit input')
elif len(lat_1_list) == 3:
    lat1_deg = clean_numbers(lat_1_list[0])
    lat1_min = clean_numbers(lat_1_list[1])
    if lat_1_list[2] == 'N' or lat_1_list[2] == 'E':
        lat1_sign = 1
    elif lat_1_list[2] == 'S' or lat_1_list[2] == 'W':
        lat1_sign = -1
    else:
        print('invalit input')
else:
    print('invalit input')


long_1_list = slice_better(long_1)
if len(long_1_list) == 2:
    long1_deg = clean_numbers(long_1_list[0])
    long1_min = 0
    if long_1_list[1] == 'N' or long_1_list[1] == 'E':
        long1_sign = 1
    elif long_1_list[1] == 'S' or long_1_list[1] == 'W':
        long1_sign = -1
    else:
        print('invalit input')
elif len(long_1_list) == 3:
    long1_deg = clean_numbers(long_1_list[0])
    long1_min = clean_numbers(long_1_list[1])
    if long_1_list[2] == 'N' or long_1_list[2] == 'E':
        long1_sign = 1
    elif long_1_list[2] == 'S' or long_1_list[2] == 'W':
        long1_sign = -1
    else:
        print('invalit input')
else:
    print('invalit input')


lat_2_list = slice_better(lat_2)
if len(lat_2_list) == 2:
    lat2_deg = clean_numbers(lat_2_list[0])
    lat2_min = 0
    if lat_2_list[1] == 'N' or lat_2_list[1] == 'E':
        lat2_sign = 1
    elif lat_2_list[1] == 'S' or lat_2_list[1] == 'W':
        lat2_sign = -1
    else:
        print('invalit input')
elif len(lat_2_list) == 3:
    lat2_deg = clean_numbers(lat_2_list[0])
    lat2_min = clean_numbers(lat_2_list[1])
    if lat_2_list[2] == 'N' or lat_2_list[2] == 'E':
        lat2_sign = 1
    elif lat_2_list[2] == 'S' or lat_2_list[2] == 'W':
        lat2_sign = -1
    else:
        print('invalit input')
else:
    print('invalit input')


long_2_list = slice_better(long_2)
if len(long_2_list) == 2:
    long2_deg = clean_numbers(long_2_list[0])
    long2_min = 0
    if long_2_list[1] == 'N' or long_2_list[1] == 'E':
        long2_sign = 1
    elif long_2_list[1] == 'S' or long_2_list[1] == 'W':
        long2_sign = -1
    else:
        print('invalit input')
elif len(long_2_list) == 3:
    long2_deg = clean_numbers(long_2_list[0])
    long2_min = clean_numbers(long_2_list[1])
    if long_2_list[2] == 'N' or long_2_list[2] == 'E':
        long2_sign = 1
    elif long_2_list[2] == 'S' or long_2_list[2] == 'W':
        long2_sign = -1
    else:
        print('invalit input')
else:
    print('invalit input')


print(distance(int(lat1_sign), int(lat1_deg),int(lat1_min),int(long1_sign), int(long1_deg),int(long1_min), int(lat2_sign),int(lat2_deg), int(lat2_min),int(long2_sign),int(long2_deg),int(long2_min)))