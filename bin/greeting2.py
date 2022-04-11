#!/usr/bin/python3

stunde = input('Geben Sie die Uhrzeit ein: ')
stunde = int(stunde)

if stunde >= 8 and stunde <12:
    print('Guten Morgen')
#    exit(12)
elif stunde >= 12 and stunde < 17:
    print('Guten Tag')
else:
    print('Gute Nacht')



#if stunde >= 8:
#    if stunde <12:
#        print('Guten Morgen')
#        exit(2)


