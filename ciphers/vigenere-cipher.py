# Functia de criptare 
def vigenere_encrypt(text, keyword):
    # Ne asiguram ca datele de intrare sunt compuse doar din litere mari. 
    text = text.upper() 
    keyword = keyword.upper()

    # Vom stoca textul ctiptat in acest vector.
    ciphertext = []

    # Parcurgem intregul string litera cu lietra.
    # Functia 'enumerate(text)' ataseaza un index pentru fiecare litera. 
    for i, c in enumerate(text):
        # Obtinem litera corespunzatoare cuvantului cheie.
        k = keyword[i % len(keyword)]
        
        # Vrem ca spatiile sa fie ignorate.
        if c.isspace():
            ciphertext.append(c)
            continue

        # 0. Schimbam fiecare litera din textul care trebuie criptat cu valoarea corespunzatoare cuvantului cheie.
        # 2. Functia 'ord(c)/ord(k)/ord('A')' retuneaza valoarea ascii a caracterului transimis.
        # 3. '% 26' Este folosit pentru a ramane in cadrul alfabetului.
        # 4. Adaugam valoarea literii A (care este 65) pentru a ne asigura ca caracterul criptat este o litera.
        # 5. Functia 'chr(value)' este folosit pentru a trasforma valoare obtinuta intro litera.
        # 6. In final folosim 'append()' pentru atasa litera la finalul vectorului ciphertext.
        ciphertext.append(chr((ord(c) + ord(k)) % 26 + ord('A'))) 
    
    # Transformam vectorul intr un-string.
    return ''.join(ciphertext)

# Functia de decriptare
def decrypt(ciphertext, keyword):
    # Ne asiguram ca datele de intrare sunt compuse doar din litere mari. 
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    
    # Vom stoca textul ctiptat in acest vector.
    text = []
    
    # Parcurgem intregul string litera cu lietra.
    # Functia 'enumerate(text)' ataseaza un index pentru fiecare litera. 
    for i, c in enumerate(ciphertext):
        # Obtinem litera corespunzatoare cuvantului cheie.
        k = keyword[i % len(keyword)]
        
        # Vrem ca spatiile sa fie ignorate.
        if c.isspace():
            text.append(c)
            continue
        
        # Algoritmul de decriptare
        text.append(chr((ord(c) - ord(k) + 26) % 26 + ord('A')))

    # Transformam vectorul intr un string.
    return ''.join(text)

ciphertext = vigenere_encrypt("Acesta este un mesaj secret", "secret")
print("Textul criptat: " + ciphertext)

text = decrypt(ciphertext, "secret")
print("Textul decriptat: " + text)
