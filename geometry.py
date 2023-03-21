from math import pi, sqrt

# Exercise 2 - Importing Modules
# In VS Code, create a module titled geometry and add two functions in there. One that will calculate the area of a circle given a radius. The second will find the hypotenuse of a right angle given the two sides. Import the module or the functions from the module and use it to find the answers to the below questions

# What is the area of a circle with a radius of 7cm?

def area_of_circle(radius):
    return pi *(radius**2)

# What is the hypotenuse of a right angle with sides of 3in and 4in?

def find_hypotenuse(a, b):
    return sqrt(a**2 + b**2)


print(area_of_circle(10))
