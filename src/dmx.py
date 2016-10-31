import array

from ola.ClientWrapper import ClientWrapper

UNIVERSE = 1
data = array.array('B')


def send_dmx():
    wrapper = ClientWrapper()
    client = wrapper.Client()

    client.send(UNIVERSE, data, lambda state: wrapper.Stop())

    wrapper.Run()


def change_data(startAddress, data):
    for i in range(len(data)):
        data[startAddress + i] = data[i]
