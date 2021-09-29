from bcolors import print_error
from design_pattern.invoker import Invoker


class CLI:

    def __init__(self):
        self.invoke = Invoker()

    def start(self):
        while True:
            print('> cmd >>>', end=' ')
            line_input = input().split() # accept the command from the user
            if len(line_input) < 1: # if the user didn't entry command
                print(print_error('ValueError'))
                continue
            if self.invoke.command(line_input): # save the command and all the other details
               self.invoke.execute() # execute the command


if __name__ == '__main__':
    cli = CLI()
    cli.start()