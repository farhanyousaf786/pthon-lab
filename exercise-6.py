# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.



input_month = input("Enter the month of the year (Jan - Dec) ").lower()
day = int(input("Enter the day of the month: "))

if input_month in ('jan', 'feb', 'mar', "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"):
  if   input_month == "mar":
     if  day  <  20:
       season = "Winter"
     else :
       season = "Spring"
  elif   input_month == "apr" or input_month == "may":
     season   =  "Spring"
  elif   input_month == "jun":
     if  day  <  21:
       season = "Spring"
     else :
       season = "Summer"
  elif   input_month == "jul" or input_month == "aug":
     season   =  "Summer"
  elif   input_month == "sep":
     if  day  <  22:
       season = "Summer"
     else :
       season = "Fall"
  elif   input_month == "oct"  or input_month == "nov":
     season   =  "Fall"
  elif   input_month == "dec":
     if  day  <  21:
       season = "Fall"
     else :
       season = "Winter"
  elif  input_month == "jan" or input_month == "feb":
     season   =  "Winter"     
print (input_month, day,  "is in", season,  "season")