# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

# use of replace() method 
 
name = str(input("Enter your first and last name? "))
rule = name.find(" ")
name_length = len(name)
first = name[0:rule]
last = name[rule + 1 : name_length]
if name_length is 6:
    print("welcome to AI and XR.")

else:
    print("ERROR: only enter fisrt name")