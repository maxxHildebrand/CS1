seconds = int(input("How many seconds? "))

secondsleft = seconds%60
minutes = seconds // 60
minutesleft = minutes % 60
hours = minutes // 60
hoursleft = hours%24
days = hours // 24
daysleft = days % 7
weeks = days // 7



print(seconds, " seconds is ", days, " days, ", hours, "hours, ", minutes, " minutes, and ", secondsleft, "seconds.")
