print("   WELCOME TO THE COFFEE MAKER    ")
MENU={
    "espresso":{
        "ingriedients":{
            "water":50,
            "coffee":18
        },
        "cost":1.5
    },
    "latte":{
        "ingriedients": {
            "water": 200,
            "coffee": 24
        },
        "cost": 2.5

    },

    "cappuccino": {
        "ingriedients": {
            "water": 250,
            "milk":100,
            "coffee": 24
        },
        "cost": 3.0,

    }
}
resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}
def paise():
    print("Please insert coins")
    quarter=int(input("How many Quarter: "))
    dimes=int(input("How many Dimes: "))
    nickeles=int(input("How many Nickeles: "))
    pennies=int(input("How many Pennies:"))
    Paise=round(((0.25*quarter)+(0.1*dimes)+(0.05*nickeles)+(0.01*pennies)),2)

    print(Paise)
    return Paise
def report():
    water=resources["water"]
    milk=resources["milk"]
    money=resources["money"]
    coffee=resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCofee: {coffee}g\nMoney: ${money}")
    return

def order():
    machine = input("What would you like(latte/cappuccino/espresso): ")
    if machine=="report":
        report()
        order()
        return
    elif machine=="off":
        return False
    else:
        if machine not in MENU:
            print("Drink not available")
            order()
            return False
        a = paise()
        for item, amount in MENU[machine]["ingriedients"].items():

            if resources[item] < amount:
                print(f"Sorry there is There is not enough {item}")
                order()
                return
            else:
                resources[item] -= amount
        if(a<MENU[machine]["cost"]):
            print(f"You don't buy the cofee here is your {a} money back")
            order()
            return False
        else:
            change = round((a - MENU[machine]["cost"]), 2)
            print(f"Here is {change} in change.")
            print(f"Here is your drink {machine} Enjoy!")
            resources["money"] += MENU[machine]["cost"]
            order()
            return True


order()




