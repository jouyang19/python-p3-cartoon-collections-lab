def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        # print(str(num) + ".", dwarf)
        print(f"{num}. {dwarf}")
        num += 1

def summon_captain_planet(calls):
    result = []
    for call in calls:
        new_call = f"{call.capitalize()}!"
        result.append(new_call)
    return result

        

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheeses:
            return food

roll_call_dwarves(["Dopey", "Grumpy", "Bashful"])
summon_captain_planet(["carrot", "cucumber", "pepper"])
long_planeteer_calls(["axe", "earth", "wind", "fire"])