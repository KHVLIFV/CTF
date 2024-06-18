from Crypto.Util.number import *

p = getPrime(2048);
q = getPrime(2048) ;

e = 65537

n = //

phi = //

flag = "Hackerlab2024"

d = //

cipher = pow(flag,e,n)

t = pow(flag,q,n)
k = pow(flag,p,n)
f = pow(flag,n,n)

with open('output.txt','w+') as file:
	file.write("n = "+ str(n)+"\n\n")
	file.write("t = "+ str(t)+"\n\n")
	file.write("k = "+ str(k)+"\n\n")
	file.write("f = "+ str(f)+"\n\n")
	file.write("encrypt = "+ str(cipher)+"\n\n")

