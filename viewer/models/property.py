from viewer.models.common import BaseModel

## SELECT __key__ FROM __property__
## WHERE __key__ HAS ANCESTOR Key(Namespace('arepa'), `__kind__`, 'order')

class PropertyModel(BaseModel):
    def __init__(self, kind='__property__'):
        super().__init__(kind)

    @classmethod
    def get_all_available_property(cls, kind, namespace=None):
        """gets all namespace available

        Parameters
        ----------
        kind : str
            entity to retrieve parameters for
        namespace : str
            limit available properties to this namespace

        Returns
        --------------
        list(str)
            containing names of available namespace kinds in the datastore
        """
        query = cls.client().query(**dict(kind='__property__'))
        return [
            entity.key.id_or_name if entity.key.id_or_name != 1 else 'default'
            for entity in query.fetch()
        ]
