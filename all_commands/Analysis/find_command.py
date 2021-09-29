from bcolors import print_error
from design_pattern.collection import Collection
from design_pattern.DNA_seq import DnaSequence


class Find:
    _collection = Collection()

    def perform_action(self, command):
        seq = Find._collection.get_seq(command)
        if not seq:
            return print_error('ValueError in the <seq>')

        sub_seq = Find._collection.get_seq([command[1]])
        if type(sub_seq) is DnaSequence:
            sub_seq = str(sub_seq)

        if sub_seq == 0:
            sub_seq = command[1]

        elif not sub_seq:
            return print_error('ValueError in the <seq>')
        res = str(seq).find(sub_seq)
        if res >= 0:
            return res
        else:
            return 'The sub-string was not found'
