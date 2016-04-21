from storageapi.strtype import Base


class StorageDevice(Base):
    """
    Base class for any possible storage devices being created
    """
    def __init__(self, provider):
        """
        :param strtype: storage type
        :type strtype: instance of StorageDevice
        :param provider: storage provider
        :type provider: instance of StorageProvider
        """
        self.provider = provider

    @property
    def strtype(self):
        return self.provider.strtype

    def destroy(self):
        """
        Destroy this device
        """
        raise NotImplementedError()
