import phonenumbers

from phonenumbers import geocoder

a = input("Enter the Phone Number: ")

phonenumber = phonenumbers.parse(a)

print(geocoder.description_for_number(phonenumber,'en'))
