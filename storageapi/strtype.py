import pkg_resources
from storageapi.base import Base


class StorageType(Base):
    """
    Base class for any possible storage type which needs to be handled
    """
    name = None

    @classmethod
    def get_providers(cls):
        """
        :return: list of providers
        """
        providers = []
        for ep in pkg_resources.iter_entry_points(
            group='storageapi.providers'
        ):
            Provider = ep.load()
            try:
                if Provider.providers(cls):
                    providers.append(Provider)
            except NotImplementedError:
                pass
        return providers


# TODO: have no idea what it is ... yet (:
# class PNFSStorageType(StorageType):
#     str_type = "PNFS"
