from math import *
from pandas import *

rho = 6.371*10**6
def convertirLat(phi1, phi2):
    return rho*2*pi/360*(phi1-phi2)

def convertirLon(phi1, phi2):
    return rho*cos(2*pi*2.34842/360)*2*pi/360*(phi1-phi2)

def distanceM(point1, point2):
    return abs(convertirLon(point1[0], point2[0]))+ abs(convertirLat(point1[1], point2[1]))

def distanceE(point1, point2):
    return sqrt((convertirLon(point1[0], point2[0]))**2+ (convertirLat(point1[1], point2[1]))**2)

vehicules = read_csv("sujet/instances/vehicles.csv")
