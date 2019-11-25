'''
Created on 22 nov. 2019

@author: Cecy Rodríguez
'''
#AbstractFactory

from abc import ABC, abstractmethod

class InstrumentFactory(ABC):
    @abstractmethod
    def Create_windInstruments(self):
        pass
    
    def Create_stringInstruments(self):
        pass
    
class SopranosFactory(InstrumentFactory):
    def Create_windInstruments(self):
        return Clarinet()
    
    def Create_stringInstruments(self):
        return Harp()

class BaritonosFactory(InstrumentFactory):
    def Create_windInstruments(self):
        return Saxophone() 
    
    def Create_stringInstruments(self):
        return Cello()
    
class WindInstrument(ABC):
    def HumanBlow(self):
        pass
    
    def MechanicalBlow(self):
        pass
    
class StringInstrument(ABC):
    @abstractmethod
    def rub(self):
        pass
    
    def dot(self):
        pass
    
class Clarinet(WindInstrument):
    def HumanBlow(self):
        print ('Clarinet HumanBlow called')
    
    def MechanicalBlow(self):
        print ('Clarinet MechanicalBlow called')

class Saxophone(WindInstrument):
    def HumanBlow(self):
        print ('Saxophone HumanBlow called')
    
    def MechanicalBlow(self):
        print ('Saxophone MechanicalBlow called')
        
class Harp(StringInstrument):
    def rub (self):
        print ('Harp rub called')
        
    def dot(self):
        print ('Harp dot called')
        
class Cello(StringInstrument):
    def rub (self):
        print ('Cello rub called')
        
    def dot(self):
        print ('Cello dot called')
        
class Client:
    def getInstrument(self):
        abs_factory = SopranosFactory()
        
        ins_factory = abs_factory.Create_windInstruments()
        ins_factory.HumanBlow()
        ins_factory.MechanicalBlow()
        
        ins_factory = abs_factory.Create_stringInstruments()
        ins_factory.rub()
        ins_factory.dot()
        
        abs_factory = BaritonosFactory()
        
        ins_factory = abs_factory.Create_windInstruments()
        ins_factory.HumanBlow()
        ins_factory.MechanicalBlow()
        
        ins_factory = abs_factory.Create_stringInstruments()
        ins_factory.rub()
        ins_factory.dot()
        
c = Client()
c.getInstrument()
        
        
        
        
        
        
        
    
    
    
    
