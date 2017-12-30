favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("edward favorite language is " +
 favorite_languages['edward'].title() +  ".")

print("\n#6.1")
My_Friend ={
    'First_Name': 'Muhammad', 'Last_Name': 'Ali',
    'Age': 26, 'City': 'Karachi',
}
print("My Friend's FirstName is:" + My_Friend['First_Name'].title() +"")
print("My Friend's LastName is:" + My_Friend['Last_Name'].title() +"")
print("My Friend's Age is:"+str(My_Friend['Age']))
print("My Friend's City is:" + My_Friend['City'].title() +"")

print("\n#6.2")
Favorite_Numbers={
    'Umair': 3,
    'Saad': 5,
    'Sumair': 8,
    'Kashif': 29,
    'Faraz': 39,
}

for key, value in Favorite_Numbers.items():
    print(key + ":" + str(value) + "\n")

print("\n#6.3")
Glossary = {
    'List': 'a collection of items in a particular order.',
    'Tuple': 'an immutable list is called a tuple.',
    'Dictionary': 'a collection of key-value pairs.',
    'Spark': 'is a cluster computing framework',
    'Dispersion': 'refers to measures of how spread out our data is.',
}
for key, value in Glossary.items():
    print(key + "\n" + value + "\n")
