#!/usr/bin/env python2
import time

import cwiid
from wiimote import Wiimote

def main_loop():
    pass

if __name__ == '__main__':
    wiimote = Wiimote()

    while True:
        acc = wiimote.get_accelerometer()
        roll = wiimote.get_roll()
        pitch = wiimote.get_pitch()
        acceleration = wiimote.get_acceleration()

        print "X: %.3f Y: %.3f Z: %.3f\tRoll: %.2f Pitch: %.2f Acc: %.2f" % (acc[cwiid.X], acc[cwiid.Y], acc[cwiid.Z], roll, pitch, acceleration)
        time.sleep(0.1)

    wiimote.close()

