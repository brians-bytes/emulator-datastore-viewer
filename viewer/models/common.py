from google.cloud import datastore


class BaseModel(object):

    __kind__ = None
    __client = None
    __entity = {}

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
        pass

    @classmethod
    def get(cls, entity_id):
        """get specific entity from datastore

        Parameters
        --------------
        entity_id : str
            key of the entity to retrieve

        Returns
        --------------
        subclass of BaseModel
        """
        pass

    @classmethod
    def all(cls):
        """get all entities for `__kind__`

        Returns
        --------------
        list(BaseModel)
            list of items of entity kind
        """
        pass

    def update_attrs(self, **kwargs):
        """update attributes for the entity"""
        pass

    def delete(self):
        """delete entity form `__kind__`"""
        pass

    def put(self):
        """save entity form `__kind__`"""
        pass

    def id(self):
        """get key of the entity

        Returns
        --------------
        str
            unique key representing the entity
        """
        if 'id' in self.__entity:
            return self.client().key(self.__kind__, self.__entity['id'])
        return self.client().key(self.__kind__)
