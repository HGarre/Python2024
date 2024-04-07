from string_slicing import slice_better

#lat_1 = input('give the latitude of city 1 as sign (1 for east, -1 for west) degrees minutes seperated by spaces: ')
#long_1 = input('give the longitude of city 1 as sign (1 for north, -1 for south) degrees minutes seperated by spaces: ')
#lat_2 = input('give the latitude of city 2 as sign (1 for east, -1 for west) degrees minutes seperated by spaces: ')
#long_2 = input('give the longitude of city 2 as sign (1 for north, -1 for south) degrees minutes seperated by spaces: ')

def clean_numbers (num):
    if type(num) == str:
        out = ''
        for i in num:
            if i.isdigit():
                out += i
        result = out
    else:
        result = num
    return result

def convert_coordinates (lat_1, long_1, lat_2, long_2):
    if type(lat_1) == str and type(long_1) == str and type(lat_2) == str and type(long_2) == str:
        lat_1_list = slice_better(lat_1)
        long_1_list = slice_better(long_1)
        lat_2_list = slice_better(lat_2)
        long_2_list = slice_better(long_2)
    elif type(lat_1) == tuple and type(long_1) == tuple and type(lat_2) == tuple and type(long_2) == tuple:
        lat_1_list = list(lat_1)
        long_1_list = list(long_1)
        lat_2_list = list(lat_2)
        long_2_list = list(long_2)
    else:
        raise TypeError('Input must be sting or tuple')

    result = ''

    if len(lat_1_list) == 2:
        lat1_deg = clean_numbers(lat_1_list[0])
        lat1_min = 0
        if lat_1_list[1] == 'N' or lat_1_list[1] == 'E':
            lat1_sign = 1
        elif lat_1_list[1] == 'S' or lat_1_list[1] == 'W':
            lat1_sign = -1
        else:
            result = 'invalit input'
    elif len(lat_1_list) == 3:
        lat1_deg = clean_numbers(lat_1_list[0])
        lat1_min = clean_numbers(lat_1_list[1])
        if lat_1_list[2] == 'N' or lat_1_list[2] == 'E':
            lat1_sign = 1
        elif lat_1_list[2] == 'S' or lat_1_list[2] == 'W':
            lat1_sign = -1
        else:
            result = 'invalit input'
    else:
        result = 'invalit input'

    if len(long_1_list) == 2:
        long1_deg = clean_numbers(long_1_list[0])
        long1_min = 0
        if long_1_list[1] == 'N' or long_1_list[1] == 'E':
            long1_sign = 1
        elif long_1_list[1] == 'S' or long_1_list[1] == 'W':
            long1_sign = -1
        else:
            result = 'invalit input'
    elif len(long_1_list) == 3:
        long1_deg = clean_numbers(long_1_list[0])
        long1_min = clean_numbers(long_1_list[1])
        if long_1_list[2] == 'N' or long_1_list[2] == 'E':
            long1_sign = 1
        elif long_1_list[2] == 'S' or long_1_list[2] == 'W':
            long1_sign = -1
        else:
            result = 'invalit input'
    else:
        result = 'invalit input'

    if len(lat_2_list) == 2:
        lat2_deg = clean_numbers(lat_2_list[0])
        lat2_min = 0
        if lat_2_list[1] == 'N' or lat_2_list[1] == 'E':
            lat2_sign = 1
        elif lat_2_list[1] == 'S' or lat_2_list[1] == 'W':
            lat2_sign = -1
        else:
            result = 'invalit input'
    elif len(lat_2_list) == 3:
        lat2_deg = clean_numbers(lat_2_list[0])
        lat2_min = clean_numbers(lat_2_list[1])
        if lat_2_list[2] == 'N' or lat_2_list[2] == 'E':
            lat2_sign = 1
        elif lat_2_list[2] == 'S' or lat_2_list[2] == 'W':
            lat2_sign = -1
        else:
            result = 'invalit input'
    else:
        result = 'invalit input'

    if len(long_2_list) == 2:
        long2_deg = clean_numbers(long_2_list[0])
        long2_min = 0
        if long_2_list[1] == 'N' or long_2_list[1] == 'E':
            long2_sign = 1
        elif long_2_list[1] == 'S' or long_2_list[1] == 'W':
            long2_sign = -1
        else:
            result = 'invalit input'
    elif len(long_2_list) == 3:
        long2_deg = clean_numbers(long_2_list[0])
        long2_min = clean_numbers(long_2_list[1])
        if long_2_list[2] == 'N' or long_2_list[2] == 'E':
            long2_sign = 1
        elif long_2_list[2] == 'S' or long_2_list[2] == 'W':
            long2_sign = -1
        else:
            result = 'invalit input'
    else:
        result = 'invalit input'

    if result == '':
        result = {'lat1_sign': int(lat1_sign), 'lat1_deg': int(lat1_deg),'lat1_min': int(lat1_min),'long1_sign': int(long1_sign),'long1_deg': int(long1_deg),'long1_min': int(long1_min),'lat2_sign': int(lat2_sign),'lat2_deg': int(lat2_deg),'lat2_min': int(lat2_min),'long2_sign': int(long2_sign),'long2_deg': int(long2_deg),'long2_min': int(long2_min)}
    return result

if __name__ == '__main__':
    lat_1 = '1 1 E'
    long_1 = '1 1 N'
    lat_2 = '1 0 E'
    long_2 = '1° 2 N'
    print(convert_coordinates(lat_1, long_1, lat_2, long_2))

    lat_1_t = (1,1,'E')
    long_1_t = (1,1,'N')
    lat_2_t = (1,2,'E')
    long_2_t = (1, 2,'N')
    print(convert_coordinates(lat_1_t, long_1_t, lat_2_t, long_2_t))