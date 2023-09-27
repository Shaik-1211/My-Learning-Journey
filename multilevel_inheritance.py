class Product:
    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price

    def get_product_details(self):
        return {
            "name" : self.name,
            "description" : self.description,
            "price" : self.price
        }
    
# Inherits attributes and methods from Product class
class Car(Product):
    def __init__(self, name, description, price,color):
        super().__init__(name, description,price)#attributes of product class
        self.color = color #attribute of Car class

    def get_car_details(self):
        return {
            "name" : self.name,
            "description" : self.description,
            "price" : self.price,
            "color" : self.color
        }
    
#Inherits attributes and methods from Car class(Multilevel Inheritance)
class Toyota(Car):
    def __init__(self,description):
        name = "Toyota Rumion"
        price = 1000000
        color = "Black"
        Car.__init__(self, name,description,price,color)
        self.fueltype = "Petrol"
        self.Transmission = "Manual and Automatic"

    def toyota_rumion_description(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "color" : self.color,
            "description" : self.description,
            "fueltype" : self.fueltype,
            "transmission" : self.Transmission
        }

#creating a product instance
item = Product("Toyota","Automobile",10000) 
print(item.get_product_details())
# create an instance of car
car = Car("BMW","Luxury sports car",2000000,"grey")
print(car.get_car_details())#get details from class car
#create an instance of Toyota Rumion which inherits from car class
#Car class is a subclass of Product class
my_car = Toyota("Luxurious")
print(my_car.toyota_rumion_description())

