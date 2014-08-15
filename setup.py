import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='picctv',
    version='0.1.2',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    license='proprietary',
    entry_points={
        'console_scripts': ['picctv = picctv.picctv:main']
    },
    description='CCTV for the RaspberryPi & Camera Module.',
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    url='https://github.com/richardasaurus/pi-cctv',
    zip_safe=True,
    install_requires=[
        'picamera>=1.7',
        'Pillow>=2.5.2',
        'docopt>=0.6.2',
        'pytest>=2.6.1',
    ]
)
