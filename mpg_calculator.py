# THIS PROGRAM CALCULATES MILES PER GALLON FOR USER INPUT

print("-- MILES PER GALLON CALCULATOR --")

miles_driven = input("Enter miles driven: ") #input data via stream
miles_driven = float(miles_driven) #converts from a string input to float
gallons_used = input("Enter gallons used: ")
gallons_used = float(gallons_used) #conversion of data type
mpg = miles_driven / gallons_used
print("Miles per gallon: ", mpg)