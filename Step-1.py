
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
        
def get_camp_choice():
    print("\nAvailable Camps:")
    for option, camp in camps.items():
        print(f"{option}. {camp['name']} - {camp['days']} days - ${camp['cost']}")

    while True:
        try:
            choice = int(input("Choose a camp (1-3): "))

            if choice in camps:
                return choice
            else:
                print("Please choose a valid camp number.")
        except ValueError:
            print("Please enter a number.")        
            
def get_transport():
    while True:
        transport = input("Will the camper use the shuttle bus? (yes/no): ").lower()

        if transport in ["yes", "y"]:
            return True
        elif transport in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def get_meal():
    print("\nMeal Options:")
    for meal in MEAL_OPTIONS:
        print("-", meal.title())

    while True:
        meal = input("Choose a meal preference: ").lower()

        if meal in MEAL_OPTIONS:
            return meal.title()
        else:
            print("Please choose Standard, Vegetarian, or Vegan.")


print("=== School Holiday Camp Registration ===\n")

name = get_name()
age = get_age()
camp_choice = get_camp_choice()
transport = get_transport()
meal = get_meal()

camp = camps[camp_choice]
total_cost = camp["cost"]

if transport:
    total_cost += SHUTTLE_COST

    print("\n--- Registration Summary ---")
    print(
        f"{name} (age {age}) is attending the "
        f"{camp['name']} camp for {camp['days']} days."
    )
    print(f"They chose a {meal.lower()} meal.")
    
    if transport:
        print("They will use the shuttle bus.")
    else:
        print("They will make their own way to the camp.")
    
    print(f"The total cost is ${total_cost}.")
    
    
    while True:
        confirm = input("\nConfirm registration? (yes/no): ").lower()
        
        if confirm in {"yes","y"}:
            print("Registration confirmed")
            break
        elif confirm in {"no","n"}:
            print("Registration Cancelled")
            break
        else: 
            print("Please enter yes or no")
        
    
    