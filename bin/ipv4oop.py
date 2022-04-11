#!/usr/bin/python3

import ipaddress

vorgabe = "19.138.27.199/22"
print(f'IP Adresse: "{vorgabe}":')

ipadresse = ipaddress.ip_interface(vorgabe)
netzadresse = ipadresse.network
print(f'Die Netzadresse ist: {netzadresse}')

netzadresse = ipaddress.ip_network(netzadresse)
anzahl_hosts = netzadresse.num_addresses
print(f'Es gibt {anzahl_hosts} Hosts')

netzmaske = netzadresse.netmask
print(f'die Netzmaske lautet:{netzmaske}')

adressierbar = anzahl_hosts -2
print(f'es gibt {adressierbar} adressierbare Hosts')

class Ipadresse:
	def __init__(self, adresse):
		self.adresse = adresse
		self.ipadresse = ipaddress.ip_interface(adresse)
		self.netzadresse1 = self.ipadresse.network

	def netzadresse(self):
               print(f'Die Netzadresse lautet: {netzadresse}')

	def ipadresse(self):
		print(f'Die IP Adresse lautet: {vorgabe}')

vorgabe = '92.138.27.199/22'
ip = Ipadresse(vorgabe)
ip.netzadresse()
