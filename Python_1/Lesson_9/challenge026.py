sentence = str(input("Digit a sentence: ")).strip().lower()
userLetter = str(input("Choose a letter: ")).lower()
r = sentence.count(userLetter)
firstPosition = sentence.find(userLetter)+1
lastPosition = sentence.rfind(userLetter)+1


print(f"letter is shower {r} times! \nFirst Position was {firstPosition} and Last Position was {lastPosition}.")