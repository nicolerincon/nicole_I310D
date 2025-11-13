import math

def calculate_sphere_volume(radius):
  volume = (4/3) * math.pi * (radius ** 3)
  return volume

# Get radius from user input
try:
  r = float(input("Enter the radius of the sphere: "))
  if r < 0:
    print("Radius cannot be negative. Please enter a positive value.")
  else:
    sphere_volume = calculate_sphere_volume(r)
    print(f"The volume of the sphere with radius {r} is: {sphere_volume:.2f}")
except ValueError:
  print("Invalid input. Please enter a numerical value for the radius.")