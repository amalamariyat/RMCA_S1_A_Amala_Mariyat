import math
def areacir(r):
    a=r**2 * math.pi
    return a
r=float(input("Enter the radius of the circle:"))
print("%.2f" %areacir(r))
