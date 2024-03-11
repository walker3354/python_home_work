# Loop and list
def main():
    for i in range(0, 10, 2):
        print(i)
    drink = ["tea", "coffe", "soda", "soda"]
    print("list size was {}".format(len(drink)))
    print("there have {} soda in this list".format(drink.count("soda")))
    print("the tea index is in {}".format(drink.index("tea")))


main()
