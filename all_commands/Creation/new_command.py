from bcolors import print_error
from design_pattern.collection import Collection
from design_pattern.DNA_seq import DnaSequence


class New:
    _collection = Collection()
    __counter_obj = 0
    __counter_default_name = 0

    def perform_action(self, command):

        try:
            if command[1][0] != '@':
                return print_error('Must be @ before the name seq')
            name = command[1][1:]
            if name in New._collection.get_name().keys():
                return print_error('The name already exists')
        except:
            New.__counter_default_name += 1
            name = f'seq{New.__counter_default_name}'
            while name in New._collection.get_name().keys():
                New.__counter_default_name += 1
                name = f'seq{New.__counter_default_name}'
        New.__counter_obj += 1
        try:
            dna = DnaSequence(command[0], name, New.__counter_obj)
        except:
            New.__counter_obj -= 1
            New.__counter_default_name -= 1
            return print_error('ValueError')
        New._collection.add_dna(New.__counter_obj,dna)
        seq = self.format(command[0])
        return f"[{New.__counter_obj}] {name}: {seq}"



    def format(self, seq):
        if len(seq) > 40:
            return seq[:32] + '...' + seq[-3:]
        return seq