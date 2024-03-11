# review set ->{} tuple ->{} list ->[]
# dictionary changeable
capitials = {'Taiwan': 'Taipei', 'India': 'New Dehli', 'China': 'Beijing'}

print(capitials['Taiwan'])
print(capitials.get('Japan'))  # <- more safe wont gneerate error
# False
print(capitials.keys())  # print whole dictionary key
# Taiwan India China
print(capitials.values())  # print whole dictionary value
# Taipei New Dehli Beijing

capitials.update({'Japan': 'Tokyo'})  # add new element in dictionary

print("this is whole dictionary contain")
for indx, value in capitials.items():
    print("index:{} value:{}".format(indx, value))
