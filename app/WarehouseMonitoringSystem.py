
import random
import math

#Import stataments
from .model import Database
from .model import Seafood
from .model import Temperature
from .model import Publisher
from .model import Subscriber
from . import Subscription
from .model import Input
from .model import Output

#CONSTANTS - INITIAL CONDITIONS 
SIMULATION_TIME = 30 #Measured in days
THRESHOLD = 0.7 #Probability in [0 - 1] range

#INDEPENDENT VARIABLES - INITIAL CONDITIONS 
MINUTE = 0 #measured in minutes
DAY = 0 #measured in days
TIMESTAMP = "Next" #Stop or Next
RANDOM_VALUE = 0.0 #in [0 - 1] range
OCURRENCE = "Inactive" #Active or Inactive
THERMOMETER_STATE = "Off" #On or Off
RFID_STATE = "Off" #On or Off

#Input event object initialization from Input class
INPUT = Input.INPUT(7) 
#Input attribute vector,  position 0 assignation 
INPUT.ATTRIBUTE[0] = "Seafood.amount"
#Input attribute vector, Position 1 assignation 
INPUT.ATTRIBUTE[1] = "Seafood.total_amount"
#Input attribute vector, Position 2 assignation 
INPUT.ATTRIBUTE[2] = "Seafood.price"
#Input attribute vector, Position 3 assignation 
INPUT.ATTRIBUTE[3] = "Seafood.total_price"
#Input attribute vector, Position 4 assignation 
INPUT.ATTRIBUTE[4] = "Seafood.time" 
#Input attribute vector, Possition 5 assignation 
INPUT.ATTRIBUTE[5] = "Temperature.value"
#Input attribute vector, Possition 6 assignation 
INPUT.ATTRIBUTE[6] = "Temperature.time"

#Output event object initialization from Output class
OUTPUT = Output.OUTPUT()

#Publisher object initialization from Publisher class
PUBLISHER = Publisher.PUBLISHER(2)
#Publisher ID vector, position 0 assignation
PUBLISHER.ID[0] = "PU1"
#Publisher ID vector, position 1 assignation
PUBLISHER.ID[1] = "PU2"
#Publisher name vector, position 0 assignation
PUBLISHER.NAME[0] = "Thermometer"
#Publisher name vector, position 1 assignation
PUBLISHER.NAME[1] = "RFID"

#Subscriber object initialization from Subscriber class
SUBSCRIBER = Subscriber.SUBSCRIBER(4)
#Subscriber ID vector, position 0 assignation
SUBSCRIBER.ID[0] = "SU1"
#Subscriber ID vector, position 1 assignation
SUBSCRIBER.ID[1] = "SU2"
#Subscriber ID vector, position 2 assignation
SUBSCRIBER.ID[2] = "SU3"
#Subscriber ID vector, position 3 assignation
SUBSCRIBER.ID[3] = "SU4"
#Subscriber name vector, position 0 assignation
SUBSCRIBER.NAME[0] = "System Management Dashboard"
#Subscriber name vector, position 1 assignation
SUBSCRIBER.NAME[1] = "Company Customer"
#Subscriber name vector, position 2 assignation
SUBSCRIBER.NAME[2] = "Email system"
#Subscriber name vector, position 3 assignation
SUBSCRIBER.NAME[3] = "Warehouse display"

SUBSCRIPTION = Subscription.SUBSCRIPTION()

SUBSCRIPTION.BLOCK = []

TermB = 0
TermS = 1
TermF = 1

NEW_PREDICATE_STATE = "Yes" #Yes or No
NEW_FILTER_STATE = "Yes" #Yes or No

FILTER_RESULT = "False" #True or False

#DATABASE CONFIGURATION
database = Database.Database(1)

#Principal execution thread
def main():
    while(True):
        #Interface interaction
        if(input("(1) CREATE SUBSCRIPTION \n(0) Continue to simulation\n")!=str(1)):
            break;
        SUBSCRIPTION.CREATES()
        
    #Interface interaction
    #SUBSCRIPTION.printSubsciption()
    #input("PRESS ENTER TO CONTINUE")
    
    i = 0
    while(i<44640):
        SEAFOOD_ARRIVES_TO_WAREHOUSE()
        TEMPERATURE_EMERGES()
        TIME_PASSES()
        EVENT_MESSAGE_EMERGES()
        i += 1
        
#Events section

#Timer speciffication
def TIME_PASSES():
    global MINUTE
    global DAY
    global TIMESTAMP
    #We verify the bounds of simulation
    if(DAY <= SIMULATION_TIME 
       and 
       TIMESTAMP == "Next"):
        #One minute passed
        if(MINUTE<1440):
            MINUTE = MINUTE + 1
    if(MINUTE == 1440):
        #Next day begins
        DAY = DAY + 1
        MINUTE = 0

#RFID speciffication
def SEAFOOD_ARRIVES_TO_WAREHOUSE():
    global RANDOM_VALUE
    global OCURRENCE
    global RFID_STATE
    global TIMESTAMP
    
    #We verify simulation bounds
    if(DAY <= SIMULATION_TIME and TIMESTAMP == "Next"):
        #We generate new random number
        RANDOM_VALUE = random.random()
    
    if(RANDOM_VALUE >= THRESHOLD):
        OCURRENCE = "Active"
        TIMESTAMP = "Stop"
        RFID_STATE = "On"
        RANDOM_VALUE = 0
        #Seafood insertion
        seafoodRecord = Seafood.SEAFOOD(round(gaussian_generator(317, 237)), 
                                        round(gaussian_generator(138333, 99482)), 
                                        DAY, database)
        seafoodRecord.INSERTS()
        #Push specification
        INPUT.VALUE[0] = seafoodRecord.AMOUNT
        INPUT.VALUE[1] = seafoodRecord.TOTAL_AMOUNT
        INPUT.VALUE[2] = seafoodRecord.PRICE
        INPUT.VALUE[3] = seafoodRecord.TOTAL_PRICE
        INPUT.VALUE[4] = seafoodRecord.TIME
        
        TIMESTAMP = "Next"
        
    else:
        OCURRENCE = "Inactive"
        RFID_STATE = "Off"
        
#Thermometer specification
def TEMPERATURE_EMERGES():
    global THERMOMETER_STATE
    global TIMESTAMP
    global DAY
    
    #We verify simulation bounds
    if(DAY <= SIMULATION_TIME and TIMESTAMP == "Next"):
        THERMOMETER_STATE = "On"
        TIMESTAMP = "Stop"
        #Inserts Temperature
        temperatureRecord = Temperature.TEMPERATURE(round(gaussian_generator(-20, 3)), 
                                                    DAY,
                                                    database)
        temperatureRecord.INSERTS()
        
        #Push specification
        INPUT.VALUE[5] = temperatureRecord.VALUE
        INPUT.VALUE[6] = temperatureRecord.TIME
        
        TIMESTAMP = "Next"
    else: 
        THERMOMETER_STATE = "Off"

#Event message emerges specification
def EVENT_MESSAGE_EMERGES():
    global FILTER_RESULT
    for BLOCK in SUBSCRIPTION.BLOCK:
        #For each Block
        for SUBSCRIPTION_VECTOR in SUBSCRIPTION.SUBSCRIPTION:
            #For each subscription vector in SUBSCRIPTION object
            if(SUBSCRIPTION_VECTOR[0] == BLOCK):
                #IF SUBSCRIPTION ID IS EQUALS SUBSCRIPTION ID IN BLOCK
                for FILTER_ID in SUBSCRIPTION_VECTOR[1:]:
                    #For each filter ID in subscription vector
                    for FILTER_VECTOR in SUBSCRIPTION.FILTER:
                        #For each filter vector in subscription filter vector
                        TermO = 0
                        if (FILTER_VECTOR[0] == FILTER_ID):
                            #IF FILTER ID IS EQUALS TO FILTER ID IN SUBSCRIPTION VECTOR
                            Terml = 0
                            FILTER_RESULT = "True"
                            while(Terml < 7):
                                #For each attribute in Input attribute vector
                                for PREDICATE_ID in FILTER_VECTOR[1:]:
                                    #For each predicate ID in filter vector
                                    for PREDICATE_VECTOR in SUBSCRIPTION.PREDICATE:
                                        #For each predicate vector in subscription predicate vector
                                        if(PREDICATE_VECTOR[0] == PREDICATE_ID):
                                            #IF PREDICCATE ID IS EQUALS TO PREDICATE ID IN FILTER VECTOR
                                            if(INPUT.ATTRIBUTE[Terml] == PREDICATE_VECTOR[1]):
                                                #IF ATTRIBUTE IN INPUT ATTRIBUTE VECTOR IS EQUALS TO PREDICATE VECTOR INDEX 1   
                                                #Match specification
                                                if(Operator(INPUT.VALUE[Terml],PREDICATE_VECTOR[2], PREDICATE_VECTOR[3])):
                                                    OUTPUT.ATTRIBUTE.append(INPUT.ATTRIBUTE[Terml])
                                                    OUTPUT.VALUE.append(INPUT.VALUE[Terml])
                                                    if(Terml>4):
                                                        OUTPUT.PUBLISHER_ID.append(PUBLISHER.ID[0])
                                                    else:
                                                        OUTPUT.PUBLISHER_ID.append(PUBLISHER.ID[1])
                                                    TermO = TermO + 1
                                                    FILTER_RESULT = "True"
                                                else:
                                                    FILTER_RESULT = "False"
                                                    while(TermO > 0):
                                                        OUTPUT.ATTRIBUTE.pop()
                                                        OUTPUT.VALUE.pop()
                                                        OUTPUT.PUBLISHER_ID.pop()
                                                        TermO = TermO - 1
                                                    break;
                                    if(FILTER_RESULT == "False"):
                                        break;
                                if(FILTER_RESULT == "False"):
                                    break;
                                Terml = Terml + 1
                            #Publish specification
                            if(Terml >= 7 and FILTER_RESULT == "True"):
                                OUTPUT.SUBSCRIPTION_ID.append(SUBSCRIPTION_VECTOR[0])
                                OUTPUT.printOutput(TermO)
#Operator                                          
def Operator(leftVariable, operator, rightVariable):
    if(operator == "<"):
        if(leftVariable < rightVariable):
            return True
        else:
            return False
    if(operator == ">"):
        if(leftVariable > rightVariable):
            return True
        else:
            return False
    if(operator == "="):
        if(leftVariable == rightVariable):
            return True
        else:
            return False
    if(operator == "!="):
        if(leftVariable != rightVariable):
            return True
        else:
            return False
    if(operator == "<="):
        if(leftVariable <= rightVariable):
            return True
        else:
            return False
    if(operator == ">="):
        if(leftVariable >= rightVariable):
            return True
        else:
            return False
                    
          
def gaussian_generator(mean, dest):
    #Box-Muller method
    U1 = random.uniform(0,1) #Uniform variable 1 [0, 1]
    U2 = random.uniform(0,1) #Uniform variable 2 [0, 1]
    Z = math.sqrt((-2*math.log(U1)))*math.cos(2*math.pi*U2) #Standard normal distribution mean = 0 dest = 1
    return Z*dest + mean + dest*2.698