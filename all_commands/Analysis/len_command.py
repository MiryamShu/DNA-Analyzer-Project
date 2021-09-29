from bcolors import print_error
from design_pattern.collection import Collection


class Len:
    _collection = Collection()

    def perform_action(self, command):

        if command[0][0] == '@':
            return print_error('Send only ID')
        seq = Len._collection.get_seq(command)
        if not seq:
            return print_error("Don't found {} id".format(command[0][1:]))
        return len(str(seq))
