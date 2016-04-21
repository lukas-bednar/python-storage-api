from storageapi.base import Base


class StorageProvider(Base):
    """
    Base class for any possible storage provider
    """


    @classmethod
    def provides(cls, str_type):
        """
        :param str_type: storage type
        :type str_type: class type
        """
        raise NotImplementedError()
