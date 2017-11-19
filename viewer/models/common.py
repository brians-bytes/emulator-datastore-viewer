from google.cloud import datastore


class BaseModel(object):

    __kind__ = None
    __namespace = None
    __client = None
    __entity = None
    __attr = {}

    def __init__(self, kind, namespace='default'):
        self.__kind__ = kind
        self.__namespace = namespace

    @classmethod
    def _client(cls):
        """creates new datastore client

        Returns
        --------------
        datastore.Client
            client to access datastore using default client
        """
        return datastore.Client()

    @classmethod
    def client(cls):
        """gets datastore client

        Returns
        --------------
        datastore.Client
            client to access datastore using default client
        """
        if not cls.__client:
            cls.__client = cls._client()
        return cls.__client

    @classmethod
    def from_entity(cls, entity):
        """converty entity object to instance

        Parameters
        --------------
        entity : datastore.Entity
            entity retrived from datastore

        Returns
        --------------
        dict
            containing all properties from entity
        """
        entity['id'] = entity.key.id_or_name
        return entity

    @classmethod
    def get(cls, kind, entity_id):
        """get specific entity from datastore

        Parameters
        --------------
        kind : str
            entity kind to retrieve
        entity_id : str
            key of the entity to retrieve

        Returns
        --------------
        subclass of BaseModel
        """

        current_kind = cls(kind=kind)
        entity_key = current_kind.key(entity_id)
        results = cls.client().get(entity_key)

        instance = cls(kind=results.kind)
        entity = cls.from_entity(results)

        return instance.update_attrs(**entity)

    def _load_entity(self):
        key = self.key()
        self.__entity = datastore.Entity(key=key)
        self.__entity.update(self.__attr)
        return self.__entity

    def entity(self):
        if self.__entity:
            return self.__entity
        if self.__entity is not None:
            return self.__entity
        return self._load_entity()

    def update_attrs(self, **kwargs):
        """update attributes for the entity

        Returns
        --------------
        subclass of BaseModel
        """
        self.__attr.update(kwargs)

        return self

    def delete(self):
        """delete entity form `__kind__`"""
        pass

    def put(self):
        """save entity form `__kind__`"""
        entity_key = self.key()
        entity = self.entity()
        self.client().put(entity)

    def key(self, entity_id=None):
        """get key of the entity

        Returns
        --------------
        str
            unique key representing the entity
        """
        if entity_id is not None:
            return self.client().key(self.__kind__, entity_id)
        if 'id' in self.__attr:
            return self.client().key(self.__kind__, self.__attr['id'])
        return self.client().key(self.__kind__)

    def id(self):
        return self.key().id_or_name
