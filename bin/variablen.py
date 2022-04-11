#!/usr/bin/python3
#
#a = 'Wert'
#print a.lower()
#print a.upper
#print a.capitalize
#liste = [ 2, 4, 'a', 34]
#liste.append ('Ae')
#print liste
#liste[2]
#'a
#a = liste.pop()'
#
#for teil in liste:
#	print(teil)
#	print('------')
#
#zeit = '08:23'
#for buchstabe in zeit:
#	print(buchstabe)
#
#eingabe1 = input('Bitte geben Sie die Stunde an: ')
#eingabe2 = input('Bitte geben Sie die Minuten an: ')
#
#eingabe1 = int(eingabe1)
#eingabe2 = int(eingabe2)

#eingabe = input('Bitte geben Sie die Uhrzeit an (hh:mm): ')
#liste = ['hh', 'mm',]
#for teil in liste:
#	print(teil, ':',teil)
#	exit()

############################################################################

satz = input('Gebe einen Satz ein: ')
zeichen = 'abcdefghijklmnopqrstuvwxyzäöü'
wort = ''
liste = []

for buchstabe in satz:
	if buchstabe.lower() in zeichen:
		wort += buchstabe
	else:
		if len(wort) > 0:
			liste.append(wort)
			wort = ''
if len(wort) > 0:
	liste.append(wort)
	wort = ''

print(liste)
