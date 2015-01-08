# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create / interact with a batch of updates / deletes."""
try:
    from threading import local as Local
except ImportError:     # pragma: NO COVER (who doesn't have it?)
    class Local(object):
        """Placeholder for non-threaded applications."""

from gcloud.datastore import _implicit_environ
from gcloud.datastore import datastore_v1_pb2 as datastore_pb


class _Batches(Local):
    """Manage a thread-local LIFO stack of active batches / transactions.

    Intended for use only in :class:`gcloud.datastore.batch.Batch.__enter__`
    """
    def __init__(self):
        super(_Batches, self).__init__()
        self._stack = []

    @property
    def stack(self):
        """Return a copy of our stack."""
        return self._stack[:]

    def _push_batch(self, batch):
        """Push a batch onto our stack.

        Intended for use only in :meth:`gcloud.datastore.batch.Batch.__enter__`

        :type batch: :class:`gcloud.datastore.batch.Batch` or
                    :class:`gcloud.datastore.transaction.Transaction`
        """
        self._stack.append(batch)

    def _pop_batch(self):
        """Pop a batch onto our stack.

        Intended for use only in :meth:`gcloud.datastore.batch.Batch.__enter__`

        :rtype: :class:`gcloud.datastore.batch.Batch` or
                :class:`gcloud.datastore.transaction.Transaction`
        :raises: IndexError if the stack is empty.
        """
        return self._stack.pop()


_BATCHES = _Batches()


class Batch(object):
    """An abstraction representing a collected group of updates / deletes.

    Used to build up a bulk mutuation.

    For example, the following snippet of code will put the two ``save``
    operations and the delete operatiuon into the same mutation, and send
    them to the server in a single API request::

      >>> from gcloud import datastore
      >>> batch = Batch()
      >>> batch.put(entity1)
      >>> batch.put(entity2)
      >>> batch.delete(key3)
      >>> batch.commit()

    You can also use a batch as a context manager, in which case the
    ``commit`` will be called automatically if its block exits without
    raising an exception::

      >>> with Batch() as batch:
      ...     batch.put(entity1)
      ...     batch.put(entity2)
      ...     batch.delete(key3)

    By default, no updates will be sent if the block exits with an error::

      >>> from gcloud import datastore
      >>> dataset = datastore.get_dataset('dataset-id')
      >>> with Batch as batch:
      ...   do_some_work(batch)
      ...   raise Exception() # rolls back
    """

    def __init__(self, dataset_id=None, connection=None):
        """ Construct a batch.

        :type dataset_id: :class:`str`.
        :param dataset_id: The ID of the dataset.

        :type connection: :class:`gcloud.datastore.connection.Connection`
        :param connection: The connection used to connect to datastore.

        :raises: :class:`ValueError` if either a connection or dataset ID
                 are not set.
        """
        self._connection = connection or _implicit_environ.CONNECTION
        self._dataset_id = dataset_id or _implicit_environ.DATASET_ID

        if self._connection is None or self._dataset_id is None:
            raise ValueError('A batch must have a connection and '
                             'a dataset ID set.')

        self._mutation = datastore_pb.Mutation()
        self._auto_id_entities = []

    @property
    def dataset_id(self):
        """Getter for dataset ID in which the batch will run.

        :rtype: :class:`str`
        :returns: The dataset ID in which the batch will run.
        """
        return self._dataset_id

    @property
    def connection(self):
        """Getter for connection over which the batch will run.

        :rtype: :class:`gcloud.datastore.connection.Connection`
        :returns: The connection over which the batch will run.
        """
        return self._connection

    @property
    def mutation(self):
        """Getter for the current mutation.

        Every batch is committed with a single Mutation
        representing the 'work' to be done as part of the batch.
        Inside a batch, calling ``batch.put()`` with an entity, or
        ``batch.delete`` with a key, builds up the mutation.
        This getter returns the Mutation protobuf that
        has been built-up so far.

        :rtype: :class:`gcloud.datastore.datastore_v1_pb2.Mutation`
        :returns: The Mutation protobuf to be sent in the commit request.
        """
        return self._mutation

    def add_auto_id_entity(self, entity):
        """Adds an entity to the list of entities to update with IDs.

        When an entity has a partial key, calling ``save()`` adds an
        insert_auto_id entry in the mutation.  In order to make sure we
        update the Entity once the transaction is committed, we need to
        keep track of which entities to update (and the order is
        important).

        When you call ``save()`` on an entity inside a transaction, if
        the entity has a partial key, it adds itself to the list of
        entities to be updated once the transaction is committed by
        calling this method.

        :type entity: :class:`gcloud.datastore.entity.Entity`
        :param entity: The entity to be updated with a completed key.

        :raises: ValueError if the entity's key is alread completed.
        """
        if not entity.key.is_partial:
            raise ValueError("Entity has a completed key")

        self._auto_id_entities.append(entity)

    def put(self, entity):
        """Remember an entity's state to be saved during ``commit``.

        .. note::
           Any existing properties for the entity will be replaced by those
           currently set on this instance.  Already-stored properties which do
           not correspond to keys set on this instance will be removed from
           the datastore.

        .. note::
           Property values which are "text" ('unicode' in Python2, 'str' in
           Python3) map to 'string_value' in the datastore;  values which are
           "bytes" ('str' in Python2, 'bytes' in Python3) map to 'blob_value'.

        :type entity: :class:`gcloud.datastore.entity.Entity`
        :param entity: the entity to be saved.

        :raises: ValueError if entity has no key assigned.
        """
        if entity.key is None:
            raise ValueError("Entity must have a key")

        key_pb = entity.key.to_protobuf()
        properties = dict(entity)
        exclude = tuple(entity.exclude_from_indexes)

        self.connection.save_entity(
            self.dataset_id, key_pb, properties,
            exclude_from_indexes=exclude, mutation=self.mutation)

        if entity.key.is_partial:
            self._auto_id_entities.append(entity)

    def delete(self, key):
        """Remember a key to be deleted durring ``commit``.

        :type key: :class:`gcloud.datastore.key.Key`
        :param key: the key to be deleted.

        :raises: ValueError if key is not complete.
        """
        if key.is_partial:
            raise ValueError("Key must be complete")

        key_pb = key.to_protobuf()
        self.connection.delete_entities(
            self.dataset_id, [key_pb], mutation=self.mutation)

    def begin(self):
        """No-op

        Overridden by :class:`gcloud.datastore.transaction.Transaction`.
        """
        pass

    def commit(self):
        """Commits the batch.

        This is called automatically upon exiting a with statement,
        however it can be called explicitly if you don't want to use a
        context manager.
        """
        response = self.connection.commit(self._dataset_id, self.mutation)
        # If the back-end returns without error, we are guaranteed that
        # the response's 'insert_auto_id_key' will match (length and order)
        # the request's 'insert_auto_id` entities, which are derived from
        # our '_auto_id_entities' (no partial success).
        for new_key_pb, entity in zip(response.insert_auto_id_key,
                                      self._auto_id_entities):
            new_id = new_key_pb.path_element[-1].id
            entity.key = entity.key.completed_key(new_id)

    def rollback(self):
        """No-op

        Overridden by :class:`gcloud.datastore.transaction.Transaction`.
        """
        pass

    def __enter__(self):
        _BATCHES._push_batch(self)
        self.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.commit()
            else:
                self.rollback()
        finally:
            _BATCHES._pop_batch()
