'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''
class WaterState(object):

   name = "state"
   allowed = []

   def switch(self, state):
      if state.name in self.allowed:
         print ('Current:',self,' => switched to new state',state.name)
         self.__class__ = state
      else:
         print ('Current:',self,' => switching to',state.name,'not possible.')

   def __str__(self):
      return self.name

class Cold(WaterState):
   name = "cold"
   allowed = ['hot']

class Hot(WaterState):
   name = "hot"
   allowed = ['cold','warm']

class Warm(WaterState):
   name = "warm"
   allowed = ['on']

class Water(object):
   
   def __init__(self, model='Osmo'):
      self.model = model
      self.state = Cold()
   
   def change(self, state):
      self.state.switch(state)

if __name__ == "__main__":
   wat = Water()
   wat.change(Hot)
   wat.change(Cold)
   wat.change(Hot)
   wat.change(Warm)
   wat.change(Hot)
   wat.change(Cold)