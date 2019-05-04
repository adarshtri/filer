from interface import Interface


class Observer(Interface):

    """Interface to support observers for newly registered directories"""

    def update(self, updateinfo: dict):

        """
        :param updateinfo: dictionary containing information regarding the updation.
        :return: None
        """
        pass
