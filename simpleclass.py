class Car:

    def __init__(self,brand_name,model,manufacture_year):
            self.brand_name= brand_name
            self.model=model
            self.manufacture_year=manufacture_year

    def display_info(self):
            print(f"Name of car brand is {self.brand_name},model is{self.model} and manufacture year is {self.manufacture_year}")

    def start_engine(self):
            print(f"Engine is started for car {self.brand_name}")

class Bike(Car):

    litres=25
    km=600

    def bike_mileage(self):
            print(f"mileage of bike:{self.km/self.litres}")

    def start_engine(self):
        print(f"Engine starts slowly for {self.brand_name}")


car1=Car("Renault","Kwid",2019)
car2=Bike("honda","cb350",2024)

car1.display_info()
car1.start_engine()
car2.display_info()
car2.start_engine()
car2.bike_mileage()