days_this_year = int(input("How many days are on this year? : "))

days_in_year = 365
days_in_leapYear = 366
hours_in_day = 24
munites_in_hour = 60
seconds_in_munite = 60

result = days_in_year * hours_in_day * munites_in_hour * seconds_in_munite

leapyear_result = days_in_leapYear * hours_in_day * munites_in_hour * seconds_in_munite

if days_this_year == 366 :
    print("Number of seconds in a leap year are", leapyear_result)
else: 
    print("Number of seconds in a year are", result)    