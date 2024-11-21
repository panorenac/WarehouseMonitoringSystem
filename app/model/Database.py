#Database management class
class Database:
    
    def __init__(self, version):
        self.name = "SEAFOOD_DATABASE" #database name
        self.version = version #database version
        self.seafood = [] #Seafood table representation in memory
        self.temperature = []#Temperature table representation in memory
        self.seafoodId = 1

    def insert(self, entity, entityClass):
        #We identify which database table is called for insertion
        if(entityClass == "Seafood"):
            #Insert in seafood table
            self.seafood.append(entity)
        elif(entityClass == "Temperature"):
            #Insert in temperature table
            self.temperature.append(entity)
        
    def query(self, body):
        if(body=="MAX of Seafood.total_amount"):
            maxTotalAmount = 0
            for seafood in self.seafood:
                if(seafood.TOTAL_AMOUNT>maxTotalAmount):
                    maxTotalAmount = seafood.TOTAL_AMOUNT
            return maxTotalAmount
        elif(body=="MAX of Seafood.total_price"):
            maxTotalPrice = 0 
            for seafood in self.seafood:
                if(seafood.TOTAL_PRICE>maxTotalPrice):
                    maxTotalPrice = seafood.TOTAL_PRICE
            return maxTotalPrice