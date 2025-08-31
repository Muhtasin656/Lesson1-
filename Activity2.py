# create class
class car:
    # create a init method
    def __init__(self,max_speed,mileage):
        # bind the arguements
        self.max_speed=max_speed
        self.mileage=mileage


# object creation
buggati=car(500,30)

# access variable inside init method
print("the maximum speed is ",buggati.max_speed)
print("the mileage is ",buggati.mileage)