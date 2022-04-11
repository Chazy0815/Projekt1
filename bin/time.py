#!/usr/bin/python3

eingabe1 = input('Bitte geben Sie die Stunde an: ')
#eingabe2 = input('Bitte geben Sie die Minuten an: ')
eingabe1 = int(eingabe1)

if eingabe1 <=8 and eingabe1 <=11:
	print(f'Guten Morgen! Es ist {eingabe1} Uhr!')
	exit(0)
if eingabe1 <=12 and eingabe1 <=13:
	print(f'Mahlzeit! Es ist {eingabe1} Uhr!')
	exit(1)
if eingabe1 <=14 and eingabe1 <=16:
	print(f'Guten Tag! Es ist {eingabe1} Uhr!')
	exit(2)
if eingabe1 <=17 and eingabe1 <=21:
	print(f'Guten Abend. Es ist {eingabe1} Uhr!')
	exit(3)
if eingabe1 <=23:
	print(f'Gute Nacht. Es ist {eingabe1} Uhr!')
	exit(4)
if eingabe1 >=0 or eingabe1 <=3:
	print(f'Gute Nacht. Es ist {eingabe1} Uhr!')

#if int(eingabe) <12:
#	print('Mahlzeit!')
#if int(eingabe) <14:
#	print('Guten Tag!')
#if int(eingabe) <17:
#	print('Guten Abend')
#if int(eingabe) <22:
#	print('Gute Nacht')
