"""
Base module
"""


import logging


class Base(object):
    """
    Base class for all objects in this module
    """

    _LOGGER_PREFIX = 'storageapi'

    class LoggerAdapter(logging.LoggerAdapter):
        def warn(self, *args, **kwargs):
            """
            Just alias for warning, the warn is provided by logger instance,
            but not by adapter.
            """
            self.warning(*args, **kwargs)

    def __init__(self):
        super(Base, self).__init__()
        self._logger = None

    @property
    def logger(self):
        if self._logger is None:
            logger = logging.getLogger(
                ".".join((self._LOGGER_PREFIX, self.__class__.__name__))
            )
            self._logger = self.LoggerAdapter(logger, {'self': self})
        return self._logger
