
def add_money(dict, person, amount):
    if person not in dict:
        dict[person] = 0
    dict[person] = dict[person] + amount

def split_money_spent(money_spent, list_of_people):
    """ returns a dictionary where the keys are people who owe money and the value is a dictionary containing people they owe money to, and how much they owe """
    split_ways = len(list_of_people)
    # initialize dict
    amount_owed = dict()
    for person in list_of_people:
        amount_owed[person] = dict()
    for person_who_spent in money_spent:
        portion = money_spent[person_who_spent] / split_ways
        for person_who_needs_to_pay in amount_owed:
            if person_who_needs_to_pay is not person_who_spent:
                add_money(amount_owed[person_who_needs_to_pay], person_who_spent, portion)
    return amount_owed

def simplify_amounts_due(amount_owed):
    # iterate through everyone who went on the trip
    for person_who_needs_to_pay in amount_owed:
        # for each person who went on the trip, check to see if there is someone they owe money to that also owes them money
        for other_person in amount_owed:
                both_owe_each_other = (other_person != person_who_needs_to_pay) and (other_person in amount_owed[person_who_needs_to_pay]) and (person_who_needs_to_pay in amount_owed[other_person])
                if both_owe_each_other and amount_owed[person_who_needs_to_pay][other_person] > amount_owed[other_person][person_who_needs_to_pay]:
                    amount_owed[person_who_needs_to_pay][other_person] = amount_owed[person_who_needs_to_pay][other_person] - amount_owed[other_person][person_who_needs_to_pay]
                    amount_owed[other_person][person_who_needs_to_pay] = 0
    return amount_owed



JUN = "Jun"
JACK = "Jack"
ANDREW = "Andrew"
KELSEY = "Kelsey"
BEN = "Ben"
ALEX = "Alex"
STEVE = "Steve"

things_people_bought = dict()

add_money(things_people_bought, JUN, 10.00)          #snacks
add_money(things_people_bought, ANDREW, 92.00)       # camp site fee and car fee
add_money(things_people_bought, ANDREW, 49.00)       # park entry fee
add_money(things_people_bought, ANDREW, 273.00)      # main groceries
add_money(things_people_bought, ANDREW, 187.00)      # gas
add_money(things_people_bought, JACK, 54.00)         # gas
add_money(things_people_bought, KELSEY, 28.00)       # gas
add_money(things_people_bought, JUN, 19.00)          # gas
add_money(things_people_bought, JUN, 30.00)          # gas
add_money(things_people_bought, JACK, 73.00-34.00)   # crash pads
add_money(things_people_bought, JACK, 34.00)         # additional groceries

amount_owed = split_money_spent(things_people_bought, [JUN, JACK, ANDREW, KELSEY, BEN, ALEX, STEVE])
amount_owed_final = simplify_amounts_due(amount_owed)
print(amount_owed_final)
