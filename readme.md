# Coffee Maker Project

## Description
This is a simple Coffee Maker program written in Python. It allows users to order coffee, insert coins to pay, and receive change accordingly. The machine keeps track of available resources and provides a report when requested.

## Features
- Users can order `espresso`, `latte`, or `cappuccino`.
- The machine checks if there are enough ingredients before making the drink.
- Users insert coins (`quarters`, `dimes`, `nickels`, `pennies`) to pay.
- If sufficient payment is provided, the drink is served, and change is returned.
- If ingredients are insufficient, an appropriate message is displayed.
- Users can type `report` to check the remaining resources.
- Users can type `off` to turn off the machine.

## How to Run
1. Install Python (if not already installed).
2. Save the script as `coffee_maker.py`.
3. Open a terminal or command prompt and navigate to the script's location.
4. Run the script using:
   ```sh
   python coffee_maker.py
   ```
5. Follow the on-screen prompts to order coffee.

## Coin Values
- Quarter: $0.25
- Dime: $0.10
- Nickel: $0.05
- Penny: $0.01


## Example Usage
```
WELCOME TO THE COFFEE MAKER
What would you like(latte/cappuccino/espresso): latte
Please insert coins
How many Quarters: 10
How many Dimes: 5
How many Nickels: 2
How many Pennies: 0
Here is 2.75 in change.
Here is your drink latte. Enjoy!
```

## Known Issues
- The program does not validate non-numeric inputs for coins.
- Spelling mistakes (`ingriedients` should be `ingredients`, `cofee` should be `coffee`).
- The `order()` function is recursive, which may cause a stack overflow if used extensively. Using a loop is recommended.

## Future Improvements
- Improve input validation.
- Refactor `order()` to use a loop instead of recursion.
- Implement a graphical interface.

## Author
This project was created for learning Python basics and simulating a simple coffee machine system.

