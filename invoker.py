from Batch.Batch_Controller import Controller
from command import Command


class Invoker:
    def __init__(self):
        self.argc_command, self.cmd, self.word = None, None, None
        self.com = Command()
        self.batch = Controller()

    def command(self, cmd):
        commands = {'new': self.com,
                    'load': self.com,
                    'dup': self.com,
                    'slice': self.com,
                    'pair': self.com,
                    'del': self.com,
                    'save': self.com,
                    'len': self.com,
                    'find': self.com,
                    'count': self.com,
                    'findall': self.com,
                    'batch': self.batch,
                    'run': self.batch,
                    'batchlist': self.batch,
                    'batchshow': self.batch,
                    'batchsave': self.batch,
                    'batchload': self.batch}  # Routing commands by type of the command (DNA seq or batch)

        if cmd[0] not in commands:  # If the command from the user don't exist
            print('ValueError')
            return 0

        self.cmd = commands[cmd[0]]  # Save the operator by the type of the command
        self.argc_command = cmd[1:]  # Save the details of the command
        self.word = cmd[0]  # Save the word command
        return 1

    def execute(self):
        res = self.cmd.process(self.argc_command, self.word)  # call to the operator to process the command
        if res is not None: # print the value that return if it returns
            print(res)
