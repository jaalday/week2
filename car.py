class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        
car = Vehicle("Jeep", "liberty", "2007")   
car_1= Vehicle("lexus", "rx350", "2007")

print(car.make, car.model)

def vehicle_info():
    result = ("i drive a %s, %s" % (car.make, car.model))
    print(result)
    
    
print(car_1.make, car_1.model)
    
    
