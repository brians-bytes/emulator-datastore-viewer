from viewer.models.common import BaseModel


class KindModel(BaseModel):
    def __init__(self, kind, namespace=None):
        super().__init__(kind, namespace)

    @classmethod
    def get_all_available_kinds(cls):
        """gets all kinds of entities available

        Returns
        --------------
        list(str)
            containing names of available entity kinds in the datastore
        """
        query = cls.client().query(**dict(kind='__kind__'))
        return [entity.key.id_or_name for entity in query.fetch()]
