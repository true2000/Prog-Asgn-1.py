# This tool is used to help with the calculation of how much a hotel cots

# Ryan Nock
# Aug 28 2020

name = input("What is your customers name?: ")


def main():
    print("\n")
    print("Hello " + name + " welcome to the Owl Hotel")
    print("This program allows you to calculate the total cost of a hotel.")
    print("\n")
    num_days = float(input("Please type the number of days you stayed at the hotel.: "))
    cost_per_day = float(input("Please type the daily cost for the hotel.: "))
    total = round((num_days * cost_per_day), 2)
    print("\n")
    print(name + ", your total bill is $" + str(total))
    print("Owl Hotel")

    print("          ^...^")
    print("         / o,o \ ")
    print("        |) ::: (| ")
    print("        ===w=w=== ")


main()
