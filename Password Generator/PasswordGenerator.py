import string
from random import random, shuffle, sample

# return lists of UPPER & lower case letters, 0-9 digits and punctuations
uppercase_Letter = string.ascii_uppercase
lowercase_Letter = string.ascii_lowercase
Number = string.digits
Punctuation = string.punctuation

password_String = []  # empty password list

# unlike list.append(), list.extend() updates an existing list by entering...
# ...elements of another list without creating a list of lists
password_String.extend(uppercase_Letter)
password_String.extend(lowercase_Letter)
password_String.extend(Number)
password_String.extend(Punctuation)

print("".join(sample(password_String, 10)))
