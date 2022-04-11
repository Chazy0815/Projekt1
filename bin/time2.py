stunde = input('Geben Sie die Uhrzeit ein: ')
stunde = int(stunde)

if stunde >= 8 and stunde >12:
	print('Guten Morgen')
	exit()
elif stunde >=12 and stunde < 17:
	print('Guten Tag')
else:
	print('Gute Nacht')
