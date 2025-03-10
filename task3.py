import re

def phone_number_validation(phone_number): # define function for choose onli digits 
     pattern = r"\D+"
     phone_number = re.split(pattern, phone_number)
     return phone_number[-9:]
     
def normalize_phone(phone_number): # define function for normalize phone number
    phone_number2 = ''.join(phone_number) 
    result_number = "+380" + phone_number2[-9:]
    return result_number

users_phone = input("Enter your phone number: ") # input phone number
valid_number = phone_number_validation(users_phone) # call function for choose only digits
result_number = normalize_phone(valid_number) # call function for normalize phone number

print(result_number) # output the result of the function
