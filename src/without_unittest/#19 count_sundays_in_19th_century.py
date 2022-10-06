#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def count_sundays_in_19th_century():
	month_long_not_bissextile = [31,28,31,30,31,30,31,31,30,31,30,31]

	range_year_borne_inf = 1 # 1901
	range_year_borne_sup = 100 # 2000

	current_day_in_century = 1 # 1st january 1900
	current_month = 0 # January
	current_year = 0 # 1900
	
	result = 0
	
	while current_year < range_year_borne_sup + 1:
			
			# Check current date
			# Because 1st january 1900 is a monday and is number 1
				if current_day_in_century % 7 == 0:
					if current_year >= range_year_borne_inf:
						result += 1
			
			# Go to the next first day of a month
				current_day_in_century += month_long_not_bissextile[current_month]
				# Check bissextile for february
				if current_month == 1 and \
					current_year % 4 == 0 and \
					current_year % 100 != 0 or (current_year + 300) % 400 == 0 :
					current_day_in_century += 1
				current_month += 1
				
				# Change years when necessary
				if current_month == 12:
					current_month = 0
					current_year += 1

	return result


print(count_sundays_in_19th_century())
