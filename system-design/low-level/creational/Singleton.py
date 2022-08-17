"""
Singleton Method is a type of Creational Design pattern and is one of the simplest design patterns
available to us. It is a way to provide one and only one object of a particular type. 
It involves only one class to create methods and specify the objects. 
Singleton Design Pattern can be understood by a very simple example of Database connectivity. 
When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant 
connections which can be easily done by Singleton Design Pattern.

1. Controlling over global variables: In the projects where we specifically 
need strong control over the global variables, it is highly recommended to use Singleton Method

2. Daily Developers use: Singleton patterns are generally used in providing the logging, 
caching, thread pools, and configuration settings and are often 
used in conjunction with Factory design patterns.
"""
# classic implementation of Singleton Design pattern
class Singleton:

    __shared_instance = 'GeeksforGeeks'

    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'GeeksforGeeks':
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'GeeksforGeeks':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self


# main method
if __name__ == "__main__":

    # create object of Singleton Class
    obj = Singleton()

    # pick the instance of the class
    obj = Singleton.getInstance()
    
    #Check if both objects are same
    print(obj == obj)
    
    #Try to create to singleton class again
    try:
        obj = Singleton()
    except:
        print("exception occurred")

