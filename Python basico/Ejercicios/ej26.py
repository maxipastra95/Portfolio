def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a,b in replacements:
        s = s.replace(a,b).replace(a.upper(),b.upper())
    s = s.lower()
    return s

texto = input("Inserte una frase: ")
texto = normalize(texto)
c = 0
for a in texto:
    if a == "a" or a == "e" or a =="i" or a == "o" or a =="u":
        c += 1
print(f"Hay {c} vocales")
print(texto)