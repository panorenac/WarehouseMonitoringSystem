class TEMPERATURE:
    def __init__ (self, value, time, database):
        self.TIME = time #Measurement time measured in days
        self.VALUE = value #Temperature value measured in Celsius
        #We reference the database were the objects will be allocated
        self.database = database
    
    def INSERTS(self):
        self.database.insert(self, "Temperature")