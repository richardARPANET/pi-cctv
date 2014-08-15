#!/usr/bin/env python
"""picctv RaspberryPi CCTV Camera

Usage:
  picctv -o OUTPUT_DIR
  picctv --doctest
  picctv --version

Options:
  -h --help            show this help message and exit
  -o --output OUTPUT_DIR  specify output dir to save photographs
  --doctest            run doctest on this script
"""
import os
import time
from datetime import datetime

import docopt

from PIL import Image, ImageStat

import picamera
from picctv.utils import get_logger

os.environ['TZ'] = 'Europe/London'
time.tzset()

logger = get_logger(__name__)


def get_image_brightness(image_path):
    """
    Get the average brightness value of an Image
    :returns: Int, Image average brightness value
    """
    # Convert the Image to greyscale
    img = Image.open(image_path).convert('L')
    # Get the average pixel brightness
    stat = ImageStat.Stat(img)
    return stat.rms[0]


def lights_are_on(image_path):
    """
    Check if lights are switched on in a room.
    :returns: True if the room lights are on, else Fase
    """
    _brightness = get_image_brightness(image_path)
    if _brightness > 10:
        return True
    return False


def check_image_useful(image_path):
    """
    Check if the image is bright enough to be of use.
    Otherwise deletes it.
    """
    lights_on = lights_are_on(image_path)
    if not lights_on:
        os.remove(image_path)


def generate_image_filename():
    """
    Create the filename for the image
    :returns: String, e.g. CCTV_Tue-2-Aug-04_15_32.jpg
    """
    now = datetime.now().strftime('%a-%w-%b-%H:%M:%S')
    return 'CCTV_{0}.jpg'.format(now)


class Capture(object):

    def __init__(self, camera, output_dir):
        self.camera = camera
        self.output_dir = output_dir

    def take_photo(self, output_file_path):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.camera.capture(output_file_path)
        logger.info('Captured photo %s' % output_file_path)

    def capture_photo(self, count):
        """
        Capture photo of the cameras view if the room is well lit
        """
        output_file_name = generate_image_filename()
        save_file_path = os.path.join(self.output_dir, output_file_name)

        self.take_photo(save_file_path)
        check_image_useful(save_file_path)


def main():
    arguments = docopt(__doc__)
    camera = picamera.PiCamera()
    output_dir = arguments.get('--output')
    loop_count = 0

    while True:
        c = Capture(camera=camera, output_dir=output_dir)
        c.capture_photo(loop_count)

        loop_count += 1
