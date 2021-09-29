from all_commands.Batch.batch_Collection import BatchCollection
from bcolors import print_error
from design_pattern.command import Command


class BatchRun(Command):
    _collection = BatchCollection()

    def perform_action(self, command):
        if len(command) < 1:
            return print_error('ValueError')
        if command[0][0] != '@':
            return print_error('ValueError in the <seq>')
        batch_command = self._collection.get(command[0][1:])
        if batch_command == 0:
            return print(print_error('Batch does not exist'))

        for com in batch_command:
             print(self.process(com[1:], com[0]))
        return 'finish running'
