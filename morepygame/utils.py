import math


def scr2phy(xy, surface):
    """Screen to physical coordinates conversion"""
    Y = surface.get_height()
    return xy[0], Y - xy[1]


def phy2scr(xy, surface):
    """Physical to screen coordinates conversion"""
    return scr2phy(xy, surface)


def rad2deg(rad):
    return 180 * rad / math.pi


def deg2rad(deg):
    return math.pi * deg / 180