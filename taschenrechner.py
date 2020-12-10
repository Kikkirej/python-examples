if __name__ == '__main__':
    ersteZahl = input("erste Zahl: ")
    rechenzeichen = raw_input("Rechenzeichen: ")
    zweiteZahl = input("zweite Zahl: ")
    ersteZahl = ersteZahl * 1.0
    zweiteZahl = zweiteZahl * 1.0
    print(str(ersteZahl) + rechenzeichen + str(zweiteZahl) + "=")
    ergebnis = 0
    if rechenzeichen == "+":  # ist das Rechenzeichen "+"
        ergebnis = ersteZahl + zweiteZahl
    elif rechenzeichen == "-":
        ergebnis = ersteZahl - zweiteZahl
    elif rechenzeichen == "*":
        ergebnis = ersteZahl * zweiteZahl
    elif rechenzeichen == "/":
        ergebnis = ersteZahl / zweiteZahl
    print ergebnis