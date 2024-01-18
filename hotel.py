guests = {
    '1':{
        '185': ['George', 'wheezy']
    },
    '2':{
        '236': ['jack', 'your mom']
    },
    '3':{
        '333': ['neo', 'morp', 'robot']
    }
}






menu = input("1. Would you like to check in? y/n ")
print(menu)

if menu == "y":
    floor = input("what floor would you like? ")
else:
    print("bitch come on")
    
if floor == "1":
    print("good choice")
else: 
    print("thats a bad choice " )
    
people = input("are you going to throw a wild party? ")
if people == "yes":
    print("hell ya")
else:
    print("its ok i get it, im old and tired too")
    
name = input("whats your name? ")

def edit_guests(guest_name):
    for guest in guests:
        if guest_name == guest:
            guests.remove(guest_name)
            return guests
        else:
            guests[guest_name] = guest_name
            return guests
        
result = edit_guests(name)

print(result)



# def edit_list(param, name):
#     for cat in param:
#         if cat == name:
#             param.remove(cat)
#             return param
#         else:
#             param.append("pumpkin")
#             return param



    

# guests = {
#     '1':{
#         '185': ['George', 'wheezy']
#     },
#     '2':{
#         '236': ['jack', 'your mom']
#     },
#     '3':{
#         '333': ['neo', 'morp', 'robot']
#     }
# }








# print("2. What floor number? ")
# print("3. What room number? ")
# print("4. what is your last name? ")
# print("5. are you checking out? ")