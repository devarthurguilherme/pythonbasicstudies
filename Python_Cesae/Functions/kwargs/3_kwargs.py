#Config Print
def configPrint(**kwargs):
    #Default values using get origin method
    color = kwargs.get("color", "black")
    size = kwargs.get("size", "A4")
    quantity = kwargs.get("quantity", 10)

    print(f"Print {quantity} copies in paper {size} in the color {color}")

configPrint(color="Blue", size="A3", quantity=5)
configPrint()#Here, Method will be used as a default value!
#Get is useful to avoid errors with keys don't found and to give default values!
#Use when the arguments are optional