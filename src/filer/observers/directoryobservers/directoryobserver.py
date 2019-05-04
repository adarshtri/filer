from interface import implements
from filer.observers.observer import Observer
from abc import ABC, abstractmethod


class DirectoryObserver(implements(Observer), ABC):

    @abstractmethod
    def update(self, updateinfo: dict):
        pass

    @abstractmethod
    def convertfile(self, file, type):
        pass
