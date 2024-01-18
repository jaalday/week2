class Person:
   
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []      
        
    # def friends(self, friend):
    #     self.friend = friend
    #     self.friend = {}
        
    # def num_friends():
        
    def __str__(self):   
        return "person : {} {} {}" .format(self.name, self.email, self.phone )
        
    
        
        
sonny = Person("sonny", "email", "phone", ())
jordan = Person("jordan", "email", "phone", ())

jordan.friend.append("jor")
sonny.friend.append("son")

sonny_string = str(sonny)
print(sonny_string)

print(jordan.friend)




def sonny_print_contact():
        email = jordan.email
        














#     def __friends__(self):
  
    
        
       
        
#     def print_contact_info(self, other_person):
#         result = print(self.name, self.email, other_person.name)
#         print(result)
        
    
# self = Person("sonny", "sony@hotmail.com", "8647278988")
# other_person = Person("Jordan", "jordan@aol.com", "6438293847")   

  
# def greet(self, other_person):
#         result =  ("hello %s, I am %s! " % (other_person.name, self.name))
        
#         print(result)
        
# print(other_person.email, other_person.phone)
# print(self.name, self.email, self.phone)







  

