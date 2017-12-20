# 5.3 (a) Pass if Statement
alien_color = 'Green'
if alien_color == 'Green':
    print("You Have Earned 5 Points.")

# 5.3 (b) Fail if Statement
alien_color = 'Red'
if alien_color == 'Green':
    print("You Have Earned 5 Points.")

# 5.4 (a) Pass if Statement
alien_color = 'Green'
if alien_color == 'Green':
    print("You Have Earned 5 Points.")
else:
    print("You Have Earned 10 Points.")

# 5.4 (b) Fail if Statement
alien_color = 'Red'
if alien_color == 'Green':
    print("You Have Earned 5 Points.")
else:
    print("You Have Earned 10 Points.")

# 5.5 (a)
alien_color = 'Green'
if alien_color == 'Green':
    print("You Have Earned 5 Points.")
elif alien_color == 'Yellow':
    print("You Have Earned 10 Points.")
elif alien_color == 'Red':
    print("You Have Earned 15 Points.")

# 5.5 (b)
alien_color = 'Yellow'
if alien_color == 'Green':
    print("You Have Earned 5 Points")
elif alien_color == 'Yellow':
    print("You Have Earned 10 Points.")
elif alien_color == 'Red':
    print("You Have Earned 15 Points.")

# 5.5(c)
alien_color = 'Red'
if alien_color == 'Green':
    print("You Have Earned 5 Points.")
elif alien_color == 'Yellow':
    print("You Have Earned 10 Points.")
elif alien_color == 'Red':
    print("You Have Earned 15 Points.")

# 5.6

print("Stages Of Life")
Person = 34
if Person < 2:
    print('The Person Is a Baby.')
elif Person >=2 and Person < 4:
    print('The Person Is a Toddler.')
elif Person >=4 and Person < 13:
    print('The Person Is a Kid.')
elif Person >= 13 and Person < 20:
    print('The Person Is a Adult.')
elif Person >= 13 and Person < 20:
    print('The Person Is a Teenager.')
elif Person >= 20 and Person < 65:
    print('The Person Is a Adult.')
elif Person >= 65:
    print('The Person Is a Elder.')


