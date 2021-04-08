from random import *

f = open("message.txt", "r")
f2 = open("cipher.txt", "w")
f3 = open("recovered_file.txt", "w")
M = f.readline()
K = ""
C = ""
decrypted = ""

# Generate random key
for i in range(len(M)):
    K = K + chr(randint(0, 255))

# Generate encrypted string
for j in range(len(M)):
    C = C + chr(ord(M[j]) ^ ord(K[j]))

# Write encrypted string to cipher file
f2.write(C)

# Decrypt
for k in range(len(M)):
    decrypted = decrypted + chr(ord(C[k]) ^ ord(K[k]))

# Write decryption to file
f3.write(decrypted)

f4 = open("recovered_file.txt", "r")

# Check if identical
if f.readline() == f4.readline():
    print("They are identical")
else:
    print("They are not identical")
