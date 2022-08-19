Radius = int(float(input("enter the Radius of the Cylinder : ")))
Height = int(float(input("enter the Height of the Cylinder : ")))

Volume = Height * Radius ** 2 * 3.14
Lateral_Surface = Radius * Height * 3.14 * 2
Total_Surface = (Radius * Height * 3.14 * 2) + (2) * (Radius ** 2 * 3.14)

print("Valume of Cylinder is :" ,Volume )
print("Lateral Surface of Cylinder is :" ,Lateral_Surface)
print("Total Surface of Cylinder is :f" ,Total_Surface)
