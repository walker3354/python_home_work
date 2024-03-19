text = "have a good time\n walker!"
try:
    with open('Course\\test_folder\\test2.txt', 'a') as f:
        f.write(text)
except Exception as e:
    print(e)
