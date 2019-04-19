from . import Event
class INPUT(Event.EVENT): #Input is Event structural relationship
    def __init__(self, inputNumber):
        Event.EVENT.__init__(self) #We call the Event class constructor
        #We initialize the first n = inputNumber values on 0 for indexing
        self.ATTRIBUTE[:inputNumber] = [0] * inputNumber
        self.VALUE[:inputNumber] = [0] * inputNumber