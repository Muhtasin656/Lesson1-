class parrot:
    # class variable
    species="bird"

    # instance variable
    def __init__(self,name,age):
        self.name=name
        self.age=age

parrot1=parrot("blu",10)
parrot2=parrot("wu",12)

#accessing the class variable
print(f"the species of parrot1 is {parrot1.species}")
print(f"the species of parrot2 is {parrot2.species}")
# accessing the instant variable
print(f"the name of parrot1 is {parrot1.name} and he is {parrot1.age} years old")
print(f"the name of parrot2 is {parrot2.name} and he is {parrot2.age} years old")