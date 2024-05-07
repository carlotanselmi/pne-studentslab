class Car:
    def __init__(self, brand):  # From the class to define an object
        pass  # Doesn't do anything

    def speed(self):
        return 100


# Self is the object itself
mycar = Car("Renault")  # We don't have to name the self before brand, because it's the object before the dot
print(mycar.speed())
yourcar = Car("Ferrari")
print(yourcar.speed())


class Car1:

    def __init__(self, brand):  # From the class to define an object
        self.car_brand = brand
        self.speed = 0  # We could also have put it on the init as speed=0
        # brand += " TM"  # Works because brand is a local variable

    def set_speed(self, speed):
        self.speed = speed
        # self.car_brand += " TM"
        # brand += "TM"  # DOESN'T work because brand is a local variable from another function

    def get_speed(self):
        return self.speed

    def get_brand_nationality(self):
        if self.car_brand == "Renault":
            return "France"
        elif self.car_brand == "Ferrari":
            return "Italy"


mycar1 = Car1("Renault")
print(mycar1.get_speed())
mycar1.set_speed(80)
print(mycar1.get_speed())
print(mycar1.get_brand_nationality())
yourcar1 = Car1("Ferrari")
print(yourcar1.speed)
print(yourcar1.get_speed())
print(yourcar1.get_brand_nationality())


class Ferrari(Car1):  # INHERITANCE
    # It calls the init of Car1 from before
    pass

mycar2 = Car1("Renault")
# yourcar2 = Ferrari() # Doesn't work because it doesn't have the brand inside
yourcar2 = Ferrari("Ferrari")
print(yourcar2.car_brand)
yourcar2.set_speed(120)  # As it isn't in Ferrari, it looks for it in the mother class, Car
print(yourcar2.speed)


class Ferrari1(Car1):
    # OJO We cannot have inheritance with more than one innit, because it will have already entered to the
    # daughter class initialization box
    def __init__(self):
        super().__init__("Ferrari")  # It calls the init from the mother class
        self.music = "classic"

    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return self.car_brand


yourcar3 = Ferrari1()
print(yourcar3.make_cabrio(), "and music is", yourcar3.music, "and speed is", yourcar3.speed)
