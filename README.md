pi-cctv
=======

![raspberry-pi-with-camera-module](https://i.imgur.com/zbGtq9j.jpg)

pi-cctv is a script for use with your raspberry pi and raspberry pi camera module.
When ran it will continually take image captures with the camera module (placing them in an 'images' folder). Images which appear to be at night time will be disgarded to save on disk space.

### Pre-installation tips

  If you're using Wifi you'll want to make the raspberry pi reconnect
  when it drops:

    cd /etc/ifplugd/action.d/
    mv ifupdown ifupdown.original
    cp /etc/wpa_supplicant/ifupdown.sh ./ifupdown
    sudo reboot

### Installation

    pip install picctv

### Example Usage

    picctv -o /media/ext1/