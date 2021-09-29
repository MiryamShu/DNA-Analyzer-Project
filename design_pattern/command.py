from all_commands.Analysis.count_command import Count
from all_commands.Analysis.find_command import Find
from all_commands.Analysis.findall_command import Findall
from all_commands.Analysis.len_command import Len
from all_commands.Creation.dup_command import Dup
from all_commands.Creation.load_command import Load
from all_commands.Creation.new_command import New
from all_commands.Management.del_command import Del
from all_commands.Management.save_command import Save
from all_commands.Manipulation.pair_command import Pair
from all_commands.Manipulation.slice_command import Slice


class Command:
    def __init__(self):
        self.argc_command, self.cmd, self.word = None, None, None
        self.new = New()
        self.load = Load()
        self.dup = Dup()
        self.slice = Slice()
        self.pair = Pair()
        self.delete = Del()
        self.save = Save()
        self.len = Len()
        self.find = Find()
        self.count = Count()
        self.findall = Findall()

    def process(self, command, word):
        commands = {'new': self.new,
                    'load': self.load,
                    'dup': self.dup,
                    'slice': self.slice,
                    'pair': self.pair,
                    'del': self.delete,
                    'save': self.save,
                    'len': self.len,
                    'find': self.find,
                    'count': self.count,
                    'findall': self.findall
                    }

        res = commands[word].perform_action(command)
        if res is not None:
            return res
        return 0
