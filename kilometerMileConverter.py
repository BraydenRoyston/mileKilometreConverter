print("Will you be inputting miles or kilometres?")
typeOfConversion=input()

def convertMiles(x):
    return x * 1.6
def convertKilometres(x):
    return x / 1.6

if typeOfConversion == "kilometres":
    km = int(input("Enter the number of kilometres:"))
    m = convertKilometres(km)
    print("miles=" + str(m))
elif typeOfConversion == "miles":
    m = int(input("Enter the number of miles:"))
    km= convertMiles(m)
    print("kilometres=" + str(km))
else:
    print("Please start again. Input is case sensitive!")