# READ ME SECTION

# DESCRIPTION
#This python program uses the Haversine formula to calculate the great-circle distance between two points - that is, the shortest distance over the Earth's surface - giving an "as-the-crow-flies" distance between the points (ignoring any elevations or obsticals). The Haversine formula accounts for the Earth's curvature to calculate the shortest distance between two points on the surface of a sphere.
#We chose to calculate the distance between Amsterdam and Montreal

# PARAMETERS
#The 'distance' function takes the following parameters:
#- 'lat1_sing','lat1_deg','lat1_min': The sign (1 for N/-1 for S), degrees, and minutes of the latitude for the first location.
#- 'long1_sing', 'long1_deg','long1_min': The sign (1 for E/-1 for W), degrees, and minutes of the longitude for the first location.
#- 'lat2_sing','lat2_deg,'lat2_min': The sign (1 for N/-1 for S), degrees, and minutes of the latitude for the second location.
#- 'long2_sing','long2_deg','long2_min': The sign (1 for E/-1 for W), degrees, and minutes of the longitude for the second location.

# LIMITATIONS
#- The program does not account for the elevation of the locations.
#- The program does noot account for the Earth's oblateness.
#- The program does not check the user input for valid latitude and longitude values.

# STRUCTURES
#The program consists of three main functions:
#- 'convert_to_radians': Converts degrees and minutes to radians.
#- 'haversine': Calculates the haversine distance between two points in radians.
#- 'distance': Converts latitudes and longitudes to radians and calculates the distance between the two points in kilometers.
#- Note, that the user only interacts with the 'distance' function. The other two functions are helper functions and are not called directly by the user, but by the 'distance' function.

# OUTPUT
#The program prints the calculated distances between the pairs of locations. The distances are in kilometers.



#Import module math
import math

def haversine(lat1, lon1, lat2, lon2):

#Calculating the distance
    dlat = lat2 - lat1
    dlon = lon2 - lon1

# Haversine formula
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    b = 1 - a
    d = 2 * math.atan2(math.sqrt(a), math.sqrt(b))
    return d

#Transform degree to radians
def radians (sign, deg, min):
    deg_min = deg + min/60
    radians = (deg_min/180)*math.pi*sign
    return radians

#Import the other formulas and calculate distance
def distance(lat1_sing, lat1_deg,lat1_min,long1_sing, long1_deg,long1_min, lat2_sing,lat2_deg, lat2_min,long2_sing,long2_deg,long2_min):
    long1=radians(long1_sing, long1_deg,long1_min) #Lon N
    long2=radians(long2_sing, long2_deg,long2_min)  #
    lat1=radians(lat1_sing, lat1_deg, lat1_min) #lat E
    lat2=radians(lat2_sing,lat2_deg,lat2_min)
    distance=haversine(lat1,long1,lat2,long2)*6367
    return(distance)

if __name__ == '__main__':
    #Print Distance between Amsterdam and Montreal
    print(distance(1,52,22, 1,4,32,1, 45, 30, -1, 73, 35))

