'''
Complete the function which returns the weekday according to the input number:

    1 returns "Sunday"
    2 returns "Monday"
    3 returns "Tuesday"
    4 returns "Wednesday"
    5 returns "Thursday"
    6 returns "Friday"
    7 returns "Saturday"
    Otherwise returns "Wrong, please enter a number between 1 and 7"

'''

def get_weekday(weekday_number: int) -> str:
    # if weekday_number < 1 or weekday_number > 7:
    #     return "Wrong, please enter a number between 1 and 7"

    weekdays = {
        1: "Sunday", 
        2: "Monday", 
        3: "Tuesday", 
        4: "Wednesday", 
        5: "Thursday", 
        6: "Friday", 
        7: "Saturday"
    }
    return weekdays.get(weekday_number, "Wrong, please enter a number between 1 and 7")


print(get_weekday(0))
print(get_weekday(2))
print(get_weekday(4))
print(get_weekday(7))
print(get_weekday(8))
