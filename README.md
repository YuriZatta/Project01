# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 01

![gif](https://media.giphy.com/media/67ThRZlYBvibtdF9JH/giphy.gif)

| Language | Type          | Date  | Due | Author               |
| -------- | ------------- | ----- | ---- | -------------------- |
| Python   | Project 01 - The Tax Calculator | 14/06/2020 | 18/06/2020 | Yuri Vianna Nunes |

## Project Description
Project Tax Calculator.
 - This Tax Calculator accepts a wage as an impute and besides calculate the ammount of tax paid, it'll discriminate how much money per month, week, and hours it's actualy retained for the user.
 - The Tax Calculator can also check, if you add a little bit more to your income, if your new 'After-Tax Annual Income' will be worst from what you already bring home, who knows? 
 - The Tax Calculator can also tell you how much of the 'after-tax' income is needed to pay for a particular object. Example: If your annual income 'after-tax' is of 10,000.00, you will need 10 years of your life to pay for a house that costs 100,000.00. And how many years you will need to pay if you want to keep 20%, 50%, 80% of your annual income.
 - In the future The Tax Calculator will be able to detect when you highlight any number in your browser, or in your phones apps, to automaticaly calculate for you. Like Google Translator on smartphones.

### MVP/PostMVP

First I'm creating a Tax Calculator app that has classes and methods to be called within this project or from inside another Python project. From that, in the future, I'll make a webpage and smartphone application for this calculator, so it can be automaticaly called when highlighting numbers on you device.

## Functional Components


#### MVP
| Component | Priority | Estimated Time | Actual Time |
| --- | :---: |  :---: | :---: |
| Research about how UK tax works | H | 3hrs | 6hrs |
| Parent Class for Tax Calculator  | L | 2hr| 4hrs |
| Child Classes for Self-Employed| H | 1hrs | 0.5hrs |
| Check Annual, Monthly, Weekly, and Hour User Value| H | 2hrs | 2hrs |
| Check Between two Anual Incomes which one is better | M | 0.5hr | 1hr |
| User's Desired Purchase Input | L | 0.5hrs| 0.5hrs |
| Total | H | 8h30min| 14hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Django | H | 6hrs | -hr | -hr|
| HTTP | H | 6hrs | -hr | -hr|
| CSS + JavaScript | H | 12hrs | -hr | -hr|
| Input Crash Protector | H | 6hrs | -hr | -hr|
| Android App | M | 40hrs | -hr | -hr|
| Android Touch Dynamic Calculator | M | 6hrs | -hr | -hr|
| iPhone App | L | 40hrs | -hr | -hr|
| iPhone Touch Dynamic Calculator | L | 6hrs | -hr | -hr|
| Total | H | 122hrs| -hrs | -hrs |

## Additional Libraries
 None 

## Code Snippet
I'm proud of this two simple calculators that takes the result of the actual TaxCalculator, not because they are fancy, but because its something I wanted for so long to stop doing it by my self when browsing on LinkedIn...

```python
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
```

#### Tax Rules followed in this point in time!
| Income | Gate | Estimated Tax | Local |
| --- | :---: |  :---: | :---: |
| x | < 12509 | 00% | UK Non-Scotland |
| x | > 12509 | 20% | UK Non-Scotland |
| x | < 50000 | 20% | UK Non-Scotland |
| x | > 50000 | 40% | UK Non-Scotland |
| x | < 15000 | 40% | UK Non-Scotland |
| x | > 15000 | 45% | UK Non-Scotland |
| --- | :---: |  :---: | :---: |
| Income | Gate | National Insurance | Type |
| x | < 9516 | 00% | Employed |
| x | > 9516 | 12% | Employed |
| x | < 50024 | 12% | Employed |
| x | > 50024 | 02% | Employed |
| --- | :---: |  :---: | :---: |
| x | < 9500 | 00% | Self-Employed |
| x | > 9500 | 09% | Self-Employed |
| x | < 50000 | 09% | Self-Employed |
| x | > 50000 | 02% | Self-Employed |

### User Manual
### TaxCalculator:
1. Method to input brut annual income
     * `def brut_income(self, wage):`
        * Accepts only integer data: 12500
        * The value returned is used by other methods, does not output anything
     * this methos will take care of your National Insurance and Tax for London
     
2. Method that will break down your liquid income by year, month, week, day and hours
    * `def liquid_income(self):`
        *  require print()

3. Method to check how much time do you need to buy something
     * `def how_long(self, budget, price):` 
        * require print()
        * accepts your brut annual income as budget and the price of the object

4. Method to help you to decide if you should accept more money or not
     * `def promotion_compare(self, today, tomorrow):`
        * require print()
        * accepts a brut annual income for today and the brut annual income for tomorrow

### SelfEmployed:
1. It's just a child class that change some National Insurance values
     * uses all the methods from TaxCalculator: 

### TaxList:
1. It's just a child class that prints a list of all brut income and their respectives liquid incomes
     * `def get_list(self):` 
        * No action required, automatically generates a list from 12500 to 150000
     
![gif](https://media.giphy.com/media/ND6xkVPaj8tHO/giphy.gif)