class PUBLISHER:
    def __init__(self, publisherNumber):
        self.ID = []# Publisher ID vector
        self.NAME = []# Publisher name vector
        #We initialize the first n = publisherNumber values on 0 for indexing
        self.ID[:publisherNumber] = [0]*publisherNumber 
        self.NAME[:publisherNumber] = [0]*publisherNumber