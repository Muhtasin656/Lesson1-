class dog:
    species="dog"
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=dog("poddle",6)
dog2=dog("lexi",15)
print(f"the species of dog1 is {dog1.species}")
print(f"the species of dog2 is {dog2.species}")
print(f"the name of dog1 is {dog1.name} and he is {dog1.age} years old")
print(f"the name of dog2 is {dog2.name} and she is {dog2.age} years old")