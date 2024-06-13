class Human:
    def __init__(self, n, age):
        self.n = n
        self.age = age

    def __str__(self):
        return f"My name is {self.n} and age is {self.age}"

    # Getters
    def get_age(self):
        return self.age


arthur = Human("Arthur", 32)
print(arthur)
