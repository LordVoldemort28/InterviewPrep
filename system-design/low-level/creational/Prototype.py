"""
Prototype Method is a Creational Design Pattern which aims to reduce the number of classes used for an application. 
It allows you to copy existing objects independent of the concrete implementation of their classes. 
Generally, here the object is created by copying a prototypical instance during run-time. 
It is highly recommended to use Prototype Method when the object creation is an expensive 
task in terms of time and usage of resources and already there exists a similar object. 
This method provides a way to copy the original object and then modify it according to our needs.
"""
from abc import ABCMeta, abstractmethod
import copy


# class - Courses at GeeksforGeeks
class Course(metaclass=ABCMeta):

    # constructor
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)

# class - DSA course
class DSA(Course):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"

    def course(self):
        print("Inside DSA::course() method")

# class - SDE Course
class SDE(Course):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"

    def course(self):
        print("Inside SDE::course() method.")


# class - Courses At GeeksforGeeks Cache
class Cache:

    def __init__(self):
        self.cache = {}
        self.load()

    def get_course(self, sid):
        course = self.cache.get(sid, None)
        return course.clone()

    def load(self):
        sde = SDE()
        sde.set_id("SDE")
        self.cache[sde.get_id()] = sde

        dsa = DSA()
        dsa.set_id("DSA")
        self.cache[dsa.get_id()] = dsa

# main function
if __name__ == '__main__':
    cache = Cache()

    sde = cache.get_course("SDE")
    print(sde.type)
    
    sde2 = cache.get_course("SDE")
    print(sde2.type)
    
    dsa = cache.get_course("DSA")
    print(dsa.type)
