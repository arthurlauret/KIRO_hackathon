from math import *
def distanceM(point1, point2):
    return abs(point1[0]-point2[0])+ abs(point1[1]-point2[1])

def distanceE(point1, point2):
    return sqrt((point1[0]-point2[0])**2+ (point1[1]-point2[1])**2)

