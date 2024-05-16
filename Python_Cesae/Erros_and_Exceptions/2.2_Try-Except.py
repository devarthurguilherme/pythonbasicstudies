while True:
    try:
        nameUser = str(input("Your Name: "))#Here, just numbers also works!
        print(f"Your name is: {nameUser}, ESPETÁCULO *---*")
        break#If input was correct, it can leave the loop.
    except ValueError:#Erro of  the type.Try again!
        print("This is a SALGALHADA, try again!")