from viewer.models.common import BaseModel


class KindModel(BaseModel):
    def __init__(self, kind, namespace=None):
        super().__init__(kind, namespace)

    @classmethod
    def get_available_namespaced_entity_kinds(cls, namespace=None):
        """get all kinds available in namespace

        Parameters
        ----------
        namespace : str or None
            limit to kinds available in the defined namespace, use None for the
            default namespace

        Returns
        -------
        list of dict
            containing the entity name and namespace it belongs to
        """
        available_kinds = cls.get_all_available_kinds(namespace)
        return [{
            'kind': kind_name,
            'namespace': namespace,
        } for kind_name in available_kinds]

    @classmethod
    def get_all_available_kinds(cls, namespace=None):
        """gets all kinds of entities available in the namespace

        Parameters
        ----------
        namespace : str or None
            limit to kinds available in the defined namespace, use None for the
            default namespace

        Returns
        -------
        list(str)
            containing names of available entity kinds in the datastore
        """
        query = cls.client().query(kind='__kind__', namespace=namespace)
        return [entity.key.id_or_name for entity in query.fetch()]
