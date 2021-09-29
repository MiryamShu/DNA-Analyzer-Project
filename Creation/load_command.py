from bcolors import print_error
from Creation.new_command import New


class Load:
    __obj = New()

    def perform_action(self, command):
        details = []
        try:
            file_name = 'Files/' + command[0]
            with open(file_name, 'r') as file:
                seq = file.readline()
                details.append(seq)
                try:
                    details.append(command[1])
                except:
                    details.append('@' + command[0].split('.')[0])
        except:
            return print_error('ValueError')
        return Load.__obj.perform_action(details)
