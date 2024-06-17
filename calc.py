class Calculator:

    def __init__(self):
        self.a = float(input("entre your first no\n")) 
        self.b = float(input("entre your second no\n"))
        self.menu()


    def menu (self):
        user_input=input("""
                        hello, how would you like to perform calculation
                         1. Enter 1 for Addition Operator
                         2. Enter 2 for subtraction Operator
                         3. Enter 3 for Multiplication Operator
                         4. Enter 4 for Division Operator
                         5. Enter 5 for Module Operator 
                         """)
        if user_input=="1":
            result  = "Sum of given numbers is " + str(self.add() )
    
        elif user_input=="2":
            result = "subraction of given number is "+ str(self.sub())
        elif user_input=="3":
            result= "Multplication of given number is" + str(self.mult()) 
        elif user_input=="4":
             result = "Division of given number is "+ str(self.div())
        elif user_input=="5" :
             result = "Module of given number is "+ str(self.module())
        print(result)


    def add(self):
        return(self.a+ self.b)


    def sub(self):
        return(self.a- self.b)


    def mult(self):
        return(self.a* self.b)


    def div(self):
        return(self.a/ self.b)


    def module(self):
        return(self.a% self.b)