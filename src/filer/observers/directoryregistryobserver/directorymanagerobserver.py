from filer.observers.observer import Observer
from interface import implements
import pkg_resources


class DirectoryManagerObserver(implements(Observer)):

    def __init__(self):

        self.watchdir = None

        if pkg_resources.resource_exists('filer', 'data/watchdir.dat'):
            self.watchdir = pkg_resources.resource_exists('filer', 'data/watchdir.dat')
        else:
            resourcedir = pkg_resources.resource_dir('filer', 'data/')
            self.watchdir = resourcedir + "/watchdir.dat"
