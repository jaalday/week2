class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         
    def greet(self, person2):
        print('Hello {}, I am {}!'.format(person2.name, self.name))

    def print_contact_info(self):
        print(self.name, self.email, self.phone)
    
    
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

Person.greet(sonny, jordan)
sonny.greet(jordan)

Person.print_contact_info(sonny)