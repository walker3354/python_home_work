# the local variable will stay at the "function" not while and for

def main():
    while True:
        name = 'walker'
        break
    print(name)


main()
