class Temp:

    def __init__(self, value=0, choice=''):
        self.value = value

    def KtoC(self, value):
        ktoc = 274.15 - self.value
        return ktoc

    def KtoF(self, value):
        ktof = self.value * (9/5) - 459.67
        return ktof

    def CtoK(self, value):
        ctok = self.value + 274.15
        return ctok

    def CtoF(self, value):
        ctof = self.value * 1.8000 + 32.00
        return ctof

    def FtoK(self, value):
        ftok = (self.value + 459.67) * (5/9)
        return ftok

    def FtoC(self, value):
        ftoc = (self.value -32) * (5/9)
        return ftoc

    def choice(self):


        flag1 = True
        flag2 = True
        while (flag1):
            value1 = input('Please choose the unit you want to convert (c/f/k): ')
            value2 = input('Please choose the unit you want to convert to (c/f/k): ')
            value = int(input('Please enter the value you want to be converted: '))

            if value1 == 'k' and value2 =='c':
                print(self.KtoC(value))
                while(flag2):
                    desire = input("Do you want to continue(y/n): ")
                    if(desire == 'y'):
                        flag2 = True
                        self.choice()
                    elif (desire == 'n'):
                        print("Quitting...")
                        flag2 = False
                        flag1 = False
                    else:
                        desire = input("Please select y or n: ")

            elif value1 == 'k' and value2 =='f':
                self.KtoF(value3)
                while(flag2):
                    desire = input("Do you want to continue(y/n): ")
                    if(desire == 'y'):
                        flag2 = True
                    elif (desire == 'n'):
                        print("Quitting...")
                        flag2 = False
                        flag1 = False
                    else:
                        desire = input("Please select y or n: ")
            elif value1 == 'c' and value2 =='k':
                self.CtoK(value3)
                while(flag2):
                    desire = input("Do you want to continue(y/n): ")
                    if(desire == 'y'):
                        flag2 = True
                    elif (desire == 'n'):
                        print("Quitting...")
                        flag2 = False
                        flag1 = False
                    else:
                        desire = input("Please select y or n: ")
            elif value1 == 'c' and value2 == 'f':
                self.CtoF(value3)
                while(flag2):
                    desire = input("Do you want to continue(y/n): ")
                    if(desire == 'y'):
                        flag2 = True
                    elif (desire == 'n'):
                        print("Quitting...")
                        flag2 = False
                        flag1 = False
                    else:
                        desire = input("Please select y or n: ")
            elif value1 == 'f' and value2 == 'k':
                self.FtoK(value3)
                while(flag2):
                    desire = input("Do you want to continue(y/n): ")
                    if(desire == 'y'):
                        flag2 = True
                    elif (desire == 'n'):
                        print("Quitting...")
                        flag2 = False
                        flag1 = False
                    else:
                        desire = input("Please select y or n: ")
            elif value1 == 'f' and value2 == 'c':
                self.FtoC(value3)
                while(flag2):
                    desire = input("Do you want to continue(y/n): ")
                    if(desire == 'y'):
                        flag2 = True
                    elif (desire == 'n'):
                        print("Quitting...")
                        flag2 = False
                        flag1 = False
                    else:
                        desire = input("Please select y or n: ")


def main():
    t = Temp()
    t.choice()

if __name__=='__main__':
    main()
