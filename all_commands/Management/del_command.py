from bcolors import print_error
from design_pattern.collection import Collection


class Del:
    _collection = Collection()

    def perform_action(self, command):

        seq = Del._collection.get_seq(command)
        if not seq:
           return print_error('ValueError in the <seq>')

        print("Do you really want to delete: {}?\nPlease confirm by 'y' or 'Y', or cancel by 'n' or 'N'.".format(
            seq.get_name(), seq.get_dna_seq()))
        res = str(input('> confirm >>> ')).upper()

        while res != 'Y' and res != 'N':
            print("You have typed an invalid response.\nPlease confirm by 'y' or 'Y', or cancel by 'n' or 'N'.")
            res = str(input('> confirm >>> ')).upper()

        if res == 'N':
            return 'The delete request was canceled'

        if res == 'Y':
            Del._collection.del_dna(seq)
            details = 'Deleted: [{}] {}: {}'.format(seq.get_id(), seq.get_name(), seq.get_dna_seq())
            del seq
            return details
