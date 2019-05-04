from interface import implements
from filer.directoryregistery.registeryservice import DirectoryRegistery


class DirectoryRegisteryService(implements(DirectoryRegistery)):

    def __init__(self):

        self.observers = []

    def register_new(self, observer):

        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):

        if observer in self.observers:
            self.observers.remove(observer)

    def notify_directory_registry(self, directory: dict):

        for observer in self.observers:
            observer.update(directory)
