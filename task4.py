import datetime as dt

NOW = dt.datetime.now().date()

def get_upcoming_birthdays(users): # define function get_upcoming_birthdays with 1 argument
    birthdays = []
    for user in users: # loop for each user in the list
        user_birth_temp = dt.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birth_str = str(f"{NOW.year}-{user_birth_temp.month}-{user_birth_temp.day}") # create temporary user's birthday with current year
        user_birth = dt.datetime.strptime(user_birth_str, "%Y-%m-%d").date() # convert the user's birthday to datetime
        if user_birth <= NOW + dt.timedelta(days=7): # check if the user's birthday is in the next 7 days
            birthdays.append(user)
            print(user_birth_str) 
    return birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.13"},
    {"name": "Jane Smith", "birthday": "1990.03.18"},
    {"name": "Michel Levandovskiy", "birthday": "1990.03.14"}
]

print(get_upcoming_birthdays(users)) # output result of the function
