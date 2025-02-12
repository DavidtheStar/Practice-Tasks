"""Calculate volume of concrete needed for each job, as well as the total"
("that is needed for all jobs. With commercial thickness of concrete = 0.5m "
 "and the residential are 0.25m, program will continuously repeat til X "
 "entered."""
total_volume = 0
while True:
 building_type = input("Enter your building type (residential or commercial) "
                       "or 'x' to quit?: ").lower()
 if building_type == 'x':
  break
 if building_type not in ['residential', 'commercial']:
    print("Invalid building type. Please enter 'residential' or "
          "'commercial'. ")
    continue
 length = float(input("Enter the length of the slab in metres: "))
 width = float(input("Enter the width of the slab in metres: "))

 if building_type == 'commercial':
  depth = 0.5
 elif building_type == 'residential':
  depth = 0.25

 volume = length * width * depth

 print(f"The volume of concrete required for a slab with a length of "
        f"{length} metres and width of {width} metres and a depth of"
        f" {depth} metres is {volume:.2f} cubic metres. ")
 total_volume += volume
 print()
 print(f"Therefore The total amount of concrete needed is {total_volume:.2f} "
        f"cubic "
        f"metres. ")
 print()