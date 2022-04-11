#!/usr/bin/python3
#autor: klre
#modified: 06.04.2022
# Gibt einen formatierten Text aus
"""
Ein Kommentar
über mehrere Zeilen
"""

eingabe = input('Bitte geben Sie einen Text ein: ')
if len(eingabe) <1:
	print('Sie müssen schon mit mir reden:')
	exit
laenge = len(eingabe)
#print(f'Ihre Eingabe: "{eingabe}" war {laenge} Zeichen lang.' )

#print('Hallo Welt, Sie haben folgende eingabe gemacht:' , eingabe)
#print(f"Hallo Welt, Sie haben folgende eingabe gemacht: " + '{eingabe}')

#anzahl = input('Wie breit soll die Ausgabe werden: ')
print(laenge * '#'+ 2*'#' )
print(f'#{eingabe}#')
print(laenge * '#'+ 2*'#' )
