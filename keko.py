from random import choice  
kelime = input("Cümlenizi girin: ")
randomize = ''.join(choice((str.upper, str.lower))(char) for char in kelime)
print("Kekoca: " + str(randomize))
