from all_commands.Batch.batch_Collection import BatchCollection


class BatchList:
    _collection = BatchCollection()
    def perform_action(self, command = None):
        res = list(self._collection.get_collection())
        return res if res else 'Not found any batch'
