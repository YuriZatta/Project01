# This app don't ask any input from the user, because I have designt it
# to be called by other apps in the future. Here, you will need to call
# the class method and pass an income value, then run the code!

# Thus, I haven't implemented a While Loop to ask for the User to pass
# the right number format (int) as the Brute Income! Because I want that
# Behaviour to be implemented inside the main apps.

#If there is anyreason to use this app to ask for Users Inputs, therefor
# While Loops to avoid wrong formats. Here we have two options:

# def inputWage(message):
    # while True:
    #     try:
    #         userInput = int(input(message))
    #     except ValueError:
    #         print('Please just whole numbers without "," \
    #             or "."! Try again...')
    #         continue
    #     else:
    #         return userInput
    #         break
# User wage input
# wage = int(inputWage("\n What is your annual income?\n\t--> "))

# while True:
    #     try:
    #         pass
    #     except IOError:
    #         print("Please incert numbers without  . or ,")
        
#------------------------------------------------------------------------------

# The Tax Calculator function
class TaxCalculator:
    """
    This is a Class that creates Tax Calculators related to where you 
    live in this world.
    """

    def __init__(self, local = 'London'):
        """
        In future updates it'll be possible to choose between several 
        capitals around the world.
        """
        self.local = local
        if self.local == 'London':
            self.wage = None
            # those are the key incomes that determinates 
            # when you will pay more or less tax for London!
            self.minimum_wage = 12509
            self.medium_wage = 50001
            self.high_wage = 150000
            self.national_insurance_min = 183*52
            self.national_insurance_med = 962*52
            self.national_insurance_max = (962*52)+1
            self.tax_45 = (45/100)
            self.tax_40 = (40/100)
            self.tax_20 = (20/100)
            self.ni_tax_above_min = (12/100)
            self.ni_tax_above_max = (2/100)

    # a Getter
    def liquid_income(self):
        """
        This method takes the results of the .brut_income() method, 
        and divide the User's Liquid Income into months, weeks, days, 
        and hours. So the user can have a better understanding of how 
        much is the true value of his time at the point of view of the 
        specific role he's thinking of applying his CV.
        """
        # what the user may expect to have by year
        annual = round(self.annual_income,2)
        year = (f"\n\t Your annual income after tax is: {annual} "+"\n")
        
        # what the user may expect to have by month
        self.month_income = round((self.annual_income/12),2)
        month = f"\n\t Your liquid monthly income is: {self.month_income}"
        
        # what the user may expect to have by week
        self.week_income = round((self.annual_income/52),2)
        week = f"\n\t Your liquid weekly income is: {self.week_income}"
        
        # what the user may expect to have by day
        self.day_income = round((self.week_income/5),2)
        day = f"\n\t Your liquid daily income is: {self.day_income}"
        
        # what the user may expect to have by hour
        self.hour_income = round((self.day_income/8),2)
        hour = f"\n\t Your liquid hour value is around: {self.hour_income}\n\n"
        
        return year+month+week+day+hour

    # a Getter
    def promotion_compare(self, today, tomorrow):
        """
        This method takes two arguments, the User's today income,
        and the User's tomorrow opportunity. If the User's today income 
        generates better After-Tax Income, he'll be alerted to re-think 
        the new proposal. 
        If the new income generates more After-Tax Income, the user will
        be advised to accept.
                Ex.: Some one who have only 12k/year, should accept 
                12.5k, but be carefull to accept 12.501/year. 
        """
        self.today = self.brut_income(today)
        self.tomorrow = self.brut_income(tomorrow)

        if self.today > self.tomorrow:
            return ("\n\tIf you accept the new job/income, "+
                    "you will end up having a lower After-Tax-Income!"+
                    f"\n\tToday you earn: {self.today}\n\t"+
                    f"If you accept you will drop to: {self.tomorrow}\n")
        else:
            return (f"\n\tIt seems safe to grab this new opportunity!"+
                    f"\n\tToday you earn: {self.today}"+
                    f"\n\tIf you accept you will jump to: {self.tomorrow}\n")

    # a Getter
    def how_long(self, budget, price):
        """
        A method to help the user check how long it'll take him to buy 
        something, like a house, or a new Mac Pro!
        """
        self.budget = self.brut_income(budget)
        self.price = price

        no_savings = round((self.price/self.budget),2)
        saving_90 = round((self.price/(self.budget*0.1)),2)
        saving_75 = round((self.price/(self.budget*0.25)),2)
        saving_50 = round((self.price/(self.budget*0.5)),2)
        saving_25 = round((self.price/(self.budget*0.75)),2)
        saving_10 = round((self.price/(self.budget*0.9)),2)

        return (f"\n\tYour liquid income is: {self.budget} !"+
                f"\n\tIf you want to buy something that costs: {self.price}"+
                f"...\n\tYou would need to spend {no_savings} years of "+
                f"your life without having any other dispenses After Tax."+
                f"\n\tIf you plan to save 90% of your liquid income and "+
                f"reserves only 10% as budget, you'll need: {saving_90} "+
                f"years of your life.\n\tIf you can affor to save only "+
                f"75% and use the other 25% as budget, "+
                f"you'll need: {saving_75}.\n\tIf you plan to save 50% "+
                f"of your liquid income and use the other half as the "+
                f"budget, you'll need: {saving_50}.\n\tIf you are lucky"+
                f" enough to only need 25% of your liquid income for "+
                f"other expanses and use 75% as a budget, "+
                f"you'll need: {saving_25} years of your life.\n\tIf you "+
                f"can survive with only 10% of your liquid income, "+
                f"using 90% as budget, you'll need: {saving_10} years of "+
                "your life.\n")


    # a Setter
    def brut_income(self, wage):
        """
        This method is the actual Tax Calculator. It sort out how much 
        will be your real Liquid Income after tax!
        The code decides how much tax the User needs to pay comparing 
        with the instance variables inside the __init__() method!
        """
        self.wage = wage
        real_min  = (self.minimum_wage)
        real_med  = (self.medium_wage-2)
        real_high = (self.high_wage-1)
        ni_min = self.national_insurance_min-1
        ni_med = self.national_insurance_med-2
        ni_max = self.national_insurance_max-3
        
        if self.wage >= self.high_wage:
            high_tax = (self.wage - real_high)*self.tax_45
            med_tax = (real_high - real_med)*self.tax_40
            low_tax = (real_med - real_min)*self.tax_20
            top_ni = (self.wage - ni_max)*self.ni_tax_above_max
            med_ni = (ni_med-ni_min)*self.ni_tax_above_min
            ni_total = (top_ni+med_ni)
            # To better read how many tax levels are being subtracted 
            # I decided to leave as one line, instead of add all tax in
            # one single variable!
            self.annual_income = (self.wage - high_tax - med_tax - low_tax - ni_total)
            
            # To avoid huge floating numbers I decided to use round(,2)!
            return round(self.annual_income,2)

        elif self.wage >= self.medium_wage:
            med_tax = (self.wage - real_med)*self.tax_40
            low_tax = (real_med - real_min)*self.tax_20
            top_ni = (self.wage - ni_max)*self.ni_tax_above_max
            med_ni = (ni_med-ni_min)*self.ni_tax_above_min
            ni_total = (top_ni+med_ni)
            self.annual_income = (self.wage - med_tax - low_tax - ni_total)
            return round(self.annual_income,2)

        elif self.wage > self.minimum_wage:
            low_tax = (self.wage - real_min)*self.tax_20
            l_ni = (self.wage - ni_min)*self.ni_tax_above_min
            self.annual_income = (self.wage - low_tax - l_ni)  
            return round(self.annual_income,2)
        
        elif self.wage > self.national_insurance_min:
            l_ni = (self.wage - ni_min)*self.ni_tax_above_min
            self.annual_income = (self.wage-l_ni)
            return round(self.annual_income,2)

        else:
            self.annual_income = self.wage
            return self.annual_income
        

#------------------------------------------------------------------------------

# Self Employed!
class SelfEmployed(TaxCalculator):
    """
    This child class of TaxCalculator modifies some original tax gates
    to the rules applied for the Self Employeed, and let us quickly
    change any other limits if something change eventually!
    """
    def __init__(self, local='London'):
        super().__init__(local=local)
        self.local = local
        if self.local == 'London':
            self.wage = None
            # those are the key incomes that determinates 
            # when you will pay more or less tax for London!
            self.minimum_wage = 12509
            self.medium_wage = 50001
            self.high_wage = 150000
            self.national_insurance_min = 9500
            self.national_insurance_med = 50000
            self.national_insurance_max = 50001
            self.tax_45 = (45/100)
            self.tax_40 = (40/100)
            self.tax_20 = (20/100)
            self.ni_tax_above_min = (9/100)
            self.ni_tax_above_max = (2/100)


#------------------------------------------------------------------------------

# Tax List!
class TaxList(TaxCalculator):
    """
    This child class of TaxCalculator simply print a list of possible 
    results between Brute Income and Liquid Income!
    """

    def get_list(self):
        """
        This prints a list of all possible Liquid Incomes, in a range of 
        wages that affect your amount of tax payd. For easy context 
        visualization.
        """
        self.mini_wage = self.minimum_wage - 9
        self.max_wage = self.high_wage
        while self.mini_wage < self.max_wage:
            self.mini_wage += 500
            if self.mini_wage > 150000:
                print("\n\tFinsh!\n")

            else:
                print("\n\t If your income was: " + str(self.mini_wage) 
                + " || You would be left with: " 
                + str(self.brut_income(self.mini_wage))+"\n")

    


# testing the code!
print('\n\n\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- BRUT TO LIQUID INCOME\n')
liquid_wage = TaxCalculator()
liquid_wage.brut_income(50000)
print(liquid_wage.liquid_income())

# comparing two wages! Can I get this promotion?
print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- PROMOTION COMPARE\n')
print(liquid_wage.promotion_compare(12500,12510))

# testing how long will take to buy something that costs 650000
# if your income is 48500 / year
print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- HOW LONG TO BUY?\n')
print(liquid_wage.how_long(48500,650000))

# testing how long will take to buy something that costs 12000
# if your income is 48500 / year
print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- HOW LONG TO BUY?\n')
print(liquid_wage.how_long(48500,12000))

# the new value of the inputed wage
print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- BRUT TO LIQUID INCOME\n')
liquid_wage = TaxCalculator()
liquid_wage.brut_income(49999)
print(liquid_wage.liquid_income())

# comparing two wages! Can I get this promotion?
print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- PROMOTION COMPARE\n')
print(liquid_wage.promotion_compare(49999,50001))

print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- HOW LONG TO BUY?\n')
print(liquid_wage.how_long(30000,650000))

print('\n\t||||||||||||||||||||||\n\tTESTING TAX CALCULATOR '+
      '- HOW LONG TO BUY?\n')
print(liquid_wage.how_long(30000,12000))

# Testing tax for regular employed
print('\n\t#@#@#@#@#@#@#@#@#@#@\n\tREGULAR-EMPLOYED 80k/year\n')

a = TaxCalculator()
a.brut_income(80000)
# print(a.brut_income(80000))
print(a.liquid_income())

# Testing tax for self employed
print('\n\t#@#@#@#@#@#@#@#@#@#@\n\tSELF-EMPLOYED 80k/year\n')

b = SelfEmployed()
b.brut_income(80000)
print(b.liquid_income())


# Testing the TaxList!
print('\n\t#@#@#@#@#@#@#@#@#@#@\n\n')
# c = TaxList()
# c.get_list()
