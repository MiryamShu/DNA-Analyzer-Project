from all_commands.Batch.batch_Collection import BatchCollection
from bcolors import print_error


class BatchLoad:
    _collection = BatchCollection()
    def perform_action(self, command):
        try:
            if command[-2] == ':':
                try:
                    if command[-1][0] != '@':
                        return print_error('Name must start with @')
                    name = command[-1][1:]
                except:
                    return print_error('SyntaxError')
        except:
            name = command[0].split('.')[0]

        try:
            file_name = 'Files/' + command[0]
            arr =[]
            with open(file_name, 'r') as file:
                while True:
                    line = file.readline()[:-1]
                    if line == '':
                        break
                    arr.append(line.split())
            self._collection.add_batch(name, arr)

        except:
            return print_error('Error')