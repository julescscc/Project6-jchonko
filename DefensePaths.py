import math, random
from panda3d.core import *

def Cloud(radius = 1):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1

    unitVec = Vec3(x, y, z)
    unitVec.normalize()

    return unitVec * radius

def BaseballSeams(step, numSeams, B, F = 1):
    time = step / float(numSeams) * 2 * math.pi
    
    F4 = 0

    R = 1

    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.sin(time) + B * math.sin(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)

    rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)

    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr

    return Vec3(x, y, z)

def XYplane(step, num, radius = 50.0):

    theta = step / float(num) * 2 * math.pi

    xy = radius * math.cos(theta), radius * math.sin(theta), 0.0 * math.tan(theta)

    return Vec3(xy)

def XZplane(step, num, radius = 50.0):

    theta = step / float(num) * 2 * math.pi

    xz = radius * math.cos(theta), 0.0 * math.sin(theta), radius * math.tan(theta)

    return Vec3(xz)

def YZplane(step, num, radius = 50.0):

    theta = step / float(num) * 4 * math.pi
    
    yz = 0.0 * math.cos(theta), radius * math.sin(0.5 * theta), radius * math.tan(theta)
    
    return Vec3(yz)