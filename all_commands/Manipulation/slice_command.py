from bcolors import print_error
from design_pattern.collection import Collection
from all_commands.Creation.new_command import New


class Slice:
    _collection = Collection()
    _new = New()

    def perform_action(self, command):

        if len(command) < 3:
            return print_error('ValueError')

        seq = Slice._collection.get_seq(command)
        if not seq:
           return print_error('ValueError in the <seq>')

        try:
            from_ind = int(command[1])
            to_ind = int(command[2])
        except:
            return print_error('ValueError in the <from_ind> or <to_ind> - must be Integer')

        new_seq = []
        for i in range(from_ind, to_ind):
            try:
                new_seq.append(seq[i])
            except:
                break

        if command[-2] == ':':
            if command[-1][1:] == '@':
                i = 1
                name = f'{seq.get_name()}_s{i}'
                while name in Slice._collection.get_name():
                    i += 1
                    name = f'{seq.get_name()}_s{i}'
                name = '@' + name
            else:
                name = command[-1]
            details = [''.join(new_seq),name]
            return Slice._new.perform_action(details)
        else:
            seq.set_seq(''.join(new_seq))
            Slice._collection.set_dna(seq.get_id(), seq)
            return f"[{seq.get_id()}] {seq.get_name()}: {seq.get_dna_seq()}"
