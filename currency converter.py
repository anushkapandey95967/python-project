
def converts_to_pounds(dollars):
    return dollars * 0.82

def main():
    print("This program converts US dollars to pounds sterling")
    print()

    dollars = eval(input("Enter amount in dollars:"))

    pounds = converts_to_pounds(dollars)

    print("That is", pounds, "pounds.")

if __name__ == "__main__":
    main()
     

