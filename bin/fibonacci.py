#!/usr/bin/python3

zahlen = int(input("Wieviele Zahlen? "))

z1, z2 = 0, 1
count = 0

if zahlen <= 0:
   print("Gib eine Zahl ein: ")
elif zahlen == 1:
   print(zahlen)
   print(z1)
else:
   while count <= zahlen:
       print(z1)
       z3 = z1 + z2
       z1 = z2
       z2 = z3
       count += 1
