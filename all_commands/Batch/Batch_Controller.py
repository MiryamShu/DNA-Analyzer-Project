from all_commands.Batch.batchload_command import BatchLoad
from all_commands.Batch.batchsave_command import BatchSave
from all_commands.Batch.list_command import BatchList
from all_commands.Batch import BatchCreate
from all_commands.Batch import BatchRun
from all_commands.Batch.show_command import Show


class Controller:

    def __init__(self):
        self.batch = BatchCreate()
        self.run = BatchRun()
        self.batchlist = BatchList()
        self.batchshow = Show()
        self.batchsave = BatchSave()
        self.batchload = BatchLoad()

    def process(self, command, word):
        commands = {
            'batch': self.batch,
            'run': self.run,
            'batchlist': self.batchlist,
            'batchshow': self.batchshow,
            'batchsave': self.batchsave,
            'batchload': self.batchload
        }

        res = commands[word].perform_action(command)
        if res is not None:
            return res