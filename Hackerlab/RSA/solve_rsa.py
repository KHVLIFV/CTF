import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def decrypt_RSA(C, d, N):
    M = pow(C, d, N)
    return M

# Données fournies
N = 25203072061613986373945886893335124115493463487628727874031059800822061809567
C = 21370860772767430569952506747247564236090303327355611280955497891572895095762
p = 158754754453572149934540516805858365529
q = 158754754453572149934540516805858365623

# Calcul de phi(N)
phi_N = (p - 1) * (q - 1)

# Chercher d tel que e * d ≡ 1 (mod phi_N)
e = 65537  # d'après la recherche, e = 65537 est un bon choix
d = mod_inverse(e, phi_N)

# Déchiffrement du message
M = decrypt_RSA(C, d, N)

# Conversion de M en chaîne de caractères
message = ""
while M > 0:
    message = chr(M % 256) + message
    M = M // 256

# Affichage du message déchiffré
print("Message déchiffré :")
print(message)
