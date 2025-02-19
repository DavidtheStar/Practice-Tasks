"""Write a program that requests the number of seconds between lightning and
thunder and reports the distance of the storm. Test the program for the case
where there are one and a quarter seconds between the lightning and thunder."""

sound = 0.340
seconds_lightning_thunder =float(input("How many seconds between the "
                                       "lightning and the thunder?:  "))
print(f"The storm is {seconds_lightning_thunder * sound:.2f} kms away.")