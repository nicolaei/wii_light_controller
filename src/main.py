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

    color_range = math.pi / 3
    red = max(0, math.cos(roll * color_range))
    green = max(0, math.sin(roll * color_range))
    blue = max(0, -math.cos(roll * color_range))

    # print "Colors: %.2f %.2f %.2f" % (red, green, blue)

    return red, green, blue


def get_dim():
    """
    :return: Dimming modifier between 0 and 1
    """
    return 1 - max(wiimote.get_pitch() / (math.pi / 2), 0)


def main_loop():
    selected_light = None

    # Yaw controls which light is being controlled
    for light in lights:
        # TODO: Select light with yaw
        selected_light = lights[0]

    # Get colors based on controller roll
    colors = get_colors()
    # Get dim modifier based on controller pitch
    dim_modifier = get_dim()

    selected_light.set_intensity([int(color * dim_modifier * 255) for color in colors])


if __name__ == '__main__':
    wiimote = Wiimote()

    # tmp for testing
    lights = [LED(1, 4)]

    while True:
        main_loop()
        # Debug info
        print "Red: %3d Green: %3d Blue: %3d" % (lights[0].data[0], lights[0].data[1], lights[0].data[2])

    wiimote.close()

