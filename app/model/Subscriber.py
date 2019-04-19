class SUBSCRIBER:
    def __init__(self, subscriberNumber):
        self.ID = [] #Subscriber ID vector
        self.NAME = [] #Subscriber name vector
        #We initialize the first n = subscriberNumber values on 0 for indexing
        self.ID[:subscriberNumber] = [0]*subscriberNumber 
        self.NAME[:subscriberNumber] = [0]*subscriberNumber 