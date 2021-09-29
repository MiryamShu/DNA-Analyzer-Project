from bcolors import print_error


class Collection(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_)
        return class_._instance

    _dna_collection = dict()
    _name_collection = dict()

    def get_dna(self):
        return Collection._dna_collection

    def get_name(self):
        return Collection._name_collection

    def add_dna(self, id, obj):
        Collection._dna_collection[f'{id}'] = obj
        Collection._name_collection[obj.get_name()] = f'{id}'

    def del_dna(self, seq):
        del Collection._dna_collection[str(seq.get_id())]
        del Collection._name_collection[seq.get_name()]

    def set_dna(self, id, new_obj):
        Collection._dna_collection[f'{id}'] = new_obj


    def get_seq(self,info):
        if info[0][0] == '#':
            id = info[0][1:]
            if id not in self._dna_collection.keys():
                return False
            seq = self._dna_collection.get(id)
            return seq

        elif info[0][0] == '@':
            name = info[0][1:]
            if name not in self._name_collection.keys():
                return False
            seq = self._dna_collection.get(self._name_collection.get(name))
            return seq

        else:
            return 0