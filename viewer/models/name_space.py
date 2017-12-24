from viewer.models.common import BaseModel


class NamespaceModel(BaseModel):
    def __init__(self, kind='__namespace__'):
        super(NamespaceModel, self).__init__(kind)

    @classmethod
    def get_all_available_namespaces(cls):
        """gets all namespace available

        Returns
        --------------
        list(str)
            containing names of available namespace kinds in the datastore
        """
        query = cls.client().query(**dict(kind='__namespace__'))
        return [
            entity.key.id_or_name if entity.key.id_or_name != 1 else 'default'
            for entity in query.fetch()
        ]
