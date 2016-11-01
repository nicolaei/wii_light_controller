#!/usr/bin/env python2
import time

import cwiid

import math

from fixtures import LED
from wiimote import Wiimote

lights = []


def get_colors():
    """
    :return: Color based on the controllers roll
    """
    roll = wiimote.get_roll()

    color_range = math.pi / 3.0
    offset = color_range / 2
    # sin(x * (pi/3) + (pi/3 * 2i)) + (pi/6)
    red = min(1.0, max(0.0, math.sin(roll * color_range) + offset))
    green = min(1.0, max(0.0, math.sin(roll * color_range + 2 * color_range) + offset))
    blue = min(1.0, max(0.0, math.sin(roll * color_range + 4 * color_range) + offset))

    print "Roll: %4.2f Colors: %.2f %.2f %.2f" % (roll, red, green, blue)

    return red, green, blue


def get_dim():
    """
    :return: Dimming modifier between 0 and 1
    """
    return 1 - max(wiimote.get_pitch() / (math.pi / 2), 0)


def set_color(values):
    light_range = 1000 / len(lights)  # The pos of the wii-mote is 0 to 1000
    falloff = 6

    try:
        x = wiimote.get_pos()[0]
    except TypeError:
        # The controller has no IR sensor
        x = 0
    light_index = 0

    for i in xrange(len(lights)):
        if x >= light_range * i and x < light_range * i + light_range:
            light_index = i

    #print "%d %4d" % (light_index, x)

    # Assign light value with falloff
    for i in xrange(falloff):
        if i is 0:
            lights[light_index].set_intensity([(value * 255) for value in values])
        else:
            lights[min(light_index + i, len(lights) - 1)].set_intensity([(value / i * 255) for value in values])
            lights[max(light_index - i, 0)].set_intensity([(value / i * 255) for value in values])


def main_loop():
    # Get colors based on controller roll
    colors = get_colors()
    # Get dim modifier based on controller pitch
    dim_modifier = get_dim()

    set_color([(color * dim_modifier) for color in colors])


if __name__ == '__main__':
    wiimote = Wiimote()

    print wiimote._wiimote.state
    # tmp for testing
    lights = [LED(1, 4), LED(1, 4), LED(1, 4), LED(1, 4), LED(1, 4), LED(1, 4), LED(1, 4), LED(1, 4)]

    while True:
        main_loop()
        # Debug info
        # print "Red: %3d Green: %3d Blue: %3d" % (lights[0].data[0], lights[0].data[1], lights[0].data[2])
        time.sleep(0.2)

    wiimote.close()

