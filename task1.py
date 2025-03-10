import datetime

def input_date(): 
    user_date = input("Enter the date in the format (yyyy-mm-dd): ")
    pattern = "%Y-%m-%d"
    try:    
        date = datetime.datetime.strptime(user_date, pattern).date()
    except ValueError:
        print("Invalid date format, please try again")
        return input_date()
    return date 

date = input_date()
print(f"User input date: {date}")
current_date = datetime.datetime.now().date()
print(f"Current date on pc: {current_date}")
difference = current_date - date
print(f"Difference betweenn that dates: {difference.days}")
