import datetime as dt

NOW = dt.datetime.now().date()

def get_upcoming_birthdays(users):
    birthdays = []
    for user in users:
        user_birth_temp = dt.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birth_str = str(f"{NOW.year}-{user_birth_temp.month}-{user_birth_temp.day}")
        user_birth = dt.datetime.strptime(user_birth_str, "%Y-%m-%d").date()
        if user_birth <= NOW + dt.timedelta(days=7):
            birthdays.append(user)
            print(user_birth_str) 
    return birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.13"},
    {"name": "Jane Smith", "birthday": "1990.03.18"},
    {"name": "Michel Levandovskiy", "birthday": "1990.03.14"}

print(get_upcoming_birthdays(users)) # {'name': 'John Doe', 'birthday': '1985.01.23'}