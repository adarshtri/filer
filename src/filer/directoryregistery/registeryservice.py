from interface import Interface


class DirectoryRegistery(Interface):

    """
        Interface to register observers to get notified for directory changes
        and register for different operations like zipping, encrypting.

    """

    def register_new(self, observer):

        """
        Registers an observer to be notified of all the events of the subject class implementing this interface.
        :param observer: Should be of type observer
        :return: None: Doesn't return anything
        """
        pass

    def unregister(self, observer):

        """
        Unregisters all the observers of this subject.
        :param observer: observer to be removed
        :return: None: Doesn't return anything
        """
        pass

    def notify_registeries(self):

        """
        Notifies all the registered observers of the class implementing this interface.
        :return: None
        """
        pass
