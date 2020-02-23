class car:
    def __init__(self, color='red', speed=220): # default value
        self.color = color
        self.speed = speed
        print(self.color)
        print(self.speed)

honda = car()
toyota = car('green', 240)

print('=================================================================')

class car2:
    def __init__(self, *args): # multiple arguments. it returns tuple
        self.args = args
        for item in args:
            print(item)

ford = car2()
hyundai = car2('df','cd','ab')


print('=================================================================')

class car3:
    def __init__(self, **args): # it accepts dictionary : key- value pair
        self.args = args
        for keys in args.keys():
            print (keys, "=",args[keys])


chevy = car3(name='chevrolet', color='Red')
#bmw = car3(name='BMW')

print('=================================================================')

class car4:
    def __init__(self, *argmnt, **args): # it accepts dictionary : key- value pair
        self.argmnt = argmnt
        self.args = args
        for keys in args.keys():
            print (keys, "=",args[keys])


chevy = car4(name='chevrolet', color='Red')
#bmw = car3(name='BMW')





