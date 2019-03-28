# class in object oriented programming


class computer:

    def config(self, cpu, ram, brand):

        print (self.cpu, self.ram, self.brand)

        print ("i5", "32gb", "10gb Ram")


comp1 = computer()
comp2 = computer()
# computer.config(comp1)

comp1.config()
comp2.config("i3", "32", "hp")