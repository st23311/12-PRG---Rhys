
camps = {
    1: {"name": "Cultural Immersion", "days": 5, "cost": 800},
    2: {"name": "Kayaking and Pancakes", "days": 3, "cost": 400},
    3: {"name": "Mountain Biking", "days": 4, "cost": 900}
}

SHUTTLE_COST = 80
MEAL_OPTIONS = ["standard", "vegetarian", "vegan"]


def get_name():
    while True:
        name = input("Enter camper's name: ").strip()

        if name == "":
            print("Name cannot be blank.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain letters only.")
        else:
            return name.title()

def get_age():
    while True:
        try:
            age = int(input("Enter camper's age (5-17): "))

            if 5 <= age <= 17:
                return age
            else:
                print("Age must be between 5 and 17.")
        except ValueError:
            print("Please enter a valid number.")        