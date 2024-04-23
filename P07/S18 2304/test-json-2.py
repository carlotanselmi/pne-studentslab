import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-2.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', force_color=True, end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', force_color=True, end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', force_color=True, end='')
print(len(phoneNumbers))

# Print all the phone numbers
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone " + str(i) + ": ", 'blue', force_color=True, end='')
    print(num)
