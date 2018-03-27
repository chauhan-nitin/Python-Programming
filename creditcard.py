#-------------------------------------------------------------------------------------------------------#
#_____________________________________ QUESTION ____________________________________________________#
#-------------------------------------------------------------------------------------------------------#

#Python class definition for a simple credit card class, named CreditCard with the following functionality
#Class definition for implemented CreditCard
class CreditCard:
    #Creating an empty list to hold values
    all_cc = []
    
    #Code for constructor function __init__
    def __init__(self, name, bank, ac_id, limit):
        #Creating new CreditCard for card holder 'name'
        self.__name = name
        self.__bank = bank
        self.__acid = ac_id
        self.__limit = limit
        self.__balance = limit
        CreditCard.all_cc.append(self) #Appending each cardholder details in list

    #Code for function get_balance
    def get_balance(self):
        return self.__balance

    #Code for function get_bank
    def get_bank(self):
        return self.__bank

    #Code for function get_accountid
    def get_accountid(self):
        return self.__acid

    #Code for function get_limit
    def get_limit(self):
        return self.__limit

    #Code for function get_name
    def get_name(self):
        return self.__name

    #Code for function charge(price)
    def charge(self, price):
        if (price>self.__limit):
            #transaction can't be processed
            return False
        else:
            self.__balance = self.__balance - price
            #transaction successful
            return True
        
    #Code for function make_payment(amount)
    def make_payment(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance

    #Code for function show_summary
    def show_summary(self):
        creditcards = sorted(CreditCard.all_cc,\
                             key = lambda x: x.__name, reverse=False) #sorting based on Name
        for cc in creditcards:
            print("Name:",cc.__name, "Bank:",cc.__bank, "Account ID:",cc.__acid, "Limit:",cc.__limit, "Balance:",cc.__balance)
        print("\n")

#Creating class objects to call class functions
cc1 = CreditCard("Nitin","BOI",117220,1500)
cc2 = CreditCard("Divyesh","AIB",107220,2500)
cc3 = CreditCard("Pratik","BOI",117110,2500)
cc4 = CreditCard("Abhay","BOI",118220,1200)
cc5 = CreditCard("Abhinav","AIB",106110,2500)
cc1.charge(800)
cc1.make_payment(800)
cc1.charge(1000)
cc1.charge(600)
cc1.show_summary()
