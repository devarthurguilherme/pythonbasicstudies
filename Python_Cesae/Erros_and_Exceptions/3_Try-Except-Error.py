while True:
    try:
        ageUser = int(input("How old are you? "))
        print(f"Your age is {ageUser}")
        break
    except:
        print("Put a valid integer number!")
    finally:#It works when we need to execute something even though there is some error before!
        print("This message will always be showed!")

