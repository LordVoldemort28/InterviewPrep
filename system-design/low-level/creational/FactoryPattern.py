"""
Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, 
but lets subclasses decide which class or object to instantiate. Using the Factory method, we have the best ways to create an object. 
Here, objects are created without exposing the logic to the client, and for creating the new type of object, 
the client uses the same common interface.

Advantage
1. We can easily add new types of products without disturbing the existing client code.
2. Generally, tight coupling is being avoided between the products and the creator classes and objects.

Disadvantage 
1. To create a particular concrete product object, the client might have to sub-class the creator class. try to define config class. 
2. You end up with a huge number of small files i.e, cluttering the files.
"""
class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer():
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta","cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer():
    """Simply return the same message"""

    def localize(self, msg):
        return msg

def FactorySource(language):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

class LocalizerService:
    
    def __init__(self, factorySource):
        self.factorySource = factorySource
    
    def getLocalizer(self, language):
        return self.factorySource(language)

if __name__ == "__main__":
    
    localizerService = LocalizerService(FactorySource)
    
    f = localizerService.getLocalizer("French")
    e = localizerService.getLocalizer("English")
    s = localizerService.getLocalizer("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
