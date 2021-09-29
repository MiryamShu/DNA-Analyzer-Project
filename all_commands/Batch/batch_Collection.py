from bcolors import print_error


class BatchCollection(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance

    _collection = dict()

    def get_collection(self):
        return self._collection.keys()

    def add_batch(self, name, command):
        if name in self._collection:
            i = 1
            new_name = f'{name}_{i}'
            while new_name in self._collection:
                i += 1
                new_name = f'{name}_{i}'
            name = new_name
        self._collection[name] = command

    def get(self, name):
        if name not in self._collection:
            return 0
        return self._collection[name]
