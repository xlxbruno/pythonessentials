# datetime module
import datetime

# to get datetime now
x = datetime.datetime.now()
print(x)
# to get year
print(x.year)
# to get name of day
print(x.strftime("%A") +" " + str(x.month) + " " + str(x.year))
print(x.strftime("%p"))  # to get am or pm

# to get more formats : https://www.w3schools.com/python_daytime.asp
