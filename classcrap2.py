class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friend = []
    
         
    

    def greet(self, other_person):
         return "Hello %s, I am %s!" % (other_person.name, self.name)

    def contact_info(self):
        return (self.email, self.phone)
    
    def num_friends(self):
        return len(self.friend)
    
        
sonny = Person("sonny", "your mom", "86587657")
jordan = Person("jordan", "beep", "87698769")
        
jordan.friend.append("jor")
sonny.friend.append("son")

print(sonny.friend)
sonny.greet(other_person = jordan)

       

        
        
        # print(other_person.email, other_person.phone)
        # print(self.name, self.email, self.phone)