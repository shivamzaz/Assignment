import csv

'''
	@shivamzaz
	Initial path direcotry for the importing the data

'''

path = ''

from collections import defaultdict as d

import sys

pivot_table = d(dict)

'''
	Read CSV Data and make the pivot table in this format 
					{
						 Userid : 
						    {
						      Product : Price
						    }
					}
					
'''

file=open(sys.argv[1], "r")

reader = csv.reader(file)

Command_line_args = len(sys.argv)

for line in reader:

	length_line = len(line)

	if length_line <= 3:

		pivot_table[str(line[0])][line[2].lstrip()]=line[1]

	else:

		for i in range(2 ,length_line, 1):

			pivot_table[str(line[0])][line[i].lstrip()]=line[1]


pivot_table = dict(pivot_table)

'''

	lk and pk is for defining the list range

'''
lk = 15

pk = 15

list_of_total_sum_of_items = [0]*15

count =0

check_product_in_pivot_table = [0]*Command_line_args

check_product_in_pivot_table[0]=1

check_product_in_pivot_table[1]=1

'''

	count the sum corresponding the user give products 
	also check user give products is in our data.csv

'''

for key, value in zip(pivot_table.keys(), pivot_table.values()):

	io=list_of_total_sum_of_items[count]

	for i in range(2, Command_line_args, 1):

		if sys.argv[i] in pivot_table[key]:

			check_product_in_pivot_table[i] = 1

			io+=float(pivot_table[key][sys.argv[i]])

	list_of_total_sum_of_items[count]=(key,io)

	count+=1

'''
	count non tuple Value for removing the irrelevent data according to the user query
''' 

for i in list_of_total_sum_of_items:

	if type(i)==int:

		break

	else:

		pk-=1

'''

	Finally have list of tuples which is relevent for minimum finding price finding product 

''' 

list_of_total_sum_of_items=list_of_total_sum_of_items[:lk-pk]


'''

   pluck the min value of price from the list of prices ehich came after summing the product according to the user given input products
	also if user given product is not in data.csv then show the none as  output
''' 

if 0 not in check_product_in_pivot_table:

	initial_max_value = 0

	initial_max_key = 0

	flag=0 

	for i,j in list_of_total_sum_of_items:

		if j!=0 and j>initial_max_value and flag==0:

			initial_max_key, initial_max_value,flag=i,j,1

		elif j<initial_max_value and j!=0:

			initial_max_key, initial_max_value=i,j

	print str(initial_max_key) + ", " + str(initial_max_value)

else:

	print "none"



    





