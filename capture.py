import os
import time
from datetime import datetime

from PIL import Image, ImageStat

import picamera

os.environ['TZ'] = 'Europe/London'
time.tzset()

OUTPUT_IMAGES_DIR = '/media/ext1/'
if not os.path.exists(OUTPUT_IMAGES_DIR):
    os.makedirs(OUTPUT_IMAGES_DIR)


def get_image_brightness(image_path):
    img = Image.open(image_path).convert('L')
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

    def __init__(self, camera):
        self.camera = camera

    def take_photo(self, output_file_path):
        self.camera.capture(output_file_path)
        print('Captured photo {0}'.format(output_file_path))

    def capture_photo(self, count):
        """
        Capture photo of the cameras view if the room is well lit
        """
        output_file_name = generate_image_filename()
        save_file_path = os.path.join(OUTPUT_IMAGES_DIR, output_file_name)

        self.take_photo(save_file_path)
        check_image_useful(save_file_path)

if __name__ == '__main__':
    camera = picamera.PiCamera()
    loop_count = 0

    while True:
        try:
            c = Capture(camera=camera)
            c.capture_photo(loop_count)
        except:
            print('Exception raised, re-running...')
            c = Capture(camera=camera)
            c.capture_photo(loop_count)

        loop_count += 1
