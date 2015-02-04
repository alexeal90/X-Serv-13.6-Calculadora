#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

	Alejandro Valeriano Fernandez - GITT
	Ejercicio 13.6
	Calculadora

"""

import sys

def suma(operando1, operando2):
	try:
		return int(operando1) + int(operando2)
	except NameError:
		print ("Invalid arguments")

def rest(operando1, operando2):
	try:
	 	return int(operando1) - int(operando2)
	except NameError:
		print ("Invalid arguments")

def mult(operando1, operando2):
	try:
		return int(operando1) * int(operando2)
	except NameError:
		print ("Invalid arguments")

def div(operando1, operando2):
	try:
		return float(operando1) / float(operando2)
	except NameError:
		print ("Invalid arguments") 


if __name__ == "__main__":

	if len(sys.argv) != 4:
		print
		sys.exit("Usage: $ python calculadora.py funcion operando1 operando2")
		
	if sys.argv[1] == 'add':
		print sys.argv[2] + ' mas ' + sys.argv[3] + ' = ' + str(suma (sys.argv[2], sys.argv[3]))

	if sys.argv[1] == 'substract':
		print sys.argv[2] + ' menos ' + sys.argv[3] + ' = ' + str(rest (sys.argv[2], sys.argv[3]))

	if sys.argv[1] == 'multiply':
		print sys.argv[2] + ' por ' + sys.argv[3] + ' = ' + str(mult (sys.argv[2], sys.argv[3]))

	if sys.argv[1] == 'divide':
		try:
			print sys.argv[2] + ' entre ' + sys.argv[3] + ' = ' + str(div (sys.argv[2], sys.argv[3]))

		except:
			print 'error al dividir'
	else:
		print 'Las posibles operaciones son "add", "substract", "multiply" y "divide"'
