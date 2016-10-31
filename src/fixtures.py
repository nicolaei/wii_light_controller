class _Fixture(object):
    def __init__(self, start_address, end_address):
        self.start_address = start_address
        self.data = [i for i in range(end_address - start_address)]


class PixelBar(_Fixture):
    """
    3 Channel mode:
        1: R
        2: G
        3: B
    """
    def set_red(self, value):
        self.data[0] = value

    def set_green(self, value):
        self.data[1] = value

    def set_blue(self, value):
        self.data[2] = value
