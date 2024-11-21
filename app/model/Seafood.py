#Seafood class is a representation of 
class SEAFOOD:
    
    def __init__ (self, amount, price, time, database):
        self.ID = database.seafoodId #Seafood unique identificator
        database.seafoodId = database.seafoodId + 1 #We increase the 
        self.AMOUNT = amount #Seafood amount measured in tons
        self.PRICE = price #Seafood price measured in CA
        self.TIME = time #Seafood arrival day
        #Total seafood amount in warehouse measured in tons
        self.TOTAL_AMOUNT = database.query("MAX of Seafood.total_amount") + amount
        #Total seafood price in warehouse measured in CA
        self.TOTAL_PRICE = database.query("MAX of Seafood.total_price") + price
        #We reference the database were the objects will be allocated
        self.database = database 
        
    #Seafood insertion dynamic relationship
    def INSERTS(self):
        self.database.insert(self, "Seafood")