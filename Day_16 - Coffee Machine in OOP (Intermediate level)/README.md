# Coffee Machine in Object Oriented Programming Language (OOP)
### Overview: ###
Programmed a coffee machine in Object Oriented Programming Language (OOP). 

<p align="center">
  <img src="https://github.com/w-diana/100_days_Python_Challenge/blob/main/Day_15%20-%20Coffee%20Machine%20(Intermediate%20level)/picture.jpeg" width="300">
</p>

### Coffee Machine Program Requirements: ###
#### 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ” ####
- Check the user’s input to decide what to do next.
- The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
  
#### 2. Turn off the Coffee Machine by entering “ off ” to the prompt. ####
- For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
  
#### 3. Print report. ####
- When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g. <br />
Water: 100ml <br/>
Milk: 50ml <br/>
Coffee: 76g <br/>
Money: $2.5 <br/>

#### 4. Check resources sufficient? ####
- When the user chooses a drink, the program should check if there are enough resources to make that drink.
- E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
- The same should happen if another resource is depleted, e.g. milk or coffee.
  
#### 5. Process coins. ####
- If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
- Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
- Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
  
#### 6. Check transaction successful? ####
- Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “ Sorry that's not enough money. Money refunded. ”.
- But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. <br />
Water: 100ml <br/>
Milk: 50ml <br/>
Coffee: 76g <br/>
Money: $2.5 
- If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
  
#### 7. Make Coffee. ####
- If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources. E.g. <br/> report before purchasing latte: <br/>
Water: 300ml <br/>
Milk: 200ml <br/>
Coffee: 100g <br/>
Money: $0 <br/><br/>
Report after purchasing latte: <br />
Water: 100ml <br/>
Milk: 50ml <br/>
Coffee: 76g <br/>
Money: $2.5
- Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.




### Classes, Attributes & Methods ###
#### MenuItem Class ####
Attributes:
- name
(str) The name of the drink.
e.g. “latte”
- cost
(float) The price of the drink.
e.g 1.5
- ingredients
(dictionary) The ingredients and amounts required to make the drink.
e.g. {“water”: 100, “coffee”: 16}
#### Menu Class ####
Methods:
- get_items()
Returns all the names of the available menu items as a concatenated string.
e.g. “latte/espresso/cappuccino”
- find_drink(order_name)
Parameter order_name: (str) The name of the drinks order.
Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
otherwise returns None.
#### CoffeeMaker Class ####
Methods:
- report()
Prints a report of all resources.
e.g.
Water: 300ml
Milk: 200ml
Coffee: 100g
- is_resource_sufficient(drink)
Parameter drink: (MenuItem) The MenuItem object to make.
Returns True when the drink order can be made, False if ingredients are insufficient.
e.g.
True
- make_coffee(order)
Parameter order: (MenuItem) The MenuItem object to make.
Deducts the required ingredients from the resources.
#### MoneyMachine Class ####
Methods:
- report()
Prints the current profit
e.g.
Money: $0
- make_payment(cost)
Parameter cost: (float) The cost of the drink.
Returns True when payment is accepted, or False if insufficient.
e.g. False
