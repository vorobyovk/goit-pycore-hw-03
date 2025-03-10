import re

def phone_number_validation(phone_number): # define function for choose onli digits 
     pattern = r"\D+"
     phone_number = re.split(pattern, phone_number)
     return phone_number[-9:]
     
def normalize_phone(phone_number): # define function for normalize phone number
    phone_number2 = phone_number_validation(phone_number)
    phone_number3 = ''.join(phone_number2) 
    result_number = "+380" + phone_number3[-9:]
    return result_number

users_phone = input("Enter your phone number: ") # input phone number
result_number = normalize_phone(users_phone) # call function for normalize phone number
print(result_number) # output the result of the function

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)