import array
from ola.ClientWrapper import ClientWrapper

UNIVERSE = 0
data = array.array('B', [0] * 512)

wrapper = ClientWrapper()
client = wrapper.Client()


def send_dmx():
    client.SendDmx(UNIVERSE, data, lambda state: wrapper.Stop())

    wrapper.Run()


def change_data(startAddress, new_data):
    for i in range(len(new_data)):
        data[startAddress + i] = int(new_data[i])
