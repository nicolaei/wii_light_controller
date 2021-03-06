import math
import cwiid


class Wiimote:
    _wiimote = None

    def __init__(self):
        self._connect()
        self._init_mote()

    def _connect(self):
        while not self._wiimote:
            try:
                self._wiimote = cwiid.Wiimote()
            except RuntimeError:
                print "Error while connecting, trying again"

        print "Connected"

    def _init_mote(self):
        rpt_mode = 0
        rpt_mode ^= cwiid.RPT_ACC  # Turn on accelerometer
        rpt_mode ^= cwiid.RPT_BTN  # Turn on buttons
        rpt_mode ^= cwiid.RPT_IR   # Turn on the IR sensor

        self._wiimote.rpt_mode = rpt_mode

    def close(self):
        self._wiimote.close()

    def get_buttons(self):
        return self._wiimote.state['buttons']

    def is_a_pressed(self):
        return self.get_buttons() == cwiid.BTN_A

    def get_accelerometer(self):
        # cwiid returns an 8-bit value for the accelometer
        zero = 128
        scale = 255

        return (
            float(self._wiimote.state['acc'][cwiid.X] - zero) / scale,
            float(self._wiimote.state['acc'][cwiid.Y] - zero) / scale,
            float(self._wiimote.state['acc'][cwiid.Z] - zero) / scale,
        )

    def get_pos(self):
        """
        Returns value of the first sensor
        :return: X, Y coordinates relative to IR transmitter
        """
        source = self._wiimote.state['ir_src'][0]

        if source:
            return source['pos']
        return None

    def get_roll(self):
        """
        :return: roll in radians
        """
        x, y, z = self.get_accelerometer()

        try:
            roll = math.atan(x / z)
            if z <= 0:
                roll += math.pi * (1 if x > 0 else -1)

            return roll
        except ZeroDivisionError:
            return 0

    def get_pitch(self):
        """
        :return: pitch with max of +- pi / 2
        """
        x, y, z = self.get_accelerometer()
        roll = self.get_roll()

        try:
            pitch = math.atan(y / z * math.cos(roll))
            return pitch
        except ZeroDivisionError:
            return 0

    def get_acceleration(self):
        x, y, z = self.get_accelerometer()
        return math.sqrt(x ** 2 + y ** 2 + z ** 2)
