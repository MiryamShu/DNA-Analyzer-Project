class DnaSequence:

    def __init__(self, sequence, name, number):
        for char in sequence:
            if char not in ['A', 'C', 'T', 'G']:
                raise ValueError
        self.sequence = sequence
        self.name = name
        self.number = number

    def assignment(self, other):
        if type(other) is str:
            new_sequence = other
        else: new_sequence = other.sequence
        for char in new_sequence:
            if char not in ['A', 'C', 'T', 'G']:
                raise ValueError
        self.sequence = new_sequence

    def insert(self,nucleotide ,index = 0):
        if type(index) is not int or not 0 < index < len(self.sequence):
            raise IndexError
        if nucleotide not in ['A', 'C', 'T', 'G']:
            raise ValueError
        self.sequence  = self.sequence[:index] + nucleotide + self.sequence[index:]

    def __str__(self):
        return self.sequence

    def __eq__(self, other):
        return self.sequence == other.sequence

    def __ne__(self, other):
        return self.sequence != other.sequence

    def __getitem__(self, index):
        if type(index) is not int or not 0<index<len(self.sequence):
            raise IndexError
        return self.sequence[index]

    def __setitem__(self, index, value):
        if type(index) is not int or not 0 < index < len(self.sequence):
            raise IndexError
        for char in value:
            if char not in ['A', 'C', 'T', 'G']:
                raise ValueError
        self.sequence  = self.sequence[:index] + value + self.sequence[index + 1:]

    def __len__(self):
        return len(self.sequence)

    def get_dna_seq(self):
        return self.sequence

    def set_seq(self, seq):
        self.sequence = seq

    def get_name(self):
        return self.name

    def get_id(self):
        return self.number