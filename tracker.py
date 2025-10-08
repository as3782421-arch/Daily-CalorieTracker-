
# Task 1 : Welcome message
print("------------------------------------------------------")
print("       Welcome to the Daily Calorie Tracker App!       ")
print("------------------------------------------------------")
print("This tool helps you record your meals and track your daily calorie intake.\n")

# Task 2 : Input & Data collection
meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter the name of meal {i + 1}: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(calorie_amount)

# Task 3 : Calorie Calculations
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4 : Exceed Limit Warning System
if total_calories > daily_limit:
    status = "⚠️ You have exceeded your daily calorie limit!"
else:
    status = "✅ You are within your daily calorie limit. Good job!"

# Task 5 : Neatly Formatted Output
print("\n\n----------- Daily Calorie Summary -----------")
print("Meal Name\t\tCalories")
print("--------------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:15}\t{calories[i]}")

print("--------------------------------------------")
print(f"Total Calories:\t\t{total_calories}")
print(f"Average Calories:\t{average_calories:.2f}")
print("--------------------------------------------")
print(status)
print("--------------------------------------------")

# Task 6 (Bonus) : Save Session Log to File
save_option = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save_option == "yes":
    import datetime
    now = datetime.datetime.now()
    filename = f"calorie_log_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("------ Daily Calorie Tracker Report ------\n")
        file.write(f"Date & Time: {now}\n\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:15}\t{calories[i]}\n")
        file.write("--------------------------------------------\n")
        file.write(f"Total Calories: {total_calories}\n")
        file.write(f"Average Calories: {average_calories:.2f}\n")
        file.write(status + "\n")
        file.write("--------------------------------------------\n")

    print(f"\nReport saved successfully as '{filename}'!")
else:
    print("\nOkay! Report not saved.")
