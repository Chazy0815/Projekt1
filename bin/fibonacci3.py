#!/usr/bin/python3

start_wert = 4
end_wert = 1000
prime_list = [2, 3]
for teste_zahl in range(start_wert, end_wert):

	print(f'Berechne {teste_zahl}')

	for teiler in range(2, teste_zahl):

		print(f'Teiler {teiler}')
		if teste_zahl % teiler == 0:
			print(f'KEINE PRIMZAHL {teste_zahl} % {teiler}')
			break
	prime_list.append(teste_zahl)
	print(f'{teste_zahl} appendet - {teiler}')

print(prime_list)
