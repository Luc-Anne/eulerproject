#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import copy

def formater_triangle_pour_solve_path_max(triangle):
	triangle = []
	for line in triangle_raw:
		# Separate numbers
		row = line.split(" ")
		i = 0
		while i < len(row):
			# Convert them into integer
			row[i] = int(row[i])
			i += 1
		triangle.append(row)

	# Build a triangle for direction based on triangle patron
	triangle_direction = []
	for line in triangle:
		line_direction = line.copy()
		triangle_direction.append(line_direction)
	
	return [triangle, triangle_direction]

def solve_path_max(data_triangle):
	triangle = data_triangle[0]
	triangle_direction = data_triangle[1]
	# Cas de la première ligne
	triangle_direction[0][0] = "."
	# Pour chaque ligne du triangle
	i = 1
	while i < len(triangle):
		line = triangle[i]
		# Pour chaque nombre
		j = 0
		while j < len(line):
			# Vérifier laquelle des deux précédentes routes disponibles
			# est la plus grande (sauf aux extrémités avec une seule route)
			if j == 0:
				triangle_direction[i][j] = "↑"
			elif j == len(line) - 1:
				triangle_direction[i][j] = "↖"
			else:
				if triangle[i-1][j-1] > triangle[i-1][j]:
					triangle_direction[i][j] = "↖"
				else:
					triangle_direction[i][j] = "↑"
			# Ajouter selon le résultat puis passer au nombre suivant
			if triangle_direction[i][j] == "↑":
				line[j] = line[j] + triangle[i-1][j]
			else:
				line[j] = line[j] + triangle[i-1][j-1]
			j += 1
		i += 1

	return [triangle, triangle_direction]

def max_sum_in_path_triangle(data_triangle_path):
	last_row = data_triangle_path[0][-1]
	last_row.sort()
	return last_row[-1]

# TEST

triangle_raw = [
"75", \
"95 64", \
"17 47 82", \
"18 35 87 10", \
"20 04 82 47 65", \
"19 01 23 75 03 34", \
"88 02 77 73 07 63 67", \
"99 65 04 28 06 16 70 92", \
"41 41 26 56 83 40 80 70 33", \
"41 48 72 33 47 32 37 16 94 29", \
"53 71 44 65 25 43 91 52 97 51 14", \
"70 11 33 28 77 73 17 78 39 68 17 57", \
"91 71 52 38 17 14 91 43 58 50 27 29 48", \
"63 66 04 68 89 53 67 30 73 16 69 87 40 31", \
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23" \
]

data_triangle = formater_triangle_pour_solve_path_max(triangle_raw)
for row in data_triangle[0]:
	print(row)
	
data_triangle_path = solve_path_max(data_triangle)
for row in data_triangle_path[0]:
	print(row)
for row in data_triangle_path[1]:
	print(row)

print("Max sum in triangle :")
print(max_sum_in_path_triangle(data_triangle_path))
'''
[75]
[95, 64]
[17, 47, 82]
[18, 35, 87, 10]
[20, 4, 82, 47, 65]
[19, 1, 23, 75, 3, 34]
[88, 2, 77, 73, 7, 63, 67]
[99, 65, 4, 28, 6, 16, 70, 92]
[41, 41, 26, 56, 83, 40, 80, 70, 33]
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
[75]
[170, 139]
[187, 217, 221]
[205, 252, 308, 231]
[225, 256, 390, 355, 296]
[244, 257, 413, 465, 358, 330]
[332, 259, 490, 538, 472, 421, 397]
[431, 397, 494, 566, 544, 488, 491, 489]
[472, 472, 520, 622, 649, 584, 571, 561, 522]
[513, 520, 592, 655, 696, 681, 621, 587, 655, 551]
[566, 591, 636, 720, 721, 739, 772, 673, 752, 706, 565]
[636, 602, 669, 748, 798, 812, 789, 850, 791, 820, 723, 622]
[727, 707, 721, 786, 815, 826, 903, 893, 908, 870, 847, 752, 670]
[790, 793, 725, 854, 904, 879, 970, 933, 981, 924, 939, 934, 792, 701]
[794, 855, 891, 881, 927, 913, 1040, 1068, 1054, 1074, 977, 992, 994, 796, 724]
['.']
['↑', '↖']
['↑', '↖', '↖']
['↑', '↑', '↑', '↖']
['↑', '↑', '↑', '↖', '↖']
['↑', '↑', '↑', '↖', '↖', '↖']
['↑', '↑', '↑', '↑', '↖', '↖', '↖']
['↑', '↖', '↑', '↑', '↖', '↖', '↖', '↖']
['↑', '↖', '↑', '↑', '↖', '↖', '↑', '↖', '↖']
['↑', '↑', '↑', '↑', '↑', '↖', '↖', '↖', '↖', '↖']
['↑', '↑', '↑', '↑', '↑', '↖', '↖', '↖', '↑', '↖', '↖']
['↑', '↑', '↑', '↑', '↑', '↑', '↑', '↖', '↑', '↖', '↖', '↖']
['↑', '↖', '↑', '↑', '↑', '↑', '↖', '↑', '↖', '↑', '↖', '↖', '↖']
['↑', '↖', '↑', '↑', '↑', '↑', '↑', '↖', '↑', '↖', '↖', '↖', '↖', '↖']
['↑', '↑', '↖', '↑', '↑', '↖', '↑', '↖', '↑', '↖', '↑', '↖', '↖', '↖', '↖']
Max sum in triangle :
1074
'''
