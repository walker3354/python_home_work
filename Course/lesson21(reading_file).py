try:
    # use 'with' will automatice close the file
    with open('Course\\test_folder\\test.txt', 'r') as f:  # a append r read w write
        print(f.read())
except FileNotFoundError:
    print('file miss')
except Exception as e:
    print(e)
