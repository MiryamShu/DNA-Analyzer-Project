from bcolors import print_error
from design_pattern.collection import Collection


class Save:
    _collection = Collection()

    def perform_action(self, command):

        seq = Save._collection.get_seq(command)
        if not seq:
           return print_error('ValueError in the <seq>')

        if len(command) == 2:
            file_name = command[1]

        elif len(command) == 1:
            file_name = seq.get_name() + '.rawdna'

        else:
            return print_error('ValueError')
        try:
            with open('Files/' + file_name, 'w') as file:
                file.write(seq.get_dna_seq())
        except:
            return print_error('ValueError')

        return 'Saved successfully'
