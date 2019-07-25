from . import WarehouseMonitoringSystem
class SUBSCRIPTION:
    def __init__(self):
        self.SUBSCRIPTION = [] #Subscription subscription vector
        self.FILTER = [] #Subscription filter vector
        self.PREDICATE = [] #Subscription predicate vector
        self.BLOCK = [] #Subscription block vector    
        self.ID_SUSCRIBER = [] #SUSCRIBER ID REFERENCE FROM SUSCRIBER ENTITY

    def CREATES(self):
        #Push into subscription vector specification
        WarehouseMonitoringSystem.NEW_FILTER_STATE = "Yes"
        WarehouseMonitoringSystem.NEW_PREDICATE_STATE = "Yes"
        
        self.ID_SUSCRIBER.append(1) #SUSCRIBER ID!
        
        self.SUBSCRIPTION.append([]) #We create a new subscription vector
    
        #We save the SUBSCPRITION ID IN FIRST POSITION AT THE SUBSCRIPTION VECTOR
        self.SUBSCRIPTION[len(self.SUBSCRIPTION)-1].append(WarehouseMonitoringSystem.TermB + 1)
        
        #Push into block vector specification
        self.BLOCK.append(self.SUBSCRIPTION[len(self.SUBSCRIPTION)-1][0])#We insert the new subscription ID in block vector
        
        WarehouseMonitoringSystem.TermS = 1
        #Push into subscription vector specification
        while(WarehouseMonitoringSystem.NEW_FILTER_STATE == "Yes"):
            #Push into filter vector specification
            self.FILTER.append([])
            if(len(self.SUBSCRIPTION[len(self.SUBSCRIPTION)-1])==1): 
                #If we don't have any filter yet in the subscription
                if(len(self.SUBSCRIPTION)==1):
                    #If is the first subscription, we assigne filter ID in 1
                    self.FILTER[len(self.FILTER)-1].append(1)
                else:
                    #If is the n subscription, we assigne the last filter ID of n-2 subscription plus 1
                    self.FILTER[len(self.FILTER)-1].append(self.SUBSCRIPTION[len(self.SUBSCRIPTION)-2][len(self.SUBSCRIPTION[len(self.SUBSCRIPTION)-2])-1] + 1)
            else:
                #If we have at least one filter in current filter vector, we just put the last current subscription filter ID plus 1
                self.FILTER[len(self.FILTER)-1].append(self.SUBSCRIPTION[len(self.SUBSCRIPTION)-1][WarehouseMonitoringSystem.TermS-1]+1)
            
            WarehouseMonitoringSystem.TermS = WarehouseMonitoringSystem.TermS + 1
            #We push the filter ID at the end of subscription vector
            self.SUBSCRIPTION[len(self.SUBSCRIPTION)-1].append(self.FILTER[len(self.FILTER)-1][0])
            
            WarehouseMonitoringSystem.TermF = 1
            #Push into filter vector specification
            while(WarehouseMonitoringSystem.NEW_PREDICATE_STATE == "Yes"):
                
                #Push predicate [0] specification
                self.PREDICATE.append([])
                if(len(self.FILTER[len(self.FILTER)-1])==1):
                    #if we don't have any predicate yet in the filter
                    if(len(self.FILTER)==1):
                        #if is the first filter, we assigne predicate ID in 1
                        self.PREDICATE[len(self.PREDICATE)-1].append(1)
                    else:
                        #if is the n filter, we assigne the last predicate ID of n-2 filter plus 1
                        self.PREDICATE[len(self.PREDICATE)-1].append(self.FILTER[len(self.FILTER)-2][len(self.FILTER[len(self.FILTER)-2])-1]+1)
                else:
                    #If we have at least one predicate in current predicate vector, we just put the last current filter predicate ID plus 1
                    self.PREDICATE[len(self.PREDICATE)-1].append(self.FILTER[len(self.FILTER)-1][WarehouseMonitoringSystem.TermF-1]+1)
                
                #Subscriber selects predicate input name (Index 1)
                self.PREDICATE[len(self.PREDICATE)-1].append(self.SELECTS_PREDICATE_INDEX_1())
                #Subscriber selects predicate logical operator (Index 2)
                self.PREDICATE[len(self.PREDICATE)-1].append(self.SELECTS_PREDICATE_INDEX_2())
                #Inserts predicate value (Index 3)
                self.PREDICATE[len(self.PREDICATE)-1].append(self.INSERTS_PREDICATE_INDEX_3())
                
                WarehouseMonitoringSystem.TermF = WarehouseMonitoringSystem.TermF + 1
                #We push the predicate ID at the end of filter vector
                self.FILTER[len(self.FILTER)-1].append(self.PREDICATE[len(self.PREDICATE)-1][0])
                
                self.SELECTS_NEW_PREDICATE_STATE()

            #Interface interaction
            self.SELECTS_NEW_FILTER_STATE()
       
        WarehouseMonitoringSystem.TermB = WarehouseMonitoringSystem.TermB + 1
        self.printSubsciption()
        
    
    #Interface interaction
    def SELECTS_NEW_FILTER_STATE(self):  

        if(input("SELECT NEW_FILTER_STATE \n(1) Yes \n(0) No\n")==str(1)):
            WarehouseMonitoringSystem.NEW_FILTER_STATE = "Yes"
            WarehouseMonitoringSystem.NEW_PREDICATE_STATE = "Yes"
        else:
            WarehouseMonitoringSystem.NEW_FILTER_STATE = "No"
    
    #Interface interaction
    def SELECTS_NEW_PREDICATE_STATE(self):    
        if(input("SELECT NEW_PREDICATE_STATE \n(1) Yes \n(0) No\n")==str(1)):
            WarehouseMonitoringSystem.NEW_PREDICATE_STATE = "Yes"
        else:
            WarehouseMonitoringSystem.NEW_PREDICATE_STATE = "No"
     
    #Interface interaction
    def SELECTS_PREDICATE_INDEX_1(self):
        while(True):
            print("SELECT SUBSCRIPTION.PREDICATE[1]") #Interface interaction
            i = 0
            for attribute in WarehouseMonitoringSystem.INPUT.ATTRIBUTE:
                print("(",i,")",attribute)#Interface interaction
                i+=1
            selection = int(input())
            if(selection>=0 and selection<len(WarehouseMonitoringSystem.INPUT.ATTRIBUTE)):
                return WarehouseMonitoringSystem.INPUT.ATTRIBUTE[selection]
            else:
                print("Error!") #Interface interaction
    #Interface interaction           
    def SELECTS_PREDICATE_INDEX_2(self):
        while(True):
            selection = int(input("SELECT SUBSCRIPTION.PREDICATE[2] \n| (0) < | (1) > | (2) = | (3) != | (4) <= | (5) >= | \n"))#Subscriber selects attribute
            if(selection == 0):
                return "<"
            elif(selection == 1):
                return ">"
            elif(selection == 2):
                return "="
            elif(selection == 3):
                return "!="
            elif(selection == 4):
                return "<="
            elif(selection == 5):
                return ">="
            else:
                print("Error!") #Interface interaction
    
    #Interface interaction
    def INSERTS_PREDICATE_INDEX_3(self):
        value = float(input("INSERT SUBSCRIPTION.PREDICATE[3] = ")) #Subscriber inserts value
        return value
    
    def printSubsciption(self):
        
        #MERGE DUPLICATED PREDICATES AND FILTERS
        self.mergePredicates()
        self.mergeFilters()
        #END MERGER
        
        stringBlock = "["
        stringSubscription = ""
        stringFilters = ""
        stringPredicate = ""
        for subs in self.BLOCK:
            stringBlock += " S" + str(subs)
        stringBlock += " ]\n"
        for subscriptionVector in self.SUBSCRIPTION:
            stringSubscription += "["
            for i in range(0,len(subscriptionVector)):
                if(i == 0):
                    stringSubscription += " S" + str(subscriptionVector[i])
                else:
                    stringSubscription += " F" + str(subscriptionVector[i])
            stringSubscription += " ]\n"
        for filterVector in self.FILTER:
            stringFilters +="["
            for i in range(0,len(filterVector)):
                if(i == 0):
                    stringFilters += " F" + str(filterVector[i])
                else:
                    stringFilters += " P" + str(filterVector[i])
            stringFilters += " ]\n"
        for predicateVector in self.PREDICATE:
            stringPredicate +="["
            for i in range(0, len(predicateVector)):
                if(i == 0):
                    stringPredicate += " P" + str(predicateVector[i])
                else:
                    stringPredicate += " " + str(predicateVector[i])
            stringPredicate += " ]\n"
        print("BLOCK:")
        print(stringBlock)
        print("SUBSCRIPTION:")
        print(stringSubscription)
        print("FILTER:")
        print(stringFilters)
        print("PREDICATE:")
        print(stringPredicate)
        
    def mergePredicates(self):
        i = 0
        while(i<len(self.PREDICATE)):
            j = i + 1
            while(j<len(self.PREDICATE)):
                equalPredicates = True
                for k in range(1, len(self.PREDICATE[j])):
                    if(self.PREDICATE[i][k] != self.PREDICATE[j][k]):
                        equalPredicates = False
                        break
                if equalPredicates:
                    for filterVector in self.FILTER:
                        for l in range(1, len(filterVector)):
                            if(self.PREDICATE[j][0] == filterVector[l]):
                                filterVector[l] = self.PREDICATE[i][0]
                    self.PREDICATE.pop(j)
                else:
                    j += 1
            i += 1
    
    def mergeFilters(self):
        i = 0
        while(i<len(self.FILTER)):
            j = i + 1
            while(j<len(self.FILTER)):
                equalFilters = True
                #PREDICATE IN FILTER 1
                for k in range (1, len(self.FILTER[i])):
                    predicateInFilter2 = False
                    #PREDICATE IN FILTER 2
                    for l in range(1, len(self.FILTER[j])):
                        if(self.FILTER[j][l] == self.FILTER[i][k]):
                            predicateInFilter2 = True
                            break
                    if predicateInFilter2 == False:
                        equalFilters = False
                        break
                if equalFilters:
                    for subscriptionVector in self.SUBSCRIPTION:
                        for m in range(1, len(subscriptionVector)):
                            if(self.FILTER[j][0] == subscriptionVector[m]):
                                subscriptionVector[m] = self.FILTER[i][0]
                    self.FILTER.pop(j)
                else:
                    j += 1
            i += 1