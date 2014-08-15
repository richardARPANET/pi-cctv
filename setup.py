import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='picctv',
    version='0.1.0',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    include_package_data=True,
    license='proprietary',
    entry_points={
        'console_scripts': ['picctv = picctv.picctv:main']
    },
    description='CCTV for the RaspberryPi & Camera Module.',
    long_description=README,
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    url='https://github.com/richardasaurus/pi-cctv',
    zip_safe=True,
    install_requires=[
        'picamera',
        'Pillow',
        'docopt',
        'pytest',
    ]
)
