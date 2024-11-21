from . import Event
class OUTPUT(Event.EVENT): #Output is Event structural relationship
    def __init__(self):
        Event.EVENT.__init__(self) #We call the Event class constructor
    def printOutput(self, outputLines):
        outputString = "SUBSCRIPTION: " + "S"+str(self.SUBSCRIPTION_ID[len(self.SUBSCRIPTION_ID)-1]) + "\n"
        while(outputLines>0):
            outputString += "ATTRIBUTE: " +  self.ATTRIBUTE[len(self.ATTRIBUTE)-outputLines]
            outputString += ", VALUE:  " + str(self.VALUE[len(self.VALUE)-outputLines])
            outputString += ", PUBLISHER: " + self.PUBLISHER_ID[len(self.PUBLISHER_ID)-outputLines]+" \n"
            outputLines -= 1
        print(outputString)