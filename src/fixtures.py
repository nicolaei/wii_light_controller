class _Fixture(object):
    def __init__(self, start_address, end_address):
        self.start_address = start_address
        self.data = [i for i in range(end_address - start_address)]

    def set_intensity(self, values):
        return


class LED(_Fixture):
    """
    3 Channel mode:
        1: R
        2: G
        3: B
    """

    def set_intensity(self, values):
        self.data = values
