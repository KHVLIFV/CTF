def FUN_00101220():
    # Initialisation des données
    cVar1 = -0x68
    data = [
        0x98, 0x9c, 0x82, 0x82, 0x48, 0x2b, 0x93, 0xA0,
        0xA5, 0xA5, 0x93, 0x85, 0xA0, 0x83, 0xA2, 0xA5
    ]

    # Conversion initiale de chaque octet
    i = 0
    while i < len(data):
        data[i] = (cVar1 + (-0x50)) & 0xFF  # Assurez-vous que les valeurs sont dans la plage 0-255
        cVar1 = data[i]
        i += 1

    # Afficher la chaîne résultante
    puts(bytes(data).decode('latin1', 'ignore'))

    # Ajouter 'P' (0x50) à chaque caractère non nul
    i = 0
    while i < len(data):
        if data[i] != 0:
            data[i] = (data[i] + ord('P')) & 0xFF  # Assurez-vous que les valeurs sont dans la plage 0-255
        i += 1

    return 0

# Fonction puts simulée pour afficher les données
def puts(s):
    print(s)

# Appel de la fonction pour voir le résultat
FUN_00101220()

