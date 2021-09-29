from bcolors import print_error
from design_pattern.collection import Collection
from all_commands.Creation.new_command import New


class Pair:
    _collection = Collection()
    _new = New()

    def perform_action(self, command):

        seq = Pair._collection.get_seq(command)
        if not seq:
           return print_error('ValueError in the <seq>')

        new_seq = str(seq)
        new_seq = new_seq.translate(str.maketrans("ATCG","TAGC"))

        if len(command) > 2 and command[-2] == ':':
            if command[-1][1:] == '@':
                i = 1
                name = f'{seq.get_name()}_p{i}'
                while name in Pair._collection.get_name():
                    i += 1
                    name = f'{seq.get_name()}_p{i}'
                name = '@' + name
            else:
                name = command[-1]
            details = [new_seq, name]
            return Pair._new.perform_action(details)
        else:
            seq.set_seq(new_seq)
            Pair._collection.set_dna(seq.get_id(), seq)
            return f"[{seq.get_id()}] {seq.get_name()}: {seq.get_dna_seq()}"