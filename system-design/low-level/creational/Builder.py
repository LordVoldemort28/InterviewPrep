class Computer:
    
    def __init__(self, computerBuilder):
        self.name = computerBuilder.name
        self.ipAddress = computerBuilder.ipAddress
    
    class ComputerBuilder:
        
        def __init__(self, name):
            self.ipAddress = None #Optional parameter
            self.name = name #Required parameter

        def setIpAddress(self, ipAddress):
            self.ipAddress = ipAddress
            return self
        
        def build(self):
            return Computer(self)
    
    
if __name__ == '__main__':
    computer: Computer = Computer.ComputerBuilder("Computer1") \
        .setIpAddress("192.168.0.1") \
        .build()
    print(computer.name, computer.ipAddress)
    
    computer: Computer = Computer.ComputerBuilder("Computer2") \
        .build()
    print(computer.name, computer.ipAddress)
