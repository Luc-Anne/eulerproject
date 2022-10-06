#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def list_in_file():
	file = open("#22_file.txt", "r")
	txt = file.readline()
	list = txt.split('","')
	list[0] = list[0][1:]
	list[-1] = list[-1][0:-1]
	return list

def names_scores():
	list = list_in_file()
	list.sort()
	
	letters_value = {
		"A" : 1,
		"B" : 2,
		"C" : 3,
		"D" : 4,
		"E" : 5,
		"F" : 6,
		"G" : 7,
		"H" : 8,
		"I" : 9,
		"J" : 10,
		"K" : 11,
		"L" : 12,
		"M" : 13,
		"N" : 14,
		"O" : 15,
		"P" : 16,
		"Q" : 17,
		"R" : 18,
		"S" : 19,
		"T" : 20,
		"U" : 21,
		"V" : 22,
		"W" : 23,
		"X" : 24,
		"Y" : 25,
		"Z" : 26
		}

	i = 0
	while i < len(list):
		name = list[i]
		value = 0
		for character in name:
			value += letters_value[character]
		list[i] = value * (i + 1)
		i += 1
	
	result = 0
	for j in list:
		result += j
	
	return result

# TEST
print(names_scores())
'''
871198282
'''
