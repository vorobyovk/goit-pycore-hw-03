import random

def get_numbers_ticket(min, max, quantity): # define function get_numbers_ticket with 3 arguments
    numbers = []
    if max - min < quantity:
        return "Кількість чисел більша за діапазон чисел"
    else:
        while len(numbers) < quantity: # check if the length of the list is less than the quantity
            number = random.randint(min, max)
            if number not in numbers: # check if the number is not in the list
                numbers.append(number)
        numbers=sorted(numbers) # sort the our list
        return numbers 

lottery_numbers = get_numbers_ticket(100, 150, 10) # call the function with the arguments
print(f"Ваші лотерейні числа: {lottery_numbers}") # output the result of the function

