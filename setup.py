import sys
from distutils.util import get_platform
import os
import glob

from setuptools import setup

if sys.version_info < (3, 6):
    sys.stderr.write("This module requires atleast Python 3.6\n")
    sys.exit(1)

platform = get_platform()

if not platform.startswith("linux"):
    sys.stderr.write("This modules runs only on linux\n")

if sys.version_info >= (3, 0):
    package_dir = {'filer': 'src/filer', 'filer.observers': 'src/filer/observers'}
else:
    package_dir = {'': ''}

sys.stdout.write("Specify a directory to store general module information [default /var/log/filer/]\n")
info_directory = input("Specify directory:")

if info_directory == "":
    if not os.path.isdir("/var/log/filer"):
        os.makedirs("/var/log/filer/", mode=0o777, exist_ok=True)
    else:
        for f in glob.glob("/var/log/filer/*"):
            os.remove(f)

else:
    if not os.path.isdir(info_directory):
        os.makedirs(info_directory, mode=0o777, exist_ok=True)
    else:
        for f in glob.glob(info_directory+"/*"):
            os.remove(f)

locationdatafiles = os.getcwd() + "/src/filer/data/"

packageinfofile = open(locationdatafiles + "/package.dat", 'w')

if info_directory != "":
    packageinfofile.write(info_directory)

packageinfofile.close()

classifier = [
    'Development Status :: 1 - Development',
    'Environment :: Console',
    'Intended Audience :: Developers',
    # 'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Filesystems',
    'Topic :: System :: Monitoring',
]

setup(
    name='filer',
    version='0.0.2',
    description="Linux file system monitoring",
    author="Adarsh Trivedi",
    author_email="adarsh.trivedi100@gmail.com",
    license="",
    platforms="Linux",
    classifiers=classifier,
    packages=['filer'],
    package_dir=package_dir,
    package_data={'filer': ['data/*.dat']},
    install_requires=['python-interface']
)
