#!/usr/bin/env python2
import math
import sys

from dmx import send_dmx, change_data
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

    return red, green, blue


def get_dim():
    """
    :return: Dimming modifier between 0 and 1
    """
    return 1 - max(wiimote.get_pitch() / (math.pi / 2), 0)


def set_color(values):
    light_range = 1024 / len(lights)  # The pos of the wii-mote is 0 to 1024
    falloff = 6

    try:
        x = wiimote.get_pos()[0]
    except TypeError:
        # The controller is not receiving an IR signal
        x = 0
    light_index = 0

    for i in xrange(len(lights)):
        if light_range * i <= x < light_range * i + light_range:
            light_index = i

    # Reset the lights
    for light in lights:
        light.set_intensity([0] * 3)

    # Assign light value with falloff
    for i in xrange(falloff):
        if i is 0:
            lights[light_index].set_intensity([(value * 255) for value in values])
        else:
            falloff_values = [(value / i * 255) for value in values]

            if light_index + i < len(lights):
                lights[light_index + i].set_intensity(falloff_values)
            elif light_index - i >= 0:
                lights[light_index - i].set_intensity(falloff_values)


def main_loop():
    # Get colors based on controller roll
    colors = get_colors()
    # Get dim modifier based on controller pitch
    dim_modifier = get_dim()

    set_color([(color * dim_modifier) for color in colors])

    # Snd data to dmx
    for light in lights:
        change_data(light.start_address, light.data)
    send_dmx()


def init_lights(amount):
    for i in xrange(amount):
        lights.append(LED(i * 4, i * 4 + 3))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: main.py <amount of lights>"
        sys.exit(1)

    wiimote = Wiimote()
    init_lights(int(sys.argv[1]))

    while True:
        main_loop()
