class RemoteControl:
    # characteristics
    def __init__(self, color: str, height: int, weight: int, brand: str):
        # object.attribute = parameter value
        self.color = color
        self.height = height
        self.weight = weight
        self.brand = brand

    # methods
    def printAttributes(self):
        print(
            f"Remote Control\nBrand: {self.brand}\nColor: {self.color}\nHeight: {self.height} \nWeight: {self.weight}")

    def turnUp(self, button):
        if button == "+":
            print("Turn up the sound!")

    def turnDown(self, button):
        if button == "-":
            print("Turn down the sound!")


control1 = RemoteControl("black", 12, 6, "lg")
control2 = RemoteControl("blue", 10, 4, "philips")

# Print attributes
control1.printAttributes()
control2.printAttributes()
print("*"*100)
# Using a method else
control1.turnUp("+")
control2.turnDown("-")
