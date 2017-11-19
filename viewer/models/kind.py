from viewer.models.common import BaseModel


class KindModel(BaseModel):
    def __init__(self, kind, namespace='default'):
        self.__kind__ = kind
        self.__namespace = namespace

    @classmethod
    def get_all_available_kinds(cls):
        """gets all kinds of entites available

        Returns
        --------------
        list(str)
            containing names of available enity kinds in the datastore
        """
        query = cls.client().query(kind='__kind__')
        return [entity.key.id_or_name for entity in query.fetch()]
