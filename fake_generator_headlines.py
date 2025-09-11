import random

subjects = [
    "Sharuk khan",
    "Virat kholi",
    "Nirmala sitaraman",
    "Narendra modi",
    "Auto ricksha driver from delhi"
]

actions = [
    "Lunches",
    "Cancels",
    "Dances with",
    "Declares war on",
    "Eats"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "Goa Beach",
    "Jhansi with Mumbai",
    "Island"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        break

print("\nThanks for using the fake news headlines generator. Have a fun day!")
