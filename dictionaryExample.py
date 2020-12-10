if __name__ == '__main__':
    speisekarte = {
        "Pizza": 5.6,
        "Lasange": 4.6,
        "veggie Burger": 3.0,
        "Mate": 0.74
    }
    print "Was wollen Sie kaufen? "
    benutzerauswahl = raw_input()
    kosten = speisekarte.get(benutzerauswahl)
    print "Das kostet " + str(kosten) + " Euro"
    telefonbuch = {
        "Fabian": 44879,
        "Daniel": "42"
    }
    kontaktliste = [
        "Kontakt1",
        "Kontakt2",
        "Kontakt3"
    ]