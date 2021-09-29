from all_commands.Batch.batch_Collection import BatchCollection
from bcolors import print_error


class BatchCreate:
    _collection = BatchCollection()

    def perform_action(self, command):
        if len(command) != 1:
            return print_error('ValueError')
        arr_commands = ['new', 'load', 'dup', 'slice', 'pair', 'delete', 'save', 'len', 'find', 'count', 'findall']
        name = command[0]
        arr = []
        while True:
            print('> batch >>>', end=' ')
            command = input()
            line_input = command.split()
            if command == 'end':
                break
            if len(line_input) < 2 or line_input[0] not in arr_commands:
                print(print_error('ValueError'))
                continue
            arr.append(line_input)

        BatchCreate._collection.add_batch(name, arr)
