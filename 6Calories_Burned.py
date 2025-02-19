"""The numbers of calories burned per hour by bicycling, jogging,
and swimming are 200, 475, and 275, respectively. A person loses one 454gms
of weight for each 3500 calories burned.Write a program that requires the
user to input the number of hours spent at each activity and then calculates
the number of kilograms worked off."""

biking = 200
jogging = 475
swimming = 275

calories_per_kg = 3500 / 0.454 #= 7704 calories a kg

hours_biking = float(input("Enter hours spent bicycling: "))
hours_jogging = float(input("Enter hours spent jogging: "))
hours_swimming = float(input("Enter hours spent swimming: "))

total_calories = (
    (hours_biking * biking) +
    (hours_jogging * jogging) +
    (hours_swimming * swimming)
)

weight_loss_kg = total_calories / calories_per_kg


print(f"\nTotal weight lost: {weight_loss_kg:.3f} kg")