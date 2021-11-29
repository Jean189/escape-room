from PIL import Image
with Image.open('https://gitlab.switch.ch/jean-paul.mathieu/escape-room/-/blob/cd4406073f3a145cd37a4d35649eb57386ff4f0a/raetsel.png') as img:
    img.show()

print("Findest du die den richtigen 3-stelligen Zahlencode? Gib den Code an oder ein Fragezeichen für Hinweis")

hinweis = False
while True:
    antwort = input("> ")
    if antwort == "?":
        if not hinweis:
            print("Um das Rätsel zu lösen, muss man die Verbindung zwischen den zwei sich gegenüber liegenden Zeichen herausfinden. Z.B. 1 = E, 3 = D, 6 = S, 7 = S")
            hinweis = True
        else:
            print("Wie bei Hinweis 1 erwähnt: Eins = E, Drei = D, Sechs = S, Sieben = 7")
    elif antwort == "284":
        print("Herzlichen Glückwunsch, die Antwort ist korrekt. Merke Dir den Namen: Paul")
        liste = []
        liste.append("Paul")
        break
    else:
        print("Leider falsch, versuche es nochmal")


        
        