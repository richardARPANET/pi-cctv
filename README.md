pi-cctv
=======

![raspberry-pi-with-camera-module](https://i.imgur.com/zbGtq9j.jpg)

pi-cctv is a script for use with your raspberry pi and raspberry pi camera module.
When ran it will continually take image captures with the camera module (placing them in an 'images' folder). Images which appear to be at night time will be disgarded to save on disk space.


### Installation

    git clone https://github.com/richardasaurus/pi-cctv.git
    cd ./pi-cctv
    pip install -r requirements.txt

### Example Usage

    python capture.py