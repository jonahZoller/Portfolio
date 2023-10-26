from CheckInput import CheckInput
#from Order import Order

# ASCII art menu that will show the selection of what a person can order
menu = '''
 ________________________________________________________________________
| ______________________________________________________________________ |
||    _______    ________    __       __        _______    __    __     ||
||   | ______|  |  ___   |  |  |     |  |      |   ____|  |  |  |  |    ||
||   | |  ___   | |___|  |  |  |     |  |      |  |___    |  |__|  |    ||
||   | | |__ |  |  ____  |  |  |     |  |      |   ___|   |__    __|    ||
||   | |___| |  | |    | |  |  |___  |  |___   |  |_____     |  |       ||
||   |_______|  |_|    |_|  |______| |______|  |________|    |__|       ||
||                                                                      ||
||           _______     _______      __     __      _______            ||
||          | ______|   |  ___  |    |  |   |  |    |   __  |           ||
||          | |  ___    | |___| |    |  |   |  |    |  |__|_|           ||
||          | | |__ |   |   _  |     |  |   |  |    |   __|_            ||
||          | |___| |   |  | |_ |    |  |___|  |    |  |__| |           ||
||          |_______|   |__|   |_|   |_________|    |_______|           ||
||                                                                      ||
||                                                                      ||
||                                                                      ||
||                            SANDWICHES                                ||
||    KRABY PATTY........................................... 1.25       ||
||            w/ sea cheese................................. 1.50       || 
||    DOUBLE KRABY PATTY.................................... 2.00       || 
||            w/ sea cheese................................. 2.25       || 
||    TRIPLE KRABY PATTY.................................... 3.00       || 
||            w/ sea cheese................................. 3.25       || 
||                                                                      ||
||                            CORAL BITS                                ||   
||    Small................................................. 1.00       || 
||    Medium................................................ 1.25       || 
||    Large................................................. 1.50       || 
||                                                                      ||
||                            KELP RINGS                                || 
||    KELP RINGS............................................ 1.50       || 
||            w/ salty sauce................................  .50       || 
||                                                                      ||
||                              MEALS                                   || 
||    KRABY MEAL............................................ 3.50       || 
||    DOUBLE KRABY MEAL..................................... 3.75       || 
||    TRIPLE KRABY MEAL..................................... 4.00       || 
||                                                                      ||
||                           SPECIALTIES                                || 
||    SALTY SEA DOG......................................... 1.25       || 
||    FOOTLONG.............................................. 2.00       || 
||    SAILORS SUPRISE....................................... 3.00       || 
||    GOLDEN LOAF........................................... 2.00       || 
||            w/ sauce...................................... 2.50       || 
||                                                                      || 
||    KELP SHAKE............................................ 2.00       || 
||                                                                      || 
||                          SEAFOAM SODA                                || 
||    Small................................................. 1.00       || 
||    Medium................................................ 1.25       || 
||    Large................................................. 1.50       || 
||                                                                      ||
||                                                                      ||
||______________________________________________________________________||
|________________________________________________________________________|
'''
print(menu)
total = 0
id = 0
order = []

iu = input("Would you like to order? (y/n) ")
CheckInput.getCorrectInput(iu.lower(), ["y","yes","no","n"], "Would you like to order? (y/n) ")

while iu == "y" or iu == "yes":
    # add a list to the existing order to add mutiple orders inside one order
    newOrder = []
    order.append(newOrder)
    id += 1
    ui = input("What would you like? (sandwich, coral bits, kelp rings, meal, specialty, seafoam soda, end) ")
    # checks to see if the user is smart or if they put in something random 
    # if input is something random repeat question
    ui = CheckInput.getCorrectInput(ui.lower(), ["sandwich","coral bits", "kelp rings", "meal", "specialty", "seafoam soda", "none"], "What would you like? (sandwich, coral bits, kelp rings, meal, specialty, seafoam soda, end) ")
    while ui != "none":
        if ui == "sandwich":
            sandwich = input("What sandwich would you like? (Kraby Patty, Double Kraby Patty, Triple Kraby Patty) ")
            sandwich = CheckInput.getCorrectInput(sandwich.lower(), ["kraby patty", "double kraby patty", "triple kraby patty"], "What sandwich would you like? (Kraby Patty, Double Kraby Patty, Triple Kraby Patty) ")        
            if sandwich == "kraby patty":
                total += 1.25
            elif sandwich == "double kraby patty":
                total += 2.00
            elif sandwich == "triple kraby patty":
                total += 3.00
            cheese = input(f"Would you like cheese on your {sandwich}? (y/n) ")
            cheese = CheckInput.getCorrectInput(cheese.lower(), ["y","yes","no","n"], f"Would you like cheese on your {sandwich}? (y/n) ")
            if cheese == "y" or cheese == "yes":
                total += 0.50
                sandwich = f"{sandwich} w/ cheese"
                newOrder.append(sandwich)
            else:
                newOrder.append(sandwich)

        if ui == "coral bits":
            coralBits = input("Would you like small, medium, or large? (s,m,l) ")
            coralBits = CheckInput.getCorrectInput(coralBits.lower(), ["s","m","l","small","medium","large"], "Would you like small, medium, or large? (s,m,l) ")
            if coralBits == "s" or coralBits == "small":
                total += 1.00
                coralBits = "small"
            elif coralBits == "m" or coralBits == "medium":
                total += 1.25
                coralBits = "medium"
            elif coralBits == "l" or coralBits == "large":
                total += 1.50
                coralBits = "large"
            newOrder.append(f"{coralBits} coral bits")

        if  ui == "kelp rings":
            total += 1.50
            sauce = input("Would you like sauce with the kelp rings? (y/n) ")
            sauce = CheckInput.getCorrectInput(sauce.lower(), ["y","yes","no","n"], "Would you like sauce with the kelp rings? (y/n) ")
            if sauce == "yes" or sauce == "y":
                total += 0.50
                newOrder.append("Kelp Rings w/ sauce")
            else:
                newOrder.append("Kelp Rings")
        
        if ui == "meal":
            meal = input("Would you like a single, double, or triple meal? (s,d,t) ")
            meal = CheckInput.getCorrectInput(meal.lower(), ["s","d","t","single", "double", "triple"], "Would you like a single, double, or triple meal? (s,d,t) ")
            if meal == "single" or meal == "s":
                total += 3.50
                meal = "single"
            elif meal == "double" or meal == "d":
                total += 3.75
                meal = "double"
            elif meal == "triple" or meal == "t":
                total += 4.00
                meal = "triple"
            newOrder.append(f"{meal} Kraby Patty Meal")

        if ui == "specialty":
            specialty = input("Which specialty would you like? (Salty Seadog, Footlong, Saliors Suprise, Golden Loaf, or Kelp Shake) ")
            specialty = CheckInput.getCorrectInput(specialty.lower(), ["salty seadog", "footlong", "saliors suprise", "golden loaf", "kelp shake"], "Which specialty would you like? (Salty Seadog, Footlong, Saliors Suprise, or Golden Loaf) ")
            if specialty == "salty seadog":
                total += 1.25
                newOrder.append(specialty)
            elif specialty == "footlong":
                total += 2.00
                newOrder.append(specialty)
            elif specialty == "saliors suprise":
                total += 3.00
                newOrder.append(specialty)
            elif specialty == "kelp shake":
                total += 2.00
                newOrder.append(specialty)
            elif specialty == "golden loaf":
                specialSauce = input("Would you like sauce with that? (y/n) ")
                specialSauce = CheckInput.getCorrectInput(specialSauce.lower(), ["y","n","yes","no"], "Would you like sauce with that? (y/n) ")
                if specialSauce == "yes" or specialSauce == "y":
                    total += 2.50
                    newOrder.append(f"{specialty} w/ sauce")
                else:
                    total += 2.00
                    newOrder.append(specialty)
        
        if ui == "seafoam soda":
            soda = input("Would you like a small, medium, or large? (s,m,l) ")
            soda = CheckInput.getCorrectInput(soda.lower(), ["s","m","l","small","medium","large"], "Would you like a small, medium, or large? (s,m,l) ")
            if soda == "s" or soda == "small":
                total += 1.00
                soda = "small"
            elif soda == "m" or soda == "medium":
                total += 1.25
                soda = "medium"
            elif soda == "l" or soda == "large":
                total += 1.50
                soda = "large"
            newOrder.append(f"{soda} seafoam soda")

        ui = input("What would you like? (sandwich, coral bits, kelp rings, meal, specialty, seafoam soda, none) ")
        # checks to see if the user is smart or if they put in something random 
        # if input is something random repeat question
        ui = CheckInput.getCorrectInput(ui.lower(), ["sandwich","coral bits", "kelp rings", "meal", "specialty", "seafoam soda", "none"], "What would you like? (sandwich, coral bits, kelp rings, meal, specialty, seafoam soda, none) ")


    for i in range(len(order)):
        print("")
        print(f"Order {i+1}")
        print(order[i])
    print(total)
    print(order)
    iu = input("Would you like order another? (y/n) ")
    CheckInput.getCorrectInput(iu.lower(), ["y","yes","no","n"], "Would you like to order? (y/n) ")
