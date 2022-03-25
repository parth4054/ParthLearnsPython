class Computer:

    def __init__(self, cpu, ram):
        self.computer_cpu = cpu
        self.computer_ram = ram

    def config(self):
        print("The configuration is ", self.computer_cpu, self.computer_ram)


com1 = Computer("i5", 8)
com2 = Computer("i7", 16)

com1.config()
com2.config()





