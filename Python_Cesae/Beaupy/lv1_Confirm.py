#User Interface with BeauPy
from beaupy import confirm

def yes():
    print("Yes, I like a lot!")

def no():
    print("No, I hate it!")

if confirm("Do you like programming?"):
    yes()
else:
    no()

