from bcolors import print_error
from design_pattern.collection import Collection
from all_commands.Creation.new_command import New


class Dup:
    __obj = New()
    _collection = Collection()

    def perform_action(self, command):
        details = []
        if command[0][0] == '#':
            id = command[0][1:]
            if id not in Dup._collection.get_dna().keys():
                return print_error("Don't found {} id".format(id))
            seq = Dup._collection.get_dna().get(id)

        elif command[0][0] == '@':
            name = command[0][1:]
            if name not in Dup._collection.get_name().keys():
                return print_error("Don't found {} name".format(name))
            seq = Dup._collection.get_dna().get(Dup._collection.get_name().get(name))

        else:
            return print_error('ValueError in the <seq>')



        details.append(str(seq))
        try:
            details.append(command[1])
        except:
            i = 1
            name = f'{seq.get_name()}_{i}'
            while name in Dup._collection.get_name():
                i += 1
                name = f'{seq.get_name()}_{i}'
            details.append(f'@{seq.get_name()}_{i}')
        return Dup.__obj.perform_action(details)
