
def ft_plant_age():
    age_input = input("Enter plant age in days: ")
    age = int(age_input)
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
