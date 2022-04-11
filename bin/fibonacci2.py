#!/usr/bin/python3

erste = 1
zweite = 0
dritte = 0

folge = [ 1 ]

counter = 99
for zahl in folge:
	dritte = erste + zweite
	folge.append(dritte)
	counter = counter -1
	if counter == 0:
		print(folge)
		exit(0)
	zweite = dritte + erste
	folge.append(zweite)
	counter = counter - 1
	if counter == 0:
		print(folge)
		exit(0)
	erste = zweite + dritte
	folge.append(erste)
	counter = counter -1
	if counter == 0:
		print(folge)
		exit(0)
