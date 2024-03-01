'''
we given a licence plate,you have to determinate the type and convert to other
A: "AB1234"
B: "1234AB"
'''
license_plate = input("please input the license number:")
if license_plate[0].isalpha() or license_plate[1].isalpha():
    license_plate = license_plate[2:] + license_plate[:2]
else:
    license_plate = license_plate[4:] + license_plate[:4]
print(license_plate)
