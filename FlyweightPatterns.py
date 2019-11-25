'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''

import abc


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    
    def operation(self, extrinsic_state):
        pass

class Client:
    def fly(self):
        flyweight_factory = FlyweightFactory()
        concrete_flyweight = flyweight_factory.get_flyweight("key")
        concrete_flyweight.operation(None)


c = Client()
c.fly()