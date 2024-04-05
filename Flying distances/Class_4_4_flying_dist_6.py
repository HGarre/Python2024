def controller (file_name):
    dic = {}
    file = open(file_name, 'r')
    for line in file:
        tup = delegate(line)
        dic[tup[0]] = tup
    file.close()
    return dic

def delegate(line):
    liste = line.split()
    liste_short = (liste[1], liste[3], liste[5])
    lat = liste_short[1]
    lat = lat.split(chr(176))
    lat[1] = lat[1].split(chr(39))
    lat_tup = (int(lat[0]),int(lat[1][0]),lat[1][1])
    long = liste_short[2]
    long = long.split(chr(176))
    long[1] = long[1].split(chr(39))
    long_tup = (int(long[0]),int(long[1][0]),long[1][1])
    tup = (liste_short[0],lat_tup, long_tup)
    return tup

print(controller('cities.txt'))