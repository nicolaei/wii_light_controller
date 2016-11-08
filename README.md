# Wii Light Controller
This is a python thingy created to show at expos for the University of Oslo.


## Setup
* Put an OLA image on a SD card
* Disable all plugins in `~pi/.ola` except `ola-uartdmx.conf`
* Install cwiid (see the dependencies section for relevant pacakges)
* Create an init script that runs `utils/set_output_mode.sh` on boot.


## Starting
* Start `olad` (Optionally with `-l 3` if you want debug info)
* Run `src/main.py <Amount of lights>`
* Press 1 and 2 on the wii-mote to connect.


## Dependencies
### Hardware
* Open Lighting Architecture supported DMX device
* Wii-mote
* Bluetooth dongle

### Software
* Python 2.7
* cwiid (`apt-get install libcwiid1 lswm wminput`)
* ola (open lighting architecture)


## Helpfull pages
Running stuff - http://www.raspberrypi-dmx.com/raspberry-pi-ola-dmx512-sender

Pre-compiled OLA Raspbian image - http://dl.openlighting.org/

Creating your own OLA Raspbian image - https://wiki.openlighting.org/index.php/Building_a_Custom_Raspbian_Image
