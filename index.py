# comprehensions
stuff = ["name", "age", "address", "phone"]

# These three examples do the same thing: loop through the stuff list and make a new list that contains the words capitalized
#1 good old for loop example
cap_stuff = []
for foo in stuff:
  cap_stuff.append(foo.capitalize())

#2 map example
cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))

#3 This is the comprehension example
cap_stuff = [ foo.capitalize() for foo in stuff ]

# Comprehensions can run on any collection. Here's a dictionary example
profile = {
  "name": "Fred",
  "age": 34,
  "address": "123 Sesame St"
}

# for loop version
profile_strings = []
for key, value in profile.items():
  obj.strings.append(f"The key is {key}. The value is {value}")

# dict comprehension version
profile_strings = [f"The key is {key}. The value is {value}" for key, value in profile.items()]
