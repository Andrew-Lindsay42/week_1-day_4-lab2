def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack.lower() == food.lower():
            return True

    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]

    return total

def lend_money(lender, lendee, loan):
    lender["monies"] -= loan
    lendee["monies"] += loan

def all_favourite_foods (people):
    foods = []
    for person in people:
        i = 0
        while i < len(person["favourites"]["snacks"]):
            foods.append(person["favourites"]["snacks"][i])
            i += 1
    return foods

def find_no_friends(people):
    no_pals = []
    for person in people:
        if person["friends"] == []:
            no_pals.append(person)
    return no_pals

