#####Module 4
#####4.1.6.5 Tuples and dictionaries

dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}

empty_dictionary = {}


for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

print("Second part of the testing program")


for key in sorted(dictionary.keys()):
    print(key,"->", dictionary[key])

print("Language testing")

for english, french in dictionary.items():
    print(english, "->", french)

for french in dictionary.values():
    print(french)


print("Let's replace the value")

dictionary['cat'] = 'minou' #change a key
print(dictionary)

dictionary['swan'] = 'cigne' #add a key
print(dictionary)

dictionary.update({"Dick":"Pato"}) #another way to add a key
print(dictionary)

del dictionary["dog"]
print(dictionary)

dictionary.popitem() #Del the last key
print(dictionary)



