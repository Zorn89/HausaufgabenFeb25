# Hier ist eine Python-Funktion, die eine vom Benutzer eingegebene Zahl mit den ersten 5 Primzahlen multipliziert

def multipliziere_mit_primzahlen():
    # Eingabe der Zahl vom Benutzer
    zahl = int(input("Gib eine Zahl ein: "))
    
    # Die ersten 5 Primzahlen
    primzahlen = [2, 3, 5, 7, 11]
    
    # Berechnung des Produkts
    produkt = zahl
    for prim in primzahlen:
        produkt *= prim
    
    # Ausgabe des Ergebnisses
    print(f"Das Produkt der Zahl {zahl} mit den ersten 5 Primzahlen ist: {produkt}")

# Funktion aufrufen
multipliziere_mit_primzahlen()



# Eine Funktion die eine vom Nutzer eingebene Zahl codiert:

def codiere_zahl():
    # Eingabe der Zahl vom Benutzer
    zahl = int(input("Gib eine Zahl ein: "))
    
    # Eine einfache Codierung durch Multiplikation und Addition
    geheime_nummer = (zahl * 7 + 13)
    
    # Ausgabe der codierten Zahl
    print(f"Die codierte Zahl ist: {geheime_nummer}")

# Funktion aufrufen
codiere_zahl() 


# Hier ist ein einfaches Beispiel, das eine Zahl von einem Benutzer nimmt, sie hasht und dann in einer "Benutzerdatenbank" speichert:

import hashlib

def signup():
    # Benutzer gibt eine Zahl ein (z.B. ein Passwort)
    zahl = input("Gib eine Zahl ein, um dich zu registrieren: ")
    
    # Hashen der Zahl (Verwendung von SHA256)
    hashed_zahl = hashlib.sha256(zahl.encode()).hexdigest()
    
    # Simulierter Signup-Prozess
    print(f"Deine Zahl wurde erfolgreich gehasht und gespeichert!\n")
    print(f"Der Hash deiner Zahl ist: {hashed_zahl}")
    
    # In einem echten Szenario würde man den Hash in einer Datenbank speichern
    # Zum Beispiel:
    # datenbank[benutzername] = hashed_zahl

# Funktion aufrufen
signup() 


# Beispiel für die Überprüfung eines Anmeldeversuchs:

def anmelden():
    # Benutzer gibt eine Zahl ein (z.B. ein Passwort)
    zahl = input("Gib deine Zahl ein, um dich anzumelden: ")
    
    # Hashen der eingegebenen Zahl
    hashed_zahl = hashlib.sha256(zahl.encode()).hexdigest()
    
    # Simulierte „Datenbank“ mit einem gespeicherten Hash
    gespeicherter_hash = "dein_hash_wird_hier_sein"  # Hier sollte der Hash gespeichert sein
    
    # Überprüfen, ob der eingegebene Hash mit dem gespeicherten Hash übereinstimmt
    if hashed_zahl == gespeicherter_hash:
        print("Anmeldung erfolgreich!")
    else:
        print("Fehlerhafte Anmeldung. Hash stimmt nicht überein.")

# Registrierung und Anmeldung in der Praxis
signup()
anmelden()