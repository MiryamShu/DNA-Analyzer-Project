from all_commands.Batch.batch_Collection import BatchCollection
from bcolors import print_error


class BatchSave:
    _collection = BatchCollection()

    def perform_action(self, command):
        if len(command) < 1:
            return print_error('ValueError')
        if command[0][0] != '@':
            return print_error('ValueError in the <seq>')
        batch_command = self._collection.get(command[0][1:])
        if batch_command == 0:
            return print(print_error('Batch does not exist'))
        try:
            name = command[1]
        except:
            name = command[0][1:] + '.dnabatch'
        file_name = 'Files/' + name
        try:
            with open(file_name, 'w') as file:
                for com in batch_command:
                    file.write(f"{' '.join(com)}\n")

        except:
            return print_error('Error')
