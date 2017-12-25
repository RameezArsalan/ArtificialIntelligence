
# 5.8
# For loop in List
print("\n Exercise-5-8 , Hello Admin")
admins = ['kashif', 'admin' , 'ramiz']
for admin in admins:
    if admin == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + admin + ", Thank you for logging in again!")

# 5.9
#Check if List is Empty
print("\n Exercise-5-9 , No User")
admins = []
if admins:
    admins=[]
    print("We need to find some users!")
else:
    print("No Items in list!")

#5.10
#Check if User Exist in current User List
current_users=["Kashif", "Ramiz", "Faraz", "Arsalan", "Musharaf"]
new_users = ["Kashif", "Faraz", "Saad", "Soniya", "Huma"]
k=0
for User in new_users:
    if User in current_users:
        print(User + " Is Available")
    else:
        print(User + " will need to enter a UserName")

#5.10-UPPER
current_users=["Kashif", "Ramiz", "Faraz", "Arsalan", "Musharaf"]
k=0
for i in range(0,len(current_users)):
    current_users[i]=current_users[i].upper()

print(current_users)
